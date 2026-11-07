# M3-03 · 其他主流 AI 编程工具

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02
>
> 本页按「2026-11 现状 → 关键信息 → 变化/历史」组织。已改名、被收购、停运或进入维护模式的项目会明确标注。

---

## 一句话结论

2026 年工具格局最大的变化不是「又多了几个工具」，而是**一批老名字消失或易主**：Windsurf 更名 Devin Desktop，Gemini CLI 退居企业版、个人入口让位给 Antigravity CLI，Continue 仓库只读，Aider 进入低维护状态。选型时**先确认项目是否还在活跃维护**，再谈能力强弱。

---

## Claude Code（Anthropic）

> 终端优先的 Agent，2026 年已扩展到 IDE、桌面、Web、移动和 Slack。

**2026-11 现状：**
- 形态：终端 CLI、VS Code / JetBrains 扩展、桌面 App、Web（claude.ai/code）、iOS / Android、Slack、Chrome
- 模型：Claude 5.5 家族（Opus / Sonnet / Haiku）+ Fable 5.1
- 计费：含在 Claude 付费计划（Pro $20/月起），也可用 API 按 token 计费
- 关键能力：子 Agent、**Agent Teams（实验，需 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`）**、Skills、Plugins、Hooks、Projects、定时任务、代码审查、沙箱权限

**适合：** 代码库级改造、终端自动化、CI/CD、长任务；已经用 Claude 订阅的团队几乎零额外成本。

**变化提示：**
- Agent Teams 默认关闭，属于实验特性，token 成本明显高于单会话；顺序任务/同文件修改不建议用。
- 2026 年 Claude Code 的入口从「终端」扩到「桌面 + Web + 移动 + Slack」，团队需要重新定义「在哪跑」。
- 详见 [M5-08 Claude 配置](../05-practical/08-claude-setup.md) 与 [官方文档](https://code.claude.com/docs/en/overview)。

---

## OpenAI Codex（OpenAI）

> 从 CLI 长成「CLI + IDE + Cloud + App + SDK」的完整 Agent 产品线。

**2026-11 现状：**
- 形态：Codex CLI、IDE 扩展、Codex Cloud、macOS / Windows 桌面 App、Codex SDK、Codex Micro
- 模型：GPT-6 家族——Astra（旗舰）、6.1 Sol、6.1 Terra、Luna
- 计费：含在 ChatGPT 计划（Free / Go / Plus / Pro / Business / Enterprise）；超出用量买 credits
- 关键能力：`AGENTS.md`、子 Agent、云端任务、Codex Security、审批与沙箱

**适合：** 终端推理、云端异步任务、OpenAI 生态；已经在用 ChatGPT 付费计划的团队。

**变化提示：**
- 2026-09-03 GPT-6 Astra 发布（09-04 起公开；1.05M 上下文、128K 输出）；2026-09-29 GPT-6.1 Sol 发布（$2/$10 per MTok）。
- Codex 不再只是 CLI：云端任务、App、SDK 都是正式入口，团队要统一「哪种任务放云端」的规则。
- 来源：[OpenAI Codex 定价](https://chatgpt.com/codex/pricing/)、[模型文档](https://developers.openai.com/api/docs/models)（2026-11）。

---

## Gemini CLI / Antigravity CLI（Google）

> Gemini CLI 仍在，但已「企业化」；个人用户和 Gemini 4 的新入口是 Antigravity CLI。

**Gemini CLI 现状（2026-11）：**
- 只面向 **Gemini Code Assist Standard / Enterprise** 和 **Code Assist for GitHub**（Google Cloud）许可证用户。
- **没有免费层，也不再接 Google AI Pro / Ultra**；个人入口已于 **2026-06-18** 迁移到 [Antigravity CLI](https://antigravity.google/product/antigravity-cli)。
- 官方明确说明：**未针对 Gemini 4+ 优化**，不要用它给 Gemini 4 跑 benchmark。
- 仓库仍活跃（约 108.8k stars，2026-11），但定位收窄。

**Antigravity CLI（`agy`）现状：**
- 面向交互式多 Agent 编码终端，支持 Gemini 4 Argon+、免费/Google AI Pro & Ultra 账号、Google Cloud。
- 子 Agent 面板（`/agents`）、斜杠命令、`/config`、`/keybindings`。
- 与 Antigravity App / IDE / SDK 共用一套 Agent 运行时。

**适合：** 企业 Google Cloud 用户继续用 Gemini CLI；个人和新项目优先评估 Antigravity CLI。

来源：[Gemini CLI README](https://github.com/google-gemini/gemini-cli)、[Antigravity CLI](https://antigravity.google/product/antigravity-cli)（2026-11）。

---

## GitHub Copilot（GitHub / Microsoft）

> 从「补全插件」变成「多入口 AI 编码 Agent」，并把第三方 Agent 接进来。

**2026-11 现状：**
- 形态：VS Code、Visual Studio、JetBrains、Eclipse、Xcode、Vim/Neovim、Zed；桌面 App、CLI、Web、Mobile、Slack、Teams
- 模型：多模型可选（含 Claude Opus、GPT-6 系列），也可接自己的 API Key、Ollama、Foundry Local
- 计费：Free $0 / Pro $10 / Pro+ $39 / Max $100；Agent 用量走 AI Credits（Pro $15、Pro+ $70、Max $200 额度）
- 关键能力：Agent mode、cloud agent、Copilot code review、定制 instructions / agents
- **第三方 Agent**：Pro+ 起可委派 Claude Code 和 Codex（预览）

**适合：** 已深度使用 GitHub 的团队、JetBrains / VS Code 混合团队、合规要求高的企业。

**变化提示：**
- 2026 年 Copilot 的「护城河」从补全转向 **GitHub 工作流集成**（Issue → Agent → PR → Review → Merge）。
- 补全和 next edit 不消耗 credits，但 Agent 会话按模型与复杂度计费，团队要设预算。
- 来源：[Copilot 功能页](https://github.com/features/copilot)、[Plans & pricing](https://github.com/features/copilot/plans)（2026-11）。

---

## Windsurf → Devin Desktop（Cognition）

> **已改名**：Windsurf 于 2026-06-02 更名为 Devin Desktop，成为 Cognition Devin 平台的 IDE 入口。

**2026-11 现状：**
- 形态：本地 IDE（VS Code 系）+ Devin Cloud 异步 Agent 统一订阅
- 计费（第三方口径，2026-10）：Free、Pro $20/月、Max $200/月、Teams $80/月起 + $40/座；**以官网为准**
- 能力：本地编辑 + 云端 Devin 会话管理、MCP、企业合规（SOC 2 / ISO 27001 / FedRAMP High）

**适合：** 想同时拥有「本地 IDE」和「异步云端 Agent」的团队；已经在用 Devin 的团队。

**历史：**
- 2025-07：Cognition 收购 Windsurf（Google 另聘走部分高管）。
- 2026-05-28：Cognition 以 $26B 估值融资 >$1B，年化收入 $492M。
- 2026-06-02：Windsurf 品牌更名为 Devin Desktop。

> ⚠️ 旧文章里的 `windsurf.com` / Codeium 入口可能不再是最新入口，引用前先核对官网。

---

## Google Antigravity 2.0（Google）

> 2026-05-20 发布 2.0，从「Agent IDE」升级为 **App + IDE + CLI + SDK** 的 Agent 平台。

**2026-11 现状：**
- 形态：桌面 App（macOS / Windows / Linux / Googlebook）、IDE 扩展、CLI（`agy`）、SDK、Extensions
- 模型：Gemini 4 系列（Argon / Carbon），2.0 发布时以 Gemini 3.5 Flash 驱动部分功能
- 计费：个人 Free $0；Google AI Pro / Ultra（Ultra $100、$200 档）；Business 经 Google Cloud，$30+/座/月
- 关键能力：多 Agent 并行、动态子 Agent、定时任务（cron）、Artifacts、Skills、Projects、语音输入

**适合：** 想用 Gemini 4、需要「多 Agent 编排 + 定时任务」的团队；已经买 Google AI Pro / Ultra 的用户。

**变化提示：**
- Antigravity 2.0 的 CLI 是 Google 新一代终端入口，**Gemini CLI 个人用户被引导迁移到这里**。
- 2026-10 Gemini 4 Argon / Carbon 发布后，Antigravity 成为 Gemini 4 的主要编程入口之一。
- 来源：[Antigravity 官网](https://antigravity.google/product/antigravity-2)、[定价](https://antigravity.google/pricing)、[官方博客](https://antigravity.google/blog/google-io-2026)（2026-11）。

---

## Kiro（AWS）

> AWS 的「Agent 开发环境」，已承接 Amazon Q Developer 的编码用户。

**2026-11 现状：**
- 形态：桌面 IDE、CLI、Web、移动 App、**Kiro Crew**（持久化 Agent 工作区）
- 模型：Auto 混合模型；可选 GPT-5.6（Sol / Terra / Luna）、Claude（Opus 5 / 4.8、Sonnet 5 / 4.6 / 4.5、Haiku 4.5）、开源权重模型（DeepSeek 3.2、MiniMax M2.5、GLM-5、Qwen3 Coder Next）
- 计费：Free 50 credits；Pro $20 / Pro+ $40 / Pro Max $100 / Power $200；团队 $20/座（500 credits/座/月）+ 加购 $0.04/credit
- 关键能力：Spec 驱动开发、Steering、Agent hooks、Kiro Crew bots（2026-11 新增）

**适合：** AWS 生态团队、规格驱动/强流程团队、需要 credits 预算可控的团队。

**变化提示：**
- 2026-11 Kiro 推出 **Crew bots**：每个 bot 是命名、长期运行、带独立记忆的 Agent，账单统一走 Kiro 计划。
- Amazon Q Developer 的用户被引导迁移到 Kiro；老文档里的 Amazon Q 入口要更新。
- 来源：[Kiro 定价](https://kiro.dev/pricing/)、[The Register 报道](https://www.theregister.com/ai-and-ml/2026/11/05/aws-kiro-aims-to-solve-identity-crisis-by-adding-another-identity-bot-orchestrator/5307965)（2026-11-05）。

---

## Kimi Code（月之暗面）

> 国内团队可用的开源终端 Agent。

**2026-11 现状：**
- 形态：CLI（`kimi`），开源 **MIT**，官方安装脚本，无需 Node.js
- 版本：**2.5.2**（2026-11-06，npm `@moonshot-ai/kimi-code`）
- 能力：读写代码、执行命令、搜索文件、抓取网页；Skills、子 Agent、MCP、视频/录屏输入
- 模型：默认接 Kimi 模型，可配置兼容 provider
- 仓库：约 8.2k stars（2026-11）

**适合：** 数据不能出境、需要可自部署/可审计的国内团队；长上下文任务。

来源：[Kimi Code GitHub](https://github.com/MoonshotAI/kimi-code)、[文档](https://moonshotai.github.io/kimi-code/en/)（2026-11）。

---

## MiniMax Code（MiniMax）

> MiniMax 的「一体化通用 Agent」，绑定自家 M3 / M3.1 Flash 模型。

**2026-11 现状：**
- 形态：通用 Agent 产品（Web / 客户端），面向任务执行而不只是代码补全
- 模型：MiniMax M3、M3.1 Flash（开源权重多模态模型）
- 适合：国内团队、需要多模态/低成本的通用 Agent 任务

> 具体套餐与功能以 [MiniMax 官网](https://www.minimax.io/) 为准；本课程暂不展开。

---

## Aider（开源 CLI）

> 老牌开源结对编程 CLI，2026 年进入低维护状态，使用前需评估。

**2026-11 现状：**
- 形态：Python CLI，支持 100+ 模型（含本地 Ollama）
- 能力：自动 git commit、多模型切换、repo map
- 仓库：约 50.0k stars；**最后一次实质代码提交为 2026-05-22**
- 社区在 2026-08 发起 issue 讨论维护状态，维护者长期未回应

**建议：** 仍可用于稳定的本地/多模型场景，但**不要把它作为唯一主力**；新项目优先评估 Cline / Kimi Code / Codex CLI。

来源：[Aider GitHub](https://github.com/Aider-AI/aider)、[维护状态讨论 #5647](https://github.com/Aider-AI/aider/issues/5647)（2026-08）。

---

## Cline（开源 Agent）

> 开源、可自带模型的 IDE + 终端 + 桌面 Agent。

**2026-11 现状：**
- 形态：VS Code 扩展、CLI、桌面 App
- 模型：自带 API Key，支持多 provider
- 能力：Plan / Act 模式、MCP、checkpoint、终端执行
- 仓库：约 71.4k stars，持续活跃（2026-11 仍有提交）

**适合：** 想掌控模型、数据与成本的团队；需要审计 Agent 行为的场景。

来源：[Cline GitHub](https://github.com/cline/cline)（2026-11）。

---

## Continue（开源，已进入维护模式）

> **重要变化**：`continuedev/continue` 仓库已不再积极维护，**对所有用户只读**。

**2026-11 现状：**
- 形态：CLI、VS Code 扩展、JetBrains 插件（最终 **2.0.0** 版本）
- 能力：开源编码 Agent、可接本地/云端模型
- 状态：仓库只读，不再合并 PR；约 36.4k stars

**建议：** 新项目不要选 Continue 作为长期方案；已有项目可继续用 2.0.0，但要规划迁移（Cline / Aider / 各厂商官方 Agent）。

来源：[Continue GitHub](https://github.com/continuedev/continue)（2026-11）。

---

## v0（Vercel）

> 从「UI 生成器」扩展为「全栈应用生成 + 部署」。

**2026-11 现状：**
- 形态：Web（[v0.app](https://v0.app) / v0.dev）
- 能力：自然语言生成全栈应用、连接 GitHub、设计系统、数据库/API 集成、一键部署到 Vercel
- 计费：免费 + 订阅；支持「用你的 ChatGPT 计划」登录
- 适合：前端原型、全栈小应用、产品验证

**变化提示：**
- 2026 年的 v0 已不只生成 React 组件，而是「Plan → 建任务 → 连数据库 → 部署」的 Agent 式流程。

---

## 工具现状汇总（2026-11）

| 工具 | 2026-11 状态 | 形态 | 计费口径 | 一句话建议 |
|------|-------------|------|----------|-----------|
| **Claude Code** | 活跃 | CLI / IDE / 桌面 / Web | 订阅 / API | 代码库级任务首选之一 |
| **OpenAI Codex** | 活跃 | CLI / IDE / Cloud / App | ChatGPT 计划 / credits | OpenAI 生态首选 |
| **Gemini CLI** | 收窄为企业版 | CLI | Code Assist 许可 | 仅企业 Cloud 用户 |
| **Antigravity CLI** | 活跃（接替个人 Gemini CLI） | CLI / App / IDE / SDK | 免费 / AI Pro / Ultra | Gemini 4 新入口 |
| **GitHub Copilot** | 活跃 | 插件 / 桌面 / CLI / 云 | 订阅 + credits | GitHub 团队默认选项 |
| **Devin Desktop（原 Windsurf）** | 活跃（已改名） | IDE + 云 | 订阅 | 要 Devin 云才选 |
| **Antigravity 2.0** | 活跃 | App / IDE / CLI / SDK | 免费 / 订阅 / Cloud | 多 Agent 编排 |
| **Kiro** | 活跃 | IDE / CLI / Web / Crew | credits 订阅 | AWS / 规格驱动 |
| **Kimi Code** | 活跃 | CLI | 开源 + 模型费 | 国内合规/自部署 |
| **MiniMax Code** | 活跃 | Web / 客户端 | 以官网为准 | 国内通用 Agent |
| **Cline** | 活跃 | IDE / CLI / 桌面 | 开源 + 模型费 | 自带模型、可控 |
| **Aider** | 低维护 | CLI | 开源 + 模型费 | 可用但别做唯一主力 |
| **Continue** | 已只读 | CLI / 插件 | 开源 + 模型费 | 不建议新项目采用 |
| **v0** | 活跃 | Web | 免费 + 订阅 | 前端/全栈原型 |

---

## 历史沿革

- **2026-11**：新增 Kiro Crew bots；Kimi Code 2.5.2；Aider 低维护、Continue 只读被明确标注。
- **2026-10**：Gemini 4 Argon（10-13）/ Carbon（10-28）发布；Antigravity 成为 Gemini 4 主要入口。
- **2026-09**：GPT-6 Astra（09-03 发布 / 09-04 公开）、GPT-6.1 Sol（09-29）、Claude 5.5 家族陆续发布。
- **2026-06**：Windsurf 更名 Devin Desktop（06-02）；Gemini CLI 个人入口迁移到 Antigravity CLI（06-18）；SpaceX 收购 Anysphere（06-16）。
- **2026-05**：Antigravity 2.0 发布（05-20）；Cognition 融资 $1B / 估值 $26B（05-28）。
- **2026-04**：本页旧版按「稳态信息」写法，主要保留工具定位，价格与版本被删除；现已恢复 2026-11 快照。
- **2026-03**：Cursor 支持 JetBrains ACP；本课程统一 Cursor Rules 写法。
- **2025**：Windsurf 被 Cognition 收购；Gemini CLI 以「免费开源」快速起量；Aider 仍是主流开源 CLI。
- **2024 及以前**：Copilot 补全 + Cursor Tab 为主，CLI Agent 尚未成为独立品类。

---

## 下一步

- [M3-04 AI 编程工具底层原理](./04-how-it-works.md)
- [M5-08 Claude 正确配置与使用](../05-practical/08-claude-setup.md)
- [M11-05 Claude Code 省 Token 指南](../11-dev-tools/05-claude-code-token-optimization.md)
