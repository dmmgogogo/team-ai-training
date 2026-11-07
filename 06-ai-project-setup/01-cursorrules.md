# ⭐️ M6-01 · AI 项目配置：从 .cursorrules 到 AGENTS.md（2026）

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 2026 年的事实标准已经变成：**`AGENTS.md` 作为跨工具的统一入口**，各工具再叠加自己的原生文件（`CLAUDE.md`、`.cursor/rules/*.mdc`、skills 目录、MCP 配置）。`.cursorrules` 退居历史，`.mdc` 仍在，但"只写一个文件"的时代结束了。

---

## 一句话结论

| 你要解决的问题 | 2026-11 推荐写法 |
|----------------|------------------|
| 让所有 AI 工具都认识你的项目 | `AGENTS.md`（根目录；monorepo 可嵌套） |
| 给 Claude Code 更细的指令 | `CLAUDE.md` + `.claude/rules/*.md` |
| 给 Cursor 条件化规则 | `.cursor/rules/*.mdc`（或直接 `AGENTS.md`） |
| 复用多步骤流程 | `.claude/skills/<name>/SKILL.md`、`.agents/skills/` |
| 接外部工具 | `.mcp.json`（Claude Code）、`mcp.json`（Cursor） |
| 旧项目迁移 | `.cursorrules` → `.cursor/rules/*.mdc` → `AGENTS.md` / `CLAUDE.md` |

---

## 一、2026 年的项目配置全景

```
your-project/
├── AGENTS.md                    # ⭐ 跨工具统一入口（Codex / Cursor / Claude / Copilot…）
├── CLAUDE.md                    # Claude Code 专属指令（可选，可 @AGENTS.md 复用）
├── .claude/
│   ├── rules/
│   │   ├── code-style.md        # 按主题拆分的规则
│   │   └── api.md               # 可加 paths: 做路径内生效
│   └── skills/
│       └── code-review/SKILL.md # 团队技能
├── .cursor/
│   ├── rules/*.mdc              # Cursor 规则（带 frontmatter）
│   └── mcp.json                 # Cursor 的 MCP 配置
├── .agents/skills/              # 跨工具技能目录（Cursor 等可读）
├── .mcp.json                    # Claude Code 项目级 MCP
└── docs/                        # 架构、决策、运行手册
```

**核心原则：事实只写一份，其他文件引用它。**

```
AGENTS.md          ← 项目事实（构建命令、架构、约定）
   ↑ 被引用
CLAUDE.md          ← Claude 专属补充（可 @AGENTS.md）
.cursor/rules/     ← Cursor 条件化规则（可只写 Cursor 特有的）
.claude/skills/    ← 流程（按需加载，不占常驻上下文）
```

---

## 二、五种机制分别解决什么

