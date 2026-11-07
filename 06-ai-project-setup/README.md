# M6 · AI 项目配置规范

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 帮助开发团队为 AI 编程工具配置最佳项目上下文，让 AI 更懂你的代码库。2026 年的标准是 **AGENTS.md 统一入口 + 各工具原生文件 + Skills + MCP**。

---

## 模块概述

本模块聚焦如何系统化地为 AI 工具配置项目环境：

- **AGENTS.md / CLAUDE.md**：项目常驻事实与约定
- **`.cursor/rules/*.mdc` / `.claude/rules/`**：条件化规则
- **Skills 目录**：可复用的多步骤流程
- **MCP 配置**：连接项目工具与数据

目标是让一份事实只维护一次，同时覆盖 Cursor、Claude Code、Codex 等不同工具。

**适合人群**：开发同学

---

## 本模块文件

| 编号 | 文件 | 内容概述 |
|------|------|----------|
| [M6-01 ⭐️](./01-cursorrules.md) | **AI 项目配置：从 .cursorrules 到 AGENTS.md** | AGENTS.md / CLAUDE.md / .cursor/rules / skills / MCP 全套写法与迁移 |
| [M6-02 ⭐️](./02-ai-context.md) | **给 AI 喂上下文：项目文档规范** | 上下文分层、AGENTS.md 模板、monorepo、docs 结构 |
| [M6-03](./03-mcp-integration.md) | **MCP 项目集成** | 项目级 MCP 配置、权限与安全、团队共享 |
| [M6-04 ⭐️](./04-real-world-template.md) | **真实案例：全栈项目 AI 配置实战** | 全栈项目模板与 2026-11 升级 checklist |

---

## 学完本模块你将掌握

- 写出团队共用的 `AGENTS.md`（含 monorepo 嵌套写法）
- 为 Claude Code 配置 `CLAUDE.md` 与 `.claude/rules/`
- 为 Cursor 配置 `.cursor/rules/*.mdc`，理解四种触发模式
- 用 Skills 承载多步骤流程，避免上下文膨胀
- 在项目中安全地集成 MCP（只读优先、密钥隔离、项目级审批）
- 把旧的 `.cursorrules` 项目平滑迁移到 2026 标准

---

## 历史沿革

| 时间 | 变化 |
|------|------|
| 2023 | `.cursorrules` 单文件成为主流 |
| 2025 | `.cursor/rules/*.mdc` 取代单文件；AGENTS.md 开放格式发布 |
| 2026 | AGENTS.md 被 6 万+ 项目采用，Claude Code 原生支持；Skills 成为跨工具标准 |
| 2026-11 | 推荐组合：AGENTS.md + CLAUDE.md + rules + skills + MCP |

---

*← 返回 [课程总览](../README.md)*
