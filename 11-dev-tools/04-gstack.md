# M11-04 · gstack：YC CEO 的 AI 软件工厂

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02
>
> 截至 2026-11：**约 140.5k ⭐**，最新版 **v1.96.0.0**（2026-11-05）。gstack 把 Claude Code（及其他编码 Agent）变成一支虚拟工程团队：CEO、工程经理、设计师、QA Lead、安全官、发布工程师全部到位。
>
> GitHub：[garrytan/gstack](https://github.com/garrytan/gstack) ｜ 作者：Garry Tan（Y Combinator 总裁兼 CEO）｜ MIT 开源

> "在过去 60 天里：60 万行生产代码（35% 是测试），每天 1 万-2 万行，兼职完成，同时全职运营 YC。"
> — Garry Tan（2026 年的说法，具体数字以作者原文为准）

---

## 解决什么问题？

AI 编程助手会写代码，但缺少：

- 产品层面的挑战与追问（"你描述的是功能，但真正的问题是什么？"）
- 设计 Review（识别"AI 垃圾风格"）
- 工程架构锁定（数据流图、状态机、边界条件）
- 真实浏览器 QA 测试
- 安全审计（OWASP Top 10 + STRIDE）
- 规范化 PR 发布流程

gstack 把这些全部封装成可复用的 Slash 命令。

---

## 2026-11 的 gstack 有什么新东西

| 变化 | 说明 |
|------|------|
| **工具数量增加** | 官方描述仍是「23 个有主见的工具」，但 README 已列出 30+ 命令（`/verify`、`/spec`、`/learn`、`/make-pdf`、`/diagram`、`/retro` 等） |
| **`/browse` 成为基础设施** | 所有浏览器类技能都建立在 `/browse` 上；优先驱动 [Aside](https://aside.com) 浏览器（真实登录态） |
| **稳定通道** | 新安装默认跟随 `stable` 通道（周一/周四发版，最多每 72 小时一次） |
| **依赖升级** | 需要 Bun v1.4.2+（低于 1.3.3 会被拒绝）、Git；Windows 需 Node.js |
| **GBrain** | 持久化知识库，让 Agent 跨会话记住项目模式与偏好 |
| **全链路打通** | `/spec` → `/autoplan` → 实现 → `/qa` → `/review` → `/ship` → `/land-and-deploy` → `/document-release` |

> `/cso` 需要本机原生工具链；没有工具链时 setup 会明确提示该技能不可用，但不阻塞安装。

---

## 一次完整 Sprint 示例

```
你说：   "我想做一个日历每日简报 App"
/office-hours  →  Agent 追问：具体痛点是什么？
Claude：  "你描述的不是简报 App，而是个人 AI 首席助理"
          [发现 5 个你没意识到的需求]
          [挑战 4 个假设]
          [生成 3 种实现方案 + 工作量估算]

/plan-ceo-review  →  挑战范围，找到最小有价值版本
/plan-eng-review  →  ASCII 数据流图、状态机、测试矩阵
（你确认方案）
（Claude 写 2400 行代码，~8 分钟）
/review           →  自动修复 2 个问题，1 个 Race Condition 等你确认
/qa https://staging.myapp.com  →  真实浏览器点击，发现并修复 1 个 Bug
/ship             →  测试 42→51（新增 9 个），开 PR
```

---

## 核心 Skills 速查（2026-11 摘要）

### Think（想清楚再动手）

| 命令 | 角色 | 作用 |
|------|------|------|
| `/office-hours` | YC Office Hours | 6 个追问重构你的产品，生成设计文档 |
| `/plan-ceo-review` | CEO/创始人 | 挑战范围，找到真正值得做的最小版本 |
| `/plan-eng-review` | 工程经理 | 锁定架构、数据流、边界条件、测试矩阵 |
| `/plan-design-review` | 高级设计师 | 每个设计维度 0-10 评分，识别 AI 垃圾风格 |
| `/design-consultation` | 设计伙伴 | 从零搭设计系统，输出 `DESIGN.md` |
| `/spec` | 规格作者 | 把模糊意图写成可执行 spec，带质量门禁 |
| `/autoplan` | 流水线 | 一键跑 CEO → 设计 → DX → 工程全链路 Review |

### Build（执行）

| 命令 | 角色 | 作用 |
|------|------|------|
| `/design-shotgun` | 设计探索 | 生成 4-6 个 AI 设计变体，浏览器对比选择 |
| `/design-html` | 设计工程师 | 把设计稿转成可发布的生产级 HTML/CSS |
| `/design-motion` | 动效设计 | 生成展示循环 / GIF / MP4（需 ffmpeg） |
| `/investigate` | 调试专家 | 系统化根因定位，3 次失败后停止报告 |
| `/verify` | 构建循环 | 跑仓库自己的 typecheck / lint / build / tests，修到绿 |

### Review & Test（检查）

| 命令 | 角色 | 作用 |
|------|------|------|
| `/review` | Staff Engineer | 找生产环境才暴露的 Bug，自动修复显而易见的问题 |
| `/qa <URL>` | QA Lead | 真实浏览器 / API / CLI / job / webhook 测试 |
| `/qa-only` | QA 报告员 | 只探索+报告，不改产品代码 |
| `/cso` | 首席安全官 | OWASP Top 10 + STRIDE，可选运行时扫描 |
| `/codex` | 第二意见 | 让 OpenAI Codex 独立 Review 同一份代码 |

### Ship（发布）

| 命令 | 角色 | 作用 |
|------|------|------|
| `/ship` | 发布工程师 | 同步 main、跑测试、审查覆盖率、推送、开 PR |
| `/land-and-deploy` | 发布工程师 | 合并 PR、等待 CI 和部署、验证生产健康状态 |
| `/document-release` | 技术写手 | 更新漂移的文档 |
| `/document-generate` | 文档作者 | 用 Diataxis 框架从零生成缺失文档 |

### 效率 & 安全

| 命令 | 作用 |
|------|------|
| `/browse` | 给 Agent「眼睛」：驱动 Aside / 内置 Chromium 真实浏览 |
| `/learn` | 管理跨会话记忆（项目模式、坑、偏好） |
| `/retro` | 团队周报 / 复盘（可跨项目、跨 AI 工具） |
| `/make-pdf` / `/diagram` | Markdown → 出版级 PDF；英文 → Mermaid/Excalidraw/SVG |
| `/careful` | 破坏性命令前警告（rm -rf、DROP TABLE、force-push 等） |
| `/freeze` / `/unfreeze` | 锁定/解锁编辑范围到指定目录 |
| `/guard` | `/careful` + `/freeze` 合体 |

> 命令清单随版本增长很快，以 [README](https://github.com/garrytan/gstack) 和 `docs/skills.md` 为准。

---

## 安装

### 30 秒安装（Claude Code）

在 Claude Code 中粘贴：

```
Install gstack: run git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup
```

安装后按提示在 `CLAUDE.md` 里加 gstack 段落（让 Agent 用 `/browse` 而不是内置 Chrome MCP）。

### Cursor

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack && ./setup --host cursor
```

### 其他平台

| 平台 | 命令 |
|------|------|
| Codex CLI | `./setup --host codex` |
| Codex App | 插件市场安装 |
| OpenCode | `./setup --host opencode` |
| Factory Droid | `./setup --host factory` |
| Kimi Code / Gemini / Copilot | 以 README 的平台表为准 |

### 团队模式（推荐）

```bash
# 每个成员全局安装后，为仓库初始化
cd ~/.claude/skills/gstack && ./setup --team
cd <你的仓库>
~/.claude/skills/gstack/bin/gstack-team-init required
git add .claude/ CLAUDE.md && git commit -m "require gstack for AI-assisted work"
```

团队成员启动 Claude Code 时自动更新 gstack，无需手动维护版本。新安装默认跟 `stable` 通道。

---

## 并行 Sprint（进阶用法）

gstack 与 Conductor 配合可同时运行 10-15 个并行 Sprint：

- 一个 Session 跑 `/office-hours` 探索新功能
- 一个跑 `/review` 检查 PR
- 一个实现具体功能
- 一个对 staging URL 跑 `/qa`
- 其余在其他分支推进

**每个 Session 都知道自己处于哪个阶段**，不会互相干扰。

---

## 与 Superpowers 的对比

| 维度 | gstack | Superpowers |
|------|--------|-------------|
| 侧重点 | 产品/工程/设计/发布全链路角色扮演 | 开发流程约束（TDD、子 Agent 协作） |
| 触发方式 | 手动调用 `/slash-command` | 自动检测任务类型并触发 |
| 设计能力 | 强（`/design-shotgun`、`/design-html`、`/design-motion`） | 无 |
| 浏览器 QA | 真实浏览器（Aside / 内置 Chromium） | 无内置 |
| 安全审计 | `/cso` OWASP+STRIDE | 无内置 |
| 适合场景 | 产品决策驱动、快速发布迭代 | 质量/测试覆盖/严格流程优先 |
| 星标（2026-11） | 约 140.5k | 约 313.6k |

---

## 参考

- [gstack GitHub](https://github.com/garrytan/gstack)
- [Skills 详细说明](https://github.com/garrytan/gstack/blob/main/docs/skills.md)
- [Builder Ethos](https://github.com/garrytan/gstack/blob/main/ETHOS.md)
- [上一篇：M11-03 Superpowers](./03-superpowers.md)
- [下一篇：M11-05 Claude Code 省 Token 指南（图文整理）](./05-claude-code-token-optimization.md)

---

## 历史沿革

- **2026-11**：约 140.5k ⭐，v1.96.0.0；新增 `/verify`、`/spec`、`/learn`、`/make-pdf`、`/diagram`、`/design-motion` 等；`/browse` 成为浏览器基础设施；安装要求 Bun v1.4.2+。
- **2026 年中**：引入 `stable` 更新通道与 GBrain 持久化知识库；平台支持扩到 Cursor / Codex / OpenCode / Factory Droid 等。
- **2026-04（旧版）**：当时约 65.9k ⭐，文档写「23 个专家角色」，命令以 `/office-hours`、`/review`、`/qa`、`/ship` 为主。
- **2026-03**：项目首次进入课程 M11。

---

*← 返回 [M11 开发提效工具](./README.md) | [课程总览](../README.md)*
