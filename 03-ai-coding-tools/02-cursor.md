# M3-02 · Cursor 使用指南

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02
>
> 当前版本：**Cursor 3**（2026-04-02 发布，以 Agent 为中心的新界面）。老版本 Cursor 2 / IDE 形态保留在文末「历史沿革」。

---

## 一句话结论

Cursor 不再是「加了 AI 的 VS Code」，而是**一个以 Agent 为中心的软件工作台**：本地 Agent、云端 Agent、Mobile、Slack、GitHub、Linear 触发的会话都在同一个侧边栏里；界面随时可以切回 IDE 看文件、跑 LSP。2026-06 起 Cursor 母公司 Anysphere 被 SpaceX 收购，默认模型家族转向 Grok，但第三方模型仍可接入。

- 下载地址：[cursor.com/download](https://cursor.com/download)
- 官方文档：[cursor.com/docs](https://cursor.com/docs)
- 新界面入口：`Cmd+Shift+P` → `Agents Window`（旧 IDE 界面仍可切回）

---

## Cursor 3 的五个关键变化

| 变化 | 说明 |
|------|------|
| **Agents Window** | 新界面以 Agent 会话为中心，所有本地/云端 Agent 统一出现在侧边栏 |
| **多仓库（multi-repo）** | 新界面天然支持跨仓库工作，不再局限单项目窗口 |
| **并行 Agent** | 可同时跑多个 Agent，包括从 Mobile / Web / Slack / GitHub / Linear 触发的会话 |
| **本地 ⇄ 云端交接** | 会话可在本地与云端之间迁移：本机调试、离线长任务都覆盖 |
| **Agent SDK + CLI** | Agent 可以「作为代码」定义、评测、部署（2026-10 起 GA） |

> 云端 Agent 会产出 demo 和截图供你验收；合并前仍建议人工 review（见 [M5-10 代码审查](../05-practical/10-code-review.md)）。

---

## 核心功能

### 1. Tab 补全（最常用）

```
你写代码时，Cursor 会灰色提示你"接下来可能写什么"
按 Tab 键接受建议，Esc 忽略
```

不只补全一行，而是能补全整个函数、整块逻辑。补全由 Cursor 自有小模型（`cursor-small` 一类）负责，速度快、成本低。

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

适合：快速重构、修改逻辑、格式转换。

---

### 3. Cmd+L · Chat 模式（对话）

按 `Cmd+L` 打开 Chat 面板：

- 问代码问题："这个 bug 是什么原因？"
- 让它生成代码："写一个 JWT 验证中间件"
- 解释代码："解释这段正则表达式"

**关键技巧：** 使用 `@` 引用文件/函数

```
@src/auth.py 这个文件的认证逻辑有什么问题？

@docs/api.md 根据这个 API 文档，帮我写请求函数
```

---

### 4. Agent / Agents Window（自动任务）

Cursor 最强大的模式。你描述需求，它自动：

- 读取相关文件
- 修改多个文件
- 运行命令和测试
- 修复出现的错误
- 需要时在云端继续跑

```
示例 Prompt：
"根据 models/user.py 中的用户模型，
 创建 CRUD API 接口，包含增删改查，
 并添加输入验证和错误处理"
```

Cursor 3 里 Agent 会话不再局限于当前窗口：本地会话可以「交给云端」继续跑，云端会话也可以「拉回本地」调试。

---

### 5. Cursor CLI（终端）

```bash
# 安装后即可在任意项目目录启动 Agent
agent
```

常用：

- 在终端里跑 Agent（适合远程服务器 / tmux）
- 接 GitHub Actions、脚本、自动化
- 通过 `--model` 选择模型（Grok 4.7 / Opus 5.5 / GPT-5.6 Sol / Fable 5.1 / Gemini 3.1 Pro / Composer 2.5 等，以 CLI `/model` 列表为准）

---

## 模型选择（2026-11）

Cursor 3 可切换多家族模型。**注意套餐限制**：Plus（$8）只能用 Grok 模型；Premium 及以上才能用第三方模型，且第三方模型按 API 价另计。

| 模型 | 适合场景 | 备注 |
|------|---------|------|
| **Grok 4.7**（默认家族之一） | 长程编码、Agent 任务 | 256k 标准上下文 / 500k 长上下文（[来源](https://cursor.com/grok)，2026-09-21） |
| **Composer 2.5** | 日常迭代、快速修改 | Cursor 自有模型，用量限制较宽松 |
| **Claude Opus 5.5 / Sonnet 5.5** | 复杂重构、代码审查 | 第三方模型，按 API 价 |
| **GPT-6 系列 / Fable 5.1 / Gemini 3.1 Pro** | 按任务选择 | 以客户端列表为准 |

**配置建议：**
- Tab 补全 → 默认小模型（速度优先，不占对话额度）
- Chat 对话 → Sonnet 5.5（质量/成本平衡）
- Agent 任务 → Grok 4.7 或 Opus 5.5（能力优先）
- 简单批量任务 → Haiku 5.5 / Composer

> 模型家族与可用性变化很快；`/model` 里没有的模型就是当前套餐不可用，**以客户端为准**。

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

### Cursor Rules（规则体系）

Cursor 现在支持四类规则（[官方文档](https://cursor.com/docs/rules)，2026-11）：

| 类型 | 位置 | 作用 |
|------|------|------|
| **Project Rules** | `.cursor/rules/*.mdc` | 随仓库版本控制，按路径/关键词/手动触发 |
| **User Rules** | 客户端设置 | 对当前用户全局生效 |
| **Team Rules** | 团队后台 | Team / Enterprise 计划可用，团队统一 |
| **AGENTS.md** | 仓库根目录 | 纯 Markdown 的轻量替代方案 |

```
.cursor/rules/project.mdc 示例：

---
description: Python FastAPI 后端规范
globs: ["**/*.py"]
alwaysApply: false
---

You are an expert in Python FastAPI.
- Always use async/await
- Follow PEP8 style
- Add docstrings to all functions
- Use Pydantic v2 for data validation
- Write tests for all new functions
```

> `.cursorrules` 是旧写法，已不推荐；`.md` 文件放在 `.cursor/rules/` 下不会被识别（缺 frontmatter），要写纯 Markdown 就用 `AGENTS.md`。详见 [M6-01 Cursor Rules 配置指南](../06-ai-project-setup/01-cursorrules.md)。

---

## 常用快捷键

| 快捷键 | 功能 |
|--------|------|
| `Tab` | 接受代码补全 |
| `Cmd+K` | 内联编辑 |
| `Cmd+L` | 打开 Chat |
| `Cmd+I` | 打开 Agent |
| `Cmd+Shift+L` | 把选中代码发送到 Chat |
| `Cmd+Shift+P` → `Agents Window` | 打开 Cursor 3 新界面 |
| `Esc` | 拒绝建议 / 暂停 Agent |

（Windows 把 Cmd 换成 Ctrl）

---

## 定价（2026-11 官网口径）

| 计划 | 价格 | 主要内容 |
|------|------|----------|
| **Free** | $0/月 | 有限的 Agent / Chat 请求 |
| **Plus** | $8/月 | 共享 AI 用量池；**仅 Grok 模型** |
| **Premium**（最热门） | $30/月 | 4× Plus 用量；Grok 最新模型；Cloud agents；第三方模型按 API 价另计 |
| **Super** | $100/月 | 15× Plus 用量；高峰期优先 |
| **Ultra** | $200/月 | 50× Plus 用量；最早获得新模型/产品 |
| **Teams** | $30+/人/月 | 团队管理、用量分析、隐私设置、SSO |
| **Enterprise** | 定制 | 更细的权限、审计、网络与 MCP 管控 |

> 价格不含税；第三方模型单独计费。来源：[cursor.com/pricing](https://cursor.com/pricing)（2026-11 核对），**以官网为准**。
>
> ⚠️ 2026 年价格档位相比 2025 年的 Pro $20 / Business $40 已经重构，旧文章里的价格不要直接引用。

---

## JetBrains 支持（2026）

- 2026-03-04 起，Cursor 通过 **ACP（Agent Client Protocol）** 进入 IntelliJ IDEA、PyCharm、WebStorm 等 JetBrains IDE。
- 安装方式：在 JetBrains 的 ACP Registry 里安装 Cursor ACP，用 Cursor 账号登录。
- 能力：Chat、代码解释、Agent 任务；付费计划用户免费使用。
- 注意：**不是完整 Cursor 客户端**，Tab 补全等 IDE 原生能力仍以 JetBrains 自己的 AI 功能为准。

来源：[Cursor 官方博客](https://cursor.com/blog/jetbrains-acp)，2026-03-04。

---

## 实战场景示例

### 场景一：Debug
```
1. 代码报错 → 复制错误信息
2. Cmd+L → 粘贴错误 → "这是什么错误，怎么修复？"
3. 让 Agent 修改并跑测试验证
```

### 场景二：快速生成 API
```
1. 描述需求："用 FastAPI 写一个用户注册接口，
   包含邮箱密码验证，密码 bcrypt 加密"
2. Agent 生成代码并运行测试
3. 用 Cmd+K 调整细节
```

### 场景三：理解陌生代码库
```
1. Clone 一个新项目
2. Chat → "@src/ 介绍一下这个项目的架构"
3. 需要跨仓库时，在 Agents Window 里开多仓库会话
```

### 场景四：本地写一半，交给云端继续
```
1. 本地 Agents Window 里启动任务
2. 点击 "move to cloud"，关掉电脑
3. 回来在侧边栏看云端 Agent 的 diff / 截图并验收
```

---

## 历史沿革

- **2026-11**：价格档位为 Free / Plus $8 / Premium $30 / Super $100 / Ultra $200；Teams $30+/人；Grok 4.7 为默认模型家族之一。
- **2026-10-20**：Cursor Agent SDK 正式可用（Agent as code、evals、部署）。
- **2026-09-21**：Grok 4.7 发布（与 SpaceXAI 联合训练，256k / 500k 上下文）。
- **2026-06-16**：SpaceX 宣布以 $60B 收购 Anysphere（Cursor 母公司），预计 Q3 完成；Cursor 年化 B2B 收入约 $2.6B（媒体报道）。
- **2026-04-02**：**Cursor 3** 发布，以 Agent 为中心的新界面、多仓库、并行 Agent、本地⇄云端交接。
- **2026-03-19**：Composer 2 发布（Cursor 自有前沿编码模型）。
- **2026-03-04**：Cursor 通过 ACP 支持 JetBrains IDE。
- **2026-02-24**：Cursor Agent 可控制自己的电脑（computer use）。
- **2025**：Cursor 2 / Composer 工作流，Agent 成为核心交互；Pro $20、Business $40。
- **2024**：Composer 与多文件 Agent 起步，Cursor 从「VS Code 分支」变成独立品类。
- **2023**：Cursor 发布，早期以 Tab 补全和 Chat 为主。

---

## 下一步

- [M3-03 其他主流工具](./03-other-tools.md)
- [M3-04 AI 编程工具底层原理](./04-how-it-works.md)
