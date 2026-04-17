# M3-01 · AI 编程工具全景概览

> P26年4月。  
> 本页采用“稳态信息”维护：保留工具定位与使用建议，删除易失真硬编码数据（如固定跑分、用户数、ARR）。

---

## 工具分类（长期有效版）

```
AI 编程工具
│
├── IDE / 编辑器类（主战场）
│   ├── Cursor
│   ├── Windsurf
│   ├── GitHub Copilot
│   └── Zed / Continue（插件形态）
│
├── CLI / 终端类（自动化和批处理友好）
│   ├── Claude Code
│   ├── OpenAI Codex CLI
│   ├── Gemini CLI
│   └── Aider
│
├── Agent 构建类（高度自定义）
│   ├── Cline
│   ├── Kilo Code
│   └── OpenCode
│
└── 生成式应用类（偏产品和原型）
    ├── v0
    └── Lovable
```

---

## 主流工具对比（稳态维度）

| 工具 | 形态 | 计费模式 | 适合场景 | 风险点 |
|------|------|----------|----------|--------|
| **Cursor** | IDE | 订阅制 | 日常主力开发、多人协作 | 上下文过大时成本上升 |
| **Windsurf** | IDE | 免费+订阅 | 个人开发、自动任务 | 新功能迭代快，行为可能变化 |
| **GitHub Copilot** | 插件 | 订阅制 | JetBrains/VS Code 团队 | 深度自动化能力相对保守 |
| **Claude Code** | CLI | API 计费 | 代码库级改造、批量任务 | 任务放权过大需审查 |
| **Codex CLI** | CLI | API 计费 | 终端推理、快速迭代 | 成本波动依赖模型与上下文 |
| **Gemini CLI** | CLI | 免费/配额 | 低预算试用、轻量任务 | 区域可用性与策略变化 |
| **Aider** | CLI | 开源+模型费 | 多模型接入、本地模型 | 初次配置门槛略高 |
| **v0** | Web | 免费+订阅 | 前端页面原型与组件生成 | 偏前端场景，不适合后端主流程 |

---

## 选型四问（先问再选）

1. **团队主战场在哪？**  
   - IDE 为主：优先 Cursor / Copilot / Windsurf  
   - 终端自动化为主：优先 Claude Code / Codex CLI / Aider

2. **预算模型是“订阅”还是“按量”？**  
   - 预算稳定：订阅更好管控  
   - 需求波动大：API 按量更灵活

3. **合规要求高吗？**  
   - 高合规：优先可控的数据策略（团队版、私有化、本地模型）

4. **是否需要 AI 自动执行整套任务？**  
   - 需要：选 Agent 能力强的工具（Cursor Agent / Claude Code / Windsurf）

---

## 团队推荐基线组合（可直接落地）

- **IDE 主力**：Cursor 或 Copilot（二选一）
- **CLI 补位**：Claude Code 或 Codex CLI（二选一）
- **本地兜底**：Aider + Ollama（用于敏感数据或离线开发）
- **前端提速**：v0（仅用于 UI 草图与组件初稿）

---

## 为什么删除了很多“排行榜数字”

这次深度维护主动删除了以下高过期风险信息：

- 固定跑分结论（如“某工具长期第一”）
- 固定商业数据（如 ARR、付费用户规模）
- 固定速度口径（如 tok/s 单值）

原因：这些信息变化太快，且不同评测口径差异大。课程以“决策方法”优先，避免团队被陈旧数字误导。

---

## 官方入口（按需自查最新信息）

| 工具 | 官网 | 文档 |
|------|------|------|
| Cursor | [cursor.com](https://www.cursor.com) | [docs.cursor.com](https://docs.cursor.com) |
| Windsurf | [codeium.com/windsurf](https://codeium.com/windsurf) | [docs.codeium.com/windsurf](https://docs.codeium.com/windsurf/getting-started) |
| GitHub Copilot | [github.com/features/copilot](https://github.com/features/copilot) | [docs.github.com/en/copilot](https://docs.github.com/en/copilot) |
| Claude Code | [anthropic.com/claude-code](https://www.anthropic.com/claude-code) | [docs.anthropic.com](https://docs.anthropic.com/en/docs/claude-code/overview) |
| Codex CLI | [openai.com](https://openai.com) | [platform.openai.com/docs](https://platform.openai.com/docs) |
| Gemini CLI | [github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | — |
| Aider | [aider.chat](https://aider.chat) | [aider.chat/docs](https://aider.chat/docs/install.html) |
| v0 | [v0.dev](https://v0.dev) | — |

---

## 下一步

- [M3-02 Cursor 使用指南](./02-cursor.md)
- [M3-03 其他主流工具](./03-other-tools.md)
- [M3-04 AI 编程工具底层原理](./04-how-it-works.md)
