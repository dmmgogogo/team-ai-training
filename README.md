# 🤖 AI 技术培训课程

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 面向技术团队的系统性 AI 课程：从大模型原理，到模型选型、AI 编程工具、Agent 工作方式，再到安全、成本与质量控制。
>
> 这套课程不只回答"现在怎么做"，也记录"我们是怎么走到今天的"——每一次模型迭代、工具更替和认知转变，都在 **[M0 · AI 演进史](./00-history/)** 里留下了痕迹。

| 状态 | 说明 |
|------|------|
| 📅 **内容基准** | 2026-11（时效性内容以此为准，逐篇标注核对日期） |
| 🕰️ **历史快照** | `snapshot-2026-04` / `-07` / `-pre-reorg` / `-11`（git tag） |
| 🔁 **复核节奏** | 高时效内容每季度复核；每周自动体检链接与过期项 |
| 🧰 **维护方式** | 见 [MAINTAINING.md](./MAINTAINING.md) ｜ 变更记录见 [CHANGELOG.md](./CHANGELOG.md) |

---

## 一、这套课程想解决什么

- 理解大模型的工作原理，不再把它当"黑盒"
- 在模型快速迭代的环境里，掌握**选型方法**而不是记模型名
- 上手主流 AI 编程工具，形成可复用的 Agent 工作流
- 建立上下文工程、评测、安全、成本与质量的工程习惯
- 理解 AI 的演进脉络，对"下一个变化"有判断力

---

## 二、怎么用这套课

### 按角色选路线

```
管理者 / 非技术同学
  M0 时间线 → M1-01 → M2 格局 → M5-01 → M5-09 安全 → M5-11 成本

一线开发者
  M0 → M1 全 → M2 选型 → M3 工具 → M5-02 工作流 → M6 项目配置 → M5-10 代码审查

技术负责人 / 架构师
  M0 → M4 原理 → M5-05 多智能体 → M7/M8 生态 → M10 Cloud Agent → MAINTAINING

想系统补课
  M0 → M1 → M2 → M3 → M4 → M5 → M6 → M7 → M8 → M9 → M10 → M11
```

### 阅读约定

- 每篇开头有 **📅 内容基准 / ⏱️ 时效性 / 🔁 下次复核**，先看这三个标签判断可信度。
- 标 **⭐️** 的是核心篇目。
- 每个时效性模块末尾有 **「历史沿革」**，记录该主题的关键版本变化；旧内容不会被删除。
- 内容分层：**稳定层**（原理/方法）｜**时效层**（模型/价格/工具）｜**历史层**（M0，只追加）。

---

## 三、课程地图

### 🕰️ 第 0 部分 · 历史与全景

| 模块 | 主题 | 回答什么问题 | 时效 |
|------|------|--------------|------|
| [M0](./00-history/) | **AI 演进史** | 从 Transformer 到 Agent 时代，发生了什么？我们当时怎么想？ | 只追加 |

### 📚 第 1 部分 · 基础

| 模块 | 主题 | 回答什么问题 | 时效 |
|------|------|--------------|------|
| [M1](./01-llm-basics/) | **AI 大模型基础** | LLM 是什么？Transformer、训练、核心概念怎么理解？ | 低 |
| [M4](./04-principles/) | **底层原理深入** | Attention、RAG、Agent、MCP、上下文工程、评测是怎么回事？ | 低–中 |

### 🧠 第 2 部分 · 模型与工具

| 模块 | 主题 | 回答什么问题 | 时效 |
|------|------|--------------|------|
| [M2](./02-llm-landscape/) | **国内外主流大模型** | 2026-11 的模型格局如何？怎么选？ | 高 |
| [M3](./03-ai-coding-tools/) | **AI 编程工具全景** | Cursor / Claude Code / Codex / Copilot 怎么选、怎么用？ | 高 |
| [M11](./11-dev-tools/) | **开发提效工具** | Token 节省、上下文压缩、工作流约束有哪些工具？ | 高 |

### 🛠️ 第 3 部分 · 工作方式

