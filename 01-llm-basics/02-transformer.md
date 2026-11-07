# M1-02 · Transformer 架构

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：低 ｜ 🔁 下次复核：2027-05
>
> LLM 的"心脏"——不需要数学背景，看懂核心思想，以及 2026 年它进化成了什么样。

---

## 为什么叫 Transformer？

2017 年，Google 发表了论文《Attention Is All You Need》，提出了 **Transformer 架构**。它彻底改变了 NLP（自然语言处理）领域，是现代所有 LLM（GPT、Claude、Gemini、DeepSeek）的基础。

2026 年的模型仍然是 Transformer，但"零件"换了不少：前馈网络在很多旗舰模型里换成了 **MoE 专家**，注意力换成了 **稀疏/压缩注意力**，输入也不再只有文本。主干没变，效率优化翻天覆地。

---

## 核心思想：Attention（注意力机制）

人类读文章时，会根据上下文"关注"重要的词。

例如句子：
> **"它**去市场，**买**了苹果，然后**它**吃掉了。"

两个"它"指的是同一个主体，理解这一点需要联系上下文。

**Attention 机制**就是让模型学会：在生成每个词时，应该"关注"输入序列中的哪些位置。

```
输入: ["银行", "的", "利率", "很", "高"]
                                ↑
生成"高"时，模型会重点关注"利率"这个词
```

---

## Transformer 整体结构

```
输入（文本 / 图像 / 音频 / 视频）
    ↓
[Tokenization] 统一切成 Token 序列
    ↓
[Embedding] Token → 向量（数字表示）
    ↓
[位置编码] 加入位置信息（RoPE 等）
    ↓
[N × Transformer Block]  ← 核心，重复多层
  ├─ Multi-Head Self-Attention（注意力）
  ├─ Add & Norm（残差连接 + 归一化）
  ├─ MoE / FFN（前馈网络；2026 旗舰多用 MoE）
  └─ Add & Norm
    ↓
[输出层] 预测下一个 Token 的概率分布
    ↓
输出（文本 / 结构化数据 / 工具调用）
```

---

## Self-Attention 工作方式（直觉理解）

对于序列中的每个词，计算它与其他所有词的"相关性得分"：

```
Q（Query）：当前词想问"谁和我相关？"
K（Key）：每个词说"我的特征是这些"
V（Value）：每个词说"如果你关注我，我贡献这些信息"

注意力分数 = softmax(Q × K^T / √d) × V
```

**多头（Multi-Head）**：同时做多组不同的注意力计算，相当于从多个角度看语义关系（语法关系、语义关系、指代关系等）。

> 想看公式拆解和 FlashAttention / 稀疏注意力，去 [M4-01 Attention 机制详解](../04-principles/01-attention.md)。

---

## 为什么 Transformer 那么强？

| 特性 | 好处 |
|------|------|
| 并行计算 | 不像 RNN 串行处理，训练速度快得多 |
| 长距离依赖 | 任意两个位置都能直接交互，不受距离限制 |
| 可扩展 | 加更多层 / 更多参数，性能持续提升 |
| 通用性 | 不只用于 NLP，图像（ViT）、音频、视频都能用 |
| 易工程优化 | 注意力可分块、可稀疏、可缓存，撑起 1M 上下文 |

---

## 2026 的关键进化一：MoE（混合专家）

传统 Transformer 每个 Token 都要过同一个前馈网络（FFN）。到千亿/万亿参数，这太贵了。

**MoE（Mixture of Experts）** 把 FFN 拆成很多"专家"，每个 Token 只路由到其中少数几个：

```
Token → Router（路由器）→ 选 Top-k 个专家 → 只计算这几个
                         （其余专家不参与，等于"休眠"）
```

| 概念 | 含义 |
|------|------|
| 总参数 | 所有专家加起来，决定"知识容量" |
| 激活参数 | 每个 Token 真正用到的参数，决定"推理成本" |
| 稀疏激活 | 总参数远大于激活参数，用便宜的价格获得大容量 |

