# M1-04 · 核心概念速查

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：低 ｜ 🔁 下次复核：2027-05
>
> 跟 AI 打交道必须懂的术语，按主题分组。2026 年新增的概念已标 🆕。

---

## 一、基础概念

| 术语 | 中文 | 解释 |
|------|------|------|
| **Token** | 词元 | 模型处理的最小单位。英文约 1 Token = 0.75 词；中文约 1 Token = 0.5 个汉字（不同分词器有差异） |
| **Context Window** | 上下文窗口 | 模型一次能处理的最大 Token 数。2026 年旗舰普遍到 1M 级 |
| **Context Rot** 🆕 | 上下文腐烂 | 上下文越长，模型对中间信息的召回与推理越容易退化；窗口大 ≠ 注意力不衰减 |
| **Prompt** | 提示词 | 你给模型的输入，包括指令、背景、示例 |
| **Completion** | 补全/回复 | 模型生成的输出 |
| **Hallucination** | 幻觉 | 模型自信地编造不存在的事实，包括编造引用 |
| **Inference** | 推理/推断 | 使用已训练模型生成输出的过程（≠ 逻辑推理） |
| **Temperature** | 温度 | 控制输出随机性。注意：推理模型通常忽略该参数，改用 effort 控制思考深度 |
| **Top-P / Top-K** | 采样参数 | 控制生成时考虑多少候选词，影响多样性 |
| **Logits** | 未归一化分数 | 模型对每个候选 Token 的原始打分，softmax 后变概率 |

---

## 二、模型能力与推理

| 术语 | 解释 |
|------|------|
| **Reasoning（推理）** | 模型进行逻辑推导的能力；推理模型专门优化了这一点 |
| **Reasoning Model / Thinking Mode** 🆕 | 先花 Token 生成"思考过程"，再给答案；2026 年常以双模式或自适应方式提供 |
| **Reasoning Effort** 🆕 | 思考强度档位，常见 low / medium / high / xhigh / max；越高质量/延迟/成本越高 |
| **Chain of Thought（CoT）** | 让模型一步步思考，而不是直接给答案 |
| **Test-time Compute** 🆕 | 推理时多花算力（更长的思考）换取更好结果，与"训练时堆参数"相对 |
| **Zero-shot** | 不给示例，直接让模型完成任务 |
| **Few-shot** | 给几个示例，引导模型理解任务格式 |
| **In-context Learning** | 模型从 Prompt 中的示例"即时学习"，无需重新训练 |
| **Grounding** | 让模型基于真实数据回答，减少幻觉 |
| **Structured Output** 🆕 | 让模型按 JSON Schema 等固定结构输出，便于程序解析 |

---

## 三、模型结构与参数

| 术语 | 解释 |
|------|------|
| **Parameter（参数）** | 模型可学习的权重数量 |
| **MoE（混合专家）** 🆕 | 前馈网络拆成多个专家，每个 Token 只激活少数几个 |
| **Total Params / Active Params** 🆕 | 总参数决定知识容量，激活参数决定单次推理成本（如 DeepSeek-V4-Pro：1.6T 总 / 49B 激活） |
| **Dense Model** | 每个 Token 都过全部参数的传统模型 |
| **KV Cache** 🆕 | 缓存已计算的 Key/Value，避免重复计算；长上下文与多轮对话的关键优化 |
| **Sparse / Compressed Attention** 🆕 | 只计算部分注意力或先压缩再计算，降低 1M 上下文的成本 |
| **Quantization（量化）** | 压缩模型精度（如 4-bit / FP8 / FP4），减少内存占用，可能轻微损失质量 |
| **GGUF / GGML** | 本地运行量化模型的文件格式，常见于 Ollama、LM Studio |
| **Embedding** | 把文字转化为向量（数字数组），用于语义搜索、聚类、RAG |
| **Multimodal / Native Multimodal** 🆕 | 原生处理文本、图像、音频、视频，而不是外挂一个视觉编码器 |

---

## 四、上下文与成本 🆕

| 术语 | 解释 |
|------|------|
| **Context Engineering** | 上下文工程：把系统提示、工具、检索内容、历史、记忆作为一个整体来设计，而不是只改一句 Prompt |
| **Prompt Caching / Context Caching** | 缓存重复的上下文前缀；命中后按更低价计费，并降低首 Token 延迟。各厂商 TTL 与折扣不同，以官网为准 |
| **Cache Hit / Cache Miss** | 请求是否命中已缓存前缀；系统提示、固定文档、代码库前缀越稳定，命中率越高 |
| **Compaction（压缩）** | 接近上下文上限时，把历史总结成更短的摘要，再继续任务 |
| **Just-in-time Retrieval** | 不预先塞入所有资料，而是让 Agent 在需要时用工具按需读取 |
| **Context Budget** | 一次任务可用的上下文/Token 预算；长任务要主动分配与回收 |

**上下文窗口量级参考（2026-11）**：

| 大小 | 能处理什么 | 2026 年定位 |
|------|-----------|------------|
| 4K / 8K | 短文、单文件 | 历史规格 |
| 128K | 一本书 / 一个中型模块 | 入门级 |
| 200K | 多份文档、较大仓库 | 常见默认 |
| 1M | 多本书、整个中型仓库、长对话 | 2026 旗舰标配 |
| >1M | 超大资料集 | 部分模型支持，具体以官网为准 |

