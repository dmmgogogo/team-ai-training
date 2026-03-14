# M5-06 · Cursor 正确配置与高效使用

> 下载装上不等于用好。从配置到工作流，完整上手指南。

---

## 安装与初始配置

**下载：** [cursor.com](https://www.cursor.com)（选对应系统版本）

安装后首次启动：
1. 导入 VS Code 配置（插件、主题、快捷键，一键迁移）
2. 登录 / 注册 Cursor 账号
3. 选择订阅计划（团队建议 Business，个人 Pro 即可）

---

## 模型选择配置

**位置：** 右上角齿轮 → Models

| 模型 | 适合场景 | 速度 |
|------|---------|------|
| **claude-sonnet-4-5**（推荐） | 日常编码，代码质量高 | 中 |
| **claude-sonnet-4-6** | 最新，复杂推理任务 | 中 |
| **gpt-4o** | 多模态（图片分析）、通用任务 | 快 |
| **o3 / o4-mini** | 数学、算法、复杂推理 | 慢但准 |
| **cursor-small** | 简单补全，极快，省额度 | 极快 |

**配置建议：**
- Tab 补全 → cursor-small（速度优先）
- Chat 对话 → claude-sonnet-4-5（质量优先）
- Agent 任务 → claude-sonnet-4-6（能力优先）

---

## .cursorrules 必配

在**每个项目根目录**创建 `.cursorrules` 文件，这是 Cursor 最重要的配置之一。

**通用模板：**

```markdown
# 项目信息
这是一个 [你的项目类型] 项目。

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

**前端项目模板：**

```markdown
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
- 代码不会被发送给 Anthropic/OpenAI 用于训练
- 对话不会被存储在 Cursor 服务器
- Business 计划默认开启

> ⚠️ Free 计划无法使用 Privacy Mode，团队项目务必使用 Pro / Business。

---

## Agent 模式最佳实践

**打开方式：** `Cmd+I`（Mac）/ `Ctrl+I`（Windows）

### ✅ 适合 Agent 的任务
```
"根据 @docs/requirements.md 实现用户模块，包含注册、登录、修改密码接口"

"重构 @src/legacy/ 目录下的旧代码，按照 .cursorrules 规范统一风格"

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

运行前建议：
- git commit 保留干净状态（万一改坏了可以回滚）
- 明确指定需要修改哪些文件，用 @引用
```

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

---

## JetBrains 用户配置（2026.3 新增）

Cursor 现已支持 JetBrains IDE（需要版本 ≥ 2025.3.2）：

1. 在 JetBrains Marketplace 安装 **AI Assistant** 插件
2. 在 AI Assistant 设置中选择 **Cursor** 作为提供商
3. 登录 Cursor 账号

功能覆盖：Chat、代码解释、Agent 任务（暂不含 Tab 补全）

---

## 快捷键速查表

| 快捷键（Mac）| Windows | 功能 |
|-------------|---------|------|
| `Tab` | `Tab` | 接受代码补全 |
| `Esc` | `Esc` | 拒绝补全 |
| `Cmd+K` | `Ctrl+K` | 内联编辑（选中代码后）|
| `Cmd+L` | `Ctrl+L` | 打开 Chat |
| `Cmd+I` | `Ctrl+I` | 打开 Agent |
| `Cmd+Shift+L` | `Ctrl+Shift+L` | 把选中代码发到 Chat |
| `@` | `@` | 在 Chat 中引用文件/符号 |
| `Cmd+.` | `Ctrl+.` | 接受下一个单词 |

---

## 常见问题

**Q：补全一直是错的怎么办？**
→ 检查 .cursorrules 是否清晰；在 Chat 里先解释项目背景

**Q：Agent 改了不该改的文件？**
→ 运行前 git commit；用 @文件名 明确范围

**Q：速度很慢？**
→ Tab 补全换 cursor-small 模型；Chat 换 claude-haiku

**Q：团队协作怎么统一配置？**
→ 把 .cursorrules 提交到 git，所有人自动共享

---

## 下一步

- [M5-07 ChatGPT 正确配置与使用](./07-chatgpt-setup.md)
- [M5-08 Claude 正确配置与使用](./08-claude-setup.md)
