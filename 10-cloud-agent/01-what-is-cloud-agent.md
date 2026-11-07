# M10-01 · 什么是 AI Cloud Agent

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 不在你的电脑上跑的 AI，却能完成完整的软件/知识工作任务。**2026 年的关键变化：它不再只是"云端写代码"，而是分成托管云沙箱、本地+远程控制、桌面代理、自托管网关四种形态。**

---

## 一句话结论

Cloud Agent = **隔离执行环境 + 真实工具权限 + 异步任务 + 可审查的交付物（PR/文件/报告）**。

到了 2026-11，选型的第一问题不再是"哪个 Agent 最聪明"，而是：

1. **代码/数据要不要离开你的机器？**
2. **你要它跑几分钟还是几小时？**
3. **它能碰生产环境吗？谁批准？**
4. **按订阅、按席位还是按 token 付费？**

---

## 从一个场景说起

```
你：把这个旧项目从 Python 2 迁移到 Python 3
本地 AI：好的，我来帮你……（改了一半，上下文爆了）
```

```
你：跑一遍所有测试，把失败的都修掉
本地 AI：我没有权限执行命令 / 只能给你建议
```

Cloud Agent 解决的是这两件事：**长任务**与**真实执行**。你发出任务后可以去开会、睡觉，它在一个隔离环境里读代码、改代码、跑测试、开 PR。

---

## 2026-11 产品版图

### 托管云沙箱（代码/任务在厂商云上执行）

| 产品 | 执行位置 | 触发方式 | 权限模型 | 计费口径 | 适用场景 |
|------|----------|----------|----------|----------|----------|
| **Claude Code cloud sessions** | Anthropic 托管 VM，或企业自托管环境 | `claude.ai/code`、Claude 手机 App 的 Code、桌面 Cloud、`claude --cloud`、定时任务 | 按会话选权限模式；GitHub App / `/web-setup`；组织策略可禁用 | 计入 Claude/Claude Code 套餐用量；云 VM 不单独收费（以官网为准） | 长任务、并行任务、离开电脑后继续 |
| **Claude Cowork** | 桌面端本地隔离 VM；Web/移动端为远程会话 | Claude Desktop / Web / 移动端；可设定时任务 | 每会话授权连接器；敏感动作需确认 | 含在 Claude 套餐内（Pro/Max/Team/Enterprise） | 知识工作：报告、表格、调研、跨应用流程 |
| **Claude Duet** | 云端"它自己的电脑" | 手机 App（研究预览，候补制） | 发消息/付款/签文件/删除前必须批准 | 含在 Pro/Max/Ultra，无额外费用（预览期） | 个人事务：邮件、日程、账单、调研 |
| **OpenAI Codex Cloud** | OpenAI 云环境 | ChatGPT Web/移动/桌面，或 CLI 发起 | 环境级网络与密钥配置；任务可开 PR | ChatGPT 套餐 + Codex-only 按量席位 | 编码任务、多任务并行、PR 交付 |
| **GitHub Copilot in the cloud** | 默认 cloud sandbox；可选 GitHub Actions 或远程自定义环境 | GitHub.com / Mobile / IDE / CLI；会话跨端继续 | 仓库写权限决定可写/只读；组织策略 | 付费 Copilot 套餐；cloud/Actions 有月度额度，AI credits 另计 | GitHub 重度团队、Issue→PR |
| **Google Antigravity** | 云端后台任务 + agent-first 开发环境 | Antigravity App / CLI / IDE | Google 账号与项目权限 | 见官网 Pricing（2026-11 未固定口径） | Gemini 生态、远程后台任务 |
| **Devin** | Devin Cloud | Devin 桌面/云、Slack/Teams、API | 仓库与集成授权 | 个人 Free/$20/$200；Team $80/月 + $40/席位（2026-11 官网价） | 复杂工程任务、团队协作 |
| **Cursor Cloud Agents** | Cursor 云端 | Cursor IDE 内 Background/Cloud 模式 | 仓库与工具授权 | Cursor 套餐 | 已在 Cursor 工作流里的团队 |

### 本地执行 + 远程控制（代码不离开你的机器）

| 产品 | 特点 |
|------|------|
| **Claude Code Remote Control** | CLI/桌面/VS Code 会话在本机跑，手机/浏览器远程查看与操控；适合"人离开但机器还开着" |
| **OpenClaw** | 自托管 Gateway，渠道（Telegram/微信/飞书…）+ 云端会话 + 定时/事件自动化；数据完全自控 |

> 关键区别：**托管云 = 代码上传到厂商环境**；**Remote Control = 执行仍在本地，只是操作入口远程**。合规敏感团队优先看后者。

---

## 形态分类：四种模式

