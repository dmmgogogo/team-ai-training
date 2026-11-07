# M4-04 · MCP：模型上下文协议

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：中 ｜ 🔁 下次复核：2027-05
>
> 让 AI 工具互联互通的"USB 接口"。2026 年，MCP 已从 Anthropic 的提案变成 Linux 基金会下的行业标准。

---

## 什么是 MCP？

**MCP（Model Context Protocol）** 是 2024 年底由 Anthropic 提出的开放标准，定义了 AI 模型与外部工具/数据源之间的**标准化通信协议**。

**类比：** 就像 USB 统一了各种设备的接口，MCP 统一了 AI 调用外部工具的方式。

没有 MCP 之前：
```
Cursor 要调用 GitHub → 写专用的 GitHub 集成代码
Claude 要调用 GitHub → 再写一次不同的 GitHub 集成代码
ChatGPT 要调用 GitHub → 又写一次...
```

有了 MCP：
```
任何支持 MCP 的 AI 工具 → 直接用同一个 MCP GitHub Server
```

---

## 2026 年的 MCP：三个关键事实

| 事实 | 说明 | 来源 |
|------|------|------|
| **已捐给 Linux 基金会** | MCP 捐给 **Agentic AI Foundation（AAIF）**，由 Anthropic、Block、OpenAI 共同创立，Google、Microsoft、AWS、Cloudflare、Bloomberg 支持 | [Anthropic 公告](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)，2025 年底 |
| **生态规模** | 超过 **10,000** 个公开 MCP Server；ChatGPT、Cursor、Gemini、Microsoft Copilot、VS Code 等已支持；官方 Registry 上线；Python/TypeScript SDK 月下载量 9,700 万+ | 同上（MCP 一周年数据） |
| **规范持续演进** | 2025-11-25 版本引入异步、无状态、服务端身份、官方扩展；**2026-07-28** 成为最新修订版 | [MCP 规范 Changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) |

> 一句话：MCP 已经过了"要不要用"的阶段，现在的问题是"怎么安全地用、怎么治理"。

---

## MCP 架构

```
┌─────────────────────────────────┐
│         AI 应用（Host）          │
│  （Claude / Cursor / 你的 App）  │
│  ┌───────────────────────────┐  │
│  │ MCP Client（每个 Server 一个）│  │
│  └───────────────────────────┘  │
└──────────────┬──────────────────┘
               │ MCP 协议（JSON-RPC / stdio / Streamable HTTP）
       ┌───────┴───────┐
       ▼               ▼
┌──────────┐    ┌──────────────┐
│ MCP      │    │ MCP          │
│ Server A │    │ Server B     │
│ (GitHub) │    │ (数据库)     │
└──────────┘    └──────────────┘
```

**三个角色：**
- **Host**：AI 应用（Claude Desktop、Cursor、Claude Code、你的 Agent）
- **Client**：Host 内的 MCP 客户端，与 Server 一对一连接
- **Server**：提供工具/数据/提示模板的 MCP 服务端

### 2026 规范的重要变化：走向无状态

2026-07-28 版规范做了几件大事（来源：[Key Changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog)）：

| 变化 | 影响 |
|------|------|
| **移除协议级会话与 `Mcp-Session-Id`** | 不再依赖 `initialize` 握手；每次请求自带协议版本与能力 |
| **新增 `server/discover`** | Server 必须实现，用于声明支持的版本、能力与身份 |
| **`subscriptions/listen`** | 用单一长连接替代原来的 HTTP GET + 资源订阅 |
| **MRTR（多轮请求）** | 用 `InputRequiredResult` 替代服务端主动发起的 sampling/elicitation/roots 请求 |
| **`resultType` 必填** | 区分 `complete` 与 `input_required` |
| **Tasks 扩展** | 长任务能力移出核心协议，改为官方扩展，支持轮询与更新 |
| **移除 ping / logging.setLevel** | 日志级别改为按请求通过 `_meta` 传递 |

> 这对普通用户是"无感升级"，对自建 Server 的团队是**必须关注的破坏性变更**：升级前先看 changelog 与 SDK 适配情况。

---

## MCP Server 能提供什么？

### Tools（工具）
AI 可以调用的函数：

```json
{
  "name": "create_github_issue",
  "description": "在 GitHub 仓库创建 Issue",
  "inputSchema": {
    "type": "object",
    "properties": {
      "title": { "type": "string" },
      "body": { "type": "string" },
      "labels": { "type": "array", "items": { "type": "string" } }
    },
    "required": ["title", "body"]
  }
}
```

### Resources（资源）
AI 可以读取的数据（文件、数据库、API 返回）：

```
mcp://github/repos/myorg/myrepo/issues
mcp://database/users/table
mcp://filesystem/home/user/docs/
```

### Prompts（提示模板）
预定义的任务模板，让 Host 以统一方式调用。

### 其他能力（2026）
- **Sampling**：Server 请求 Host 侧的模型补全
- **Elicitation**：向用户追问缺失信息
- **Roots**：声明可访问的文件系统范围
- **Tasks 扩展**：长任务异步执行（轮询 `tasks/get` / `tasks/update`）

---

## 常见 MCP Server 列表

| Server | 功能 | 提供方 |
|--------|------|--------|
| **github** | GitHub 仓库、PR、Issue | 官方/社区 |
| **filesystem** | 读写本地文件 | 官方 |
| **postgres / sqlite** | 查询数据库 | 社区 |
| **brave-search** | 网络搜索 | 社区 |
| **slack** | 发送 Slack 消息 | 社区 |
| **notion** | 读写 Notion | 社区 |
| **puppeteer / playwright** | 控制浏览器 | 社区 |
| **memory** | 持久化 AI 记忆 | 官方 |

