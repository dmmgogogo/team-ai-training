# ⭐️ M5-04b · Skills：技能扩展（重要）

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 2025–2026 年最大的变化：Skills 从"各平台自定义助手"收敛成了**以 `SKILL.md` 为载体的开放标准**，再通过**插件市场**分发。学会写一个 Skill，等于把你的工作方法变成可复用、可版本控制、跨工具迁移的资产。

---

## 一句话结论

- **Tools/MCP 解决"能做什么"**，**Skills 解决"按什么步骤做"**。
- 一个好 Skill = **一句能被匹配的 description** + **可执行的步骤** + **按需加载的脚本/模板**。
- 2026-11 的生态已经统一到 **Agent Skills 开放标准**（`SKILL.md`），Claude、Cursor、Codex 等都能读。

---

## 一、Skills 到底是什么

Skill 就是一个目录，核心是一个 `SKILL.md`：

```
my-skill/
├── SKILL.md          # 必需：frontmatter（元信息）+ 正文（步骤说明）
├── scripts/          # 可选：可执行脚本
├── references/       # 可选：参考资料
└── assets/           # 可选：模板、素材
```

`SKILL.md` 的最小写法：

```markdown
---
name: code-review
description: 按安全、性能、可维护性三个维度审查代码。当用户要求 review、检查代码质量或提交 PR 前使用。
---

# 代码审查

1. 先读 diff，列出本次变更涉及的文件与意图。
2. 按「安全 → 性能 → 可维护性」顺序检查，每条给出文件:行号。
3. 输出格式：🔴 必须修复 / 🟡 建议优化 / 🟢 值得学习。
4. 不要直接改代码，除非用户明确要求。
```

### 渐进式加载（progressive disclosure）

这是 Skills 最重要的设计，也是它比"把所有规则塞进系统提示"更省 token 的原因：

| 阶段 | 加载什么 | 大约成本 |
|------|----------|----------|
| ① 平时 | 只有每个 skill 的 name + description | 约 100 tokens / 个 |
| ② 命中 | 加载 `SKILL.md` 正文 | 通常 < 5k tokens |
| ③ 需要时 | 打开 scripts / references / assets | 按需 |

