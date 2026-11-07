# M8-03 · 效率工具类 MCP

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 打通 Slack、Notion、Google Workspace、网页抓取，让 AI 帮你处理沟通与信息管理。**2026 年的关键词：官方远程 MCP + OAuth + 按功能/范围授权。**

---

## 一句话结论

效率类 MCP 是"官方接管"最彻底的一类：

- **Slack** 在 2026-02-17 发布官方 MCP Server，并配套 Real-time Search API（RTS），把搜索权限拆成 `search:read.public / private / im / mpim` 细粒度 scope。
- **Notion** 提供官方 MCP（远程 + 本地），支持 OAuth 与企业托管授权。
- **Google Workspace** 提供官方 MCP servers（Drive / Gmail / Calendar 等），由管理员在 Google Cloud 侧配置。
- 旧的 `server-slack`、`server-gdrive` 参考实现已归档。

> 效率类 MCP 的风险不在"能不能连"，而在**能读到多少别人的数据**。授权前先想清楚 scope。

---

## 2026-11 现状速查

| MCP | 形态 | 维护方 | 访问方式 | 风险提示 |
|-----|------|--------|----------|----------|
| **Slack MCP** | 官方（SaaS） | Slack | OAuth / bot token | 频道、私信、搜索范围都要显式授权 |
| **Notion MCP** | 官方远程 + 本地 | Notion | OAuth / 集成 token | 页面级共享；企业可托管授权 |
| **Google Workspace MCP** | 官方（自建配置） | Google | OAuth + Cloud 项目 | 管理员需配置同意屏与安全策略 |
| **Fetch MCP** | 官方参考实现 | MCP 项目组 | 本地 stdio | 抓取内容可能含 prompt injection |
| ~~Slack 参考服务器~~ | — | — | — | **已归档**，曾由 Zencoder 接手维护 |
| ~~Google Drive 参考服务器~~ | — | — | — | **已归档** |

---

## Slack MCP ⭐

**功能：** 让 AI 在 Slack 里搜索、读取、总结、起草回复，并作为 agent 的沟通入口。

**2026 年变化：**

- 官方 MCP Server（2026-02-17 发布）：工具描述与返回面向 LLM 设计，返回自然语言结果。
- Real-time Search API（RTS，原 Data Access API 演进）：不要求第三方存储客户数据。
- 搜索 scope 细分为：`search:read.public`（必需）、`search:read.private`、`search:read.im`、`search:read.mpim`（后三者需用户同意）。
- 2026-06-18 起还有 **Slackbot MCP Client**：让 Slack 里的 agent 反过来调用外部 MCP。

**配置思路：** 在 Slack 侧创建/安装 app，取得 bot token 或走 OAuth，再把 MCP server 地址与凭据填进客户端。具体字段以 [Slack MCP 文档](https://docs.slack.dev/ai/slack-mcp-server) 为准。

**典型用法：**

```
你：总结 #tech-discuss 今天的重要讨论
AI：[检索频道消息 → 提取决策/待办 → 输出摘要]

你：把 #project-alpha 里关于上线的讨论整理成 checklist
AI：[跨消息聚合 → 生成清单]
```

⚠️ **注意：** 能读私信/私有频道是高风险能力。默认只给 public，需要时再申请细粒度 scope；离职/项目结束时记得撤销授权。

---

## Notion MCP ⭐

**功能：** 读写 Notion 页面与数据库，把调研结果沉淀到知识库。

**2026 年变化：**

- 官方 MCP 提供**远程托管**形态，OAuth 授权，不必自己跑进程。
- 支持 **Enterprise-managed authorization**（企业统一管控授权）。
- 官方单独维护"Skills via MCP"与"MCP 安全最佳实践"文档。

**配置思路：**

1. 在 Notion 里创建集成/授权 MCP 客户端；
2. 把目标页面或数据库**显式共享**给该集成；
3. 在客户端填入远程 URL（或本地命令），完成 OAuth。

**典型用法：**

```
你：把今天的技术调研整理到「AI 基础设施」数据库
AI：[创建页面 → 按既有字段填属性 → 回填链接]
```

来源：[Notion MCP 文档](https://developers.notion.com/guides/mcp/overview)。

---

## Google Workspace MCP

**功能：** 让 AI 读 Gmail、Google Calendar、Google Drive 等 Workspace 数据。

**2026 年状态：** Google 官方提供 Workspace MCP servers，并单独发布"MCP 安全配置"指南；此外还有 Universal Search MCP（`search_corpus`）用于跨 Workspace 内容检索。

**接入要点：**

- 不是"装个 npx 包"那么简单：需要在 Google Cloud 建项目、启用 API、配置 OAuth 同意屏与凭据。
- 企业环境还要管理员在 Workspace 侧配置访问控制与安全策略。
- 具体步骤以 [Google Workspace MCP 配置文档](https://developers.google.com/workspace/guides/configure-mcp-servers) 为准。

**适合：** 邮件摘要、日程整理、文档检索、会议材料准备。

---

## Fetch MCP ⭐ 常用

**功能：** 抓取网页并转成适合 LLM 的文本。

```json
{
  "mcpServers": {
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"]
    }
  }
}
```

**能做什么：**

- 读取第三方 API 文档
- 抓取网页做对比分析
- 检查 URL 是否可访问

**典型用法：**

```
你：读一下这个文档，给我写调用示例
    https://docs.stripe.com/api/charges/create
AI：[抓取正文 → 提取参数 → 生成可运行示例]
```

⚠️ **安全提醒：** 网页内容是不可信输入，可能包含针对模型的指令（prompt injection）。抓取类 MCP 应配合"内容只当资料、不当指令"的系统提示，以及工具审批。

---

## 组合建议：个人效率最小集

```json
{
  "mcpServers": {
    "slack": { "...": "只读 public 搜索" },
    "notion": { "...": "只授权目标数据库" },
    "fetch": { "command": "uvx", "args": ["mcp-server-fetch"] }
  }
}
```

原则：

1. **一个来源一个授权**：不要用一个"全能 token"打通所有 Workspace。
2. **先只读**：读通了再逐项开写权限。
3. **定期复查**：项目结束后撤销不再需要的集成。

---

## 历史沿革

- **2026-11**：Slack 官方 MCP + RTS 细粒度 scope 成为企业推荐做法；Notion 官方远程 MCP 支持企业托管授权；Google Workspace 官方 MCP 需要 Cloud 侧配置。
- **2026-02-17**：Slack 发布官方 MCP Server 与 Real-time Search API（[来源](https://docs.slack.dev/changelog/2026/02/17/slack-mcp)）。
- **2026 年**：`@modelcontextprotocol/server-slack`（归档，后由 Zencoder 维护社区版）、`@modelcontextprotocol/server-google-drive`（归档）逐步退出主流。
- **~~已过时~~ 早期配置（2026-03 版课程）**：
  - Slack：`@modelcontextprotocol/server-slack` + `SLACK_BOT_TOKEN` / `SLACK_TEAM_ID` → 改用 Slack 官方 MCP
  - Notion：`@notionhq/notion-mcp-server` + `OPENAPI_MCP_HEADERS` 环境变量 → 官方已支持远程 + OAuth，旧 header 写法仅在本地/兼容场景保留
  - Google Drive：`@modelcontextprotocol/server-google-drive` → 已归档，改用 Google Workspace 官方 MCP

---

## 下一步

- [⭐️ M8-04 通用工具类 MCP](./04-utilities.md)
- [⭐️ M8-01 开发工具类 MCP](./01-dev-tools.md)
- [⭐️ M8-02 数据库类 MCP](./02-database.md)