| 机制 | 加载时机 | 适合写什么 | 不适合写什么 |
|------|----------|-----------|--------------|
| **AGENTS.md** | 会话开始（离当前文件最近的优先） | 构建/测试命令、架构、约定、PR 规范 | 特定工具的独有语法 |
| **CLAUDE.md** | 会话开始（目录层级向上合并） | 项目规范、Claude 专属偏好 | 大段参考资料 |
| **.claude/rules/** | 启动或命中 `paths` 时 | 按主题/路径拆分的规则 | 多步骤流程 |
| **.cursor/rules/*.mdc** | Always / 智能 / 文件匹配 / 手动 | Cursor 条件化规则 | 全项目通用的事实（放 AGENTS.md） |
| **Skills** | 需要时（渐进式加载） | 多步骤流程、检查清单、模板 | 每次都要知道的事实 |

> 判断口诀：**"事实"进 AGENTS.md，"条件规则"进 rules，"流程"进 skills。**

---

## 三、AGENTS.md 怎么写

### 它是什么

`AGENTS.md` 是给 AI 看的 README：一个简单、开放的格式，被 6 万多个开源项目采用，由 **Agentic AI Foundation（Linux 基金会）** 托管（来源：[agents.md](https://agents.md/)，2026-11）。

支持它的工具包括：OpenAI Codex、Google Jules、Cursor、GitHub Copilot、Gemini CLI、Aider、goose、opencode、Zed、Warp、VS Code、Devin、Junie、Amp、Windsurf、Augment Code 等。

### 写法要点

1. **覆盖"新人上手"需要的信息**：项目是什么、怎么装、怎么跑、怎么测。
2. **写约定，不写教程**：写"用 2 空格缩进"，不要写"缩进是代码格式的一种"。
3. **命令要能直接执行**，并说明期望结果。
4. **大仓库用嵌套**：每个子包一个 `AGENTS.md`，离文件最近的优先。
5. **别和 README 重复**：README 给人看，AGENTS.md 给 agent 看。

### 模板

```markdown
# AGENTS.md

## 项目概述
一句话：这是一个 [业务] 的 [技术栈] 项目，服务于 [用户]。

## 环境与命令
- 安装依赖：`pnpm install`
- 本地启动：`pnpm dev`（默认 http://localhost:5173）
- 运行测试：`pnpm test`
- 类型检查：`pnpm typecheck`
- 提交前必须：`pnpm lint && pnpm test`

## 架构
- `src/api/`      接口封装，组件内禁止直接调 axios
- `src/pages/`    页面
- `src/components/` 复用组件
- `src/stores/`   Pinia 状态
- `src/types/`    TypeScript 类型

## 代码规范
- TypeScript strict，禁止 `any`
- 组件 PascalCase，工具函数 camelCase
- 所有异步操作必须处理 loading / error / empty
- 新增依赖前先说明理由

## 不要动
- `src/legacy/`：旧代码，只读
- `vite.config.ts`：有特殊配置，改动需说明

## 提交与 PR
- commit 信息：`feat|fix|docs|refactor: 描述`
- PR 必须包含：改动说明、测试方式、影响范围
```

### monorepo：嵌套 AGENTS.md

```
repo/
├── AGENTS.md                 # 全局：技术栈、命令、协作约定
├── apps/web/AGENTS.md        # 前端专属：路由、组件规范
├── services/api/AGENTS.md    # 后端专属：分层、错误码、数据库
└── packages/ui/AGENTS.md     # 组件库专属：API 设计、版本策略
```

规则：**离被编辑文件最近的 AGENTS.md 优先**，越具体越优先。

---

## 四、CLAUDE.md 怎么写

Claude Code 在会话启动时加载 `CLAUDE.md` / `CLAUDE.local.md`，从工作目录向上逐层合并；子目录的 `CLAUDE.md` 在需要时按需加载（来源：[Claude Code Memory 文档](https://code.claude.com/docs/en/memory)，访问于 2026-11）。

### 位置与作用域

| 作用域 | 位置 | 用途 |
|--------|------|------|
| 组织级 | 受管策略目录（macOS：`/Library/Application Support/ClaudeCode/CLAUDE.md`） | 公司级规范、安全要求 |
| 用户级 | `~/.claude/CLAUDE.md` | 个人偏好 |
| 项目级 | `./CLAUDE.md` 或 `./.claude/CLAUDE.md` | 团队共享的项目规范 |
| 本地 | `./CLAUDE.local.md`（加入 `.gitignore`） | 个人项目偏好 |

### 2026 年的重要变化：Claude Code 也能读 AGENTS.md

Claude Code **v2.1.277 起**原生支持 `AGENTS.md`：

- 默认模式 `claude-md-or-agents-md`：有 `CLAUDE.md` 就读它，没有才读 `AGENTS.md`。
- 可切换为 `claude-md-and-agents-md`：两者都读。
- 想共用一份文件：在 `CLAUDE.md` 里写 `@AGENTS.md` 导入，或建软链接。

```markdown
@AGENTS.md

## Claude Code 专属
- 改动 `src/billing/` 前先进入 plan mode
- 提交前运行 `pnpm test`
```

来源：[Claude Code Memory 文档](https://code.claude.com/docs/en/memory)，2026-11。

### CLAUDE.md 写作建议

- **控制在 200 行以内**：越长越容易被忽略。
- **具体、可验证**："使用 2 空格缩进" 优于 "注意代码格式"。
- **只写 Claude 无法自己推导的信息**：命令、约定、坑、业务背景。
- **流程性内容移到 skills**，路径相关的内容移到 `.claude/rules/`。

### `.claude/rules/`：按主题/路径拆分

```markdown
---
paths:
  - "src/api/**/*.ts"
