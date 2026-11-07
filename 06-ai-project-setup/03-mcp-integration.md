# M6-03 · MCP 项目集成

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> MCP（Model Context Protocol）让 AI 直接连接你的项目工具——读文件、查数据库、操作 GitHub。2026 年 MCP 已是开放标准（规范 `2026-07-28`），集成方式也从"改一个 JSON 文件"变成"项目级配置 + 审批 + 权限控制"。

---

## 一句话结论

- **项目级共享**：Claude Code 用仓库根目录的 `.mcp.json`；Cursor 用 `mcp.json`。
- **优先远程 HTTP**：能走官方远程 MCP 就不自己跑本地进程。
- **默认只读**：数据库、监控类工具一律用只读账号。
- **来源要审**：MCP Server 能读数据、能发请求，等于给 AI 开了权限。

---

## 一、哪些 MCP Server 对项目开发最实用

### 必装（大多数项目通用）

| Server | 作用 | 推荐接入方式 |
|--------|------|--------------|
| **Filesystem** | 读写项目文件 | 本地 stdio，路径限制到项目目录 |
| **GitHub** | Issue / PR / 代码搜索 | 远程 HTTP + PAT 或 OAuth |
| **数据库** | 查询表结构、跑只读 SQL | 本地/远程 + 只读账号 |
| **浏览器 / Playwright** | 打开页面、截图、调试 UI | 本地 stdio |
| **监控 / 错误追踪**（Sentry 等） | 查线上错误 | 远程 HTTP + OAuth |

### 按项目类型选装

| 项目类型 | 建议 |
|----------|------|
| Vue / UniApp | 浏览器类 MCP（看页面、读 console）+ 后端 API 文档 MCP |
| Flutter | 暂无统一官方 MCP；用 Filesystem + 截图/日志工具组合 |
| Go 后端 | 数据库 MCP（只读）+ OpenAPI 文档 MCP + Sentry |
| 数据/分析 | 数据库 MCP + 文件系统 MCP + 代码执行（沙箱） |

