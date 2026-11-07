# M10-04 · 自建 Cloud Agent 工作流

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 不依赖单一商业平台，用 Claude Code、Codex、OpenClaw 或 CI 拼出你自己的 Agent 工作流。
> 2026 年的新变化：**官方也提供"自托管执行环境"**，你可以既用托管产品的能力、又把代码留在自己的基础设施里。

---

## 一句话结论

自建不等于"从零写 Agent 框架"。2026-11 有四条成熟路径：

1. **官方云 + 自托管环境**：Claude Code cloud 任务跑在你自己的环境里（Team/Enterprise）。
2. **CLI/Headless + CI**：`claude -p` / Codex CLI 嵌进 GitHub Actions、cron、Webhook。
3. **Agent SDK**：用官方 SDK 写自己的调度、审批与交付逻辑。
4. **自托管网关**：OpenClaw 这类 Gateway 把渠道、模型、工具、自动化收在一起。

---

## 为什么自建？

| 维度 | 商业 Cloud Agent | 自建方案 |
|------|------------------|----------|
| 数据隐私 | 代码/数据进入厂商云 | 可留在自己的环境 |
| 成本 | 订阅/席位费 | 主要是 API token + 算力 |
| 定制化 | 受产品边界限制 | 触发、权限、交付全可控 |
| 运维 | 厂商负责 | 自己负责（升级、监控、安全） |
| 上手 | 简单 | 需要配置与工程能力 |
| 适合 | 快速开始 / 标准流程 | 私有代码 / 特殊流程 / 合规要求 |

---

## 方案零：团队现成实例（新手推荐）

> 不需要任何配置：团队基于 Cursor 搭建的 Cloud Agent 实例，可直接体验"派任务 → 等结果"。

