# M3-01 · AI 编程工具全景概览

> 最后更新：2026年3月。AI 编程工具市场竞争激烈，新工具持续涌现。

---

## 工具分类（2026年现状）

```
AI 编程工具
│
├── 编辑器/IDE 类（代码编辑主战场）
│   ├── Cursor          — AI 原生 IDE，市场领导者（$500M+ ARR）
│   ├── Windsurf        — Codeium 出品，agentic 能力强，个人免费
│   ├── GitHub Copilot  — 老牌，VS Code + JetBrains 全覆盖
│   └── Zed             — 性能优先，内置 AI，原生多人协作
│
├── 终端/CLI 类（命令行直接对话）
│   ├── Claude Code     — SWE-bench 最高（80.9%），能力最强
│   ├── OpenAI Codex CLI — o3/o4 驱动，Terminal-bench 第二（77.3%）
│   ├── Gemini CLI      — 完全免费开源，Google 出品
│   └── Aider           — 开源，支持多模型，含本地模型
│
├── 自定义 Agent 类（BYOM，自带模型）
│   ├── Cline           — VS Code 插件，开源
│   ├── Kilo Code       — 轻量级
│   └── OpenCode        — 新兴
│
├── 网页/聊天类
│   ├── v0 by Vercel    — 前端 UI 生成最强
│   └── Lovable AI      — 全栈应用生成
│
└── 新兴工具（2025-2026）
    ├── Antigravity     — 完全免费（预览期无付费计划）
    ├── Kimi Code       — 月之暗面出品，开源，可自部署
    └── Kiro（AWS）     — Amazon 出品，企业向
```

---

## 主流工具对比表（2026年3月）

| 工具 | 类型 | 底层模型 | 价格 | 特色 |
|------|------|---------|------|------|
| **Cursor** | IDE | Claude / GPT-4 | $20/月 | 市场领导者，360K付费用户 |
| **Windsurf** | IDE | Claude / DeepSeek | $15/月（个人免费） | Cascade 自动任务，性价比最优 |
| **GitHub Copilot** | 插件 | GPT-4o | $10/月 | 最便宜入门，JetBrains 支持好 |
| **Claude Code** | CLI | Claude Sonnet | API 计费 | SWE-bench 第一（80.9%） |
| **Codex CLI** | CLI | o3/o4-mini | API 计费 | 速度快（240+ tok/s） |
| **Gemini CLI** | CLI | Gemini | **完全免费开源** | 唯一零成本 CLI |
| **Aider** | CLI | 多模型 | 开源+模型费 | 支持 100+ 模型含本地 |
| **Antigravity** | IDE | 多模型 | **完全免费**（预览期）| 新兴，值得关注 |
| **Kimi Code** | CLI/插件 | Kimi | 开源 | 国内可自部署 |
| **v0** | 网页 | GPT-4o | 免费额度 | 前端 UI 生成神器 |

---

## 能力维度说明

| 能力 | 说明 | 代表工具 |
|------|------|---------|
| **代码补全** | 输入时自动续写代码 | Copilot, Cursor, Windsurf |
| **Chat 对话** | 聊天方式问代码问题 | 所有工具 |
| **代码库理解** | 理解整个项目，跨文件问答 | Cursor, Claude Code |
| **自动完成任务（Agentic）** | 给个需求，自动改多个文件 | Cursor Agent, Claude Code, Windsurf Cascade |
| **终端执行** | 自动运行命令、测试 | Claude Code, Codex CLI, Aider |
| **本地模型支持** | 用 Ollama 等跑本地模型 | Aider, Cline, Kimi Code |
| **协作编辑** | 多人同时编辑 | Copilot, Windsurf, Lovable |

---

## 2026年市场关键数据

- **Cursor**：市场领导者，$500M+ ARR，360K 付费用户
- **Claude Code**：SWE-bench 评测第一（80.9%），代码能力最强
- **Codex CLI**：Terminal-Bench 第二（77.3%），速度最快（240+ tok/s）
- **Windsurf**：个人版免费，agentic 类别最佳性价比
- **Copilot**：$10/月，最便宜的有 Git 深度集成的方案

> 💡 专业建议：**同时使用多个工具**效率最高——Cursor 做日常编码，Claude Code 处理复杂代码库级任务。

---

## 选型建议

**团队日常开发首选：**
→ Cursor（综合最强，体验最好）

**预算为零：**
→ Antigravity（预览期完全免费）或 Gemini CLI（永久免费开源）

**数据隐私要求高：**
→ Aider / Kimi Code + 本地 Ollama（数据不出网）

**想让 AI 自动完成完整任务：**
→ Claude Code（代码库级自动化任务首选）

**前端/UI 开发：**
→ v0.dev（React 组件生成神器）

**已在用 JetBrains：**
→ GitHub Copilot 或 **Cursor**（2026年3月起支持 JetBrains！）

---

## 下一步

- [M3-02 Cursor 使用指南](./02-cursor.md)
- [M3-03 其他主流工具](./03-other-tools.md)
- [M3-04 底层原理](./04-how-it-works.md)
