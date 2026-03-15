# M8-03 · 效率工具类 MCP

> 打通 Slack、Notion、邮件、日历，让 AI 帮你处理沟通和信息管理。

---

## Slack MCP

**功能：** AI 读写 Slack，自动处理消息和频道

```json
{
  "slack": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-slack"],
    "env": {
      "SLACK_BOT_TOKEN": "xoxb-your-token",
      "SLACK_TEAM_ID": "T0XXXXXXX"
    }
  }
}
```

**能做什么：**
- 总结指定频道的未读消息
- 搜索历史消息（找某个决策/讨论）
- 帮你起草回复
- 查找特定人的消息

**典型用法：**
```
你：帮我总结一下 #tech-discuss 频道今天的重要讨论
AI：[读取频道消息，提取关键信息，整理成摘要]

你：帮我在 #project-alpha 发送今日进展报告
AI：[生成规范的进展报告并发送]
```

---

## Notion MCP

**功能：** AI 读写 Notion 数据库和页面

```json
{
  "notion": {
    "command": "npx",
    "args": ["-y", "@notionhq/notion-mcp-server"],
    "env": {
      "OPENAPI_MCP_HEADERS": "{\"Authorization\": \"Bearer your_notion_token\", \"Notion-Version\": \"2022-06-28\"}"
    }
  }
}
```

**能做什么：**
- 读取 Notion 数据库内容
- 创建/更新页面
- 搜索 Notion 工作区

**典型用法：**
```
你：帮我把今天的技术调研结果整理到 Notion 知识库
AI：[自动创建格式规范的 Notion 页面]
```

---

## Google Drive MCP

```json
{
  "google-drive": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-google-drive"]
  }
}
```

**能做什么：**
- 搜索文件（找到具体文档）
- 读取 Google Docs 内容
- 整理文件结构

---

## Fetch MCP ⭐ 常用

**功能：** AI 直接抓取任意网页内容

```json
{
  "fetch": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-fetch"]
  }
}
```

**能做什么：**
- 读取第三方 API 文档
- 抓取网页内容做分析
- 检查 URL 是否正常响应

**典型用法：**
```
你：帮我读一下这个文档，然后给我写调用示例
    https://docs.stripe.com/api/charges/create
AI：[直接读取文档，生成准确的代码示例]
```

---

## 下一步

- [⭐️ M8-04 通用工具类 MCP](./04-utilities.md)
- [⭐️ M8-01 开发工具类 MCP](./01-dev-tools.md)