🔗 **[https://vibe.iamxmm.xyz/dashboard](https://vibe.iamxmm.xyz/dashboard)**

- 零配置，打开即用；
- 适合第一次尝试、演示与协作；
- 若地址/可用性有变化，以团队通知为准。

> 2026 年提醒：团队实例适合"跑通流程"，**不要把生产凭据或敏感仓库放进去**；涉及私有数据请走下面的自建方案。

---

## 方案一：Claude Code（CLI / Headless / Cloud）

### 本地/CI 非交互执行

```bash
# 安装（以官方文档为准）
npm install -g @anthropic-ai/claude-code

# 非交互：适合脚本与 CI
claude -p "给 src/auth.js 写单元测试"

# 指定权限模式（自动化场景）
claude -p --permission-mode acceptEdits "修复 lint 错误"
```

> 旧教程里的 `--permission-mode bypassPermissions` 风险很高，**不要在生产仓库默认开启**；优先用白名单 + 审批 + 沙箱。

### 直接起云会话

```bash
claude --cloud "执行 docs/migration-plan.md 里的迁移计划"
```

适合：任务长、本机不想跑、需要多任务并行。

### 自托管执行环境（Team / Enterprise）

Claude Code 支持把云会话路由到**你自己的执行环境**（self-hosted environment）：由 Anthropic 编排，但代码与网络在你自己的基础设施里。适合"要云体验、又要数据边界"的团队。

> 配置方式与前置条件见官方文档：[Self-hosted environments](https://code.claude.com/docs/en/self-hosted-environments)。

### GitHub Actions 示例

```yaml
# .github/workflows/agent-task.yml
name: Claude Code Agent Task

on:
  workflow_dispatch:
    inputs:
      task:
        description: "告诉 Agent 要做什么"
        required: true

jobs:
  agent:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v4

      - name: 安装依赖
        run: npm ci

      - name: 运行 Agent
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          npx @anthropic-ai/claude-code -p --permission-mode acceptEdits \
            "${{ inputs.task }}"

      - name: 提交并开 PR
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          if git diff --quiet; then
            echo "没有变更"; exit 0
          fi
          BRANCH="agent/task-$(date +%Y%m%d-%H%M%S)"
          git checkout -b "$BRANCH"
          git config user.name "Claude Code Agent"
          git config user.email "agent@ci"
          git add -A
          git commit -m "chore: agent task - ${{ inputs.task }}"
          git push origin "$BRANCH"
          gh pr create --fill --base main --head "$BRANCH"
```

也可以直接用官方的 GitHub Action（`anthropics/claude-code-action`），减少自己拼装的工作量。

---

## 方案二：OpenAI Codex Cloud / CLI

- **Cloud**：在 ChatGPT 里建环境、派任务、收 PR（见 [M10-03](./03-using-cloud-agent.md)）。
- **CLI**：本地执行、脚本化调用，或从终端起云任务；配置在 `~/.codex/config.toml`。
- **计费**：随 ChatGPT 套餐，或 Codex-only 按量席位（2026-04 起）；具体价格以官网为准。

适合：已有 ChatGPT 套餐、希望"云上跑 + 本地也能跑"的团队。

---

## 方案三：OpenClaw 自托管网关

如果需求是"多渠道 + 定时/事件触发 + 多模型"，OpenClaw 比自写脚本更省事：

```
IM/Webhook/cron → OpenClaw Gateway → Agent（Skills + MCP）→ 结果回投递渠道
```

典型用法：

- 每天定时跑代码质量报告，发到 Telegram/飞书；
- GitHub Issue 触发 → Agent 分析 → 回帖；
- 多人共享一个 Gateway，按用户/渠道隔离权限。

> 安装与配置见 [M9-02](../09-openclaw/02-setup.md)，Skills/MCP 见 [M9-03](../09-openclaw/03-skills-mcp.md)。

---

## 方案四：定时/事件触发的最小脚本

最灵活、也最"原始"的方案：shell + cron + CLI。

```bash
#!/bin/bash
# agent-task.sh —— 在隔离工作目录里跑一个 Agent 任务
set -euo pipefail

TASK="${1:?用法: ./agent-task.sh \"任务描述\"}"
REPO="git@github.com:your-org/your-repo.git"
BRANCH="agent/task-$(date +%Y%m%d-%H%M%S)"
WORKDIR="$(mktemp -d)"
trap 'rm -rf "$WORKDIR"' EXIT

git clone --depth 1 "$REPO" "$WORKDIR"
cd "$WORKDIR"
git checkout -b "$BRANCH"

# 安装依赖（按项目调整）
npm ci

# 运行 Agent（非交互）
claude -p --permission-mode acceptEdits "$TASK"

# 无变更则退出
if git diff --quiet; then
  echo "没有变更，任务可能无需修改"
  exit 0
fi

git config user.name "Claude Agent"
git config user.email "agent@local"
git add -A
git commit -m "agent: $TASK"
git push origin "$BRANCH"

echo "✅ 已推送分支 $BRANCH，请创建/查看 PR"
```

调用：

```bash
./agent-task.sh "给 src/api/ 下缺少校验的 POST 接口添加 Zod 校验"
```

**要点：**

- 每次任务用**临时目录**，避免污染本机；
- 用 `trap` 清理；失败不要留半成品；
- 推送后由人开 PR / review，不要自动合并。

---

## 实用工作流示例

### 每周代码质量报告

```bash
# cron: 每周一 9:00
0 9 * * 1 cd /path/to/repo && claude -p "分析 src/，输出：
1. 超过 100 行的函数
2. 没有注释的 exported 函数
3. 重复代码片段
以 Markdown 输出" > weekly-report.md
```

### PR 自动 Review

```yaml
name: AI Code Review
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          git diff origin/main...HEAD > pr.diff
          claude -p "Review 以下变更，指出 Bug、安全问题、性能问题、可读性建议：
          $(cat pr.diff)" > review.md
          gh pr comment ${{ github.event.pull_request.number }} --body-file review.md
```

### 事件驱动（Issue → Agent）

```
GitHub Issue 打上 label:ai-task
  → Webhook / Actions 触发
  → 起云会话或本地容器
  → Agent 修复并开 PR
  → 通知到 IM
```

---

## 费用参考（怎么算，而不是记死数字）

自建成本 ≈ **API token 费 + 运行环境费 + 你的维护时间**。

```
单任务成本 ≈ (输入 token × 输入单价) + (输出 token × 输出单价)
月成本 ≈ 任务数 × 单任务成本 + 失败重试成本
```

- 不要照抄旧文章的"每次 ¥1.5"——模型价格、缓存价、批量折扣都变了；
- 用官方 pricing 页的最新单价代入；
- 估算时把**失败重试**和**并行任务**算进去，实际往往是名义值的 1.5–3 倍；
- 对比商业方案时，把"平台费 + 席位费"和"你的维护时间"都折算进去。

> 价格以各厂商官网为准（2026-11 核对时点）。Claude 价格见 [claude.com/pricing](https://claude.com/pricing)，OpenAI 见 [openai.com/pricing](https://openai.com/pricing)。

---

## 选型建议

| 方案 | 适合 | 上手难度 |
|------|------|----------|
| 团队实例 [vibe.iamxmm.xyz](https://vibe.iamxmm.xyz/dashboard) | 零配置体验 | ⭐ |
| Claude Code + GitHub Actions | 想集成到 PR 流程 | ⭐⭐ |
| Claude Code 自托管环境 | 数据要留在自己基础设施 | ⭐⭐⭐ |
| Codex Cloud / CLI | 已有 ChatGPT 套餐 | ⭐⭐ |
| OpenClaw | 多渠道、定时/事件、多模型 | ⭐⭐⭐ |
| 自定义脚本 | 特殊触发与交付逻辑 | ⭐⭐⭐ |

**原则：** 先用托管产品跑通一个真实任务，再判断"哪里不够用"，最后才自建。**不要为了自建而自建。**

---

## 安全清单

- [ ] Agent 用独立账号/最小权限 token
- [ ] 生产凭据不进 Agent 环境；用密钥代理/短期令牌
- [ ] 任务在临时目录/容器/隔离环境中执行
- [ ] 分支保护 + 必需 review；Agent 不能直接 push main
- [ ] CI 在干净环境重跑；检查测试文件是否被改
- [ ] 记录会话日志与用量；设预算告警
- [ ] 定期清理旧分支、旧凭据、旧环境

---

## 历史沿革

- **2026-11**：官方自托管环境、Agent SDK、云会话 CLI 成为"自建"的新选项；OpenClaw 继续承担"多渠道 + 自动化"角色。
- **2026-04**：Codex 推出团队按量付费席位；Cowork GA 后，知识工作类的自建需求部分被托管产品吸收。
- **~~已过时~~ 2026-03 版内容**：
  - 方案主线是"Cursor 团队实例 + Claude Code CLI + ChatGPT Codex + 自定义脚本"；
  - CI 示例使用 `--permission-mode bypassPermissions`（高风险，已不推荐默认使用）；
  - 费用示例写死"中型任务约 ¥1.5/次、Devin 约 ¥3,600/月"——这些数字已过期，改为按官方单价计算；
  - `npx @anthropic-ai/claude-code` 的包名与安装方式以当前官方文档为准。

---

## 模块回顾

完成 M10，你应该掌握：

- ✅ Cloud Agent 是什么，和本地 AI 工具的本质区别；
- ✅ 2026-11 的产品版图：Claude Code cloud / Remote Control、Cowork、Duet、Codex Cloud、Copilot in the cloud、Antigravity、Devin、OpenClaw；
- ✅ 各形态的执行位置、触发方式、权限与计费口径；
- ✅ 如何写任务、如何 review、如何避坑；
- ✅ 如何用 CLI/CI/SDK/自托管网关搭自己的流程。

**下一步：** 挑一个你手上的真实任务，用 Cloud Agent 跑一遍，并完整 review 它给出的 PR。
