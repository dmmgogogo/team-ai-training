# M3-01 · AI 编程工具全景概览

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02
>
> 本页采用「当前快照 + 历史沿革」写法：工具格局、价格、状态是 2026-11 的快照；原理与选型方法长期有效。价格以官网为准。

---

## 一句话结论

截至 2026-11，AI 编程工具的主战场已经从「IDE 里的补全」变成「**Agent 工作台 + 云端 Agent + 终端 Agent**」：Cursor 3 把 IDE 重构成以 Agent 为中心的界面，Claude Code / Codex / Antigravity CLI 在终端和云端并行跑任务，GitHub Copilot 则把第三方 Agent（Claude Code、Codex）接进了自己的入口。**选工具时先选「工作流形态」，再选价格。**

---

## 工具分类（2026-11 版）

```
AI 编程工具
│
├── Agent 工作台 / IDE（人机协作主界面）
│   ├── Cursor 3（Agents Window，多仓库、本地⇄云端交接）
│   ├── GitHub Copilot（VS Code / JetBrains / Xcode / 桌面 App / CLI）
│   ├── Google Antigravity 2.0（App / IDE / CLI / SDK）
│   ├── Kiro（AWS，桌面 IDE / CLI / Web / 移动 / Crew）
│   ├── Devin Desktop（原 Windsurf，Cognition）
│   └── Claude Code / Cursor 的 JetBrains 插件
│
├── 终端 / CLI Agent（自动化、批处理、CI）
│   ├── Claude Code（终端 / IDE / 桌面 / Web / 移动 / Slack）
│   ├── OpenAI Codex（CLI / IDE 扩展 / Cloud / App / SDK）
│   ├── Antigravity CLI（agy，接替 Gemini CLI 的个人入口）
│   ├── Kimi Code CLI（月之暗面，开源）
│   └── Aider（开源，多模型）
│
├── 云端 Agent（异步、长任务）
│   ├── Cursor Cloud Agents
│   ├── Codex Cloud
│   ├── Devin Cloud（Cognition）
│   ├── Copilot cloud agent
│   └── Claude Code on the web
│
├── 开源 / 可自托管 Agent
│   ├── Cline（IDE + 终端 + 桌面）
│   ├── Continue（仓库已只读，最终 2.0.0）
│   ├── Aider
│   └── Kimi Code（MIT）
│
└── 生成式应用类（偏产品与原型）
    ├── v0（Vercel，已扩展到全栈应用）
    └── Lovable / Bolt / Replit 等
```

> 分类是「主形态」，不是「唯一形态」。例如 Cursor 3 同时有 CLI、Cloud Agents 和 Agent SDK；Claude Code 同时有终端、IDE、桌面和 Web。

---

## 主流工具对比（2026-11 快照）