---

# API 开发规则

- 所有接口必须做入参校验
- 统一错误响应格式
- 不允许在 handler 里直接拼 SQL
```

没有 `paths` 的规则在启动时加载；有 `paths` 的规则只在 Claude 读写匹配文件时加载。

---

## 五、Cursor Rules 怎么写（`.cursor/rules/*.mdc`）

Cursor 支持四类规则（来源：[Cursor Rules 文档](https://cursor.com/docs/rules)，2026-11）：

| 类型 | 位置 | 说明 |
|------|------|------|
| **Project Rules** | `.cursor/rules/*.mdc` | 进版本库，按项目生效 |
| **User Rules** | Cursor 设置 | 个人全局 |
| **Team Rules** | 团队后台 | Team / Enterprise |
| **AGENTS.md** | 仓库根目录 | 纯 Markdown 的简化替代 |

### `.mdc` 的 frontmatter

```markdown
---
description: 规则描述（Apply Intelligently 时 AI 据此判断是否加载）
globs: src/**/*.vue, src/**/*.ts
alwaysApply: true
---

规则正文（Markdown）
```

| 模式 | 配置 | 适合 |
|------|------|------|
| Always | `alwaysApply: true` | 全局规范 |
| Apply to Specific Files | 填 `globs` | 特定目录/文件类型 |
| Apply Intelligently | 填 `description` | 让 Agent 自行判断 |
| Apply Manually | 都不填 | 用 `@rule-name` 手动引用 |

> 注意：`.cursor/rules/` 下必须是 `.mdc` 扩展名；普通 `.md` 会被忽略（要纯 Markdown 就用 `AGENTS.md`）。

### 示例

```markdown
---
alwaysApply: true
---

# 项目说明
Vue 3 + Composition API + TypeScript + Pinia + Element Plus。

# 约定
- 组件文件名 PascalCase，变量/函数 camelCase，常量 UPPER_SNAKE_CASE
- 组件内禁止直接调 API，必须走 `src/api/`
- 新增页面必须同时更新路由
- 所有异步操作处理 loading / error / empty
```

---

## 六、通用规则模板（所有项目都建议加）

这部分从旧版课程保留下来，仍然是最有效的"AI 协作约定"：

```markdown
## 语言
- 所有回复使用简体中文。

## 编码前
1. 需求有歧义时先提问确认，禁止猜测后直接编码。
2. 预计修改超过 3 个文件时，先输出任务拆分方案（每个子任务 ≤ 3 个文件）。
3. 涉及业务逻辑、数据结构、接口、数据库、权限、依赖变更时，先描述方案并等待确认。

## 编码中
4. 修 bug 的顺序：先写复现测试 → 修复 → 确认测试通过。

## 编码后
5. 列出本次变更的边缘案例与测试建议。
6. 输出变更清单表格：文件路径 | 变更类型 | 具体内容。
7. 对本次变更做一次自查（潜在 bug、安全、可读性）。

## 全局
8. 被纠正时输出：错误点 / 根因 / 防复发规则。
```

> 建议放在 `AGENTS.md` 的「协作约定」章节；Claude Code 用户也可以单独放 `.claude/rules/collaboration.md`。

---

## 七、技术栈示例（精简版）

### Go 后端（`services/api/AGENTS.md`）

```markdown
# Go 后端

## 结构与约定
- 分层：handler → service → repo，禁止跨层
- 统一响应：{"code": 0, "msg": "ok", "data": {}}
- 错误必须向上传递，禁止 log 后丢弃
- 新增接口同时更新路由注册
- 数据库字段变更需写 migration