| 模块 | 主题 | 回答什么问题 | 时效 |
|------|------|--------------|------|
| [M5](./05-practical/) | **实战与最佳实践** | Prompt / 上下文工程、Agent 工作流、Skills、多智能体、安全、成本、代码审查 | 中–高 |
| [M6](./06-ai-project-setup/) | **AI 项目配置规范** | AGENTS.md / CLAUDE.md / .cursor/rules / Skills / MCP 怎么配？ | 中–高 |
| [M7](./07-skills/) | **Skills 精选** | GPT Store、Claude Skills/Plugins、Cursor Rules、OpenCLI 有哪些值得用？ | 高 |
| [M8](./08-mcp/) | **MCP 精选** | 开发/数据库/效率/通用 MCP 怎么选、怎么安全接入？ | 高 |

### 🌐 第 4 部分 · 新形态

| 模块 | 主题 | 回答什么问题 | 时效 |
|------|------|--------------|------|
| [M9](./09-openclaw/) | **OpenClaw 小🦞** | 自托管 AI 网关怎么把 AI 接到 Telegram/Discord？ | 高 |
| [M10](./10-cloud-agent/) | **AI Cloud Agent** | 云端常驻 Agent（Cowork / Cloud Code / Codex Cloud…）怎么用、怎么自建？ | 高 |

---

## 四、2026 年值得注意的变化（截至 2026-11）

> 详细时间线与来龙去脉见 [M0-01 大事记](./00-history/01-timeline.md)，模型版本演进见 [M0-03 模型家谱](./00-history/03-model-lineage.md)。

- **模型进入 5.5 / 6 代号时代**：Anthropic 的 Claude 5.5 家族（Opus / Sonnet / Haiku）与 Fable / Mythos 前沿线；OpenAI 的 GPT-6 家族（Astra 旗舰、Sol / Terra / Luna 分档）；Google 的 Gemini 4 Argon（主力）与 Carbon（前沿限量）；国内 DeepSeek V4 系列、Qwen3.8 Max、Kimi K3.1 Pro、GLM-5.3、MiniMax M3 等陆续开放权重或降价。
- **编程从"补全"变成"托管任务"**：Cursor 3（2026-04）、Claude Code（含 Agent Teams 实验特性）、OpenAI Codex、Google Antigravity 2.0 都能接手跨文件、跨会话的完整任务；Windsurf 更名 Devin Desktop，Gemini CLI 转向企业化，Aider / Continue 进入低维护状态。
- **Agent 的协作形态成熟**：Agent Teams（多会话编排）、Claude Cowork / Duet（常驻与主动式 Agent）、GPT-6 Dots、Codex Cloud、Copilot in the cloud；Google Jules 于 2026-10 宣布关停并并入 Antigravity。
- **Skills / Plugins 成为能力分发方式**：把团队规范、流程、工具封装成可安装的 Skill；Claude 插件市场、Cursor Skills、AGENTS.md 跨工具约定逐步统一。
- **MCP 成为工具接入的通用协议**：2026-07-28 规范加入无状态化、`server/discover`、Tasks 扩展等；Registry 仍为 preview，安全与权限成为落地重点。
- **工程关注点转向 Context Engineering + 评测**：上下文怎么组织、怎么压缩、怎么验证，比"提示词技巧"更决定效果；Agent 的权限、审计与成本成为新的工程课题。
- **11 月第一周又是一波**：腾讯混元 Hy4（11-04，770B/49B，视觉 + Computer Use）、百度 ERNIE 5.5 Flash Base（11-05，280B/14B，开放权重）、字节豆包 Seed-Evolving（11-02）、Thinking Machines Inkling 2 Small（11-05，计划 Apache 2.0）、OpenAI GPT-6 Cyber（11-05）、Gemini Omni 1.2 Flash（11-05）；阿里 Qwen4 已预热，预计 11–12 月陆续发布。
- **产业格局也在变**：Cursor 被 SpaceX 以约 600 亿美元收购（2026-06，据公开报道）；Anthropic 递交 S-1 启动 IPO 流程（2026-10）。这些变化会影响工具的中长期选型。

