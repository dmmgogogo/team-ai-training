# M0-02 · 六次范式转移：我们如何与 AI 协作

> 🕰️ 历史档案 ｜ 记录范围：2022 – 2026-11 ｜ 只追加，不回改
> 📅 内容基准：2026-11 ｜ 时效性：历史层（不做时效复检）

---

## 一句话结论

**每一次范式转移，都不是"新名词取代旧名词"，而是旧方法撞到墙之后，换一种方式分配"人、模型、上下文、工具"的责任。**

理解这一点，遇到下一个新词时就不会慌：先问它解决的是哪堵墙。

---

## 总览：六次转移 + 一次正在进行的延伸

| # | 范式 | 大致时间 | 核心问题 | 一句话 |
|---|------|----------|----------|--------|
| 1 | Prompt Engineering | 2022–2023 | 怎么把话说清楚 | 人写指令，模型一次性回答 |
| 2 | RAG | 2023–2024 | 模型不知道我的数据 | 先检索，再生成 |
| 3 | Tool Use / Function Calling | 2023–2024 | 模型不能行动 | 用结构化协议调用外部能力 |
| 4 | Agentic Engineering | 2025–2026 | 模型能行动，但项目级任务做不完 | 人做编排与验收，Agent 写代码 |
| 5 | Context Engineering | 2025–2026 | 塞得越多，模型越笨 | 管理"进入模型的全部 token" |
| 6 | Skills / Plugins + Multi-Agent | 2025-10 – 2026 | 能力怎么沉淀、怎么分工 | 技能可复用，多 Agent 并行 |
| 7（延伸） | 常驻 / 后台 Agent | 2026 – | 人不在场时，Agent 还能不能干活 | 从"问答"到"持续运行" |

> 注意：这些范式**不是替代关系，而是叠加关系**。2026 年做 Agent，仍然需要 Prompt、RAG、Tool Use、Context Engineering——只是它们退到了"基本功"的位置。

---

## 1. Prompt Engineering（2022–2023）

**为什么出现：** 模型能力够用，但输出不稳定。同样的模型，问法不同，结果天差地别。于是"怎么问"成了一门手艺。

**标志性事件：**

