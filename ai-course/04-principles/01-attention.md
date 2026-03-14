# M4-01 · Attention 机制详解

> 从直觉到公式，彻底理解"注意力"是怎么工作的。

---

## 为什么需要 Attention？

在 Transformer 之前，处理序列数据用 RNN（循环神经网络）：
- 一个词一个词串行处理
- 无法并行，训练慢
- 长距离依赖容易"遗忘"（梯度消失）

Attention 机制解决了这些问题：**让每个词直接"看到"序列中所有其他词**。

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
| `softmax(...)` | 归一化 | 把分数变成概率（加和为1） |
| `× V` | 加权求和 | 按注意力权重聚合信息 |

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

GPT-3 有 96 层，每层 96 个头。

---

## Self-Attention vs Cross-Attention

| 类型 | Q 来源 | K/V 来源 | 用途 |
|------|--------|----------|------|
| **Self-Attention** | 同一序列 | 同一序列 | 理解句子内部关系 |
| **Cross-Attention** | 目标序列 | 源序列 | 翻译（对齐源和目标）|

GPT（Decoder-only）只用 Self-Attention，且是**因果注意力**（Causal），只能看到前面的词（防止"作弊"）。

---

## Flash Attention

标准 Attention 的内存复杂度是 O(n²)，n 是序列长度。
100K Token 的序列会消耗天量显存。

**Flash Attention** 是一种高效实现：
- 分块计算，不把完整注意力矩阵存到显存
- 速度快 2-4 倍，内存降低 5-20 倍
- 让 100K+ 长上下文成为可能
- 现在所有主流 LLM 都用 Flash Attention

---

## 位置编码（Positional Encoding）

Attention 本身不知道词的顺序（"我吃鱼" 和 "鱼吃我" 对它来说一样）。
需要额外注入位置信息：

| 方法 | 代表 | 特点 |
|------|------|------|
| 正弦位置编码 | 原始 Transformer | 固定，不可学习 |
| 可学习位置 | BERT | 上限固定（512位置）|
| **RoPE**（旋转位置编码） | LLaMA、GPT-NeoX | 可外推到更长序列 |
| **ALiBi** | Bloom | 直接修改注意力分数 |

RoPE 是目前最主流的方案，让模型能处理比训练时更长的序列。

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

---

## 总结

| 概念 | 要点 |
|------|------|
| Attention | 动态计算词与词之间的相关性权重 |
| Self-Attention | 序列内部的注意力 |
| Multi-Head | 多角度捕捉不同类型的关系 |
| Flash Attention | 工程优化，让长上下文可行 |
| RoPE | 位置编码，让模型理解顺序 |

---

## 延伸阅读

- 论文：[Attention Is All You Need](https://arxiv.org/abs/1706.03762)（2017，Transformer 原文）
- 论文：[FlashAttention-2](https://arxiv.org/abs/2307.08691)

---

## 下一步

- [M4-02 RAG 检索增强生成](./02-rag.md)