> ⚠️ 以上是 2026-11 的快照。模型与工具变化极快，具体版本、价格、榜单请以各模块内的官方入口为准。

---

## 五、各模块文件索引

### 🕰️ M0 · AI 演进史
- [M0 导读](./00-history/README.md)
- [M0-01 AI 大事记（2017–2026）](./00-history/01-timeline.md)
- [M0-02 六次范式转移：我们如何与 AI 协作](./00-history/02-paradigm-shifts.md)
- [M0-03 模型家谱：各模型家族的版本演进](./00-history/03-model-lineage.md)
- [M0-04 年度回顾：当年的判断与后来的现实](./00-history/04-yearly-review.md)

### M1 · AI 大模型基础
- [M1-01 什么是大语言模型](./01-llm-basics/01-what-is-llm.md)
- [M1-02 Transformer 架构](./01-llm-basics/02-transformer.md)
- [M1-03 训练过程：预训练、微调与 RLHF](./01-llm-basics/03-training.md)
- [M1-04 核心概念速查](./01-llm-basics/04-key-concepts.md)

### M2 · 国内外主流大模型
- [M2-01 国际主流模型](./02-llm-landscape/01-global-models.md)
- [M2-02 国内主流模型](./02-llm-landscape/02-domestic-models.md)
- [M2-03 模型横向对比与选型](./02-llm-landscape/03-comparison.md)

### M3 · AI 编程工具全景
- [M3-01 AI 编程工具概览](./03-ai-coding-tools/01-overview.md)
- [M3-02 Cursor 使用指南](./03-ai-coding-tools/02-cursor.md)
- [M3-03 其他主流 AI 编程工具](./03-ai-coding-tools/03-other-tools.md)
- [M3-04 AI 编程工具底层原理](./03-ai-coding-tools/04-how-it-works.md)

### M4 · 底层原理深入
- [M4-01 Attention 机制详解](./04-principles/01-attention.md)
- [M4-02 RAG 检索增强生成](./04-principles/02-rag.md)
- [M4-03 AI Agent 智能体原理](./04-principles/03-agent.md)
- [M4-04 MCP 模型上下文协议](./04-principles/04-mcp.md)
- [M4-05 上下文工程](./04-principles/05-context-engineering.md)
- [M4-06 评测与质量闭环](./04-principles/06-evaluation.md)

### M5 · 实战与最佳实践
- [M5-01 ⭐️ Prompt 工程与上下文设计](./05-practical/01-prompt-engineering.md)
- [M5-02 ⭐️ Agentic 开发工作流](./05-practical/02-workflow.md)
- [M5-03 避坑指南与注意事项](./05-practical/03-pitfalls.md)
- [M5-04 Tools：工具调用](./05-practical/04-tools.md)
- [M5-04b ⭐️ Skills：技能扩展](./05-practical/04-skills.md)
- [M5-05 ⭐️ Multi-Agent 多智能体实战](./05-practical/05-multi-agent.md)
- [M5-06 ⭐️ Cursor 正确配置与高效使用](./05-practical/06-cursor-setup.md)
- [M5-07 ChatGPT 正确配置与高效使用](./05-practical/07-chatgpt-setup.md)
- [M5-08 Claude 正确配置与高效使用](./05-practical/08-claude-setup.md)
- [M5-09 ⭐️ AI 安全与数据隐私](./05-practical/09-security-privacy.md)
- [M5-10 ⭐️ 代码审查与质量控制](./05-practical/10-code-review.md)
- [M5-11 ⭐️ 成本管理与模型选型](./05-practical/11-cost-management.md)

### M6 · AI 项目配置规范
- [M6-01 ⭐️ AI 项目配置：从 .cursorrules 到 AGENTS.md（2026）](./06-ai-project-setup/01-cursorrules.md)
- [M6-02 ⭐️ 给 AI 喂上下文：项目文档规范](./06-ai-project-setup/02-ai-context.md)
- [M6-03 MCP 项目集成](./06-ai-project-setup/03-mcp-integration.md)
- [M6-04 ⭐️ 真实案例：全栈项目 AI 配置实战](./06-ai-project-setup/04-real-world-template.md)

