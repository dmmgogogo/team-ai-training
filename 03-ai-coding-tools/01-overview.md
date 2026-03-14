# M3-01 · AI 编程工具全景概览

> 2025 年，不用 AI 辅助写代码，效率至少落后一半。

---

## 工具分类

```
AI 编程工具
│
├── 编辑器/IDE 类（代码编辑主战场）
│   ├── Cursor          — AI 原生 IDE，最受欢迎
│   ├── Windsurf        — Codeium 出品，后起之秀
│   ├── GitHub Copilot  — 老牌，VS Code 插件
│   └── JetBrains AI    — IntelliJ 系列内置
│
├── 终端/CLI 类（命令行直接对话）
│   ├── Claude Code     — Anthropic 官方，能力最强
│   ├── OpenAI Codex CLI — o3 驱动，新发布
│   └── Aider           — 开源，支持多模型
│
├── 网页/聊天类（无需安装，开箱即用）
│   ├── ChatGPT         — OpenAI 官网
│   ├── Claude.ai       — Anthropic 官网
│   ├── GitHub Copilot Chat — 网页版
│   └── v0 by Vercel    — 专注前端 UI 生成
│
└── 代码审查/专项工具
    ├── Codium PR-Agent — PR 自动审查
    ├── Sweep           — 自动修复 GitHub Issue
    └── Continue.dev    — 开源 IDE 插件，支持本地模型
```

---

## 主流工具一览表

| 工具 | 类型 | 底层模型 | 价格 | 特色 |
|------|------|---------|------|------|
| **Cursor** | IDE | Claude / GPT-4 | $20/月 | 最强代码补全+对话 |
| **Windsurf** | IDE | Claude / Deepseek | $15/月 | Cascade 自动完成任务 |
| **GitHub Copilot** | 插件 | GPT-4o | $10/月 | 最广泛集成 |
| **Claude Code** | CLI | Claude Sonnet | API 计费 | 理解整个代码库 |
| **Aider** | CLI | 多模型 | 开源 | 支持本地模型 |
| **Continue.dev** | 插件 | 多模型 | 免费/开源 | 支持 Ollama 本地 |
| **v0** | 网页 | GPT-4o | 免费额度 | 前端 UI 生成最强 |

---

## 能力维度说明

| 能力 | 说明 | 代表工具 |
|------|------|---------|
| **代码补全** | 输入时自动续写代码 | Copilot, Cursor, Windsurf |
| **Chat 对话** | 聊天方式问代码问题 | 所有工具 |
| **代码库理解** | 理解整个项目，跨文件问答 | Cursor, Claude Code |
| **自动完成任务** | 给个需求，自动改多个文件 | Cursor Agent, Claude Code |
| **终端执行** | 自动运行命令、测试 | Claude Code, Aider |
| **本地模型支持** | 用 Ollama 等跑本地模型 | Continue.dev, Aider |

---

## 选型建议

**团队日常开发首选：**
→ Cursor（综合最强，体验最好）

**预算敏感 / 隐私要求高：**
→ Continue.dev + 本地 Ollama（免费，数据不出网）

**想让 AI 自动完成完整任务：**
→ Claude Code（CLI，适合自动化流水线）

**前端/UI 开发：**
→ v0.dev（生成 React 组件神器）

**已经在用 VS Code / JetBrains：**
→ GitHub Copilot（最无缝集成）

---

## 下一步

- [M3-02 Cursor 使用指南](./02-cursor.md)
- [M3-03 其他主流工具](./03-other-tools.md)
- [M3-04 底层原理](./04-how-it-works.md)
