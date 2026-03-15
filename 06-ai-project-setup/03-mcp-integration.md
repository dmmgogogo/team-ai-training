# M6-03 · MCP 项目集成

> MCP（Model Context Protocol）让 AI 直接连接你的项目工具——读文件、查数据库、操作 GitHub。配好了，AI 不只是"建议"，还能直接动手。

---

## 哪些 MCP Server 对项目开发最实用

### 必装（所有项目通用）

**1. Filesystem — 让 AI 读写本地文件**
```json
{
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem", "/你的项目路径"]
  }
}
```
- AI 可以直接读你的项目文件，不用手动复制粘贴
- 可以让 AI 直接写文件，修改完立刻生效

**2. GitHub — 让 AI 操作仓库**
```json
{
  "github": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "env": {
      "GITHUB_PERSONAL_ACCESS_TOKEN": "你的token"
    }
  }
}
```
- 让 AI 直接查 Issue、PR、提交记录
- 可以让 AI 帮你写 commit message、创建 PR 描述

---

### 按项目类型选装

**Vue / UniApp 项目**

**Browser Tools — 让 AI 看到浏览器实时状态**
```json
{
  "browser-tools": {
    "command": "npx",
    "args": ["-y", "@agentdeskai/browser-tools-mcp@1.2.0"]
  }
}
```
- AI 可以直接看你的页面截图，帮你调 UI bug
- 可以读 console 报错，直接定位问题

**Flutter 项目**

**Flutter 暂无官方 MCP**，推荐用 Filesystem + 截图工具组合：
- 配 Filesystem 让 AI 读 dart 文件
- 报错时直接把错误信息粘贴给 AI，配合 `@文件名` 引用

---

## MCP 配置文件位置

```
Claude Desktop:
~/Library/Application Support/Claude/claude_desktop_config.json

Cursor:
Settings → MCP（图形界面配置）
```

### 完整配置示例

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/你的用户名/Projects/你的项目"
      ]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxxx"
      }
    }
  }
}
```

---

## 实际用法示例

**有了 MCP 后，你可以这样和 AI 说：**

```
"帮我看一下 src/pages/order/index.vue 里的问题"
→ AI 直接读文件，不用你复制粘贴

"我刚提了一个 bug Issue #42，帮我看看该怎么修"
→ AI 直接读 GitHub Issue 内容，给出修复方案

"帮我把修好的代码写进 src/utils/request.js"
→ AI 直接写入文件，不用你手动改
```

---

## 团队统一 MCP 配置建议

在项目根目录创建 `docs/mcp-setup.md`，说明团队统一的 MCP 配置：

```markdown
# 团队 MCP 配置说明

## 必装 MCP
1. Filesystem：指向本项目目录
2. GitHub：使用个人 Token，勾选 repo 权限

## 安装步骤
1. 打开 Claude Desktop 配置文件
2. 复制以下配置（替换路径和 Token）：
   [配置内容]
3. 重启 Claude Desktop
```

这样新人加入团队，按文档配一次，AI 能力直接拉满。

---

## 下一步

- [⭐️ M6-01 .cursorrules 配置指南](./01-cursorrules.md)
- [⭐️ M6-02 给 AI 喂上下文：项目文档规范](./02-ai-context.md)
