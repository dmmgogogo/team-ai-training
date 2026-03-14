# M4-02 · RAG：检索增强生成

> 让 LLM 知道它原本不知道的事——你的私有数据。

---

## 问题：LLM 不知道你的业务数据

LLM 训练完之后，知识就"冻结"了：
- 不知道你公司的产品文档
- 不知道你内部的代码规范
- 不知道昨天发生的新闻
- 不知道你的数据库里有什么

**解决方案：** 把相关信息"临时塞进" Prompt，让 LLM 基于它回答。

这就是 **RAG（Retrieval-Augmented Generation，检索增强生成）**。

---

## RAG 工作流程

```
离线阶段（一次性预处理）：

知识库文档（PDF/Word/网页/代码）
    ↓
[文本分块（Chunking）]
    ↓
[Embedding 模型] → 把每个 Chunk 变成向量
    ↓
[向量数据库] ← 存储所有文档的向量表示


在线阶段（每次查询）：

用户提问
    ↓
[Embedding 模型] → 把问题变成向量
    ↓
[向量相似度检索] → 找 Top-K 最相关 Chunk
    ↓
[构建 Prompt] = 检索到的内容 + 用户问题
    ↓
[LLM 生成] → 基于检索内容回答
    ↓
最终回答
```

---

## 核心组件

### 1. Embedding 模型

把文字变成数字向量（float 数组）：

```python
"今天天气很好" → [0.12, -0.43, 0.87, ...]  # 1536 维向量
"The weather is nice today" → [0.11, -0.41, 0.89, ...]  # 语义相似，向量相近！
```

语义相似的文字，在向量空间中距离近。

**常用 Embedding 模型：**
| 模型 | 提供方 | 特点 |
|------|--------|------|
| text-embedding-3-small | OpenAI | 便宜，效果好 |
| text-embedding-3-large | OpenAI | 最强，贵 |
| bge-m3 | 智源 | 开源，中文好 |
| nomic-embed | Nomic | 开源，免费 |

---

### 2. 向量数据库

专门存储和检索向量的数据库：

| 数据库 | 特点 | 适合 |
|--------|------|------|
| **Chroma** | 轻量，开源，本地 | 原型开发 |
| **Qdrant** | 开源，高性能 | 生产环境 |
| **Pinecone** | 云服务，全托管 | 快速上线 |
| **Weaviate** | 开源，GraphQL | 复杂查询 |
| **pgvector** | PostgreSQL 扩展 | 已有 PG 的团队 |
| **Milvus** | 国内阿里生态 | 大规模企业 |

---

### 3. 文本分块（Chunking）

把长文档切成合适大小的片段：

```
# 按固定大小
chunk_size = 512 tokens
overlap = 50 tokens（相邻块有重叠，保持上下文连续）

# 按语义边界（更智能）
- 按段落分割
- 按章节分割
- 按函数分割（代码）
```

**分块质量直接影响检索效果！** 太长会引入噪音，太短会丢失上下文。

---

## 简单代码示例

```python
from openai import OpenAI
import chromadb

client = OpenAI()
chroma = chromadb.Client()
collection = chroma.create_collection("docs")

# 1. 建立知识库
documents = ["公司请假规定...", "报销流程...", "IT 使用规范..."]
for i, doc in enumerate(documents):
    embedding = client.embeddings.create(
        input=doc, model="text-embedding-3-small"
    ).data[0].embedding
    collection.add(embeddings=[embedding], documents=[doc], ids=[str(i)])

# 2. 查询
query = "员工如何申请年假？"
query_embedding = client.embeddings.create(
    input=query, model="text-embedding-3-small"
).data[0].embedding

results = collection.query(query_embeddings=[query_embedding], n_results=3)
context = "\n".join(results["documents"][0])

# 3. 生成回答
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": f"基于以下内容回答：\n{context}"},
        {"role": "user", "content": query}
    ]
)
print(response.choices[0].message.content)
```

---

## RAG vs 微调（Fine-tuning）

| 维度 | RAG | 微调 |
|------|-----|------|
| 更新知识 | 更新文档即可，实时 | 需要重新训练，耗时耗钱 |
| 成本 | 低（主要是存储） | 高（GPU 训练） |
| 幻觉风险 | 低（有文档支撑） | 较高 |
| 适合 | 知识查询、QA | 改变模型风格/能力 |
| 不适合 | 需要模型"内化"知识 | 需要实时更新 |

**结论：** 大多数企业知识库场景，RAG 是更优选择。

---

## 进阶：混合检索

只用向量搜索有时效果不好（关键词匹配失败）。
混合检索结合两种方式：

```
向量搜索（语义）+ BM25（关键词）→ RRF 融合排序 → 最终结果
```

**Reranker（重排序）**：检索后用专门的模型对结果重新打分，提升精度。

---

## 企业落地建议

1. **从简单开始**：先用 LangChain / LlamaIndex 快速原型
2. **数据质量是关键**：垃圾进垃圾出，文档要清洗
3. **评估检索质量**：检索对了，回答才可能对
4. **考虑混合检索**：纯向量搜索可能漏掉精确关键词匹配
5. **Chunk 策略很重要**：不同文档类型用不同分块方式

---

## 常用框架

| 框架 | 特点 |
|------|------|
| **LangChain** | 功能最全，生态最大 |
| **LlamaIndex** | 专注 RAG，更简洁 |
| **Dify** | 可视化平台，国内流行 |
| **FastGPT** | 开源，国内部署方便 |

---

## 下一步

- [M4-03 Agent 原理](./03-agent.md) — RAG + Agent = 强大的 AI 应用
