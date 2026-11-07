# ⭐️ M6-02 · 给 AI 喂上下文：项目文档规范

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> AI 对你项目的了解程度，直接决定它输出的质量。2026 年的做法不再是"额外写一个 AI-CONTEXT.md"，而是**把上下文分层写进 AGENTS.md / CLAUDE.md / rules / skills**，让每个工具都能按需读取。

---

## 一句话结论

```
常驻事实  → AGENTS.md（或嵌套 AGENTS.md）
条件规则  → .claude/rules/、.cursor/rules/*.mdc
多步流程  → Skills（SKILL.md）
外部系统  → MCP
人看文档  → docs/（架构、决策、运行手册）
```

**原则：同一份事实只写一次，其他地方引用；越靠近代码的规则越具体。**

---

## 一、AI 读项目的方式（2026-11）

一次编码会话里，AI 通常按以下顺序获取上下文：

```
1. 系统提示 + 工具定义
2. AGENTS.md / CLAUDE.md        ← 项目常驻事实
3. .claude/rules / .cursor/rules ← 条件规则（可能按路径加载）
4. Skills                        ← 命中时才加载的流程
5. MCP 工具                      ← 需要时调用外部系统
6. 你 @ 引用的文件 / 检索结果     ← 本次任务相关代码
```

**问题**：自动检索能看到的代码有限，复杂项目里 AI 经常"找不到"关键信息。

**解法**：把你希望它**每次都知道**的事写进 AGENTS.md；把**只在特定场景需要**的事写成 rules 或 skills。

---

## 二、先分层，再动笔

| 内容类型 | 放哪里 | 例子 |
|----------|--------|------|
| 项目是什么、怎么跑、怎么测 | `AGENTS.md` | 安装命令、启动命令、测试命令 |
| 架构与目录约定 | `AGENTS.md` | `src/api/` 管接口，组件禁止直接调 axios |
| 按文件类型生效的规范 | `.claude/rules/`、`.cursor/rules/*.mdc` | `src/api/**` 下的错误处理规范 |
| 多步骤流程 | Skills | 代码审查、发版检查、事故复盘 |
| 背景资料、决策记录 | `docs/` | ADR、数据库设计、接口文档 |
| 外部系统连接 | MCP | 查数据库、读 Issue、查监控 |

---

## 三、AGENTS.md 完整模板

```markdown
# AGENTS.md

> 本文件给 AI 编码 agent 阅读。人类入门请看 README.md。

## 1. 项目概述
[一句话：这是一个什么项目，解决什么问题，服务谁]

## 2. 环境与命令
| 目的 | 命令 | 备注 |
|------|------|------|
| 安装依赖 | `pnpm install` | Node >= 20 |
| 本地启动 | `pnpm dev` | http://localhost:5173 |
| 运行测试 | `pnpm test` | 提交前必须通过 |
| 类型检查 | `pnpm typecheck` | |
| Lint | `pnpm lint` | |

## 3. 架构
```
src/
├── api/          # 接口封装（按模块分文件）
├── components/   # 公共组件
├── pages/        # 页面
├── stores/       # Pinia store
├── types/        # TypeScript 类型
└── utils/        # 工具函数
```

## 4. 核心业务
- 用户：登录/注册/权限，见 `src/pages/auth/`
- 订单：下单/支付/查询，见 `src/pages/order/`

## 5. 约定
- TypeScript strict，禁止 `any`
- 组件 PascalCase，变量/函数 camelCase
- 所有异步操作处理 loading / error / empty
- 新增接口必须在 `src/api/` 建对应文件
- 统一错误处理在 `src/utils/errorHandler.ts`

## 6. 不要动
- `src/legacy/`：旧代码，只读
- `vite.config.ts`：有特殊配置

## 7. 提交与 PR
- commit：`feat|fix|docs|refactor: 描述`
- PR 必须包含：改动说明、测试方式、影响范围

## 8. 协作约定
- 需求不清晰先提问，不要猜
- 修改只改必要部分，不重构无关代码
- 引入新依赖前先说明
```

### 使用方式

```
你：@AGENTS.md 帮我在订单模块新增一个退款申请页面
AI：[基于完整上下文，给出符合项目规范的代码]
```

---

## 四、CLAUDE.md 模板（Claude Code 用户）

如果同时用 Claude Code，推荐让 `CLAUDE.md` **导入** `AGENTS.md`，只补 Claude 专属内容：

```markdown
@AGENTS.md

## Claude Code 专属
- 改动 `src/billing/` 前先进入 plan mode
- 提交前运行 `pnpm test`
- 生成代码后自行跑 `pnpm typecheck`
```

> Claude Code v2.1.277+ 默认在**没有** CLAUDE.md 时直接读 AGENTS.md；也可以设置 `claude-md-and-agents-md` 两者都读（见 [M6-01](./01-cursorrules.md)）。

### 什么时候需要额外的 CLAUDE.md

- 团队里 Claude Code 用法有特殊约定（plan mode、hook、权限）；
- 需要按目录给 Claude 更细的指令（如 `backend/CLAUDE.md`）；
- 需要引用 Claude 专属的 skills / subagents。

---

## 五、`.claude/rules/`：按主题和路径拆分

```
.claude/rules/
├── code-style.md
├── testing.md
├── security.md
└── api.md
```

