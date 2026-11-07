# M11-03 · Superpowers：AI 编程 Agent 完整开发工作流

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02
>
> 截至 2026-11：**约 313.6k ⭐**，最新版 **v7.0.2**（2026-11-03）。已从「Claude Code 插件」发展成**跨 Agent 的软件开发方法论 + Skills 框架**，支持 15+ 种编码 Agent。
>
> GitHub：[obra/superpowers](https://github.com/obra/superpowers)

---

## 解决什么问题？

默认情况下，AI 编程 Agent 会立刻开始写代码，缺乏：

- 需求澄清与规格确认环节
- 严格的测试驱动开发（TDD）约束
- 代码审查与质量门禁
- 多 Agent 并行协作机制

Superpowers 通过 Skills 系统，让 Agent 在开始任何任务前**自动检查并触发对应的工作流**，而不是等你手动提醒。

---

## 2026-11 的 Superpowers 有什么新东西

| 变化 | 说明 |
|------|------|
| **跨 Agent（15+）** | Claude Code、Antigravity、Codex App / CLI、Cursor、Devin CLI、Factory Droid、Gemini CLI、GitHub Copilot CLI、Grok Build CLI、Kimi Code、OpenCode、Pi、Qwen Code、Muse、Hermes 等 |
| **官方市场** | Claude 官方插件市场、Codex 官方市场、xAI 官方市场、Kimi Code 插件市场都能一键安装 |
| **v7 系列** | v7.0.0（2026-10-10）→ v7.0.2（2026-11-03），围绕跨 Agent 兼容与流程稳定性 |
| **新增技能** | `diagnosing-superpowers`（诊断一次会话哪里出问题、可导出脱敏报告） |
| **流程微调** | `executing-plans` 明确为「单上下文执行 + 最终一次审查」；`subagent-driven-development` 仍是主推路径 |

> 重要：Superpowers 的定位是「**方法论 + 自动触发的工作流约束**」，不是提示词集合。它的效果取决于 Agent 是否支持 Skills/Plugins 机制。

---

## 核心工作流（按顺序触发）

| 阶段 | Skill | 作用 |
|------|-------|------|
| 1. 需求澄清 | `brainstorming` | 通过追问提炼真实需求，分段确认设计，保存为设计文档 |
| 2. 隔离工作区 | `using-git-worktrees` | 在新分支创建独立工作目录，验证初始测试基线 |
| 3. 实现计划 | `writing-plans` | 拆解为 2-5 分钟的微任务，每个任务含明确文件路径和验证步骤 |
| 4. 自动执行 | `subagent-driven-development` | 每个任务派发独立子 Agent，完成后两阶段 Review（规格符合性 + 代码质量） |
| 5. 测试驱动 | `test-driven-development` | 强制 RED-GREEN-REFACTOR 循环，先测试再写代码 |
| 6. 代码审查 | `requesting-code-review` | 按严重等级报告问题，Critical 问题阻断后续步骤 |
| 7. 完成分支 | `finishing-a-development-branch` | 验证测试，选择 merge/PR/保留/丢弃，清理工作目录 |

---

## Skills 库总览（v7.0.2）

### 测试
- **test-driven-development** — RED-GREEN-REFACTOR 严格循环

### 调试
- **systematic-debugging** — 4 阶段根因定位（含条件等待、防御深度等技术）
- **verification-before-completion** — 宣布「修好了」之前必须验证
- **diagnosing-superpowers** — 诊断一次会话哪里出了问题，可导出脱敏报告

### 协作
- **brainstorming** — Socratic 式需求设计
- **writing-plans** — 详细实现计划
- **executing-plans** — 单上下文执行 + 最终一次审查
- **dispatching-parallel-agents** — 并发子 Agent 工作流
- **requesting-code-review** / **receiving-code-review** — 提交/接收 Review
- **using-git-worktrees** — 并行开发分支管理
- **finishing-a-development-branch** — Merge/PR 决策流
- **subagent-driven-development** — 快速迭代 + 两阶段 Review

### 元技能
- **writing-skills** — 创建新 Skill 的规范
- **using-superpowers** — 系统入门

---

## 安装（按你的 Agent 选）

### Claude Code（官方市场，最简单）

```bash
/plugin install superpowers@claude-plugins-official
```

### Antigravity

```bash
agy plugin install https://github.com/obra/superpowers
```

### Codex App / CLI

在 Codex 的 Plugins 面板搜索安装，或：

```bash
/plugins
# 搜索 superpowers → Install Plugin
```

### Cursor

在 Cursor Agent 对话框中：

```text
/add-plugin superpowers
```

### Kimi Code

```text
/plugins
# Marketplace → Superpowers → Install
# 或
/plugins install https://github.com/obra/superpowers
```

### Gemini CLI

```bash
gemini extensions install https://github.com/obra/superpowers
```

### GitHub Copilot CLI

```bash
copilot plugin marketplace add obra/superpowers-marketplace
copilot plugin install superpowers@superpowers-marketplace
```

### Grok Build CLI

```bash
grok plugin install superpowers@xai-official --trust
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
| 平台支持 | 15+ Agent（Claude Code、Antigravity、Codex、Cursor、Kimi Code 等） | Claude Code、Cursor、Codex 等 |
| 星标（2026-11） | 约 313.6k | 约 140.5k |

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

---

## 历史沿革

- **2026-11**：约 313.6k ⭐，v7.0.2；支持 15+ Agent；新增 `diagnosing-superpowers`；各主流 Agent 官方市场可一键安装。
- **2026-10-10**：v7.0.0 发布，跨 Agent 兼容成为主线。
- **2026-04（旧版）**：当时约 138k ⭐，只列 Claude Code / Cursor / Codex / Gemini CLI 四种安装方式，Skills 数量更少。
- **2025-10**：首次发布（作者博客），以 Claude Code 插件形式提供。

---

*← 返回 [M11 开发提效工具](./README.md) | [课程总览](../README.md)*