官方 Registry 与 Server 列表：[modelcontextprotocol.io](https://modelcontextprotocol.io)（2026 年已提供 Registry 用于发现与安装）。

---

## 配置示例（Claude Desktop）

**macOS**：`~/Library/Application Support/Claude/claude_desktop_config.json`
**Linux**：`~/.config/claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_URL": "postgresql://localhost/mydb"
      }
    }
  }
}
```

> ⚠️ 包名、配置字段与传输方式随规范演进会变，**以 MCP 官方文档与对应 Server 的 README 为准**。不要把 token 写进仓库。

---

## 写一个简单的 MCP Server（伪代码）

```python
from mcp import Server, Tool
import mcp.server.stdio

server = Server("my-company-tools")

@server.tool()
async def query_employee(employee_id: str) -> str:
    """查询员工信息（只读）"""
    # 连接内部数据库；使用参数化查询，避免 SQL 注入
    employee = db.query("SELECT * FROM employees WHERE id = %s", (employee_id,))
    return employee.to_json()

@server.tool()
async def send_internal_notice(to: str, subject: str, content: str) -> str:
    """发送内部通知（写操作，建议加审批）"""
    result = email_system.send(to=to, subject=subject, body=content)
    return f"通知已发送：{result}"

mcp.server.stdio.run(server)
```

然后在 AI 工具中配置这个 Server，AI 就能调用你的内部系统。

> 真实项目请使用官方 SDK（Python / TypeScript / Java / C# 等），并按 2026-07-28 规范处理 `server/discover`、`_meta` 与 `resultType`。

---

## MCP vs 传统 API 调用

| 维度 | 传统 API 集成 | MCP |
|------|-------------|-----|
| 开发成本 | 每个 AI 工具都要单独适配 | 一次开发，到处使用 |
| 安全性 | 需要自己处理授权 | 协议层统一授权模型（OAuth 等） |
| 标准化 | 各平台格式不一 | 统一 Schema 与发现机制 |
| 生态 | 割裂 | 共享 Server 生态与 Registry |
| 长任务 | 自己实现轮询/回调 | Tasks 扩展提供统一模式 |

---

## 安全：2026 年 MCP 最大的坑

MCP 把"外部能力"接进 AI，也把"外部风险"接了进来。常见攻击面：

| 风险 | 场景 | 防护 |
|------|------|------|
| **工具投毒（Tool Poisoning）** | 恶意 Server 在工具描述里藏指令，诱导模型泄露数据 | 只用可信 Server；审查工具描述；固定版本/哈希 |
| **间接提示注入** | 工具返回的网页/文档里含"忽略之前指令" | 把工具结果当数据不当指令；隔离标签；输出过滤 |
| **权限过大** | 一个 filesystem Server 给了整个 home 目录 | 最小权限；只读优先；限定 roots |
| **供应链风险** | `npx -y` 直接拉最新版，包被投毒 | 锁版本、私有 Registry、代码审计 |
| **凭证泄露** | token 写进配置文件并提交 | 环境变量/密钥管理；定期轮换 |
| **越权调用** | Agent 自主调用写操作（删库、发消息） | 写操作审批；沙箱；审计日志 |

> 有研究专门对 MCP 生态做威胁建模，指出工具投毒与提示注入是生产环境的主要风险（例：[MCP Threat Modeling（arXiv:2603.22489）](https://arxiv.org/abs/2603.22489)，2026）。

**企业落地底线**：
1. Server 白名单 + 版本锁定
2. 读写分离，写操作必须人工确认
3. 每个 Server 独立最小权限凭证
4. 全量审计日志（谁、在什么上下文、调了什么）
5. 敏感数据不出内网（自建 Server / 网关代理）

---

## 企业应用场景

用 MCP 可以让 AI 接入你的内部系统：

```
Claude / Cursor / 自建 Agent
    ↓
自建 MCP Server（统一网关 + 鉴权 + 审计）
    ├─ 内部 ERP 系统
    ├─ CRM 客户数据
    ├─ 代码仓库（GitLab 私有）
    ├─ 知识库文档（Confluence）
    └─ 监控告警系统
```

这样 AI 就能：
- "查一下客户 XX 最近的订单状态"
- "帮我查生产环境最近 1 小时的错误日志"
- "根据 Confluence 文档帮我写这个功能"

---

## 状态（2026-11）

- MCP 由 **Agentic AI Foundation（Linux 基金会）** 托管，厂商中立
- 已被 OpenAI、Google、微软等主流厂商及主流 IDE 支持
- 官方 Registry、SDK、扩展生态逐步完善
- **规范仍在快速演进**：自建 Server 要跟版本，升级前读 changelog

---

## 历史沿革

- **2026-07-28**：MCP 最新规范发布：无状态化、`server/discover`、`subscriptions/listen`、MRTR、Tasks 扩展。
- **2026-10**：Anthropic 把 **Agent Skills** 标准也捐给 AAIF，Agent 生态标准进一步集中。
- **2025-12**：MCP 一周年，超过 10,000 个公开 Server；Anthropic 将 MCP 捐给 Linux 基金会下的 AAIF。
- **2025-11-25**：规范引入异步操作、无状态、服务端身份与官方扩展。
- **2024-11**：Anthropic 发布 MCP 初始版本，提出"AI 工具的 USB 接口"。

---

## 下一步

- [M5-02 Agentic 开发工作流](../05-practical/02-workflow.md) — 把 MCP 接进日常开发
- [M7 / M8 Skills 与 MCP 生态](../08-mcp/README.md) — 具体 Server 选型与实战