```markdown
---
paths:
  - "src/api/**/*.ts"
  - "src/types/**/*.ts"
---

# API 与类型规范

- 每个接口必须有请求/响应类型定义
- 错误统一抛 `ApiError`，不在调用方手写 try/catch
- 不允许在类型文件里写运行时逻辑
```

加载规则：

| 规则 | 加载时机 |
|------|----------|
| 无 `paths` | 每次会话启动时 |
| 有 `paths` | Claude 读写匹配文件时 |
| 子目录 `.claude/rules/` | 进入该目录时按需加载 |

> 官方建议：**常驻内容控制在 200 行以内**；超出部分拆成 rules 或 skills。

---

## 六、Monorepo：用嵌套文件表达"局部事实"

```
repo/
├── AGENTS.md                  # 全局事实与约定
├── apps/
│   ├── web/AGENTS.md          # 前端：路由、组件、状态
│   └── app/AGENTS.md          # 移动端：平台差异、发布流程
├── services/
│   ├── api/AGENTS.md          # 后端：分层、错误码、数据库
│   └── worker/AGENTS.md       # 任务队列：重试、幂等
└── packages/
    └── ui/AGENTS.md           # 组件库：API 设计、版本策略
```

规则：**离被编辑文件最近的 AGENTS.md 优先**。子项目的规范不要塞进根文件，否则根文件会失控膨胀。

---

## 七、文档怎么写，AI 才用得上

### 1. 具体、可验证

```markdown
❌ "注意代码风格"
✅ "使用 2 空格缩进；字符串用单引号；禁止分号"
```

### 2. 写"差异"，不写"常识"

模型已经知道什么是 REST、什么是单元测试。写你们**和默认做法不一样**的地方：

```markdown
- 我们不使用 ORM 的自动迁移，所有 schema 变更走手写 SQL + migration 文件
- 分页参数统一用 page/page_size，默认 page_size=20
```

### 3. 给"坑"留位置

```markdown
## 已知的坑
- `src/utils/date.ts` 里的时区处理有历史包袱，新增逻辑请用 dayjs
- 测试环境 Redis 是共享的，测试用例必须用独立 key 前缀
```

### 4. 控制长度

- AGENTS.md 建议 **200 行以内**；
- 超过 200 行 → 拆分（嵌套 AGENTS.md / rules / skills）；
- 大段资料 → 放 `docs/`，在 AGENTS.md 里给路径。

### 5. 保持"活"的

规则会过期。每次发现 AI 重复犯同一个错，就更新一次规则；定期用 `/doctor prompt-audit` 这类工具检查冲突和过时指令。

---

## 八、人看的文档：`docs/` 该有什么

AI 也需要"能查到"的项目资料。建议的最小集合：

| 文档 | 内容 | AI 怎么用 |
|------|------|-----------|
| `docs/ARCHITECTURE.md` | 系统架构、模块边界、数据流 | 复杂改动前引用 |
| `docs/ADR/` | 架构决策记录（为什么这么选） | 避免 AI 提出已被否决的方案 |
| `docs/API.md` | 接口清单与约定 | 生成调用代码 |
| `docs/SCHEMA.md` | 数据库表结构 | 写 SQL、改模型 |
| `docs/RUNBOOK.md` | 部署、回滚、排障 | 运维类任务 |
| `docs/GLOSSARY.md` | 业务术语表 | 统一命名与理解 |

在 `AGENTS.md` 里指向它们：

```markdown
## 深入资料
- 架构：`docs/ARCHITECTURE.md`
- 决策记录：`docs/ADR/`
- 接口：`docs/API.md`
- 排障：`docs/RUNBOOK.md`
```

---

## 九、历史：AI-CONTEXT.md 时代（2025）

2025 年很多团队会额外维护一个 `AI-CONTEXT.md`，在对话里手动 `@` 引用：

```markdown
# 项目 AI 上下文文档
## 项目概述
## 技术栈
## 目录结构
## 核心业务模块
## 重要约定
## 不要碰的地方
```

**这种做法今天仍然可用，但已不是首选**，原因：

1. 需要手动引用，AI 不会自动读；
2. 与 AGENTS.md / CLAUDE.md 内容重复；
3. 多工具场景下每换一个工具就要重新适配。

**迁移建议**：把 `AI-CONTEXT.md` 的内容拆进 `AGENTS.md`（常驻事实）、`.claude/rules/`（条件规则）、`docs/`（参考资料），然后删除旧文件。

---

## 历史沿革

- **2023**：手工维护 `AI-CONTEXT.md`，在对话里手动引用。
- **2024**：`.cursorrules` / `CLAUDE.md` 成为主流，工具开始自动读取。
- **2025**：`AGENTS.md` 出现并被多个工具支持；规则开始分目录、分场景。
- **2026**：AGENTS.md / CLAUDE.md / `.cursor/rules/` / Skills 分层共存，强调"常驻事实 + 条件规则 + 按需知识"。

---

## 十、下一步

- [M6-03 MCP 项目集成](./03-mcp-integration.md)
- [⭐️ M6-01 AI 项目配置：从 .cursorrules 到 AGENTS.md](./01-cursorrules.md)
- [⭐️ M6-04 真实案例：全栈项目 AI 配置实战](./04-real-world-template.md)