## 命令
- 测试：`go test ./...`
- 本地启动：`make run`
```

### Flutter（`apps/app/AGENTS.md`）

```markdown
# Flutter App

## 约定
- 状态管理 Riverpod，路由 GoRouter
- 日志统一走 AppLogger，禁止 print
- 异步操作 > 300ms 必须显示 loading 并禁用按钮
- 网络图片必须有加载失败占位
- 只调用 `/api/backend/*` 与 `/api/common/*`
```

更多技术栈模板见 [M6-04 真实案例](./04-real-world-template.md)。

---

## 八、从 `.cursorrules` 迁移到 2026 标准

### 迁移路径

| 阶段 | 文件 | 状态 |
|------|------|------|
| 2023–2025 | `.cursorrules`（根目录单文件） | ❌ 旧写法，仅向后兼容 |
| 2025 | `.cursor/rules/*.mdc` | ✅ 仍有效，Cursor 官方推荐 |
| 2025–2026 | `AGENTS.md` | ✅ 跨工具标准 |
| 2026 | `AGENTS.md` + `CLAUDE.md` + rules + skills | ✅ 推荐组合 |

### 操作步骤

1. **先写 `AGENTS.md`**：把 `.cursorrules` 里的通用事实（技术栈、命令、约定）搬过去。
2. **Claude Code 用户**：让 `CLAUDE.md` 导入 `@AGENTS.md`，只补 Claude 专属内容。
3. **Cursor 用户**：保留 `.cursor/rules/*.mdc` 中依赖 glob 的条件规则；通用规则可删掉，避免重复。
4. **流程性内容拆成 skills**：审查清单、发版步骤、文档模板。
5. **验证**：分别用 Cursor、Claude Code 各跑一个真实任务，确认规则被读到。
   - Claude Code：`/context all` 查看 Memory files；`/doctor prompt-audit` 检查过时/冲突指令。
   - Cursor：在对话里问"本项目有哪些约定"，看是否引用了你的规则。
6. **删旧文件**：迁移完成后再删 `.cursorrules`，避免两套规则打架。

### 自动化辅助

- Claude Code `/init` 会读取 Cursor / Copilot 等工具的配置文件，生成 `CLAUDE.md`。
- Cursor 提供 `/migrate-to-skills`，可把部分 rules / slash commands 转成 Agent Skills。

---

## 九、团队共享与版本控制

1. `AGENTS.md`、`CLAUDE.md`、`.cursor/rules/`、`.claude/skills/` **全部提交到 Git**。
2. 个人偏好放 `CLAUDE.local.md` / 用户级规则，并加入 `.gitignore`。
3. 规则变更走 PR，指定 owner review。
4. 在 README 里说明"本项目已配置 AI 协作文件"，降低新人成本。
5. 定期清理：删除过时、冲突、重复的规则（Claude Code 可用 `/doctor prompt-audit`）。

---

## 十、历史沿革

| 时间 | 事件 |
|------|------|
| 2023 | Cursor 推出 `.cursorrules`，成为最早的"项目级 AI 规则"实践 |
| 2024–2025 | `.cursor/rules/*.mdc` 取代单文件 `.cursorrules`，支持 glob 与多文件 |
| 2025-08 | `AGENTS.md` 开放格式发布，多家编码 agent 支持 |
| 2026 | `AGENTS.md` 被 6 万+ 开源项目采用，转由 Agentic AI Foundation（Linux 基金会）托管 |
| 2026 | Claude Code 原生支持 `AGENTS.md`（v2.1.277+），默认"有 CLAUDE.md 读 CLAUDE.md，否则读 AGENTS.md" |
| 2026-11 | 推荐组合：`AGENTS.md` + `CLAUDE.md` + rules + skills + MCP 配置 |

---

## 十一、下一步

- [⭐️ M6-02 给 AI 喂上下文：项目文档规范](./02-ai-context.md)
- [M6-03 MCP 项目集成](./03-mcp-integration.md)
- [⭐️ M6-04 真实案例：全栈项目 AI 配置实战](./04-real-world-template.md)