来源：[Claude Skills 文档](https://claude.com/docs/skills/overview)、[Agent Skills 规范](https://agentskills.io/specification)、[Skills explained](https://claude.com/resources/articles/skills-explained)（2026-03/2026-11）。

### Skills 和相邻概念的分工

| 概念 | 解决什么 | 加载方式 |
|------|----------|----------|
| **Prompt** | 这一次对话怎么说 | 一次性 |
| **Project 指令** | 这个项目长期背景 | 该项目内常驻 |
| **Rules / CLAUDE.md / AGENTS.md** | 项目规范、构建命令、约定 | 每次会话常驻 |
| **Skills** | 可复用的多步骤流程 | 按需加载 |
| **MCP / Connectors** | 连接外部工具与数据 | 工具调用时 |
| **Subagents** | 隔离上下文执行子任务 | 被委派时 |
| **Plugins** | 把上面这些打包成一件安装 | 安装后常驻 |

> 判断口诀：**"事实"进 AGENTS.md/CLAUDE.md，"流程"进 Skills，"连接"用 MCP，"分发"用 Plugin。**

---

## 二、2025–2026 的演进：从各自为政到开放标准

| 时间 | 平台动作 | 形态 |
|------|----------|------|
| 2023 | OpenAI ChatGPT Plugins → GPTs | 平台内自定义助手，绑定在 ChatGPT |
| 2024–2025 | Claude Projects、Cursor Rules 流行 | 项目上下文 + 规则文件，各平台格式不同 |
| 2025-10 | Anthropic 推出 Claude Skills | 以 `SKILL.md` 为核心，按需加载 |
| 2026-03 | Anthropic 发布 Skills 与 Prompts / Projects / MCP / Subagents 的对比指南 | Skills 定位清晰化 |
| 2026 年 | Agent Skills 成为开放标准；Cursor、Codex 等跟进 | `.agents/skills/`、`.claude/skills/` 互通 |
| 2026-09-23 | Claude Marketplace 上线 | 2000+ connectors 与 plugins，插件成为分发单位 |
| 2026-10/11 | OpenAI 宣布退役自定义 GPT，转向 **Plugins + Skills** | 跨平台收敛到"skills + apps/plugins"模型 |

### 各平台对应机制（2026-11 快照）

| 平台 | Skill 存放位置 | 入口 | 备注 |
|------|----------------|------|------|
| **claude.ai / Claude 桌面** | 账户级（Customize → Skills） | Customize → Skills → Discover | Pro/Max/Ultra/Team/Enterprise 可用；插件可携带 skill |
| **Claude Code** | `.claude/skills/<name>/SKILL.md`、`~/.claude/skills/`、插件内 `skills/` | `/skill-name` 或自动触发 | 支持 `context: fork`、`allowed-tools`、动态注入命令 |
| **Cursor** | `.agents/skills/`、`.cursor/skills/`、`~/.agents/skills/`、`~/.cursor/skills/` | `/` 菜单或自动触发 | 同时兼容 `.claude/skills/` 与 `.codex/skills/` |
| **ChatGPT / Codex** | Plugins 目录 → Skills 标签页 | 侧边栏 Plugins | Business/Enterprise/Healthcare/Edu；上传会先扫描 |
| **OpenCLI 等工具** | 通过 `npx skills add <repo>` 安装 | agent 自动发现 | 说明"skills 作为分发格式"已被第三方采用 |

来源：[Claude Skills 概览](https://claude.com/docs/skills/overview)、[Claude Code Skills](https://code.claude.com/docs/en/skills)、[Cursor Agent Skills](https://cursor.com/docs/skills)、[OpenAI Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)（均访问于 2026-11）。

---

## 三、怎么写一个好 Skill（重点）

### 原则一：description 决定"会不会被用"

模型只看得到 name + description 来决定是否加载。description 要写**做什么 + 什么时候用**：

```yaml
# ❌ 太模糊，永远匹配不上
description: 帮助处理代码

# ✅ 场景 + 触发词
description: 审查 Git diff 中的代码变更，检查安全漏洞、性能问题与可维护性。当用户要求 review、检查代码、或在提交 PR 前使用。
```

### 原则二：正文写"步骤"，不写"百科"

Skill 正文是给模型执行的操作手册，不是知识库：

```markdown
## 步骤
1. 运行 `git diff --stat` 了解范围
2. 对每个改动文件，检查：输入校验、错误处理、SQL 是否参数化
3. 输出表格：文件 | 问题级别 | 问题 | 建议
```

背景知识放 `references/`，让模型需要时再读。

### 原则三：控制体积

- 正文尽量 **< 5k tokens**；
- 大段参考资料放 `references/`；
- 能写成脚本的确定性步骤就写成脚本（放 `scripts/`），比让模型"照着做"更稳、更省。

### 原则四：给边界和失败处理

```markdown
## 边界
- 只读分析，不直接修改生产代码
- 涉及密钥、支付、权限的改动，必须标注「需人工确认」
- 信息不足时先提问，不要猜
```

### 原则五：可验证

好 Skill 的标准不是"写得漂亮"，而是**在真实任务上稳定复现**。建议准备 3–5 个真实 prompt，对比"开 skill / 关 skill"的输出差异。（Claude Code 提供 `/skill-doctor` 查看 skill 的使用与上下文成本，插件可用 `claude plugin eval` 做基线对比。）

### 一个完整示例：`code-review` Skill

```
.claude/skills/code-review/
├── SKILL.md
├── references/
│   └── checklist.md
└── scripts/
    └── collect-diff.sh
```

```markdown
---
name: code-review
description: 审查 Git diff 中的代码变更，检查安全漏洞、性能问题与可维护性。当用户要求 review、检查代码、或在提交 PR 前使用。
---

# 代码审查

## 准备
运行 `scripts/collect-diff.sh` 获取本次变更（或让用户提供 diff）。

## 检查顺序
1. **安全**：注入、越权、密钥泄露、反序列化
2. **正确性**：边界条件、错误处理、并发
3. **性能**：N+1、无界循环、内存
4. **可维护性**：命名、重复、测试覆盖

## 输出
| 文件:行 | 级别 | 问题 | 建议 |
|---|---|---|---|

最后给出一句话结论：可以合并 / 修改后合并 / 需要重做。

## 边界
- 不直接改代码
- 不确定的结论标注「需人工确认」
- 详细检查项见 `references/checklist.md`
```

---

## 四、Skill 与 MCP 的分工

这是团队最常问的问题。答案是：**它们不是替代关系，而是不同层**。

```
用户任务
   ↓
Skills：规定"怎么做"（步骤、检查项、输出格式）
   ↓
MCP / Tools：提供"能操作什么"（读文件、查库、调 API）
   ↓
模型：推理、决策、生成
```

| 对比项 | Skill | MCP |
|--------|-------|-----|
| 本质 | 说明书 / 流程 | 协议 / 连接 |
| 内容 | Markdown + 脚本 + 模板 | Server 暴露的 tools / resources / prompts |
| 是否需要服务 | 不需要（纯文件） | 需要运行 Server |
| 适合 | 团队流程、审查清单、文档模板 | 接数据库、GitHub、浏览器、SaaS |
| 分发 | Git 仓库、插件、skills 目录 | npm/容器/远程 URL、MCP 目录 |

**组合示例**：一个"发版检查"Skill 规定检查步骤，其中"查 CI 状态"通过 GitHub MCP 实现，"查线上错误率"通过监控 MCP 实现。

---

## 五、插件与市场：2026 年的分发方式

单个 Skill 可以放在仓库里共享；要跨团队、跨项目分发，就用**插件**。

| 生态 | 打包单位 | 市场/入口 | 说明 |
|------|----------|-----------|------|
| Claude | Plugin（skills + agents + hooks + MCP + commands） | [Claude Marketplace](https://claude.com/marketplace) / Claude Code `/plugin` | 2026-09-23 上线，2000+ connectors/plugins |
| Claude Code | `.claude-plugin/plugin.json` + marketplace 目录 | `/plugin marketplace add` | 官方市场默认添加；可自建团队市场 |
| Cursor | Plugin / Skill / Rule | Cursor Marketplace | 团队可发布 skill 到团队市场 |
| OpenAI | Plugin（skills + apps） | [ChatGPT 插件目录](https://chatgpt.com/plugins) | 取代自定义 GPT 的主要载体 |

**Claude Code 插件目录结构**：

```
my-plugin/
├── .claude-plugin/plugin.json   # 清单：名称、版本、描述
├── skills/review/SKILL.md       # 技能
├── agents/reviewer.md           # 子 agent
├── hooks/hooks.json             # 生命周期钩子
└── .mcp.json                    # 随插件启用的 MCP
```

> 插件启用后，其 skill/agent 的名称与描述**每轮都在上下文里**，会产生持续成本；安装前先看 Context cost 估算。

---

## 六、团队实践：Skills 仓库怎么管

```
team-ai-skills/
├── README.md                 # 索引：每个 skill 干什么、谁维护
├── skills/
│   ├── code-review/
│   ├── api-doc-gen/
│   ├── incident-analysis/
│   └── release-checklist/
├── rules/                    # 与 skills 配套的项目规则模板
└── mcp/                      # 团队统一 MCP 配置片段
```

管理建议：

1. **一个 skill 一个目录，一个 owner**，README 里登记用途与触发词。
2. **进 Git，走 PR**：skill 里的脚本等于代码，需要 review。
3. **锁定来源**：只从可信市场安装插件；第三方 skill 先读 `SKILL.md` 和 `scripts/`。
4. **定期清理**：长期不用的 skill 会持续占用上下文，按季度清理（Claude Code `/skill-doctor` 可辅助判断）。
5. **别把秘密写进 skill**：skill 会被提交、分享、上传。

---

## 七、历史沿革

| 时间 | 事件 |
|------|------|
| 2023 | ChatGPT Plugins / GPTs 出现，平台内"自定义助手"成为主流 |
| 2024–2025 | Claude Projects、Cursor Rules 各自发展，格式互不兼容 |
| 2025-10 | Anthropic 推出 Claude Skills（`SKILL.md` + 渐进式加载） |
| 2026-03 | Anthropic 明确 Skills 与 Prompts / Projects / MCP / Subagents 的分工 |
| 2026 年 | Agent Skills 成为开放标准，Cursor / Codex 等开始兼容 |
| 2026-09 | Claude Marketplace 上线，插件成为分发单位 |
| 2026-10–11 | OpenAI 退役自定义 GPT，转向 Plugins + Skills，生态进一步收敛 |

> 旧写法（GPTs、`.cursorrules`、Projects 当技能用）逐渐降级为"历史/过渡方案"，但理解它们有助于看懂今天的标准从哪来。

---

## 八、参考

- [Claude Skills 概览](https://claude.com/docs/skills/overview)
- [Claude Code：Skills](https://code.claude.com/docs/en/skills)
- [Agent Skills 规范](https://agentskills.io/specification)
- [Skills explained（Anthropic）](https://claude.com/resources/articles/skills-explained)
- [Cursor：Agent Skills](https://cursor.com/docs/skills)
- [OpenAI：Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [Claude Marketplace 发布说明](https://claude.com/resources/articles/claude-marketplace)
- [Anthropic 官方 Skills 仓库](https://github.com/anthropics/skills)

---

## 下一步

- [⭐️ M5-05 Multi-Agent 多智能体实战](./05-multi-agent.md)
- [⭐️ M5-01 Prompt 工程入门](./01-prompt-engineering.md)
- [M6-01 AI 项目配置：AGENTS.md / CLAUDE.md / .cursor/rules](../06-ai-project-setup/01-cursorrules.md)
