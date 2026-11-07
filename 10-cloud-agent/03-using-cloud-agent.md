# M10-03 · 如何使用 Cloud Agent（实战）

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 2026-11 的上手入口比 2026 年初多得多。本篇按"你想干什么"给路径，再给通用的任务描述模板与避坑清单。

---

## 一句话结论

**先选执行位置，再选产品**：

- 代码可以上云、要长任务/并行 → **Claude Code cloud / Codex Cloud / Copilot in the cloud**
- 代码不能出本机、只要远程操控 → **Claude Code Remote Control**
- 知识工作（报告/表格/调研） → **Claude Cowork**
- 个人事务主动代理 → **Claude Duet**（研究预览）
- GitHub 重度用户、Issue→PR → **Copilot in the cloud**
- Gemini 生态、远程后台任务 → **Antigravity**

---

## 路径一：Claude Code cloud sessions（编码首选）

### 从浏览器/手机开始

1. 打开 [claude.ai/code](https://claude.ai/code)，用 Pro/Max/Ultra/Team（或 Enterprise 相应席位）账号登录；
2. 首次使用按引导连接 GitHub（Claude GitHub App 或 `/web-setup`）；
3. 选一个 Cloud environment（首次会创建 Default 环境）；
4. 描述任务 → 发送；
5. 在 **Changes** 卡片看 diff，满意后创建 PR。

手机端：Claude App → **Code** 标签 → 选会话。

### 从终端开始

```bash
# 新建云会话（在当前仓库）
claude --cloud "修复 src/auth/login.ts 的鉴权 bug"

# 并行起多个任务
claude --cloud "修掉 auth.spec.ts 的 flaky 测试"
claude --cloud "更新 API 文档"

# 把云会话拉回本地继续
claude --teleport <session-id>
```

注意：

- `--cloud` 从 GitHub 克隆的是**已推送的分支**，本地未推送的 commit 不在云会话里；没 remote 时会打包上传（有大小/文件限制）。
- `--teleport` 需要干净工作区、同一仓库、同一账号。
- `--remote` 是 `--cloud` 的旧别名（已弃用）。

### Auto-fix PR

安装 Claude GitHub App 后，可以让 Claude **盯着 PR**：CI 失败或 reviewer 评论时自动修。适合"开完 PR 就下班"的场景，但要注意：

- 回复会以**你的 GitHub 账号**发出（标注来自 Claude Code）；
- 仓库若有 comment 触发的部署自动化（如 Atlantis），先确认不会被误触发。

来源：[Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web)、[Remote Control](https://code.claude.com/docs/en/remote-control)、[Run agents in parallel](https://code.claude.com/docs/en/agents)。

---

## 路径二：Claude Code Remote Control（代码不出本机）

```bash
# 在项目目录启动服务模式
claude remote-control

# 或让当前交互会话可被远程接管
claude --remote-control
# 会话内也可以 /remote-control
```

- 执行仍在你的机器上：文件、MCP、项目配置都能用；
- 手机/浏览器只是"窗口"；
- 适合：机器常开、但人不在电脑前；合规要求代码不出本机。

限制：需要 claude.ai 订阅登录（API Key 不支持）；Bedrock/Vertex/Foundry 或自定义 `ANTHROPIC_BASE_URL` 不可用；Team/Enterprise 需管理员开启。

---

## 路径三：Claude Cowork（知识工作）

- **桌面端**：Claude Desktop 里直接用；本地隔离 VM，能读写文件、用连接器；
- **Web/移动端**：2026-07 起支持远程会话（beta），关掉笔记本也能继续；
- **定时任务**：2026-02 起支持周期性/按需任务；
- **Computer use**：可让 Claude 操作你的电脑（研究预览，需授权）。

适合：

```
你：把这三份周报合并成一份季度总结，输出 PPT 大纲
你：整理这个文件夹里的发票，生成报销清单
你：每天早上汇总我的邮件与日程
```

注意：Cowork 的"远程会话"仍是 beta；涉及本地文件的自动化，先确认机器是否在线、权限是否给对。

---

## 路径四：Claude Duet（主动型个人 Agent，研究预览）

- 2026-10-21 起面向美国 Pro/Max/Ultra 用户候补开放；
- 运行在"它自己的云端电脑"；
- 会主动发晨间简报、跟进任务、起草回复；
- **发消息 / 付款 / 签文件 / 删除前必须经你批准**；
- 预览期含在套餐内，但后台工作也消耗你的用量额度。

限制（官方列出）：不能选模型（跑 Opus 5.5）、不能旁观/接管它的浏览器、按固定间隔检查账号、不能打电话/发短信、部分连接器功能受限、Microsoft 365 暂不可用。

> 结论：适合早期尝鲜与个人事务，不建议现在就把关键流程托付给它。

---

## 路径五：OpenAI Codex Cloud

1. 打开 ChatGPT（Web / 移动 / 桌面），选择 **Work in → Cloud**；
2. 选已有环境，或新建环境：选 GitHub 仓库 → 让 Codex 检查依赖并试跑 → 发布环境；
3. 描述任务 → 发送；
4. 在结果里 review、追加修改、提交或开 PR。

适合：已有 ChatGPT 套餐、希望"任务跑在云上、PR 回到 GitHub"的团队。计费随套餐，另有 Codex-only 按量席位（以官网为准）。

来源：[Codex Cloud 文档](https://learn.chatgpt.com/docs/cloud)、[Codex 团队按量计费公告](https://openai.com/index/codex-flexible-pricing-for-teams/)。

---

## 路径六：GitHub Copilot in the cloud

- 入口：[github.com/copilot](https://github.com/copilot)、仓库的 **Agents** 标签、Issue/PR 面板、GitHub Mobile、IDE、Copilot CLI；
- 环境三选一：**Cloud sandbox（默认）** / **GitHub Actions** / **Remote 自定义环境**；
- 会话可跨端继续（cloud sandbox），Actions 会话只在网页；
- 写权限决定可写/只读；Actions 会话单次最长 **59 分钟**；
- **Agent Merge**：让 Copilot 盯着 PR，修 CI 失败与合并冲突。

适合：Issue 驱动开发、希望"分配 Issue 就等 PR"的 GitHub 团队。

来源：[Copilot on GitHub.com and Mobile](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github)。

---

## 路径七：Google Antigravity / Devin

**Antigravity**：Google 的 agent-first 平台（App / CLI / IDE / SDK）。Google 已宣布 Jules 关停，把"远程后台任务 + agent-first 开发环境"统一到 Antigravity（2026-10-29 报道）。适合 Gemini 生态用户；具体能力与价格以官网为准。

**Devin**：2026 年从"企业专属"转向个人订阅：Free / Pro $20 / Max $200；Team $80/月 + $40/席位；模型为 SWE-2，支持 Devin Cloud、Desktop、API、Slack/Teams/Linear/Jira 集成。适合需要"商业 AI 工程师"做复杂任务的团队。

---

## 写一个好任务描述（最关键）

**Cloud Agent 的效果，70% 取决于任务描述质量。**

### ❌ 差的描述

```
帮我优化代码
修一下登录的 bug
重构一下项目
```

### ✅ 好模板

```
## 任务背景
[当前状况，为什么要做]

## 具体要求
[精确描述做什么，含边界条件]

## 不要改动
[哪些文件/行为不能碰]

## 完成标准
[测试通过 / 特定输出 / 代码规范 / 开 PR]
```

### 实际例子

```
## 任务背景
Express 项目里错误处理散落在各路由，风格不一致：
有的 console.error，有的直接 res.status(500)。

## 具体要求
统一 src/routes/ 下所有路由的错误处理：
- try/catch 的 catch 块改为调用 handleError(err, res)
- handleError 已在 src/utils/errorHandler.js 定义
- 只改 src/routes/ 下的 .js 文件

## 不要改动
- 不修改 handleError 本身
- 不改变任何 HTTP 状态码
- 不动路由逻辑，只改错误处理

## 完成标准
- 路由文件中不再有直接的 console.error / res.status(500)
- npm test 全部通过
- 创建 PR，附修改文件列表
```

---

## 任务类型与技巧

| 类型 | 适合度 | 技巧 |
|------|--------|------|
| **代码迁移/升级** | ⭐⭐⭐⭐⭐ | 先让 Agent 输出迁移计划；指定测试要求；分批做 |
| **批量修复** | ⭐⭐⭐⭐⭐ | 给出"什么叫有问题"的判断标准；要求先列清单 |
| **生成测试** | ⭐⭐⭐⭐ | 指定框架；覆盖正常/边界/错误；要求 mock 外部依赖 |
| **代码审查** | ⭐⭐⭐ | 先只要报告，不要直接改；你决定改哪些 |
| **知识工作**（Cowork） | ⭐⭐⭐⭐ | 给模板与验收标准；长文档让它分节产出 |

---

## 常见坑

| 坑 | 表现 | 对策 |
|----|------|------|
| 任务太大 | 改了一半、结果失控 | 限定目录/模块，一次一个目标 |
| 没说不许动什么 | "顺手优化"了无关代码 | 明确"不要改动"清单 |
| 测试通过 ≠ 功能正确 | Agent 改了测试或跳过用例 | review 测试文件；CI 在干净环境重跑 |
| 敏感信息泄露 | 代码/密钥进入云端 | 不硬编码密钥；确认公司政策；敏感仓库用 Remote Control |
| 网络/凭据没配 | 依赖装不上、API 调不通 | 先把环境跑通再派任务；用网络密钥而非明文 |
| 组织策略拦截 | IP allowlist / 云会话被禁用 | 提前和 IT 确认；必要时走自托管环境 |
| 成本失控 | 并行任务烧额度 | 设预算；小任务先小模型；限制并发 |

---

## Review PR 的正确姿势

```
1. 看 diff 统计：文件数、增删量是否合理
2. 重点看逻辑改动，不只看格式
3. 检查测试文件是否被修改/弱化
4. 在干净环境重跑 CI
5. 小批量合并，一次 review 一个模块
6. 涉及权限/鉴权/支付/数据迁移的改动，人工二次确认
```

---

## 小结

```
清晰的任务描述
+ 明确的边界（不要碰什么）
+ 具体的完成标准
+ 认真的 PR review
= 省时省力的高质量交付
```

---

## 历史沿革

- **2026-11**：入口多元：Claude Code cloud / Remote Control、Cowork、Duet、Codex Cloud、Copilot in the cloud、Antigravity、Devin。
- **~~已过时~~ 2026-03 版实战主线：Cursor Background Agent**
  - 当时的入口是 `Cmd+Shift+P → Background Agent` 或在 Chat 面板切 Background 模式；
  - 流程是"云端起环境（约 30 秒）→ 关掉 Cursor 去忙 → 完成后看结果"；
  - 工具对比里 Devin 写作"$500/月起"，Copilot Workspace 作为 Issue→PR 工具；
  - 这些描述已被 Cursor Cloud Agents、Copilot in the cloud 与 Devin 新定价取代，仅作历史对照。

---

## 下一步

- [M10-04 自建 Cloud Agent 工作流](./04-build-your-own.md) — 用 Claude Code / Codex / OpenClaw 搭自己的流程
- [M10-02 Cloud Agent 工作原理](./02-how-it-works.md) — 回看架构
