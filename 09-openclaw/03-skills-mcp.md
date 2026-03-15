# ⭐️ M9-03 · OpenClaw Skills 与 MCP 接入

> OpenClaw 原生支持 Skills 技能扩展和完整 MCP 生态，这是它比直接用 ChatGPT 强大的核心所在。

---

## Skills：给 AI 装上专属技能

### 什么是 Skills

Skills 是**可复用的 AI 能力模块**，本质是一组 Markdown 指令文件。

```
~/.nvm/.../openclaw/skills/
├── weather/         ← 查天气
│   └── SKILL.md
├── notion/          ← 操作 Notion
│   └── SKILL.md
├── coding-agent/    ← 调用编程 Agent
│   └── SKILL.md
└── nano-pdf/        ← PDF 编辑
    └── SKILL.md
```

### 安装 Skill

```bash
# 使用 ClawHub（技能商店）安装
clawhub install weather
clawhub install notion
clawhub install coding-agent

# 查看已安装技能
clawhub list
```

### 开发向必装 Skills

| Skill | 功能 | 安装命令 |
|-------|------|---------|
| **coding-agent** | 委托 Claude Code / Codex 执行复杂编程任务 | `clawhub install coding-agent` |
| **notion** | 读写 Notion 页面和数据库 | `clawhub install notion` |
| **nano-pdf** | 用自然语言编辑 PDF | `clawhub install nano-pdf` |
| **weather** | 查天气预报 | `clawhub install weather` |
| **session-logs** | 搜索分析历史对话 | `clawhub install session-logs` |

### 自定义 Skill

在工作区创建技能文件夹：

```
~/clawd/skills/code-review/
└── SKILL.md
```

`SKILL.md` 示例：

```markdown
# Code Review Skill

当用户要求 code review 时，按以下步骤执行：

1. 先问清楚：这是后端（Go）还是前端（Vue/Flutter）代码？
2. 按三个维度审查：
   - 🔴 安全问题（SQL注入、权限缺失）
   - 🟡 性能问题（N+1查询、不必要循环）
   - 🟢 代码规范（命名、错误处理）
3. 输出格式：问题描述 + 修复代码示例

语气：直接、专业，不废话。
```

---

## MCP：让 AI 操作你的工具

OpenClaw 支持完整的 MCP 协议，配置在工作区的配置文件里。

### 配置 MCP

```bash
openclaw config
```

在配置中加入 `mcpServers` 字段：

```json
{
  "model": "anthropic/claude-sonnet-4-5",
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/你的用户名/Projects"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token"
      }
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "your_key"
      }
    },
    "mysql": {
      "command": "npx",
      "args": ["-y", "mcp-server-mysql"],
      "env": {
        "MYSQL_HOST": "127.0.0.1",
        "MYSQL_USER": "ai_readonly",
        "MYSQL_PASSWORD": "your_password",
        "MYSQL_DATABASE": "your_db"
      }
    }
  }
}
```

配置完重启网关：

```bash
openclaw gateway restart
```

### 验证 MCP 是否生效

在 Telegram 发：
```
现在你有哪些工具可以用？
```

AI 会列出所有可用的 MCP 工具，比如：
```
我现在有这些工具：
- filesystem: 读写 /Users/xxx/Projects 目录
- github: 访问 GitHub 仓库
- brave-search: 搜索互联网
- mysql: 查询数据库（只读）
```

---

## 定时任务（Cron）

让 AI 定期主动做事，无需手动触发。

### 常见用法

**每天早上发日程提醒：**
```bash
openclaw cron add \
  --schedule "0 9 * * 1-5" \
  --message "获取今日日历，总结今天的会议和待办，发送到 Telegram"
```

**每周一项目周报：**
```bash
openclaw cron add \
  --schedule "0 10 * * 1" \
  --message "读取 GitHub 过去一周的 commits，生成项目进度周报"
```

**监控代码仓库更新：**
```bash
openclaw cron add \
  --schedule "*/30 9-18 * * 1-5" \
  --message "检查 GitHub 有没有新 PR 或 Issue 需要处理"
```

---

## 心跳轮询（Heartbeat）

心跳是一个更轻量的定时触发，让 AI 周期性检查：

```markdown
# HEARTBEAT.md（放在工作区根目录）

## 定期任务
- 每天早上 9 点：提醒今日日程
- 如有重要邮件：立即通知
- 没有要紧事：保持安静（HEARTBEAT_OK）
```

AI 会自动按这个文件执行，而不是每次都发完整消息。

---

## 与 M7/M8 的关系

```
Skills（M7）→ OpenClaw 技能库
MCP（M8）  → OpenClaw mcpServers 配置
Cron       → 定时自动化触发以上工具
```

三者组合：

```
你：帮我检查一下 GitHub 今天有没有新 Issue，整理到 Notion
AI：[GitHub MCP 读 Issues] + [Notion MCP 写入] + [Skill格式化输出]
```

---

## 更多资源

- 官方文档：[docs.openclaw.ai](https://docs.openclaw.ai)
- 技能商店：[clawhub.com](https://clawhub.com)
- 社区：[discord.gg/clawd](https://discord.com/invite/clawd)
- 开源：[github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)