```
① 托管云沙箱
   你 → 厂商云 VM → Agent 执行 → PR/文件
   代表：Claude Code cloud、Codex Cloud、Copilot cloud、Devin、Antigravity

② 本地执行 + 远程控制
   你（手机/浏览器）→ 你的机器上的 Agent → 本地文件/命令
   代表：Claude Code Remote Control

③ 桌面/个人代理
   Agent 在你电脑的隔离环境里操作应用与文件
   代表：Claude Cowork、Claude Duet（云端版）

④ 自托管网关
   你自己的服务器 → Gateway → 多渠道 + 多模型 + 工具
   代表：OpenClaw
```

---

## 和本地 AI 工具的区别

| 对比维度 | 本地 AI 工具（IDE Chat / CLI） | Cloud Agent |
|----------|-------------------------------|-------------|
| 执行环境 | 你的电脑 | 云端隔离环境 / 隔离 VM |
| 任务时长 | 受上下文与会话限制 | 几十分钟到数小时 |
| 是否异步 | 通常需要你在场 | ✅ 后台跑，完成通知 |
| 能跑命令吗 | 可以，但需逐条确认 | ✅ 在沙箱内完整执行 |
| 并发 | 单会话为主 | ✅ 多任务并行 |
| 结果形式 | 内联建议 | PR / 分支 / 文件 / 报告 |
| 数据边界 | 代码留在本地 | 代码/数据进入厂商环境 |

---

## 适合 / 不适合

✅ **适合：**

- 大型重构、框架升级、批量修复
- 补测试、生成文档、代码审查
- 需要跑几十分钟以上、你不想盯着的任务
- 知识工作：调研报告、表格、演示稿（Cowork / Duet）

❌ **不适合：**

- 需要你实时参与决策的探索性任务
- 直接操作生产数据库/生产环境（除非有严格审批与隔离）
- 需求本身不清晰、无法验收的任务
- 强合规场景下"代码不得出内网"（应选 Remote Control / 自托管）

---

## 风险与治理（2026 年重点）

| 风险 | 说明 | 建议 |
|------|------|------|
| 数据出境 | 托管云会把代码/文件上传 | 先确认公司政策；敏感仓库用自托管/Rremote Control |
| 凭据泄露 | 环境变量、网络密钥、Git 凭据 | 用厂商的密钥代理/网络密钥机制；不要把密钥写进仓库 |
| 提示注入 | Agent 读到的 Issue/网页/邮件可能含恶意指令 | 限制网络出口；高风险动作人工批准；审查 PR |
| 越权修改 | Agent 可能改测试、改 CI、改权限文件 | 分支保护、必需 review、检查测试文件是否被动过 |
| 成本失控 | 并行任务成倍消耗额度 | 设预算/额度；小任务先用便宜模型 |
| 供应商锁定 | 流程绑死某家产品 | 用标准交付物（PR、diff、报告）作为边界 |

---

## 小结

```
Cloud Agent = 隔离环境 + 真实执行权 + 异步调度 + 可审查交付
```

选型口诀：

> **代码能不能出去？→ 能：托管云；不能：Remote Control / 自托管。**
> **任务有多长？→ 分钟级：IDE Agent；小时级：Cloud Agent。**
> **谁来兜底？→ 永远是人 review，不是"测试通过就合并"。**

---

## 历史沿革

- **2026-10**：Claude Duet research preview（2026-10-21，美国 Pro/Max/Ultra 候补）；Google 宣布 Jules 关停，能力并入 Antigravity（2026-10-29 报道）；GitHub 推出新版 Copilot in the cloud（2026-10-28 起对付费计划开放）。
- **2026-09**：Claude Cowork 并入所有对话（2026-09-16）。
- **2026-07**：Claude Cowork 登陆 Web 与移动端（2026-07-07，远程会话 beta）。
- **2026-04**：Claude Cowork GA（2026-04-09，macOS/Windows）；OpenAI Codex 推出团队按量付费席位（2026-04-02）。
- **2026-01**：Claude Cowork 研究预览（macOS，Max → Pro）。
- **~~已过时~~ 2026-03 初版产品列表**：当时把 Cursor Background Agent、Devin、GitHub Copilot Workspace、Claude Code CLI、OpenAI Codex 并列为"主流 Cloud Agent"。今天看：
  - Cursor Background Agent 已演进为 Cursor 的 Cloud Agents；
  - GitHub Copilot Workspace 已被 Copilot in the cloud / cloud agent 取代；
  - Claude Code 从"命令行工具"扩展出 cloud sessions 与 Remote Control；
  - Codex 从"ChatGPT 内置"扩展为独立 App + Cloud + CLI；
  - Devin 从"$500/月起的企业工具"转向个人订阅 + 团队席位。

---

## 下一步

- [M10-02 Cloud Agent 工作原理](./02-how-it-works.md) — 沙箱、执行循环、凭据隔离
- [M10-03 如何使用 Cloud Agent](./03-using-cloud-agent.md) — 上手与避坑
