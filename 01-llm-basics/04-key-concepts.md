# M1-04 · 核心概念速查

> 跟 AI 打交道必须懂的术语，一张表说清楚。

---

## 基础概念

| 术语 | 中文 | 解释 |
|------|------|------|
| **Token** | 词元 | 模型处理的最小单位。英文约 1 Token = 0.75 词；中文约 1 Token = 0.5 汉字 |
| **Context Window** | 上下文窗口 | 模型一次能处理的最大 Token 数。超出则截断或遗忘 |
| **Temperature** | 温度 | 控制输出的随机性。0 = 确定性（最可能的词），1+ = 随机（更有创意）|
| **Top-P / Top-K** | 采样参数 | 控制生成时考虑多少候选词，影响多样性 |
| **Prompt** | 提示词 | 你给模型的输入，包括指令、背景、示例 |
| **Completion** | 补全/回复 | 模型生成的输出 |
| **Hallucination** | 幻觉 | 模型自信地编造不存在的事实 |
| **Inference** | 推理/推断 | 使用已训练模型生成输出的过程（≠ 逻辑推理）|

---

## 模型能力相关

| 术语 | 解释 |
|------|------|
| **Reasoning（推理）** | 模型进行逻辑推导的能力，o1/R1 系列专门优化了这一点 |
| **Chain of Thought（CoT）** | 让模型一步步思考，而不是直接给答案，提升准确性 |
| **Zero-shot** | 不给示例，直接让模型完成任务 |
| **Few-shot** | 给几个示例，引导模型理解任务格式 |
| **In-context Learning** | 模型从 Prompt 中的示例中"即时学习"，无需重新训练 |
| **Grounding** | 让模型基于真实数据回答，减少幻觉 |

---

## 部署与架构相关

| 术语 | 解释 |
|------|------|
| **API** | 通过接口调用模型，不需要自己部署 |
| **Model Weights** | 模型权重，即训练好的参数文件，可下载本地运行 |
| **Open Source Model** | 权重开放的模型，如 Llama、DeepSeek、Qwen |
| **Closed Source Model** | 权重不公开，只能调 API，如 GPT-4、Claude |
| **Quantization（量化）** | 压缩模型精度（如 4-bit），减少内存占用，轻微损失质量 |
| **GGUF / GGML** | 本地运行量化模型的文件格式，常见于 Ollama、LM Studio |
| **Embedding** | 把文字转化为向量（数字数组），用于语义搜索 |

---

## RAG 与 Agent 相关

| 术语 | 解释 |
|------|------|
| **RAG** | 检索增强生成，先搜索相关文档，再生成答案 |
| **Vector Database** | 向量数据库，存储 Embedding，用于语义检索（如 Pinecone、Chroma）|
| **Agent** | AI 智能体，能够使用工具、执行多步任务的 LLM 应用 |
| **Tool Call / Function Call** | 让模型调用外部函数/API，获取实时数据或执行操作 |
| **System Prompt** | 在对话开始前给模型的"角色设定"和"规则说明" |
| **MCP** | Model Context Protocol，标准化 AI 调用外部工具的协议 |

---

## 常见参数参考

### Context Window 大小对比
| 大小 | 能处理什么 |
|------|-----------|
| 4K | 约 3000 字，一篇短文 |
| 32K | 约 24000 字，一本短篇小说章节 |
| 128K | 约 96000 字，一整本书 |
| 1M+ | 几本书同时处理（Gemini 1.5 Pro）|

### Temperature 使用建议
| Temperature | 适合场景 |
|-------------|---------|
| 0 ~ 0.3 | 代码生成、数据提取、精确回答 |
| 0.5 ~ 0.7 | 问答、分析（默认推荐）|
| 0.8 ~ 1.0 | 创意写作、头脑风暴 |

---

## Token 计算小工具

快速估算：
- 中文 1000 字 ≈ 1500 ~ 2000 Token
- 英文 1000 词 ≈ 1300 Token
- 代码 1000 行（Python）≈ 2000 ~ 4000 Token

在线工具：[https://platform.openai.com/tokenizer](https://platform.openai.com/tokenizer)

---

## 下一步

- [M2-01 国际主流模型](../02-llm-landscape/01-global-models.md) — 认识主流 LLM
- [M5-01 Prompt 工程入门](../05-practical/01-prompt-engineering.md) — 学会写好提示词
