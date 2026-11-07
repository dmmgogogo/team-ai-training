# ⭐️ M7-02 · Claude 项目工作区：Projects → Skills / Plugins（2026）

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> Claude Projects 仍然有用，但它的定位在 2026 年已经明确：**Projects 管"背景知识"，Skills 管"怎么做"，Plugins 管"打包分发"**。把这三者混用，是很多团队配置低效的根源。

---

## 一句话结论

| 需求 | 用什么 | 加载方式 |
|------|--------|----------|
| 这个项目的背景资料、API 文档、错误码 | **Project**（项目知识） | 该项目内常驻 |
| 一套多步骤工作流（审查、发版、周报） | **Skill** | 按需加载 |
| 把 skills + connectors + commands 一次装好 | **Plugin** | 安装后常驻 |
| 连接外部服务（Slack、Drive、数据库） | **Connector / MCP** | 工具调用时 |
| 让 Claude 主动在你电脑上干活 | **Claude Cowork**（已并入 Claude） | 任务执行 |

来源：[Claude Skills 概览](https://claude.com/docs/skills/overview)、[Skills explained](https://claude.com/resources/articles/skills-explained)（2026-03/2026-11）。

---

## 一、Claude 的能力分层（2026-11）

```
Plugins（打包分发）
├── Skills（流程说明）
├── Connectors / MCP（外部连接）
├── Commands（快捷命令）
└── Agents（子 agent）
Projects（项目背景知识，某个项目内常驻）
```

官方对比表（[Skills overview](https://claude.com/docs/skills/overview)）：

| 功能 | 用途 |
|------|------|
| **Skills** | 任务相关的流程，命中时加载 |
| **Plugins** | 把多个 skills + connectors + commands + agents 打成一件安装 |
| **Projects** | 某个项目聊天里**始终加载**的背景知识 |
| **MCP connectors** | 连接外部服务与数据 |

> 记忆：**Projects 是"资料室"，Skills 是"操作手册"，Plugins 是"工具箱"。**

---

## 二、Projects 仍然值得建，但要建对

### Projects vs 普通对话

| 对比 | 普通对话 | Claude Project |
|------|---------|----------------|
| 上下文 | 每次独立 | 项目背景长期保留 |
| 文档 | 每次上传 | 一次上传，项目内可用 |
| 指令 | 每次说明 | 项目指令长期有效 |
| 适合 | 一次性任务 | 长期项目、固定资料 |

### 开发者建议建的 Projects

#### 1. 主力项目 Project（每个项目一个）

```text
你是这个项目的 AI 开发助手。

技术栈：Go 后端 + Flutter App + Vue3 管理后台
当前正在开发：[功能/模块]

工作规范：
- 后端分层：controller → service → handler → model，禁止跨层
- 统一返回：{"code": 200, "msg": "...", "data": {}}
- 不确定的地方先问，不要猜

每次回答直接给代码，不需要解释基础概念。
```

上传文档：

- 项目 README / 架构说明
- 数据库表结构
- API 接口文档
- 错误码列表

> 2026 年更推荐：这些资料如果已经写进仓库的 `AGENTS.md` / `docs/`，可以直接把仓库接到 Claude Code；Projects 适合"非仓库资料"或"网页端协作"。

#### 2. Code Review Project

```text
你是专业的代码审查专家，重点关注：
1. 安全漏洞（注入、越权、密钥泄露）
2. 性能问题（N+1、无界循环、内存）
3. 错误处理（是否所有错误都被处理）
4. 代码规范（命名、注释、结构）

每次 review 输出：
- 🔴 必须修复
- 🟡 建议优化
- 🟢 值得学习
```

> 如果这是团队的固定流程，把它升级成 **Skill**（可版本控制、可跨项目复用），而不是只放在 Project 指令里。

#### 3. 技术调研 Project

```text
你是技术调研助手。

我们的约束：
- 后端 Go，不引入 Java 生态
- 前端 Vue3 / Flutter，不用 React
- 部署 Docker + Kubernetes
- 数据库 MySQL + Redis

每次给方案：
1. 优劣势对比
2. 是否符合约束
3. 推荐方案 + 理由
4. 潜在风险
```

#### 4. 文档写作 Project

```text
你是技术文档写作助手。
风格：简洁、有代码示例、中文、结构清晰。
上传的模板：公司文档模板.md
每次写作参考该模板格式。
```

---

## 三、Skills：把"流程"从 Projects 里拿出来

Project 指令适合"长期背景"，不适合"多步骤流程"。流程应该写成 Skill：

```
.claude/skills/code-review/SKILL.md
.claude/skills/release-check/SKILL.md
.claude/skills/weekly-report/SKILL.md
```

好处：

1. **按需加载**，不占常驻上下文；
2. **可版本控制**，走 PR review；
3. **跨项目复用**；
4. **可带脚本**，确定性步骤交给脚本。

写法详见 [M5-04b](../05-practical/04-skills.md)。

---

## 四、Plugins：团队分发的正确姿势

当你有多个 skill、多个 connector、多个命令要一起发给团队时，用插件：

```
team-plugin/
├── .claude-plugin/plugin.json
├── skills/
│   ├── code-review/SKILL.md
│   └── release-check/SKILL.md
├── commands/
└── .mcp.json
```

- Claude Code：`/plugin` 安装，支持官方市场与自建团队市场；
- claude.ai / Cowork：Customize → Plugins；
- 分发渠道：[Claude Marketplace](https://claude.com/marketplace)（2026-09-23 上线，2000+ connectors/plugins）。

> 注意：插件启用后，其 skill/agent 的名称与描述每轮都在上下文里，有持续成本；安装前先看 Context cost。

---

## 五、2026 年的产品变化：Cowork 与 Duet

| 产品 | 定位 | 对你的影响 |
|------|------|-----------|
| **Claude Cowork** | 在文件与工具上执行任务的 agent | 已并入 Claude 主产品；适合"给个目标，它交付结果" |
| **Claude Duet** | 主动型 agent（research preview） | 由 Opus 5.5 驱动；每天主动汇报、起草下一步，关键动作等你确认；Pro/Max/Ultra，美国先行 |

**含义**：如果你只是要"让 Claude 懂我的项目"，Projects + Skills 就够；如果要"让 Claude 主动干活、交付文件"，那是 Cowork/Duet 的领域。

---

## 六、高效使用技巧

### 上传什么文档效果最好

| 文档类型 | 效果 | 建议 |
|---------|------|------|
| 数据库表结构 | ⭐⭐⭐⭐⭐ | 必传，写 SQL 更准 |
| API 文档 | ⭐⭐⭐⭐⭐ | 必传 |
| 错误码表 | ⭐⭐⭐⭐ | 避免乱用错误码 |
| 代码规范 | ⭐⭐⭐⭐ | 输出风格一致 |
| 业务流程图 | ⭐⭐⭐ | 帮助理解业务 |

### 提问方式

```text
❌ 低效：帮我写一个用户登录接口
✅ 高效：在用户模块新增登录接口，
        支持手机号+密码，失败 5 次锁定 1 小时，
        参考现有 BaseController 写法
```

### 什么时候不该用 Projects

- 资料需要频繁更新（放仓库/AGENTS.md 更好）；
- 多步骤流程（用 Skill）；
- 需要执行代码或操作文件（用 Claude Code / Cowork）。

---

## 七、历史沿革

| 时间 | 事件 |
|------|------|
| 2024 | Claude Projects 上线：把"项目背景 + 文档"固化到工作区 |
| 2025 | Projects 成为网页端协作的常见做法；与 GPTs 形成对照 |
| 2025-10 | Claude Skills 发布，流程类内容有了更合适的载体 |
| 2026-03 | Anthropic 明确 Projects / Skills / MCP / Subagents 的分工 |
| 2026-09 | Claude Marketplace 上线，插件成为分发单位 |
| 2026-10–11 | Cowork 并入 Claude；Duet 进入研究预览 |

---

## 八、下一步

- [⭐️ M7-03 Cursor 规则与技能社区精选](./03-cursor-rules.md)
- [⭐️ M5-04b Skills：技能扩展](../05-practical/04-skills.md)
- [M8 MCP 精选大全](../08-mcp/)
