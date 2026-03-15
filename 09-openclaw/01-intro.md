# ⭐️ M9-01 · OpenClaw 小🦞 是什么

> OpenClaw（小龙虾🦞）是一个**自托管的 AI 助手网关**，让你可以通过 Telegram、微信、Discord、iMessage 等任意聊天 App 随时随地使用 AI。
>
> 官网：[openclaw.ai](https://openclaw.ai) | 文档：[docs.openclaw.ai](https://docs.openclaw.ai) | 开源：MIT 协议

---

## 一句话理解

```
你的手机 → Telegram/Discord/iMessage → OpenClaw 网关 → Claude/GPT/Gemini
```

在家、在公司、在路上——只要打开 Telegram 发一条消息，AI 就回来了。

---

## 为什么不直接用 ChatGPT App？

| 对比 | ChatGPT/Claude App | OpenClaw |
|------|-------------------|---------|
| **平台** | 绑定 App，换手机重新配 | 自己的服务，随时访问 |
| **隐私** | 数据传到 OpenAI 服务器 | 自己托管，数据自己控制 |
| **渠道** | 只有官方 App | Telegram/Discord/iMessage 任意选 |
| **多模型** | 一个 App 一个模型 | 同时接多个模型按需切换 |
| **自动化** | 手动触发 | 定时任务、事件触发、邮件监听 |
| **技能扩展** | GPTs 商店 | 自定义 Skills，完全可控 |
| **MCP 支持** | 受限 | 完整 MCP 生态 |

---

## OpenClaw 能做什么

### 📱 随时随地用 AI
在 Telegram 发消息 → AI 立刻回复。出门在外不需要 VPN，不需要开特定 App。

### 🤖 记得你是谁
OpenClaw 有持久化记忆系统。AI 知道你的偏好、项目背景、工作规范——不需要每次重新介绍自己。

### ⚙️ 自动化定时任务
```
每天早上 9 点 → 发送今日日程摘要
每周一 → 发送项目进度提醒
收到重要邮件 → 自动通知到 Telegram
```

### 🔧 完整 MCP 支持
M8 里的所有 MCP（GitHub、数据库、Playwright 等）全部支持，AI 可以直接操作你的工具。

### 🛠️ 自定义 Skills
把常用任务封装成 Skill，一句话调用：
```
你：@技术调研 帮我调研一下 tRPC 和 REST 的对比
AI：[按照你定义的标准格式输出调研报告]
```

### 📸 多设备联动
绑定手机后，AI 可以：
- 截图你的手机屏幕
- 获取你的位置
- 读取通知消息

---

## 核心组成

```
OpenClaw
├── Gateway（网关进程）       ← 运行在你的 Mac/Linux 服务器
│   ├── 渠道连接              ← 对接各种 IM 平台
│   ├── 会话管理              ← 维护对话上下文
│   └── 工具调用              ← MCP、Skills 执行
│
├── Skills（技能库）           ← 可复用的 AI 能力模块
├── MCP Servers               ← 连接外部工具（见 M8）
├── Cron Jobs                 ← 定时自动化任务
└── Web Control UI            ← 浏览器管理界面
```

---

## 谁适合用 OpenClaw？

✅ **适合：**
- 有自己的 Mac/Linux 机器可以长期运行
- 想通过 Telegram/Discord 使用 AI
- 需要定制化 AI 工作流的开发者
- 对数据隐私有要求的团队

⚠️ **不适合：**
- 只偶尔用 AI，不需要持续在线
- 没有服务器/电脑长期运行（需要宿主机）

---

## 下一步

- [⭐️ M9-02 安装与配置](./02-setup.md)
- [⭐️ M9-03 Skills 与 MCP 接入](./03-skills-mcp.md)
