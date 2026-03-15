# ⭐️ M8-04 · 通用工具类 MCP

> 搜索、记忆、推理——这几个 MCP 能显著提升 AI 的基础能力。

---

## Brave Search MCP ⭐ 必装

**功能：** AI 联网搜索实时信息

```json
{
  "brave-search": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-brave-search"],
    "env": {
      "BRAVE_API_KEY": "your_brave_api_key"
    }
  }
}
```

**获取 API Key：** [brave.com/search/api](https://brave.com/search/api/)（每月 2000 次免费）

**能做什么：**
- 搜索最新技术文档（AI 知识有截止日期，搜索补充最新信息）
- 查找某个库/框架的最新版本
- 研究竞品技术方案
- 搜索报错解决方案

**典型用法：**
```
你：Go 1.22 有什么新特性？
AI：[搜索最新发布说明，给出准确答案，不会给过时信息]

你：Beego v2 最新版本有没有修复那个并发 Bug？
AI：[搜索 changelog，直接给出准确答案]
```

---

## Memory MCP ⭐ 推荐

**功能：** 给 AI 一个可持久化的"记忆本"

```json
{
  "memory": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-memory"]
  }
}
```

**能做什么：**
- AI 可以主动记住重要信息（你的偏好、项目决策）
- 跨对话保持记忆
- 构建知识图谱

**典型用法：**
```
你：记住，我们项目的主键统一用 bigint，不用 int
AI：[写入记忆] 好的，以后生成数据库设计都用 bigint 主键

[下次对话]
你：帮我设计用户表
AI：[自动使用 bigint 主键，不需要你重复说明]
```

---

## Sequential Thinking MCP

**功能：** 让 AI 逐步思考，提高复杂问题的准确率

```json
{
  "sequential-thinking": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
  }
}
```

**适合场景：**
- 复杂架构设计
- 多步骤调试
- 需要深度推理的问题

---

## Time MCP

**功能：** 让 AI 知道当前时间（默认 AI 不知道"今天"是几号）

```json
{
  "time": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-time"]
  }
}
```

**场景：** 需要生成带日期的内容（日报、周报、版本号等）

---

## MCP 推荐组合方案

### 开发者日常最小配置

```json
{
  "mcpServers": {
    "filesystem": { ... },       // 读写项目文件
    "github": { ... },           // 操作代码仓库
    "brave-search": { ... },     // 联网搜索
    "mysql": { ... }             // 读数据库结构（只读账号）
  }
}
```

### 全栈开发完整配置

```json
{
  "mcpServers": {
    "filesystem": { ... },
    "github": { ... },
    "brave-search": { ... },
    "mysql": { ... },
    "redis": { ... },
    "playwright": { ... },       // 前端调试
    "memory": { ... },           // 持久化记忆
    "fetch": { ... }             // 读取外部文档
  }
}
```

---

## MCP 安装位置汇总

```
Claude Desktop:
~/Library/Application Support/Claude/claude_desktop_config.json

Cursor:
Settings → Features → MCP Servers

VS Code (Copilot):
.vscode/mcp.json（项目级）
```

---

## 发现更多 MCP

| 资源 | 说明 |
|------|------|
| [modelcontextprotocol.io/servers](https://modelcontextprotocol.io/servers) | 官方 MCP 目录 |
| [mcp.so](https://mcp.so) | 社区 MCP 搜索引擎 |
| [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | GitHub 精选列表 |
| [glama.ai/mcp/servers](https://glama.ai/mcp/servers) | 评分和使用量排行 |

---

## 下一步

- [⭐️ M8-01 开发工具类 MCP](./01-dev-tools.md)
- [⭐️ M8-02 数据库类 MCP](./02-database.md)
- [M8-03 效率工具类 MCP](./03-productivity.md)
