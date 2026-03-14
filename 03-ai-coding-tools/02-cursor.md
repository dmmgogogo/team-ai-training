# M3-02 · Cursor 使用指南

> 当前最流行的 AI IDE，把 VS Code 的熟悉感和 AI 的强大结合在一起。

---

## 什么是 Cursor？

Cursor 是一个基于 VS Code 深度改造的 **AI 原生代码编辑器**。它不只是加了个 AI 插件，而是从底层重新设计了人机协作的方式。

- 下载地址：[cursor.com](https://www.cursor.com)
- 基于 VS Code，所有 VS Code 插件和快捷键都能用
- 底层调用 Claude 3.5/3.7 Sonnet 或 GPT-4o

---

## 核心功能

### 1. Tab 补全（最常用）

```
你写代码时，Cursor 会灰色提示你"接下来可能写什么"
按 Tab 键接受建议，Esc 忽略
```

不只补全一行，而是能补全整个函数、整块逻辑。

**示例：**
```python
def calculate_discount(price, member_level):
    # 按 Tab，Cursor 会自动写出逻辑
    if member_level == "gold":
        return price * 0.8
    elif member_level == "silver":
        return price * 0.9
    else:
        return price
```

---

### 2. Cmd+K（内联编辑）

在代码中按 `Cmd+K`（Mac）/ `Ctrl+K`（Windows），直接用自然语言指令修改代码：

```
选中一段代码 → Cmd+K → 输入"把这个函数改成异步的"
→ Cursor 直接在原地修改，可以接受或拒绝
```

适合：快速重构、修改逻辑、格式转换

---

### 3. Cmd+L · Chat 模式（对话）

按 `Cmd+L` 打开右侧 Chat 面板：

- 问代码问题："这个 bug 是什么原因？"
- 让它生成代码："写一个 JWT 验证中间件"
- 解释代码："解释这段正则表达式"

**关键技巧：** 使用 `@` 引用文件/函数

```
@src/auth.py 这个文件的认证逻辑有什么问题？

@docs/api.md 根据这个 API 文档，帮我写请求函数
```

---

### 4. Agent 模式（自动任务）

Cursor 最强大的模式。你描述需求，它自动：
- 读取相关文件
- 修改多个文件
- 运行命令和测试
- 修复出现的错误

```
示例 Prompt：
"根据 models/user.py 中的用户模型，
 创建 CRUD API 接口，包含增删改查，
 并添加输入验证和错误处理"
```

Cursor 会自动操作多个文件，一次性完成任务。

---

## 实用技巧

### @符号用法

| 语法 | 作用 |
|------|------|
| `@文件名` | 引用某个文件 |
| `@目录名` | 引用整个目录 |
| `@函数名` | 引用特定函数 |
| `@docs` | 搜索 Cursor 索引的文档 |
| `@web` | 实时搜索网页 |
| `@git` | 引用 Git 历史 |
| `#终端输出` | 引用终端错误信息 |

### .cursorrules 文件

在项目根目录创建 `.cursorrules` 文件，给 Cursor 写项目规则：

```
.cursorrules 示例：

You are an expert in Python FastAPI.
- Always use async/await
- Follow PEP8 style
- Add docstrings to all functions
- Use Pydantic v2 for data validation
- Write tests for all new functions
```

这样 Cursor 在这个项目里就会按你的规范写代码。

---

## 常用快捷键

| 快捷键 | 功能 |
|--------|------|
| `Tab` | 接受代码补全 |
| `Cmd+K` | 内联编辑 |
| `Cmd+L` | 打开 Chat |
| `Cmd+I` | 打开 Agent 模式 |
| `Cmd+Shift+L` | 把选中代码发送到 Chat |
| `Esc` | 拒绝建议 |

（Windows 把 Cmd 换成 Ctrl）

---

## 定价

| 计划 | 价格 | 内容 |
|------|------|------|
| Free | 免费 | 有限 Claude 使用次数 |
| Pro | $20/月 | 无限制，含 GPT-4o + Claude Sonnet |
| Business | $40/月/人 | 团队管理，数据隐私 |

> 💡 团队购买 Business 计划可以关闭"改善产品"数据收集。

---

## 实战场景示例

### 场景一：Debug
```
1. 代码报错 → 复制错误信息
2. Cmd+L → 粘贴错误 → "这是什么错误，怎么修复？"
3. 直接让 Cursor 修改代码
```

### 场景二：快速生成 API
```
1. 描述需求："用 FastAPI 写一个用户注册接口，
   包含邮箱密码验证，密码 bcrypt 加密"
2. Cursor 生成完整代码
3. 用 Cmd+K 调整细节
```

### 场景三：理解陌生代码库
```
1. Clone 一个新项目
2. Chat → "@src/ 介绍一下这个项目的架构"
3. "@src/main.py 这里的中间件是干什么的？"
```

---

## 下一步

- [M3-03 其他主流工具](./03-other-tools.md)
- [M3-04 AI 编程工具底层原理](./04-how-it-works.md)
