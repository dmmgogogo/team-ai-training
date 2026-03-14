# M1-02 · Transformer 架构

> LLM 的"心脏"——不需要数学背景，看懂核心思想。

---

## 为什么叫 Transformer？

2017 年，Google 发表了论文《Attention Is All You Need》，提出了 **Transformer 架构**。它彻底改变了 NLP（自然语言处理）领域，是现代所有 LLM（GPT、Claude、Gemini、DeepSeek）的基础。

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
输入文本
    ↓
[Tokenization] 文本 → Token ID 序列
    ↓
[Embedding] Token ID → 向量（数字表示）
    ↓
[位置编码] 加入位置信息（第几个词）
    ↓
[N × Transformer Block]  ← 这是核心，重复多层
  ├─ Multi-Head Self-Attention（多头注意力）
  ├─ Add & Norm（残差连接 + 归一化）
  ├─ Feed-Forward Network（前馈网络）
  └─ Add & Norm
    ↓
[输出层] 预测下一个 Token 的概率分布
    ↓
输出文本
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

---

## 为什么 Transformer 那么强？

| 特性 | 好处 |
|------|------|
| 并行计算 | 不像 RNN 串行处理，训练速度快得多 |
| 长距离依赖 | 任意两个位置都能直接交互，不受距离限制 |
| 可扩展 | 加更多层 / 更多参数，性能持续提升 |
| 通用性 | 不只用于 NLP，图像（ViT）、音频、视频都能用 |

---

## GPT vs BERT：两种 Transformer 用法

| | GPT（Decoder-only） | BERT（Encoder-only） |
|-|---------------------|----------------------|
| 代表 | GPT-4、Claude、DeepSeek | BERT、RoBERTa |
| 任务 | 生成文本 | 理解文本 |
| 原理 | 只看左边的词（单向） | 双向看全文 |
| 适合 | 对话、写作、编程 | 分类、搜索、NER |

现代 LLM 主要是 **Decoder-only（GPT 风格）**。

---

## 参数量从哪里来？

一个 Transformer Block 里主要参数：
- Attention 权重矩阵（Q/K/V/O）
- 前馈网络的权重矩阵

层数越多 × 向量维度越大 = 参数越多。

GPT-3（175B）= 96 层 × 12288 维度 × 多头注意力 + FFN

---

## 类比总结

把 LLM 比作一个超级读书人：
- **Embedding** = 把每个词变成"你脑中的概念"
- **Attention** = 理解上下文、找关联
- **FFN** = 深度加工、推理
- **层数** = 思考的"深度"
- **参数** = 从书本中学到的"知识"

---

## 下一步

- [M1-03 训练过程](./03-training.md) — 模型是怎么"学会"的
- [M4-01 Attention 机制详解](../04-principles/01-attention.md) — 深入数学细节