**2026 实例（DeepSeek 官方，2026-04）**：
- DeepSeek-V4-Pro：1.6T 总参数 / 49B 激活
- DeepSeek-V4-Flash：284B 总参数 / 13B 激活
- 两者都原生支持 1M 上下文（来源：[DeepSeek V4 Preview](https://api-docs.deepseek.com/news/news260424/)，2026-04-24）

MoE 也有代价：路由可能不均、训练更复杂、显存占用大、微调更挑方法。所以"MoE 一定比 Dense 好"是伪命题。

---

## 2026 的关键进化二：稀疏 / 压缩注意力

标准注意力是 O(n²)：上下文从 8K 扩到 1M，计算量按平方增长。2026 年的解法不是硬扛，而是"少算一些"：

| 方案 | 思路 | 代表 |
|------|------|------|
| **FlashAttention** | 分块计算，不把完整注意力矩阵写进显存 | 2022 起成为标配，已迭代到 FA2 / FA3 |
| **稀疏注意力（DSA）** | 用轻量索引器挑出最相关的 Token/块再算 | DeepSeek-V3.2-Exp（2025-09）首次引入 DSA |
| **压缩 + 稀疏（CSA/HCA）** | 先压缩 KV，再稀疏选择；兼顾细节与全局 | DeepSeek-V4（2026-04） |

效果有多夸张？DeepSeek 官方称 V4 在 1M 上下文下，推理计算量约为上一代 V3.2 的 27%，KV 缓存约为 10%（来源：[DeepSeek V4 Preview](https://api-docs.deepseek.com/news/news260424/)，2026-04-24）。

> 直觉：不是把整本书每个字都反复对照，而是先建索引、再挑重点看。

---

## 2026 的关键进化三：原生多模态

早期多模态是"外挂"：图像先用一个视觉编码器转成向量，再喂给语言模型。2026 年的旗舰模型更强调 **natively multimodal（原生多模态）**：文本、图像、音频、视频被统一成 Token 序列，在同一个 Transformer 里处理。

- Google 对 Gemini 4 的官方描述就是 "natively multimodal, reasoning models"（来源：[Gemini 4 Argon Model Card](https://deepmind.google/models/model-cards/gemini-4-argon/)，2026-10-13）
- 这意味着模型可以"边看边推理"，而不是先描述再理解

---

## GPT vs BERT：两种 Transformer 用法

| | GPT（Decoder-only） | BERT（Encoder-only） |
|-|---------------------|----------------------|
| 代表 | GPT-6、Claude 5.x、Gemini 4、DeepSeek V4 | BERT、RoBERTa |
| 任务 | 生成文本 / 工具调用 / 推理 | 理解文本、分类、检索 |
| 原理 | 只看左边的词（因果注意力） | 双向看全文 |
| 适合 | 对话、写作、编程、Agent | 分类、搜索、NER、Embedding |

现代 LLM 主要是 **Decoder-only（GPT 风格）**。

但 **Encoder 并没有消失**：你做 RAG 时用的 Embedding 模型、检索后的 Reranker，很多仍是 BERT 家族的变体。生成用 Decoder，检索用 Encoder，是 2026 年很常见的组合。

---

## 参数量从哪里来？

一个 Transformer Block 里主要参数：
- Attention 权重矩阵（Q/K/V/O）
- 前馈网络 / MoE 专家的权重矩阵

层数越多 × 向量维度越大 = 参数越多。

历史例子：GPT-3（175B）= 96 层 × 12288 维度 × 多头注意力 + FFN。2026 年的旗舰模型层数、维度、专家数都复杂得多，官方技术报告是唯一可靠来源。

---

## 类比总结

把 LLM 比作一个超级读书人：
- **Embedding** = 把每个词变成"你脑中的概念"
- **Attention** = 理解上下文、找关联
- **MoE** = 一个庞大的专家团队，按问题叫醒对口的几位
- **FFN** = 深度加工、推理
- **层数** = 思考的"深度"
- **参数** = 从书本中学到的"知识"

---

## 历史沿革

- **2026**：MoE 成为许多旗舰模型的主流选择；稀疏/压缩注意力把 1M 上下文成本打下来；原生多模态统一 Token 序列。
- **2024-2025**：DeepSeek-V3 用 MoE 把训练成本压到数百万美元级；DeepSeek-V3.2-Exp 引入 DSA；长上下文从 128K 迈向 1M。
- **2023**：Mixtral 证明开源 MoE 可行；FlashAttention-2 让长上下文更便宜。
- **2020-2022**：GPT-3 确立 Decoder-only 路线；ViT 证明 Transformer 可用于图像；FlashAttention（2022）解决显存瓶颈。
- **2017**：Transformer 论文发表（[arXiv:1706.03762](https://arxiv.org/abs/1706.03762)）。

---

## 下一步

- [M1-03 训练过程](./03-training.md) — 模型是怎么"学会"的
- [M4-01 Attention 机制详解](../04-principles/01-attention.md) — 深入数学细节与 FlashAttention / 稀疏注意力
- [M4-05 上下文工程](../04-principles/05-context-engineering.md) — 长上下文为什么仍需要"管理"
