# M4-04 · MCP：模型上下文协议

> 让 AI 工具互联互通的"USB 接口"

---

## 什么是 MCP？

**MCP（Model Context Protocol）** 是 Anthropic 于 2024 年底提出的开放标准，定义了 AI 模型与外部工具/数据源之间的**标准化通信协议**。

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

## MCP 架构

```
┌─────────────────────────────────┐
│         AI 应用（Host）          │
│  （Cursor / Claude / 你的 App）  │
└──────────────┬──────────────────┘
               │ MCP 协议
       ┌───────┴───────┐
       ▼               ▼
┌──────────┐    ┌──────────────┐
│ MCP      │    │ MCP          │
│ Server A │    │ Server B     │
│ (GitHub) │    │ (数据库)     │
└──────────┘    └──────────────┘
```

**三个角色：**
- **Host**：AI 应用（Cursor、Claude Desktop 等）
- **Client**：Host 内的 MCP 客户端
- **Server**：提供工具/数据的 MCP 服务端

---

## MCP Server 能提供什么？

### Tools（工具）
AI 可以调用的函数：

```json
{
  "name": "create_github_issue",
  "description": "在 GitHub 仓库创建 Issue",
  "inputSchema": {
    "title": "string",
    "body": "string",
    "labels": ["bug", "feature"]
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
预定义的任务模板

---

## 常见 MCP Server 列表

| Server | 功能 | 提供方 |
|--------|------|--------|
| **github** | GitHub 仓库、PR、Issue | Anthropic 官方 |
| **filesystem** | 读写本地文件 | Anthropic 官方 |
| **postgres** | 查询 PostgreSQL 数据库 | 社区 |
| **sqlite** | 操作 SQLite | 社区 |
| **brave-search** | 网络搜索 | 社区 |
| **slack** | 发送 Slack 消息 | 社区 |
| **notion** | 读写 Notion | 社区 |
| **puppeteer** | 控制浏览器 | 社区 |
| **memory** | 持久化 AI 记忆 | Anthropic 官方 |

社区 MCP Server 列表：[modelcontextprotocol.io/servers](https://modelcontextprotocol.io/servers)

---

## 配置示例（Claude Desktop）

**macOS** 配置文件路径：`~/Library/Application Support/Claude/claude_desktop_config.json`  
**Linux** 配置文件路径：`~/.config/claude/claude_desktop_config.json`

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

配置后，Claude 就能直接操作 GitHub 和数据库。

---

## 写一个简单的 MCP Server

```python
from mcp import Server, Tool
import mcp.server.stdio

server = Server("my-company-tools")

@server.tool()
async def query_employee(employee_id: str) -> str:
    """查询员工信息"""
    # 连接内部数据库
    # 使用参数化查询，避免 SQL 注入
    employee = db.query("SELECT * FROM employees WHERE id = %s", (employee_id,))
    return employee.to_json()

@server.tool()
async def send_internal_notice(
    to: str, 
    subject: str, 
    content: str
) -> str:
    """发送内部通知"""
    result = email_system.send(to=to, subject=subject, body=content)
    return f"通知已发送：{result}"

# 启动 MCP Server
mcp.server.stdio.run(server)
```

然后在 AI 工具中配置这个 Server，AI 就能调用你的内部系统。

---

## MCP vs 传统 API 调用

| 维度 | 传统 API 集成 | MCP |
|------|-------------|-----|
| 开发成本 | 每个 AI 工具都要单独适配 | 一次开发，到处使用 |
| 安全性 | 需要自己处理授权 | 协议层统一处理 |
| 标准化 | 各平台格式不一 | 统一 Schema |
| 生态 | 割裂 | 共享 Server 生态 |

---

## 企业应用场景

用 MCP 可以让 AI 接入你的内部系统：

```
Claude / Cursor
    ↓
自建 MCP Server
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

## 状态

- MCP 已被 **OpenAI、Google、微软** 等主流厂商支持
- Cursor、Claude Desktop、Windsurf 等 IDE 原生支持
- 成为 AI 工具互联互通的事实标准

---

## 下一步

- [M5-02 AI 辅助开发工作流](../05-practical/02-workflow.md) — 整合所有工具的实战方案
