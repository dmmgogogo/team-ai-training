# ⭐️ M9-02 · OpenClaw 安装与配置

> 从零到跑起来，大约 10 分钟。前提：有 Node.js 22+ 环境。

---

## 前置条件

- Node.js 22 LTS（推荐 v22.16+）或 Node 24
- Claude/OpenAI/Gemini 的 API Key（选一个）
- 一个用来对话的渠道账号（Telegram Bot 最简单）

---

## 安装

```bash
npm install -g openclaw@latest
```

---

## 一键引导配置

```bash
openclaw onboard --install-daemon
```

这个命令会引导你：
1. 选择 AI 模型提供商 + 填入 API Key
2. 选择对话渠道（Telegram/Discord/iMessage…）
3. 安装为系统服务（开机自启）

---

## 配置 Telegram Bot（推荐，最简单）

**第一步：创建 Bot**

1. 打开 Telegram，搜索 `@BotFather`
2. 发送 `/newbot`
3. 按提示填写 Bot 名称
4. 拿到 Bot Token（格式：`123456789:ABCDEFGxxx`）

**第二步：填入配置**

```bash
openclaw channel add telegram
# 粘贴 Bot Token，完成
```

**第三步：和 Bot 说话**

在 Telegram 搜索你创建的 Bot → 发送 `/start` → AI 回复了 ✅

---

## 配置 AI 模型

```bash
openclaw config
```

### 使用 Claude（推荐）

在 [console.anthropic.com](https://console.anthropic.com) 创建 API Key，然后：

```json
{
  "model": "anthropic/claude-sonnet-4-5",
  "providers": {
    "anthropic": {
      "apiKey": "sk-ant-xxxxx"
    }
  }
}
```

### 使用 OpenAI

```json
{
  "model": "openai/gpt-4o",
  "providers": {
    "openai": {
      "apiKey": "sk-xxxxx"
    }
  }
}
```

### 多模型备用（Claude 限额时自动切换 GPT）

```json
{
  "model": "anthropic/claude-sonnet-4-5",
  "fallbackModel": "openai/gpt-4o",
  "providers": {
    "anthropic": { "apiKey": "sk-ant-xxxxx" },
    "openai": { "apiKey": "sk-xxxxx" }
  }
}
```

---

## 常用命令

```bash
openclaw gateway start    # 启动网关
openclaw gateway stop     # 停止网关
openclaw gateway status   # 查看运行状态
openclaw gateway restart  # 重启（改配置后）

openclaw channel          # 管理渠道
openclaw config           # 编辑配置
openclaw status           # 查看整体状态
```

---

## Web 控制台

```bash
openclaw web
```

打开后可以：
- 在浏览器里直接和 AI 对话
- 查看所有会话历史
- 管理定时任务
- 配置 Skills 和 MCP

---

## 工作区（Workspace）

OpenClaw 使用一个本地工作区目录（默认 `~/clawd`）存放：

```
~/clawd/
├── SOUL.md      ← AI 的性格设定
├── USER.md      ← 关于你的信息（AI 会记住）
├── MEMORY.md    ← AI 的长期记忆
├── AGENTS.md    ← 会话规则和工作流
└── memory/      ← 每日日记（AI 自动写）
```

你可以编辑这些文件来定制 AI 的行为和记忆。

---

## 验证配置

```bash
openclaw gateway status
```

输出类似这样就是正常运行：
```
● Gateway: running
  Model:   anthropic/claude-sonnet-4-5
  Channel: telegram (connected)
  Uptime:  2h 34m
```

---

## 下一步

- [⭐️ M9-03 Skills 与 MCP 接入](./03-skills-mcp.md)
- [M8 MCP 精选](../08-mcp/01-dev-tools.md)
