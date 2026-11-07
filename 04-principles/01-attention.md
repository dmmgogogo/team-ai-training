# M4-01 · Attention 机制详解

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：低 ｜ 🔁 下次复核：2027-05
>
> 从直觉到公式，再到 2026 年的工程实现：FlashAttention、稀疏注意力与 KV 缓存。

---

## 为什么需要 Attention？

在 Transformer 之前，处理序列数据用 RNN（循环神经网络）：
- 一个词一个词串行处理
- 无法并行，训练慢
- 长距离依赖容易"遗忘"（梯度消失）

Attention 机制解决了这些问题：**让每个词直接"看到"序列中所有其他词**。

但"每个词看所有词"也带来了新问题：序列长度 n 增加时，计算量和显存按 **O(n²)** 增长。2026 年 1M 上下文的背后，就是一场围绕这个平方项的工程战争。

---

## 直觉理解：信息检索系统

Attention 的工作方式就像一个搜索引擎：

```
你提问（Query）: "苹果公司的CEO是谁？"
                    ↓
数据库里有很多条目（Keys）:
  - Key1: "苹果是一种水果"        → 相关性低
  - Key2: "苹果公司成立于1976年" → 相关性中
  - Key3: "蒂姆·库克是苹果CEO"   → 相关性高
                    ↓
根据相关性加权取值（Values）
                    ↓
答案: "蒂姆·库克"
```

在 Transformer 里：
- **Query（Q）**：当前词在"问"什么
- **Key（K）**：每个词在"说"自己是什么
- **Value（V）**：每个词真正贡献的信息

---

## 数学公式

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V$$

分解解读：

| 步骤 | 操作 | 意义 |
|------|------|------|
| `QK^T` | Q 和 K 的点积 | 计算每对词之间的相关性分数 |
| `/ √d_k` | 除以维度的平方根 | 防止分数太大导致梯度消失 |
| `softmax(...)` | 归一化 | 把分数变成概率（加和为 1） |
| `× V` | 加权求和 | 按注意力权重聚合信息 |

**因果注意力（Causal）**：Decoder-only 模型在生成第 t 个 Token 时，只能看到前 t 个 Token，防止"偷看答案"。

---

## 多头注意力（Multi-Head Attention）

单个 Attention 只能捕捉一种关系。多头并行：

```
输入
 ↓
分成 H 个头：
  Head 1 → 学习语法关系（主谓宾）
  Head 2 → 学习语义关系（近义词）
  Head 3 → 学习指代关系（it → 苹果）
  Head 4 → 学习位置关系（前后文）
  ...
 ↓
拼接所有头的输出
 ↓
线性变换
```

GPT-3 有 96 层，每层 96 个头（历史例子；2026 年旗舰的层数/头数/专家数更复杂，以技术报告为准）。

---

## Self-Attention vs Cross-Attention

| 类型 | Q 来源 | K/V 来源 | 用途 |
|------|--------|----------|------|
| **Self-Attention** | 同一序列 | 同一序列 | 理解句子内部关系 |
| **Cross-Attention** | 目标序列 | 源序列 | 翻译、多模态对齐 |

GPT（Decoder-only）只用 Self-Attention，且是**因果注意力**（Causal）。

---

## 2022-2026：把 O(n²) 打下来

### 第一招：FlashAttention（2022 → 2024）

标准 Attention 的内存复杂度是 O(n²)：100K Token 的序列会消耗天量显存。

**FlashAttention** 是一种高效实现：
- 分块计算（tiling），不把完整注意力矩阵存到显存
- 通过 kernel fusion 减少显存读写
- 速度快数倍，内存大幅降低
- 让 100K+ 长上下文成为可能

演进：FlashAttention（2022）→ FlashAttention-2（2023，更好的并行与工作划分）→ FlashAttention-3（2024，面向 Hopper GPU 的异步与低精度优化）。到 2026 年，几乎所有主流推理栈都内置了这类 kernel。

### 第二招：稀疏注意力（Sparse Attention）

并非所有 Token 都值得看。稀疏注意力只计算"重要"的部分：

| 方案 | 思路 | 代表 |
|------|------|------|
| **滑动窗口 / 局部注意力** | 每个 Token 只看邻近窗口 | Longformer、Mistral 早期方案 |
| **块稀疏** | 按块选择要计算的区域 | 多种长上下文模型 |
| **DSA（DeepSeek Sparse Attention）** | 轻量"闪电索引器"先给 Token 打分，只对 Top-k 做注意力 | DeepSeek-V3.2-Exp（2025-09） |
| **CSA + HCA（压缩 + 稀疏）** | 先压缩 KV，再稀疏选择；CSA 管细节、HCA 管全局 | DeepSeek-V4（2026-04） |

