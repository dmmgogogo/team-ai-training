# M11-03 · Superpowers：AI 编程 Agent 完整开发工作流

> `Superpowers` 是一套完整的 AI 编程 Agent 工作流框架，通过一组可组合的 "Skills" 让 Claude Code、Cursor、Codex 等 Agent 自动具备规范的软件开发流程——**不是提示词集合，是强制触发的工作流约束**。

GitHub：[obra/superpowers](https://github.com/obra/superpowers) · 138k ⭐

---

## 解决什么问题？

默认情况下，AI 编程 Agent 会立刻开始写代码，缺乏：

- 需求澄清与规格确认环节
- 严格的测试驱动开发（TDD）约束
- 代码审查与质量门禁
- 多 Agent 并行协作机制

Superpowers 通过 Skills 系统，让 Agent 在开始任何任务前**自动检查并触发对应的工作流**，而不是等你手动提醒。

---

## 核心工作流（按顺序触发）

| 阶段 | Skill | 作用 |
|------|-------|------|
| 1. 需求澄清 | `brainstorming` | 通过追问提炼出真实需求，分段确认设计方案，保存为设计文档 |
| 2. 隔离工作区 | `using-git-worktrees` | 在新分支创建独立工作目录，验证初始测试基线 |
| 3. 实现计划 | `writing-plans` | 拆解为 2-5 分钟的微任务，每个任务含明确文件路径和验证步骤 |
| 4. 自动执行 | `subagent-driven-development` | 每个任务派发独立子 Agent，完成后两阶段 Review（规格符合性 + 代码质量） |
| 5. 测试驱动 | `test-driven-development` | 强制 RED-GREEN-REFACTOR 循环，先测试再写代码，测试前写的代码直接删除 |
| 6. 代码审查 | `requesting-code-review` | 按严重等级报告问题，Critical 问题阻断后续步骤 |
| 7. 完成分支 | `finishing-a-development-branch` | 验证测试，选择 merge/PR/保留/丢弃，清理工作目录 |

---

## Skills 库总览

### 测试
- **test-driven-development** — RED-GREEN-REFACTOR 严格循环

### 调试
- **systematic-debugging** — 4 阶段根因定位（含条件等待、防御深度等技术）
- **verification-before-completion** — 在宣布"修好了"之前必须验证

### 协作
- **brainstorming** — Socratic 式需求设计
- **writing-plans** — 详细实现计划
- **executing-plans** — 批量执行 + 人工检查点
- **dispatching-parallel-agents** — 并发子 Agent 工作流
- **requesting-code-review** / **receiving-code-review** — 提交/接收 Review
- **using-git-worktrees** — 并行开发分支管理
- **finishing-a-development-branch** — Merge/PR 决策流
- **subagent-driven-development** — 快速迭代 + 两阶段 Review

### 元技能
- **writing-skills** — 创建新 Skill 的规范
- **using-superpowers** — 系统入门

---

## 安装

### Claude Code（官方市场，最简单）

```bash
/plugin install superpowers@claude-plugins-official
```

### Cursor

在 Cursor Agent 对话框中：

```text
/add-plugin superpowers
```

### Codex

告诉 Codex：

```
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.codex/INSTALL.md
```

### Gemini CLI

```bash
gemini extensions install https://github.com/obra/superpowers
```

### 验证安装

开新会话后说：`"help me plan this feature"` 或 `"let's debug this issue"`，如果 Agent 自动触发了对应 Skill，说明安装成功。

---

## 与 gstack 的对比

| 维度 | Superpowers | gstack |
|------|-------------|--------|
| 侧重点 | 开发流程约束（TDD、子 Agent 协作） | 产品/工程/设计/发布全链路角色扮演 |
| 触发方式 | 自动检测任务类型并触发 | 手动调用 `/slash-command` |
| 适合场景 | 注重质量、测试覆盖、严格流程 | 注重产品决策、设计 Review、快速迭代发布 |
| 平台支持 | Claude Code、Cursor、Codex、OpenCode、Gemini CLI | Claude Code、Cursor、Codex 等 |

---

## 核心理念

- **测试先行** — 先写测试，永远如此
- **系统化而非临时化** — 流程优于猜测
- **降低复杂度** — 简洁是第一目标
- **验证而非断言** — 宣布成功前必须有证据

---

## 参考

- [作者博客：Superpowers for Claude Code](https://blog.fsck.com/2025/10/09/superpowers/)
- [Discord 社区](https://discord.gg/35wsABTejz)
- [下一篇：M11-04 gstack](./04-gstack.md)