已核实的 1M 级例子：
- **GPT-6 Sol**：1,050,000 Token 上下文，最大输入 922,000，最大输出 128,000（[OpenAI 模型文档](https://developers.openai.com/api/docs/models/gpt-6-sol)，2026-11）
- **Claude Opus 5.5 / Sonnet 5.5**：聊天与 Claude Code 均为 1M Token（[Anthropic 帮助中心](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans)，2026-11）
- **DeepSeek-V4**：1M 上下文为官方服务默认（[DeepSeek 官方](https://api-docs.deepseek.com/news/news260424/)，2026-04-24）
- **Gemini 4 系列**：官方定位为长上下文 + 原生多模态，具体上限以 [官网](https://deepmind.google/models/model-cards/gemini-4-argon/) 为准

---

## 五、Agent 与工具 🆕

| 术语 | 解释 |
|------|------|
| **Agent** | AI 智能体：LLM 在循环中自主使用工具、观察结果、推进目标 |
| **Agent Harness / Scaffold** | 包在模型外面的工程外壳：工具执行、循环、权限、上下文管理 |
| **Tool Call / Function Call** | 让模型调用外部函数/API，获取实时数据或执行操作 |
| **MCP** | Model Context Protocol，标准化 AI 调用外部工具/数据源的开放协议 |
| **Skill** | 可复用的技能包（说明 + 脚本/资源），让 Agent 按需加载专门流程 |
| **Sub-agent** | 子 Agent：在独立上下文里做子任务，只把摘要返回主 Agent，避免主上下文被撑爆 |
| **Agent Teams** | 多个 Agent 并行分工、共享任务板/文件系统的协作方式 |
| **System Prompt** | 在对话开始前给模型的"角色设定"和"规则说明" |
| **Memory** | 跨会话保存的偏好/事实/项目状态；模型本身无状态，靠外部系统实现 |
| **Human-in-the-loop** | 关键步骤让人确认或审批，而不是全自动执行 |

---

## 六、质量与评测 🆕

| 术语 | 解释 |
|------|------|
| **Eval（评测）** | 给 AI 一组任务，用评分逻辑衡量成功率；Agent 评测通常看最终状态而不只看回答 |
| **Grader** | 评分器：代码断言、单元测试、LLM 评审、人工评审 |
| **pass@k / pass^k** | k 次尝试至少成功一次 / k 次全部成功；后者衡量稳定性 |
| **Groundedness** | 回答是否有检索到的证据支撑 |
| **Citation Accuracy** | 引用是否真实存在、是否支持对应结论（2026 年高频翻车点） |
| **Regression Eval** | 回归评测：确保改 Prompt / 换模型后没把旧能力弄坏 |

---

## 七、常用参数参考

### Temperature 使用建议（仅对支持该参数的模型有效）

| Temperature | 适合场景 |
|-------------|---------|
| 0 ~ 0.3 | 代码生成、数据提取、精确回答 |
| 0.5 ~ 0.7 | 问答、分析（默认推荐）|
| 0.8 ~ 1.0 | 创意写作、头脑风暴 |

> ⚠️ 2026 年注意：推理模型 / Thinking 模式通常**不支持或忽略** temperature、top_p 等采样参数（例如 DeepSeek Thinking Mode 官方文档明确说明）。此时用 `reasoning_effort` / `effort` 控制"想多深"，用系统提示控制"写多长"。

### Reasoning Effort 使用建议（以 Claude 官方档位为例）

| 档位 | 适合场景 |
|------|---------|
| `low` | 简单任务、分类抽取、子 Agent、追求低延迟 |
| `medium` | 常规问答、平衡成本与质量（部分模型默认） |
| `high` | 复杂推理、难代码问题、Agent 任务（多数模型默认） |
| `xhigh` | 长时间 Agent / 编程任务（30 分钟以上） |
| `max` | 极难问题、可接受高成本；简单任务容易"过度思考" |

来源：[Claude Effort 文档](https://platform.claude.com/docs/en/build-with-claude/effort)（2026-11）。GPT-6 Sol 还提供 `none`；DeepSeek V4 提供 low / high / max 档。

---

## 八、Token 计算小工具

快速估算：
- 中文 1000 字 ≈ 1500 ~ 2000 Token
- 英文 1000 词 ≈ 1300 Token
- 代码 1000 行（Python）≈ 2000 ~ 4000 Token

在线工具：[OpenAI Tokenizer](https://platform.openai.com/tokenizer)

> 经验法则：**估算成本时按"输入 Token × 单价 + 输出 Token × 单价"算，再把思考 Token 计入输出**。长上下文请求可能有阶梯价（如 GPT-6 Sol 超过 272K 输入后按 2 倍计价，见[模型文档](https://developers.openai.com/api/docs/models/gpt-6-sol)）。

---

## 历史沿革

- **2026**：新增 Context Rot、Reasoning Effort、Prompt Caching、MoE 激活参数、Sub-agent、Skill、Eval 等条目；上下文窗口基线从 128K 抬到 1M。
- **2025**：Reasoning Model、MCP、Agentic RAG、Context Engineering 成为高频词。
- **2024**：Temperature / Top-P / RAG / Tool Call 是主流术语；Context Window 以 128K 为卖点。
- **2023 之前**：Token、Embedding、Fine-tuning、Hallucination 构成入门六件套。

---

## 下一步

- [M2-01 国际主流模型](../02-llm-landscape/01-global-models.md) — 认识主流 LLM
- [M5-01 Prompt 工程与上下文设计](../05-practical/01-prompt-engineering.md) — 学会写好提示词
- [M4-05 上下文工程](../04-principles/05-context-engineering.md) — 系统管理上下文