| 工具 | 类型 | 底层模型（可切换） | 价格口径（2026-11） | 特色 | 适合场景 |
|------|------|------------------|--------------------|------|----------|
| **Cursor 3** | Agent 工作台 / IDE | Grok 4.7、Composer 2.5，以及 Anthropic / OpenAI / Google 第三方模型 | Free $0；Plus $8；Premium $30；Super $100；Ultra $200；Teams $30+/人/月；第三方模型按 API 价另计（[官网](https://cursor.com/pricing)，2026-11） | Agents Window、多仓库、本地⇄云端交接、并行 Agent、Agent SDK、插件市场 | 日常主力开发、多人协作、需要 Agent 工作台 |
| **Claude Code** | CLI / IDE / 桌面 / Web | Claude 5.5 家族（Opus / Sonnet / Haiku）与 Fable 5.1 | 含在 Claude 付费计划（Pro $20/月起）；也可用 API 按 token 计费（[官网](https://claude.com/pricing)，2026-11） | 子 Agent、Agent Teams（实验）、Skills / Plugins、Hooks、超长任务 | 代码库级改造、终端自动化、CI |
| **OpenAI Codex** | CLI / IDE / Cloud / App | GPT-6 家族（Astra / 6.1 Sol / 6.1 Terra / Luna） | 含在 ChatGPT 计划（Free ~ Pro $100/$200）；企业按 credits（[官网](https://chatgpt.com/codex/pricing)，2026-11） | CLI + 云端任务、AGENTS.md、子 Agent、Codex Security | 终端推理、云端异步任务、OpenAI 生态 |
| **GitHub Copilot** | 插件 / 桌面 / CLI / 云端 | 多模型可选（含 Claude Opus、GPT-6 系列），可接 Ollama / Foundry Local | Free $0；Pro $10；Pro+ $39；Max $100；另有 AI Credits（[官网](https://github.com/features/copilot/plans)，2026-11） | GitHub 深度集成、PR 审查、第三方 Agent（Claude Code / Codex）预览 | JetBrains / VS Code 团队、合规要求高 |
| **Antigravity 2.0** | App / IDE / CLI / SDK | Gemini 4 系列（Argon / Carbon）等 | 个人 Free $0；Google AI Pro / Ultra（Ultra $100、$200 档）；Business 经 Google Cloud $30+/座/月（[官网](https://antigravity.google/pricing)，2026-11） | 多 Agent 并行、子 Agent 编排、定时任务、CLI + SDK、语音 | 想用 Gemini 4、需要云端 Agent 编排 |
| **Devin Desktop**（原 Windsurf） | IDE + 云端 Agent | 多模型（Claude / GPT 等），按用量计费 | Free；Pro $20/月；Max $200/月；Teams $80/月起 + $40/座（第三方口径，2026-10，以官网为准） | 本地编辑器 + Devin Cloud 会话统一入口 | 想同时要 IDE 和异步云端 Agent |
| **Kiro** | Agent 开发环境 | Auto 混合模型；GPT-5.6、Claude、DeepSeek、MiniMax、GLM、Qwen 等 | Free 50 credits；Pro $20；Pro+ $40；Pro Max $100；Power $200；团队 $20/座（[官网](https://kiro.dev/pricing/)，2026-11） | Spec 驱动、Steering、Kiro Crew bots、AWS 生态 | AWS 团队、规格驱动开发 |
| **Kimi Code** | CLI | Kimi 模型（可配置兼容 provider） | 开源 MIT；模型按 Moonshot 计费（[GitHub](https://github.com/MoonshotAI/kimi-code)，2026-11） | 终端 Agent、Skills、子 Agent、MCP、视频输入 | 国内合规、可自部署、长上下文 |
| **Cline** | IDE / CLI / 桌面 | 自带 API Key，多模型 | 开源免费 + 模型费（[GitHub](https://github.com/cline/cline)，2026-11） | 开源 Agent、计划/执行模式、MCP | 想掌控模型与数据 |
| **Aider** | CLI | 100+ 模型（含本地 Ollama） | 开源免费 + 模型费（[GitHub](https://github.com/Aider-AI/aider)，2026-11） | 自动 git commit、多模型、本地模型 | 多模型切换、本地/离线 |
| **v0** | Web | OpenAI 等（可接 ChatGPT 计划） | 免费 + 订阅（[v0.app](https://v0.app)，2026-11） | 自然语言生成全栈应用、一键部署 | 前端原型、快速验证 |

> 价格均不含税，且厂商调整频繁。**引用前请以官网当日价格为准**；本表只用于建立量级概念。

---

## 市场关键事实（2026）

| 时间 | 事件 | 为什么重要 |
|------|------|-----------|
| 2026-02 | xAI 并入 SpaceX | Grok 与 Cursor 的模型/算力关系开始变化 |
| 2026-03-04 | Cursor 通过 ACP 进入 JetBrains IDE | JetBrains 用户不必换编辑器也能用 Cursor Agent |
| 2026-04-02 | **Cursor 3 发布**：以 Agent 为中心的新界面 | IDE 从「编辑器 + 插件」转向「Agent 工作台」 |
| 2026-05-20 | **Antigravity 2.0** 发布，带 CLI 与 SDK | Google 把 Agent 编排做成 App + CLI + SDK 三层 |
| 2026-05-28 | Cognition 融资 >$1B，估值 $26B，年化收入 $492M | 「独立 Agent 实验室」路线仍被资本认可 |
| 2026-06-02 | Windsurf 更名为 **Devin Desktop** | 老牌 agentic IDE 品牌退出，并入 Devin 平台 |
| 2026-06-16 | SpaceX 宣布以 **$60B** 收购 Cursor 母公司 Anysphere（Q3 完成） | 编程工具成为大模型/算力公司的战略资产 |
| 2026-06-18 | Gemini CLI 的个人免费/Google AI 计划入口迁移到 **Antigravity CLI** | Google 的 CLI 战略从 Gemini CLI 转向 Antigravity |
| 2026-09-03 | OpenAI **GPT-6 Astra** 发布（09-04 起公开） | 编程 Agent 的模型底座换代 |
| 2026-09-22 / 09-28 / 10-07 | **Claude 5.5 家族**：Opus / Sonnet / Haiku 5.5 | Claude Code 的主力模型更新，价格下降 |
| 2026-09-29 | OpenAI **GPT-6.1 Sol** 与 **Dots**（常驻 Agent） | 「常驻 Agent」成为新形态 |
| 2026-10-13 / 10-28 | **Gemini 4 Argon / Carbon** | Gemini 4 成为 Antigravity 的底座 |
| 2026-10-26 | Anthropic 递交 S-1，启动 IPO 流程 | 头部模型公司进入公开市场阶段 |
| 2026-11 | Claude Code **Agent Teams** 仍为实验特性（需环境变量开启） | 多 Agent 协作还没到「开箱即用」 |

来源：Cursor 官方博客与 changelog、Anthropic Newsroom、OpenAI News、Google Blog、Antigravity Blog、Businessworld / Reuters 报道（2026-06）；均为 2026-11 核对。

---

## 选型四问（先问再选）

1. **团队的主战场在哪？**
   - 想留在 IDE：Cursor 3、Copilot、Antigravity、Kiro、Devin Desktop
   - 想以终端/自动化为核心：Claude Code、Codex CLI、Antigravity CLI、Kimi Code、Aider
   - 想异步跑长任务：Cursor Cloud Agents、Codex Cloud、Devin Cloud、Copilot cloud agent、Claude Code Web

2. **预算模型是「订阅」还是「按量」？**
   - 预算稳定：Claude Pro / ChatGPT Plus / Copilot Pro / Cursor Premium 这类订阅
   - 需求波动大：API 按量 + 开源客户端（Cline / Aider / Continue）
   - 注意：很多「订阅」里第三方模型仍按 API 价另计（如 Cursor、Copilot）

3. **合规要求高吗？**
   - 高合规：企业版 / 私有化 / 本地模型（Copilot Enterprise、Claude Enterprise、Kiro、Cline + Ollama）
   - 注意数据是否用于训练、是否支持 SSO / 审计 / 数据驻留

4. **是否需要「多 Agent 并行」？**
   - 需要：Cursor 3、Antigravity 2.0、Claude Code Agent Teams（实验）、Codex 子 Agent
   - 注意：并行 Agent 的 token 成本明显更高，且需要更严格的权限与审查

---

## 团队推荐基线组合（2026-11）

- **Agent 工作台**：Cursor 3 或 GitHub Copilot（二选一，按是否重度用 JetBrains 决定）
- **终端/云端补位**：Claude Code 或 Codex（二选一；预算敏感可用 Antigravity CLI / Kimi Code）
- **本地兜底**：Cline / Aider + Ollama（敏感数据或离线场景）
- **前端提速**：v0（仅用于 UI 草图与全栈原型）
- **治理**：统一模型白名单、统一的 `AGENTS.md` / `.cursor/rules`、统一的审查与成本看板

---

## 官方入口（按需自查最新信息）

| 工具 | 官网 | 文档 |
|------|------|------|
| Cursor | [cursor.com](https://cursor.com) | [cursor.com/docs](https://cursor.com/docs) |
| Claude Code | [claude.com/product/claude-code](https://claude.com/product/claude-code) | [code.claude.com/docs](https://code.claude.com/docs/en/overview) |
| OpenAI Codex | [openai.com/codex](https://openai.com/codex/) | [developers.openai.com/codex](https://developers.openai.com/codex/) |
| GitHub Copilot | [github.com/features/copilot](https://github.com/features/copilot) | [docs.github.com/copilot](https://docs.github.com/en/copilot) |
| Google Antigravity | [antigravity.google](https://antigravity.google) | [antigravity.google/docs](https://antigravity.google/docs/overview) |
| Devin Desktop（原 Windsurf） | [devin.com](https://devin.com) | 以官网为准 |
| Kiro | [kiro.dev](https://kiro.dev) | [kiro.dev/docs](https://kiro.dev/docs/) |
| Kimi Code | [code.kimi.com](https://code.kimi.com) | [moonshotai.github.io/kimi-code](https://moonshotai.github.io/kimi-code/en/) |
| Cline | [cline.bot](https://cline.bot) | [docs.cline.bot](https://docs.cline.bot) |
| Aider | [aider.chat](https://aider.chat) | [aider.chat/docs](https://aider.chat/docs/) |
| v0 | [v0.app](https://v0.app) | 以官网为准 |

---

## 历史沿革

- **2026-11**：本页改为「当前快照 + 历史沿革」；工具分类加入 Agent 工作台、云端 Agent、Agent SDK；价格与市场事实更新到 2026-11。
- **2026-09 ~ 10**：GPT-6 Astra、Claude 5.5 家族、Gemini 4 Argon/Carbon 相继发布，工具底层模型整体换代。
- **2026-06**：SpaceX 以 $60B 收购 Anysphere（Cursor）；Windsurf 更名 Devin Desktop；Gemini CLI 个人入口迁移到 Antigravity CLI。
- **2026-05**：Antigravity 2.0（App + CLI + SDK）发布；Cognition 以 $26B 估值融资。
- **2026-04**：Cursor 3 发布（Agent 为中心的界面）；本课程 M3 曾按「稳态信息」写法删除价格与跑分。
- **2026-04（旧版）**：M3-01 采用「删除易失真硬编码数据」的稳态维护，只保留工具定位与选型方法。
- **2026-03**：Cursor 通过 ACP 支持 JetBrains；本课程统一 Cursor Rules 写法为 `.cursor/rules/*.mdc`。
- **2025 及以前**：工具以 IDE 补全（Copilot / Cursor Tab）和聊天为主，Agent 能力刚起步。

---

## 下一步

- [M3-02 Cursor 使用指南](./02-cursor.md)
- [M3-03 其他主流工具](./03-other-tools.md)
- [M3-04 AI 编程工具底层原理](./04-how-it-works.md)