### M7 · Skills 精选
- [M7-01 ⭐️ ChatGPT 技能生态（2026：GPT Store 退场，Plugins / Skills 接棒）](./07-skills/01-chatgpt-gpts.md)
- [M7-02 ⭐️ Claude 项目工作区：Projects → Skills / Plugins（2026）](./07-skills/02-claude-projects.md)
- [M7-03 ⭐️ Cursor Rules 社区精选](./07-skills/03-cursor-rules.md)
- [M7-04 ⭐️ OpenCLI：把网站与浏览器变成 AI 可调用的 CLI](./07-skills/04-opencli.md)

### M8 · MCP 精选
- [M8-01 ⭐️ 开发工具类 MCP](./08-mcp/01-dev-tools.md)
- [M8-02 ⭐️ 数据库类 MCP](./08-mcp/02-database.md)
- [M8-03 效率工具类 MCP](./08-mcp/03-productivity.md)
- [M8-04 ⭐️ 通用工具类 MCP](./08-mcp/04-utilities.md)

### M9 · OpenClaw 小🦞
- [M9-01 ⭐️ 什么是 OpenClaw](./09-openclaw/01-intro.md)
- [M9-02 ⭐️ 安装与配置](./09-openclaw/02-setup.md)
- [M9-03 ⭐️ Skills 与 MCP 接入](./09-openclaw/03-skills-mcp.md)

### M10 · AI Cloud Agent
- [M10-01 ⭐️ 什么是 Cloud Agent](./10-cloud-agent/01-what-is-cloud-agent.md)
- [M10-02 ⭐️ Cloud Agent 工作原理](./10-cloud-agent/02-how-it-works.md)
- [M10-03 ⭐️ 如何使用 Cloud Agent（实战）](./10-cloud-agent/03-using-cloud-agent.md)
- [M10-04 自建 Cloud Agent 工作流](./10-cloud-agent/04-build-your-own.md)

### M11 · 开发提效工具
- [M11-01 ⭐️ rtk：Token 节省利器](./11-dev-tools/01-rtk-token-killer.md)
- [M11-02 ⭐️ OpenCLI：把网站和本地工具统一成 CLI Hub](./11-dev-tools/02-opencli-cli-hub.md)
- [M11-03 ⭐️ Superpowers：AI 编程 Agent 完整开发工作流](./11-dev-tools/03-superpowers.md)
- [M11-04 ⭐️ gstack：YC CEO 的 AI 软件工厂](./11-dev-tools/04-gstack.md)
- [M11-05 ⭐️ Claude Code 省 Token 指南](./11-dev-tools/05-claude-code-token-optimization.md)

---

## 六、参考资源

- 📚 [完整参考资源与链接索引](./references.md)（榜单 / 官方文档 / 论文 / 价格）
- 🏆 常用榜单：[LMArena](https://lmarena.ai) · [SWE-bench](https://www.swebench.com) · [Artificial Analysis](https://artificialanalysis.ai/leaderboards/models) · [Epoch AI](https://epoch.ai)
- 📖 学习资源：[Learn Claude Agents](https://www.anthropic.com/engineering/building-effective-agents) · [OpenAI Cookbook](https://cookbook.openai.com) · [Anthropic Docs](https://docs.anthropic.com)

---

## 七、维护与参与

- 维护规范：[MAINTAINING.md](./MAINTAINING.md)（内容分层、更新节奏、来源规范、历史保留、责任分工）
- 变更记录：[CHANGELOG.md](./CHANGELOG.md)
- 自动体检：`python3 scripts/check_docs.py`；CI 每周一生成 `reports/docs-check-report.md`（只报告，不改内容）
- 历史版本：`git tag` 查看 `snapshot-2026-04` / `-07` / `-pre-reorg` / `-11`
- 欢迎提 Issue 或 PR；新增/修改内容请遵循维护指南的元信息与引用规范。

---

*课程持续维护中。AI 领域变化很快，建议每季度回顾一次——但先看内容基准，别把旧快照当成今天的事实。*