**DeepSeek-V4 的做法（官方 + 技术解读）**：
- **CSA（压缩稀疏注意力）**：把每 4 个 Token 的 KV 合并成 1 个压缩条目，用索引器挑出最相关的压缩块
- **HCA（重度压缩注意力）**：压缩率高达 128 倍，负责把握全局脉络
- 两者交替部署：一个拿放大镜找细节，一个站山顶看全局
- DeepSeek 官方称 1M 上下文下计算与内存成本大幅下降；公开技术解读称 V4-Pro 的推理计算量约为 V3.2 的 27%，KV 缓存约为 10%（来源：[DeepSeek V4 官方](https://api-docs.deepseek.com/news/news260424/)，2026-04-24；[观察者网技术解读](https://m.163.com/dy/article/KRMIA2MT051481US.html)，2026-04-29）

```
全量注意力：每个 Token × 所有历史 Token   → O(n²)
DSA：      每个 Token × Top-k 相关 Token  → 近似 O(n·k)
CSA/HCA：  先压缩 KV，再稀疏选择          → 进一步降内存
```

### 第三招：KV Cache 与上下文缓存

推理分两个阶段：

| 阶段 | 做什么 | 瓶颈 |
|------|--------|------|
| **Prefill（预填充）** | 一次性处理输入上下文，计算 KV | 计算密集；长上下文首 Token 延迟高 |
| **Decode（解码）** | 逐个生成输出 Token，复用 KV Cache | 显存带宽密集 |

**KV Cache** 把已计算的 K/V 存下来，避免每生成一个 Token 都重算全文。它是多轮对话和长上下文可行的前提。

**上下文缓存（Prompt/Context Caching）** 则更进一步：把稳定的前缀（系统提示、固定文档、代码库）缓存到内存甚至磁盘，命中后跳过整段 prefill。2026 年主流 API 都提供该能力，折扣与 TTL 不同，以官网为准。

---

## 位置编码（Positional Encoding）

Attention 本身不知道词的顺序（"我吃鱼" 和 "鱼吃我" 对它来说一样）。
需要额外注入位置信息：

| 方法 | 代表 | 特点 |
|------|------|------|
| 正弦位置编码 | 原始 Transformer | 固定，不可学习 |
| 可学习位置 | BERT | 上限固定（512 位置）|
| **RoPE**（旋转位置编码） | LLaMA、GPT-NeoX、多数 2026 旗舰 | 可外推到更长序列 |
| **ALiBi** | Bloom | 直接修改注意力分数 |

RoPE 是目前最主流的方案。配合位置插值、YaRN 等外推技巧，模型可以处理比训练时更长的序列——但"能读进去"不等于"能同等精度地理解"，这就是 [上下文腐烂（context rot）](./05-context-engineering.md) 的根源。

---

## Attention 可视化

研究者可以可视化注意力权重，看到模型"在关注什么"：

```
句子: The animal didn't cross the street because it was too tired

当处理 "it" 时，不同注意力头关注不同的词：
- 某些头关注 "animal"（正确的指代）
- 某些头关注 "street"（也是候选）
```

这说明模型确实学到了语言结构，而不是死记硬背。

> 注意：注意力权重 ≠ 解释。可视化是理解工具，不是"模型为什么这么说"的完整答案。

---

## 总结

| 概念 | 要点 |
|------|------|
| Attention | 动态计算词与词之间的相关性权重 |
| Self-Attention | 序列内部的注意力 |
| Multi-Head | 多角度捕捉不同类型的关系 |
| FlashAttention | 工程优化，让长上下文可行 |
| 稀疏 / 压缩注意力 | 只算重点，把 1M 上下文成本降到可商用 |
| KV Cache | 缓存历史 K/V，支撑多轮与长上下文 |
| RoPE | 位置编码，让模型理解顺序 |

---

## 延伸阅读（真实论文链接）

| 论文 | 链接 | 发表年份 |
|------|------|---------|
| Attention Is All You Need（Transformer 原文） | [arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762) | 2017，Google Brain |
| FlashAttention | [arxiv.org/abs/2205.14135](https://arxiv.org/abs/2205.14135) | 2022，Stanford |
| FlashAttention-2 | [arxiv.org/abs/2307.08691](https://arxiv.org/abs/2307.08691) | 2023，Stanford |
| FlashAttention-3 | [arxiv.org/abs/2407.08608](https://arxiv.org/abs/2407.08608) | 2024，面向 Hopper |
| RoPE 位置编码 | [arxiv.org/abs/2104.09864](https://arxiv.org/abs/2104.09864) | 2021 |
| DeepSeek-V3.2-Exp（DSA） | [DeepSeek 官方](https://api-docs.deepseek.com/news/news250929/) | 2025-09 |
| DeepSeek-V4（CSA/HCA） | [DeepSeek 官方](https://api-docs.deepseek.com/news/news260424/) | 2026-04 |

---

## 历史沿革

- **2026**：DeepSeek-V4 用 CSA/HCA 把 1M 上下文成本打下来；稀疏/压缩注意力成为旗舰标配。
- **2025**：DeepSeek-V3.2-Exp 首次引入 DSA（闪电索引器 + 细粒度稀疏）。
- **2024**：FlashAttention-3 发布；长上下文竞赛从 128K 走向 1M。
- **2023**：FlashAttention-2 成为训练/推理标配；RoPE 外推技巧（位置插值等）普及。
- **2022**：FlashAttention 论文发表，解决 O(n²) 显存瓶颈。
- **2021**：RoPE 提出，后来成为主流位置编码。
- **2017**：Transformer 论文发表，Attention 取代 RNN 成为序列建模核心。

---

## 下一步

- [M4-02 RAG 检索增强生成](./02-rag.md) — 用注意力之外的方式给模型"补知识"
- [M4-05 上下文工程](./05-context-engineering.md) — 长上下文为什么仍要精心管理