- 2022-11 ChatGPT 普及了"对话式提示"。
- 2022 年 Chain-of-Thought（思维链）论文证明：让模型"一步步想"能显著提升推理表现（[arXiv](https://arxiv.org/abs/2201.11903)）。
- 2023 年"提示词工程师"成为招聘热词。

**当时怎么做：**

- 角色设定（"你是一位资深……"）、Few-shot 示例、分步骤指令、输出格式约束。
- 把提示词当成"一次性魔法咒语"，在一个对话框里反复试。

**现在怎么做：**

- 提示词仍然是基本功，但**不再单独作为方法论**：它被吸收进系统提示、Skills、项目规则（`CLAUDE.md` / `.cursor/rules`）里。
- 评测驱动：用固定测试集比较提示词版本，而不是凭感觉。

**局限：**

- 不解决"模型不知道你的私有数据"（→ RAG）。
- 不解决"模型不能做事"（→ Tool Use）。
- 对长任务、多轮任务不稳定，提示词越写越长，边际收益递减。

---

## 2. RAG：检索增强生成（2023–2024）

**为什么出现：** 企业真正的问题不是"模型会不会聊天"，而是"它不知道我们的文档、制度、代码库"。微调成本高、更新慢，RAG 提供了一条"外挂知识"的捷径。

**标志性事件：**

- 2020 年 RAG 论文提出"检索 + 生成"框架（[arXiv](https://arxiv.org/abs/2005.11401)）。
- 2023 年向量数据库、Embedding、LangChain/LlamaIndex 生态爆发，RAG 成为企业落地默认方案。
- 2024–2025 年"长上下文"崛起，业界开始讨论"RAG 是否会被 1M 上下文取代"。

**当时怎么做：**

- 文档切块（chunking）→ 向量化 → 存向量库 → 用户提问时召回 Top-K → 拼进提示词。
- 关键词检索 + 向量检索的混合检索、重排序（rerank）逐步成为标配。

**现在怎么做：**

- **RAG 没有消失，而是"按需化"**：从"预先建索引、一次性召回"，转向 Agent 的"即时检索"（just-in-time）——模型自己决定去读哪个文件、查哪张表（见 Anthropic 对 context engineering 的总结）。
- 混合架构：`CLAUDE.md` 等稳定上下文直接放入，代码/文档靠 glob、grep、搜索工具在运行时取。
- 评测重点从"召回率"转向"端到端任务成功率"。

**局限：**

- 检索质量决定上限：切块、Embedding、召回策略任一环节出错，模型就会"一本正经地引用错误内容"。
- 索引会过期，维护成本高。
- 上下文窗口变大后，"把所有东西都塞进去"反而引入噪声（→ Context Engineering）。

---

## 3. Tool Use / Function Calling（2023–2024）

**为什么出现：** 模型再聪明，也只能"说"，不能"做"。要查实时数据、改文件、发请求，必须有一个结构化的"手脚"。

**标志性事件：**

- 2023-03 ChatGPT 插件系统：第一次大规模尝试"模型调用外部服务"。
- **2023-06-13 OpenAI 发布 Function Calling**：用 JSON Schema 描述工具，模型输出结构化调用参数，工具调用成为标准 API 能力（[OpenAI](https://openai.com/index/function-calling-and-other-api-updates/)）。
- **2024-11-25 Anthropic 发布 MCP**：把"工具/数据接入"从每家一套私有协议，变成开放标准（[MCP](https://modelcontextprotocol.io/)）。
- 2024-10 Anthropic Computer Use：工具从"API"扩展到"操作电脑"。

**当时怎么做：**

- 手写 function schema，解析模型返回的 JSON，自己实现重试与错误处理。
- 工具数量少、边界清晰，通常是"查天气、查数据库、发邮件"这类单步操作。

**现在怎么做：**

- MCP 成为事实标准：工具、资源、提示词统一描述，客户端/服务器解耦（MCP 于 2025-12 捐赠给 Linux 基金会下的 Agentic AI Foundation）。
- 工具设计本身成为工程问题：工具要"token 高效、职责单一、错误可恢复"（Anthropic 的 tool-writing 指南）。
- 权限、审计、沙箱成为必选项：Agent 能做的事越多，越需要"能做什么/不能做什么"的边界。

**局限：**

- 工具越多，模型越容易选错；"工具爆炸"会显著降低可靠性。
- 错误处理、超时、幂等、鉴权，仍然是工程难点。
- 单次工具调用解决不了"多步骤、长流程"的任务（→ Agentic Engineering）。

---

## 4. Agentic Engineering：从"写代码"到"编排 Agent"（2025–2026）

**为什么出现：** 模型已经能连续调用工具、读写文件、跑测试。人的工作从"敲每一行代码"变成"定义任务、提供上下文、验收结果"。这需要一个新的工程方法论，而不只是"更会写提示词"。

**标志性事件：**

- 2025-02-24 Claude Code 研究预览：终端里的编码 Agent。
- 2025-04-16 OpenAI Codex CLI 开源：本地编码 Agent 另一条路线。
- 2025 年下半年，Cursor、Copilot、Claude Code 等工具普遍支持"多文件修改 + 运行测试 + 迭代"。
- **2026-02-09 Andrej Karpathy 提出 "Agentic Engineering"**：强调"人类做编排与监督，Agent 写代码"是一种有深度、可学习的工程能力（[Times of India](https://timesofindia.indiatimes.com/technology/tech-news/tesla-former-ai-director-andrej-karpathy-who-coined-the-word-vibe-coding-has-a-new-word-for-engineers/articleshowprint/128098180.cms)）。

**当时怎么做（2025 上半年）：**

- "Vibe coding"：一句话让 AI 生成，能跑就行。
- 人肉把报错贴回对话框，反复试。

**现在怎么做（2026）：**

- **规格先行**：写清目标、约束、验收标准，再让 Agent 动手。
- **小步提交 + 自动化验证**：每个 Agent 任务都配测试、lint、类型检查；人只审查"为什么这么改"。
- **上下文资产化**：`CLAUDE.md`、项目文档、Skills 成为团队基础设施。
- **多 Agent 编排**：一个 Agent 做规划，多个子 Agent 并行实现/审查（见第 6 节）。

**局限：**

- **验证是瓶颈**：Agent 写得越快，人审查得越累；没有测试的项目风险极高。
- 长任务会"跑偏"：需要定期对齐目标、检查中间产物。
- 安全边界：Agent 能执行命令、访问网络，提示注入与越权是真实风险（2026-07 OpenAI Agent 自主入侵事件是警钟）。

---

## 5. Context Engineering：管理"模型看到的世界"（2025–2026）

**为什么出现：** 上下文窗口从 8K 涨到 1M，但"能塞"不等于"能用"。研究发现上下文越长，模型对中间信息的召回反而下降（"context rot"）。于是问题从"怎么写提示"变成"每一步该让模型看到什么"。

**标志性事件：**

- 2025-06 Andrej Karpathy 公开使用 "context engineering" 一词。
- 2025-09 Anthropic 发布《Effective context engineering for AI agents》，系统化提出：上下文是有限资源，要"最小化高信号 token"（[Anthropic](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)）。
- 2025-09 Claude Sonnet 4.5 同期推出 memory tool / 上下文管理能力。
- 2026 年，长上下文 + 记忆 + 压缩成为 Agent 产品的标配。

**当时怎么做：**

- 尽量把系统提示写清楚，把资料一次性塞进去。
- 上下文快满时手动开新会话。

**现在怎么做：**

- **压缩（compaction）**：接近上限时总结历史，保留架构决策、未解 bug，丢掉冗余工具输出。
- **结构化笔记 / 外部记忆**：让 Agent 把进度写到文件（`NOTES.md`、任务清单），跨会话恢复。
- **子 Agent 隔离**：子 Agent 在自己的干净上下文里深挖，只把 1–2K token 的结论回传给主 Agent。
- **即时检索**：不预加载全部资料，让 Agent 用工具按需读取。

**局限：**

- 压缩会丢信息：压得太狠，关键细节消失；压得太松，等于没压。
- 记忆需要治理：记错了、记旧了，比不记更危险。
- 没有统一标准，效果高度依赖具体任务与评测。

---

## 6. Skills / Plugins + Multi-Agent：能力沉淀与分工（2025-10 – 2026）

**为什么出现：** 两个问题同时出现：

1. **重复劳动**：每个项目都在重写同样的提示词、脚本、检查清单。
2. **单 Agent 上限**：复杂任务需要"规划 + 执行 + 审查"并行，一个上下文扛不住。

**标志性事件：**

- **2025-10-16 Anthropic 发布 Skills**：把可复用的指令、脚本、资源打包成"技能"，Agent 按需加载（[Simon Willison](https://simonwillison.net/2025/Oct/16/claude-skills/)）。
- 2025-12 Anthropic 发布 **Agent Skills 开放标准**；MCP 捐赠给 Agentic AI Foundation。
- **2026-02-05 Claude Opus 4.6 内置 Agent Teams**：多 Claude Code 会话共享任务、互相消息、协同工作（[TechCrunch](https://techcrunch.com/2026/02/05/anthropic-releases-opus-4-6-with-new-agent-teams/)｜[Docs](https://code.claude.com/docs/en/agent-teams)）。
- 2026-02-24 Cowork 插件市场；2026-09-25 Claude 插件开发者目录开放。
- 2026-08-06 企业版 Skills/插件安全扫描：技能生态开始有"供应链安全"。
- 生态侧：Kimi 的 Swarm（数百并行子 Agent）、Grok Bot（多 Bot 共享云电脑）、Meta Muse Agent 等。

**当时怎么做：**

- 把提示词存成模板，复制粘贴。
- 多 Agent 靠自己写脚本/框架拼，状态同步很脆弱。

**现在怎么做：**

- **技能即资产**：把团队的最佳实践写成 Skill（触发条件、步骤、脚本、验收），版本化管理、按需加载。
- **插件即分发**：把 MCP 服务器 + Skills + 命令打包成插件，团队内一键安装。
- **多 Agent 有明确分工**：Lead 规划与验收，子 Agent 执行，Reviewer 审查；用共享任务板而不是"聊天传递"。
- **先单 Agent，后多 Agent**：只有任务能清晰拆分、且验证成本可控时才上多 Agent。

**局限：**

- 协调成本高：Agent 之间通信、冲突合并、重复劳动都会吃掉收益。
- 技能质量参差：坏技能会稳定地教坏 Agent；需要评审与安全扫描。
- 调试困难：多 Agent 的行为难以复现，可观测性（日志、追踪）是前提。

---

## 7（延伸）常驻 / 后台 Agent：人不在场时也能干活（2026 – ）

**为什么出现：** 前六次转移都默认"人在电脑前，发起一次会话"。但很多工作（监控、日报、巡检、长任务）需要 Agent **持续运行、主动推进、完成后通知**。

**标志性事件：**

- 2026-01-12 Claude Cowork 预览；2026-04-09 正式可用；2026-07-07 上 Web/移动端。
- 2026-02-25 Cowork 支持定时任务；2026-03-17 支持手机上的持久线程；2026-09-16 与聊天合并。
- 2026-08-25 跨会话记忆。
- 2026-10-21 Claude Duet 研究预览：Claude 作为"主动型 Agent"，不等提问就推进任务。
- 同期产品：OpenAI Dots（2026-09-29）、Grok Bot（2026-08-11）、Meta Muse Agent（2026-09-08）、Gemini Spark 等。
- 课程对应模块：[M10 · AI Cloud Agent](../10-cloud-agent/README.md)。

**当时怎么做：**

- 用 cron + 脚本 + API 拼"定时任务"，失败就失败。
- 人盯着终端，任务完成才离开。

**现在怎么做：**

- **任务化**：把"帮我做 X"拆成有输入、有产出、有验收标准的后台任务。
- **可观测**：每个任务有日志、状态、产物链接；失败可重试、可人工接管。
- **权限最小化**：后台 Agent 只能访问完成任务所需的最小范围。
- **通知闭环**：完成/失败推送到 Slack、邮件、IM，而不是让人去"看"。

**局限：**

- 信任问题：后台 Agent 做错事，人可能几小时后才发现。
- 成本不可控：常驻任务会持续消耗 token，需要预算与配额。
- 身份与审计：Agent 以谁的身份操作？出了事谁负责？目前仍在探索。

---

## 一张表：今天（2026-11）怎么用

| 场景 | 优先范式 | 具体做法 |
|------|----------|----------|
| 一次性问答、文案 | Prompt | 结构化提示 + 示例 + 输出格式 |
| 企业知识问答 | RAG + Context | 混合检索 + 引用 + 评测集 |
| 需要实时数据/操作 | Tool Use / MCP | 标准化工具 + 权限 + 审计 |
| 代码库改造 | Agentic Engineering | 规格 + 小步提交 + 测试 + 人审查 |
| 长任务、跨会话 | Context Engineering | 压缩 + 笔记 + 子 Agent |
| 重复流程 | Skills | 把流程写成技能，版本化管理 |
| 复杂项目 | Multi-Agent | 明确分工 + 共享任务板 + 可观测 |
| 监控/巡检/日报 | 常驻 Agent | 定时任务 + 通知 + 最小权限 |

---

## 参考

- [Anthropic · Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)
- [Anthropic · Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [OpenAI · Function calling](https://openai.com/index/function-calling-and-other-api-updates/)
- [Model Context Protocol](https://modelcontextprotocol.io/)｜[Wikipedia: MCP](https://en.wikipedia.org/wiki/Model_Context_Protocol)
- [Claude Code · Agent Teams 文档](https://code.claude.com/docs/en/agent-teams)
- [Claude Release Notes](https://support.claude.com/en/articles/12138966-release-notes)（Cowork / Skills / 插件 / Duet 的时间线）
- [RAG 原始论文（Lewis et al., 2020）](https://arxiv.org/abs/2005.11401)｜[Chain-of-Thought（2022）](https://arxiv.org/abs/2201.11903)
- [Karpathy 谈 Agentic Engineering（2026-02）](https://timesofindia.indiatimes.com/technology/tech-news/tesla-former-ai-director-andrej-karpathy-who-coined-the-word-vibe-coding-has-a-new-word-for-engineers/articleshowprint/128098180.cms)
- 课程内：[M4-02 RAG](../04-principles/02-rag.md)｜[M4-03 Agent](../04-principles/03-agent.md)｜[M4-04 MCP](../04-principles/04-mcp.md)｜[M5-04 Tools](../05-practical/04-tools.md)｜[M5-04b Skills](../05-practical/04-skills.md)｜[M5-05 Multi-Agent](../05-practical/05-multi-agent.md)

---

## 下一步

- [M0-01 · 大事记](./01-timeline.md) —— 每个范式对应的具体日期
- [M0-03 · 模型家谱](./03-model-lineage.md) —— 能力供给侧的版本演进
- [M0-04 · 年度回顾](./04-yearly-review.md) —— 这些判断后来对了吗
- [M5 · 实战与最佳实践](../05-practical/README.md) —— 今天怎么落地
- [返回 M0 导读](./README.md)
