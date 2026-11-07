# ⭐️ M9-01 · OpenClaw 小🦞 是什么

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> OpenClaw 是一个**自托管的 AI Agent 网关**：把模型、记忆、技能、MCP、自动化接到你已经在用的聊天工具上。
>
> 官网：[openclaw.ai](https://openclaw.ai) ｜ 文档：[docs.openclaw.ai](https://docs.openclaw.ai) ｜ 代码：[github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)

---

## 一句话结论

**截至 2026-11，OpenClaw 没有停止维护，反而进入了"2.0 之后的高频迭代期"。**

- 2026-08 发布 **OpenClaw 2.0（v2026.8.1）**：重建 Web UI、简化引导、SQLite 持久化会话、增强记忆与可靠性。官方给出的规模是 **16,977 个 PR、987 位贡献者**。
- 之后保持高频发布：v2026.9.6（2,614 PR / 350 贡献者）、v2026.10.10（3,028 PR / 454 贡献者）。
- 能力边界从"聊天网关"扩展到：原生桌面/手机 App、云端会话、配对设备工作区、MCP、Skills、事件触发的自动化。

> 版本号与发布日期以 [OpenClaw Releases](https://docs.openclaw.ai/releases) 为准；本文数字来自官方 release notes（2026-11 核对）。

---

## 2026-11 项目快照

| 维度 | 现状 |
|------|------|
| 维护状态 | 活跃（每周级别发布） |
| 最新稳定版 | **v2026.10.10**（2026-10，以官网 Releases 为准） |
| 2.0 版本 | v2026.8.1（2026-08） |
| 协议 | 开源（许可证以仓库 LICENSE 为准） |
| 运行时 | Node.js 24.16+ / 26.1+（推荐 Node 26），也支持 Bun |
| 平台 | macOS、Linux、Windows、iOS/iPadOS、Android、Wear OS |
| 渠道 | Telegram、Discord、Slack、WhatsApp、微信 / 企业微信、飞书、iMessage、Signal、Matrix、Teams、LINE、QQ、短信等 30+ |
| 扩展 | Skills（ClawHub / Skill Workshop）、Plugins、MCP、Automations |
| 社区 | GitHub / Discord / Reddit / X 均有官方入口 |

---

## 它能做什么（2026-11 版）

### 📱 在任意聊天工具里用 AI

```
你的手机 → Telegram / Discord / 微信 / 飞书 / Slack → OpenClaw Gateway → Claude / GPT / Gemini / 本地模型
```

不用记某个 App、不用把工作流绑死在一家厂商；渠道层可以随时换。

### 🤖 有记忆、有性格

- 会话与记忆持久化（2.0 起会话/转录落到 SQLite）。
- 工作区里的 `SOUL.md`（性格）、`USER.md`（关于你）、`MEMORY.md`（长期记忆）、`AGENTS.md`（规则）仍然是个性化入口。
- 支持记忆搜索、记忆来源与删除、可选的外部记忆后端。

### ⚙️ 自动化：定时 + 事件触发

- **定时任务**（Automations / cron）：每天发日程、每周出周报、定时巡检仓库。
- **事件触发**：v2026.10.10 起，支持的 MCP Server 可以上报事件直接触发自动化，不必等轮询（需要公网 HTTPS 回调，只暴露回调路由）。
- **Heartbeat**：轻量周期检查（旧机制，已迁移到 Automations，见历史沿革）。

### 🔧 完整 MCP 支持

- 配置在 `mcp.servers`，支持 **Streamable HTTP / SSE / stdio** 三种传输。
- 支持 OAuth 登录（`openclaw mcp login`）、工具过滤、工具审批、`openclaw mcp doctor --probe` 连通性检查。
- 还能反向把 OpenClaw 暴露成 MCP Server（`openclaw mcp serve`），或用 **MCP Relay** 插件让 ChatGPT / Claude 连进来。

### 🛠️ Skills 与 Plugins

- **ClawHub**：技能市场（安装、发布、审计、遥测开关）。
- **Skill Workshop**：让 agent 提出、校验、应用技能修改，并支持撤销。
- **Plugins**：渠道、模型提供商、工具、UI 扩展都可以插件化。

### 💻 多设备与云端

- 原生 App（macOS 菜单栏、iPhone/iPad、Android、Wear OS）。
- **Cloud sessions**：会话可跑在云端，笔记本合上也能继续。
- **配对设备 / 远程工作区**：Gateway 跑在服务器，agent 可以操作你另一台电脑上的目录（需在设备侧配置允许的根目录）。

---

## 与"直接用官方 App"的对比

| 维度 | ChatGPT / Claude 官方 App | OpenClaw |
|------|--------------------------|----------|
| 渠道 | 官方 App / 网页 | 30+ IM，随便选 |
| 数据位置 | 厂商云 | 你自己的机器/服务器 |
| 模型 | 绑厂商 | 多 provider，可 fallback，可接本地模型 |
| 自动化 | 平台提供的定时/触发 | 自建 cron、事件、心跳、webhook |
| 扩展 | 官方插件/连接器 | Skills + Plugins + MCP，完全可控 |
| 运维 | 厂商负责 | **你负责**（升级、备份、安全、可用性） |
| 成本 | 订阅制 | 订阅/API 费 + 机器成本 + 你的时间 |

> 2026 年官方产品也在快速补齐"主动性"能力（Claude Cowork 的定时任务、Claude Duet 的主动 agent）。OpenClaw 的差异点越来越集中在**渠道自由、数据自持、模型可换**，而不是"只有它能自动化"。

---

## 核心组成（2026-11）

```
OpenClaw Gateway（常驻）
├── 渠道连接（Telegram / Discord / 微信 / 飞书 / Slack / iMessage …）
├── Agent 运行时（会话、上下文、记忆、子 agent、并行工作流）
├── 工具层（内置工具 + MCP + Skills + Plugins）
├── 自动化（Automations / 事件 / Webhook / IMAP / Gmail PubSub）
├── 审批与权限（工具策略、审批绑定到具体请求/会话/人）
└── Control UI（Web / 桌面 / 手机）+ 原生 App + 云端会话
```

---

## 谁适合用

✅ **适合：**

- 有 Mac/Linux/Windows 机器可以长期在线（或愿意上 VPS）
- 想在 Telegram / 微信 / 飞书里直接用 AI，而不是切 App
- 需要定制化工作流、定时任务、事件触发
- 对数据位置、模型选择有要求

⚠️ **不适合：**

- 只偶尔用 AI，不值得维护一个常驻服务
- 没有可长期在线的宿主机
- 团队没有能力处理升级、备份、安全暴露面

---

## 风险与治理提醒

| 风险 | 说明 | 建议 |
|------|------|------|
| 暴露面 | Gateway 对外提供 Web/回调/配对入口 | 只暴露必要端口；用反向代理 + HTTPS；不要把管理端口直接开到公网 |
| 权限过大 | Agent 可执行命令、读写文件、操作浏览器 | 用审批模式、工具策略、沙箱；高风险工具默认 deny |
| 供应链 | 第三方 Skill / Plugin / MCP 可能恶意 | 只装可信来源；关注 ClawHub 安全审计；企业环境先审后装 |
| 提示注入 | 读到的邮件/网页/消息可能含指令 | 把外部内容当资料；敏感动作必须人工确认 |
| 多用户混用 | 不同人共享一个 Gateway 可能互相看到数据 | 用多用户模式 / 独立 Gateway / 容器隔离互不信任的用户 |

---

## 历史沿革

- **2026-10**：v2026.10.10——Chat Details、实验性 Advisor、Split speech、事件触发自动化、MCP Relay。
- **2026-09**：v2026.9.6——托管更新、重启恢复、30 天用量报告、GitHub reader、远程工作区、实时会议纪要。
- **2026-08**：v2026.8.1（**OpenClaw 2.0**）——重建 Web UI、简化引导、会话/转录迁入 SQLite、原生 App、记忆与安全增强。
- **2026-03（课程初版）**：当时定位为"自托管 AI 网关"，渠道以 Telegram / Discord / iMessage 为主，扩展靠 ClawHub Skills，配置用顶层 `mcpServers`，工作区默认 `~/clawd`。这些描述对应 1.x 时代，**安装步骤已移入 [M9-02 历史沿革](./02-setup.md#历史沿革)**。

---

## 下一步

- [⭐️ M9-02 安装与配置](./02-setup.md)
- [⭐️ M9-03 Skills 与 MCP 接入](./03-skills-mcp.md)
- [M8 MCP 精选](../08-mcp/README.md)
