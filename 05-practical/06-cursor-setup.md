# M5-06 · Cursor 正确配置与高效使用

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02
>
> 基于 **Cursor 3**（2026-04 新界面）。下载装上不等于用好：从规则、模型到 Agent 工作流，这份是团队落地版。

---

## 安装与初始配置

**下载：** [cursor.com/download](https://cursor.com/download)（选对应系统版本）

安装后首次启动：
1. 导入 VS Code 配置（插件、主题、快捷键，一键迁移）
2. 登录 / 注册 Cursor 账号
3. 选择订阅计划（个人 Premium 起步，团队用 Teams；见下文价格）

**Cursor 3 的界面切换：**
- `Cmd+Shift+P` → `Agents Window`：新的 Agent 工作台
- 随时可以切回 IDE 界面看文件、跳转定义、用 LSP

---

## 模型选择配置（2026-11）

**位置：** 右上角齿轮 → Models（或在 Chat 里输入 `/model`）

| 模型 | 适合场景 | 备注 |
|------|---------|------|
| **Grok 4.7** | 长程编码、Agent 任务 | Cursor 默认家族；256k / 500k 上下文 |
| **Composer 2.5** | 日常迭代、快速修改 | Cursor 自有模型，额度较宽松 |
| **Claude Sonnet 5.5** | 日常编码、代码质量 | 第三方模型，按 API 价 |
| **Claude Opus 5.5** | 复杂架构、深度重构 | 第三方模型，贵但稳 |
| **GPT-6 系列 / Fable 5.1 / Gemini 3.1 Pro** | 按任务选择 | 以客户端列表为准 |
| **cursor-small（Tab 补全）** | 简单补全，极快省额度 | 不占对话模型额度 |

**配置建议：**
- Tab 补全 → 默认小模型（速度优先）
- Chat 对话 → Sonnet 5.5（质量/成本平衡）
- Agent 任务 → Grok 4.7 或 Opus 5.5（能力优先）
- 简单批量 → Haiku 5.5 / Composer

> ⚠️ 套餐限制：Plus（$8）**只能选 Grok 模型**；第三方模型要 Premium 及以上，且按 API 价另计。`/model` 里没有的模型就是当前套餐不可用。

---

## 规则体系（2026 正确写法）

Cursor 现在有四类规则（[官方文档](https://cursor.com/docs/rules)）：

| 类型 | 位置 | 说明 |
|------|------|------|
| **Project Rules** | `.cursor/rules/*.mdc` | 随仓库提交，团队共享 |
| **User Rules** | 客户端设置 | 当前用户全局 |
| **Team Rules** | 团队后台 | Team / Enterprise 计划 |
| **AGENTS.md** | 仓库根目录 | 纯 Markdown 的轻量方案 |

> 📌 **重要**：`.cursorrules` 是旧写法，已不推荐；`.cursor/rules/` 下的 `.md` 文件不会被识别（缺 frontmatter）。要写纯 Markdown，用根目录 `AGENTS.md`。

### 通用模板（后端）

```markdown
---
description: Python FastAPI 后端规范
globs: ["**/*.py"]
alwaysApply: false
---

# 项目信息
这是一个 B2B SaaS 后端项目。

# 技术栈
- 语言：Python 3.11+
- 框架：FastAPI
- 数据库：PostgreSQL + SQLAlchemy 2.0
- 测试：pytest

# 代码规范
- 所有函数必须有 type hints
- 公开函数必须写 docstring（Google 风格）
- 异步优先：所有 IO 操作用 async/await
- 统一错误处理：使用自定义异常类
- 日志：用 structlog，不用 print

# 命名规范
- 函数：snake_case
- 类：PascalCase
- 常量：UPPER_SNAKE_CASE
- 私有：_前缀

# 禁止事项
- 不在 API 层写业务逻辑
- 不硬编码任何密钥或配置
- 不用旧式 SQLAlchemy query() API
- 不用 print 调试，用 logger

# 输出要求
- 生成代码时同时给出单元测试框架
- 有安全风险时主动提示
```

### 前端项目模板

```markdown
---
description: React 前端规范
globs: ["src/**/*.{ts,tsx}"]
alwaysApply: false
---

# 技术栈
- React 18 + TypeScript
- Tailwind CSS + shadcn/ui
- Vite 构建
- React Query 数据请求

# 规范
- 组件用函数式，不用 class
- 状态管理用 Zustand
- 样式只用 Tailwind，不写 CSS 文件
- 组件文件：PascalCase.tsx
- 工具函数：camelCase.ts
```

### 规则写法建议

- **一条规则只解决一类问题**，按目录拆成多个 `.mdc`
- `alwaysApply: true` 只留给「所有任务都必须遵守」的硬约束，否则会浪费上下文
- 用 `globs` 限定适用范围（比如只对 `**/*.py` 生效）
- 规则越短越好；长篇规范放 `docs/`，用 `@docs` 引用

---

## Context 配置（@引用技巧）

### @文件 / @目录
```
@src/services/auth.py 这里的 JWT 验证逻辑有什么安全问题？

@src/api/ 给这个目录下所有接口添加统一的请求日志中间件
```

### @docs（第三方文档）
```
设置路径：Settings → Features → Docs → Add docs URL

添加你的技术栈文档：
- FastAPI: https://fastapi.tiangolo.com
- SQLAlchemy: https://docs.sqlalchemy.org/en/20/
- React: https://react.dev

然后使用：
@FastAPI 帮我写一个带分页的列表接口
```

### @web（实时搜索）
```
@web 2026年 Python 异步数据库最佳实践是什么？
```

### @git（代码历史）
```
@git 最近3个 commit 改了什么？有没有引入 bug 的风险？
```

---

## Privacy Mode（隐私模式）

**重要！** 如果项目有保密要求：

**位置：** Settings → General → Privacy Mode → Enable

开启后：
- 代码不会被发送给模型厂商用于训练
- 对话不会被存储在 Cursor 服务器
- Teams 及以上计划可配置团队级隐私设置

> ⚠️ Free 计划能力有限，团队项目务必使用 Premium / Teams 及以上，并在团队后台统一配置隐私与数据保留策略。

---

## Agent / Agents Window 最佳实践

**打开方式：**
- `Cmd+I`（Mac）/ `Ctrl+I`（Windows）打开 Agent
- `Cmd+Shift+P` → `Agents Window` 打开 Cursor 3 工作台

### ✅ 适合 Agent 的任务
```
"根据 @docs/requirements.md 实现用户模块，包含注册、登录、修改密码接口"

"重构 @src/legacy/ 目录下的旧代码，按照规则文件统一风格"

"为 @src/ 中所有没有单元测试的函数，生成对应的测试文件"
```

### ❌ 不适合 Agent 的任务
```
"帮我做整个系统" → 太宽泛，拆小再做
"改一下这行代码" → 用 Cmd+K 内联编辑更快
```

### Agent 运行时的控制技巧

```
运行中可以：
- 随时 ESC 暂停
- 点 Accept All / Reject All 批量接受/拒绝
- 在输入框追加说明，引导方向
- 本地任务可以 "move to cloud" 交给云端继续跑

运行前建议：
- git commit 保留干净状态（万一改坏了可以回滚）
- 明确指定需要修改哪些文件，用 @引用
- 确认没开「自动运行所有命令」
```

### 本地 ⇄ 云端交接

- **本地 → 云端**：任务跑得久、要关电脑时，把会话移到云端
- **云端 → 本地**：需要本地调试、跑测试时，把会话拉回本地
- 云端 Agent 会产出 demo / 截图，验收后再合并

---

## Notepads（跨对话记忆）

**位置：** 左侧边栏 → Notepads

可以保存常用的上下文信息，每次对话自动引用：

```
Notepad: "项目背景"
---
这是一个 B2B SaaS 平台，服务对象是中小企业 HR。
主要功能：考勤管理、薪资计算、员工档案。
数据库有 50 万员工记录，性能要求较高。
当前技术负债：有大量未测试的旧代码。
```

> 2026 年的替代方案：把这些背景写进 `AGENTS.md` 或 Project Rules，效果更稳定、可版本控制。

---

## JetBrains 用户配置（2026）

Cursor 通过 **ACP（Agent Client Protocol）** 支持 JetBrains IDE（IntelliJ IDEA、PyCharm、WebStorm 等）：

1. 在 JetBrains 的 **ACP Registry** 里安装 Cursor ACP
2. 用现有 Cursor 账号登录
3. 在 ACP 面板里选择模型、开始 Agent 任务

功能覆盖：Chat、代码解释、Agent 任务；**付费计划用户免费**。

> 注意：这不是完整 Cursor 客户端，Tab 补全等能力仍以 JetBrains 自带 AI 功能为准。来源：[Cursor 博客](https://cursor.com/blog/jetbrains-acp)，2026-03。

---

## 快捷键速查表

| 快捷键（Mac）| Windows | 功能 |
|-------------|---------|------|
| `Tab` | `Tab` | 接受代码补全 |
| `Esc` | `Esc` | 拒绝补全 / 暂停 Agent |
| `Cmd+K` | `Ctrl+K` | 内联编辑（选中代码后）|
| `Cmd+L` | `Ctrl+L` | 打开 Chat |
| `Cmd+I` | `Ctrl+I` | 打开 Agent |
| `Cmd+Shift+P` → `Agents Window` | `Ctrl+Shift+P` | 打开 Cursor 3 工作台 |
| `Cmd+Shift+L` | `Ctrl+Shift+L` | 把选中代码发到 Chat |
| `@` | `@` | 在 Chat 中引用文件/符号 |
| `Cmd+.` | `Ctrl+.` | 接受下一个单词 |

---

## 定价（2026-11，以官网为准）

| 计划 | 价格 | 内容 |
|------|------|------|
| Free | $0/月 | 有限 Agent / Chat 请求 |
| Plus | $8/月 | 共享用量池；**仅 Grok 模型** |
| Premium | $30/月 | 4× Plus；Cloud agents；第三方模型按 API 价 |
| Super | $100/月 | 15× Plus；高峰期优先 |
| Ultra | $200/月 | 50× Plus；最早获得新模型 |
| Teams | $30+/人/月 | 团队管理、SSO、隐私设置 |
| Enterprise | 定制 | 审计、网络/MCP 管控、SCIM |

来源：[cursor.com/pricing](https://cursor.com/pricing)，2026-11 核对；价格不含税，第三方模型另计。

---

## 常见问题

**Q：补全一直是错的怎么办？**
→ 检查规则文件是否清晰；在 Chat 里先解释项目背景；确认 `globs` 没写错

**Q：Agent 改了不该改的文件？**
→ 运行前 git commit；用 @文件名 明确范围；收紧命令审批

**Q：速度很慢？**
→ Tab 补全用小模型；Chat 换 Haiku 5.5 / Sonnet 5.5；检查是否是第三方模型的网络延迟

**Q：团队协作怎么统一配置？**
→ 把 `.cursor/rules/*.mdc` 提交到 git；Team 计划再用 Team Rules 兜底；跨工具统一写 `AGENTS.md`

**Q：规则文件放在 `.cursor/rules/` 但没生效？**
→ 检查扩展名是否为 `.mdc`；`alwaysApply` / `globs` / `description` 是否写对

---

## 历史沿革

- **2026-11**：按 Cursor 3 重写；规则体系改为 Project / User / Team Rules + `AGENTS.md`；模型更新为 Grok 4.7 / Composer 2.5 / Claude 5.5；价格更新为 Free / Plus $8 / Premium $30 / Super $100 / Ultra $200。
- **2026-04**：Cursor 3 发布（Agents Window、多仓库、并行 Agent、本地⇄云端交接）。
- **2026-03**：Cursor 通过 ACP 支持 JetBrains（本文「JetBrains 用户配置」一节由此而来）；本课程统一 `.cursor/rules/*.mdc` 写法。
- **2026-03 旧版**：本文曾按 `.cursorrules` + Pro $20 / Business $40 + Claude 4.5/4.6 模型编写，现已作为历史保留。
- **2025**：Cursor 2 / Composer 工作流；Rules 从 `.cursorrules` 迁移到 `.cursor/rules`。

---

## 下一步

- [M5-07 ChatGPT 正确配置与使用](./07-chatgpt-setup.md)
- [M5-08 Claude 正确配置与使用](./08-claude-setup.md)
- [M6-01 Cursor Rules 配置指南](../06-ai-project-setup/01-cursorrules.md)