> 具体可用的 Server 以 [MCP Registry/目录](https://modelcontextprotocol.io) 和 [Anthropic Directory](https://claude.ai/directory)、[Cursor Marketplace](https://cursor.com/marketplace) 为准。

---

## 二、配置文件位置（2026-11）

| 客户端 | 位置 | 作用域 |
|--------|------|--------|
| **Claude Code** | 项目根目录 `.mcp.json` | 项目级，可提交共享 |
| **Claude Code** | `~/.claude.json` | 用户级 |
| **Claude Code** | `claude mcp add` | 默认写入 local scope |
| **Cursor** | `mcp.json`（Customize → MCP 也可图形配置） | 项目/用户 |
| **Claude Desktop** | `claude_desktop_config.json`（macOS：`~/Library/Application Support/Claude/`） | 本机 |

> 路径会随版本变化，以各客户端官方文档为准。

---

## 三、Claude Code：项目级 MCP 集成

### 方式一：命令行添加（推荐）

```bash
# 远程 HTTP（推荐）
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ \
  --header "Authorization: Bearer ${GITHUB_PAT}"

# 远程 HTTP + OAuth（Notion 示例）
claude mcp add --transport http notion https://mcp.notion.com/mcp

# 本地 stdio（数据库只读示例）
claude mcp add db --env DB_DSN=postgresql://readonly:pass@host:5432/app -- \
  npx -y @bytebase/dbhub

# 查看/管理
claude mcp list
claude mcp get db
claude mcp remove db
```

进入会话后可用 `/mcp` 查看连接状态、完成 OAuth 登录。

### 方式二：`.mcp.json`（团队共享）

```json
{
  "mcpServers": {
    "db": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@bytebase/dbhub"],
      "env": {
        "DB_DSN": "${DB_DSN}"
      }
    },
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PAT}"
      }
    }
  }
}
```

要点：

- 用 `${VAR}` 引用环境变量，**不要把 token 写进仓库**。
- 有 `url` 的条目必须显式写 `"type": "http"`（否则会被当成 stdio）。
- 项目级配置首次使用需要**信任工作区并批准**，克隆来的仓库不会自动获得授权。
- 团队统一配置写进 `.mcp.json` 并提交，个人密钥放本机环境变量或 `settings.local.json`。

### 传输方式选择

| 传输 | 适合 | 说明 |
|------|------|------|
| `http`（Streamable HTTP） | 远程服务 | 首选；支持 OAuth、headers |
| `stdio` | 本地工具 | 本机进程，能力最强也最需要审 |
| `sse` | 仅支持 SSE 的旧服务 | 过渡方案，能用 HTTP 就用 HTTP |
| `ws` | 服务端主动推送 | 特殊场景 |

---

## 四、Cursor：项目级 MCP 集成

Cursor 通过 `mcp.json` 或 Customize → MCP 配置，支持 stdio / SSE / Streamable HTTP；可直接从 [Cursor Marketplace](https://cursor.com/marketplace) 一键安装官方插件（来源：[Cursor MCP 文档](https://cursor.com/docs/mcp)，2026-11）。

```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "mcp-server"],
      "env": {
        "API_KEY": "${API_KEY}"
      }
    }
  }
}
```

Cursor 还支持 **MCP Apps 扩展**：工具可以返回可交互 UI；不支持渲染的宿主会退化为普通工具输出。

---

## 五、团队统一 MCP 配置建议

### 1. 在仓库里放一份说明

`docs/mcp-setup.md`：

```markdown
# 团队 MCP 配置说明

## 必装 MCP
1. GitHub：远程 HTTP，个人 PAT，repo 只读优先
2. 数据库：只读账号，DSN 放本机环境变量
3. 浏览器：本地 stdio，仅开发环境

## 安装步骤
1. 复制 `.mcp.json` 到项目根目录（已在仓库中）
2. 在本机设置环境变量：GITHUB_PAT、DB_DSN
3. 启动 Claude Code，首次运行批准项目 MCP
4. `/mcp` 确认三个服务都是 ✔ Connected
```

### 2. 用作用域区分"共享"与"个人"

| 内容 | 放哪里 |
|------|--------|
| 团队都要用的 Server 定义 | `.mcp.json`（提交） |
| 个人 token / DSN | 本机环境变量 |
| 个人额外 Server | `~/.claude.json` 或 local scope |

### 3. 给每个 Server 定"最小权限"

- GitHub：fine-grained PAT，只授权需要的仓库与只读权限；
- 数据库：只读账号 + 限制库/表；
- 文件系统：路径限定到项目目录；
- 浏览器：仅开发环境，不登录生产账号。

---

## 六、实际用法示例

```
"帮我看一下 src/pages/order/index.vue 里的问题"
→ AI 直接读文件，不用你复制粘贴

"我刚提了一个 bug Issue #42，帮我看看该怎么修"
→ AI 读 Issue 内容，给出修复方案

"帮我查一下最近 7 天 orders 表的增长趋势"
→ AI 用只读账号执行 SQL，返回结果并画图

"这个 PR 的测试挂了，帮我看下 Sentry 上的错误"
→ AI 查错误详情，定位到具体代码
```

---

## 七、安全与权限（重点）

| 风险 | 说明 | 对策 |
|------|------|------|
| **提示注入** | 网页、Issue、日志里可能藏指令 | 工具输出当不可信数据；危险操作人工确认 |
| **权限过大** | root 数据库、整个 home 目录 | 只读账号、路径白名单、最小 scope |
| **密钥泄露** | token 写进 `.mcp.json` 或日志 | `${VAR}` 环境变量；日志脱敏 |
| **恶意 Server** | 第三方 MCP 可能读数据外发 | 只用可信来源；审代码；限制网络出口 |
| **供应链** | 插件携带 MCP，一键安装即运行 | 先看插件包含哪些 MCP / 权限 |
| **越权串联** | 读到的数据被另一个工具发出去 | 按数据域隔离工具；审批写操作 |

三条团队规则：

1. **生产只读**：数据库/监控类 MCP 默认只读账号。
2. **写操作要审批**：发消息、改配置、删数据类工具，必须人工确认。
3. **来源可追溯**：记录每个 MCP Server 的来源、版本、维护人。

---

## 八、性能与成本

- MCP 工具定义会占用上下文；工具很多时优先用支持 **tool search / 按需加载** 的客户端。
- 远程 Server 断连会拖慢会话，建议只保留常用 Server。
- 大结果（日志、表格）让 Server 侧做分页/裁剪，别把原始数据全塞回模型。

---

## 九、历史沿革

| 时间 | 事件 |
|------|------|
| 2024-11 | Anthropic 开源 MCP，统一"AI 接工具"的协议 |
| 2025 | Claude Desktop / Cursor / VS Code 等快速跟进，MCP Server 生态爆发 |
| 2025–2026 | 远程 HTTP 传输、OAuth、MCP Apps 扩展逐步成熟 |
| 2026-07 | MCP 规范更新至 `2026-07-28` |
| 2026-09 | Claude Marketplace 上线，connectors/plugins 统一分发 |
| 2026-11 | 项目级配置 + 审批 + 只读账号成为团队标准实践 |

---

## 十、下一步

- [⭐️ M6-01 AI 项目配置：从 .cursorrules 到 AGENTS.md](./01-cursorrules.md)
- [⭐️ M6-02 给 AI 喂上下文：项目文档规范](./02-ai-context.md)
- [M8 MCP 精选大全](../08-mcp/)
