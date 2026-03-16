# M10-04 · 自建 Cloud Agent 工作流

> 不依赖第三方平台，用 Claude Code 或 Codex 搭建你自己的 Agent 工作流

---

## 为什么要自建？

| | 商业 Cloud Agent | 自建方案 |
|---|---|---|
| 数据隐私 | 代码上传到对方服务器 | 完全在你的环境里 |
| 成本 | 平台订阅费（$20-500/月） | 只付 API Token 费用 |
| 定制化 | 有限 | 完全自由 |
| 上手难度 | 简单 | 需要配置 |
| 适合 | 快速开始 / 公司项目 | 个人项目 / 私有代码 |

---

## 方案零：直接用团队现成实例（最推荐新手）

> **不需要任何配置**，团队已经用 Cursor 搭建了一套开箱即用的 Cloud Agent 实例，所有人都可以直接使用。

### 访问地址

🔗 **[https://vibe.iamxmm.xyz/dashboard](https://vibe.iamxmm.xyz/dashboard)**

### 特点

```
✅ 零配置，打开即用
✅ 基于 Cursor 搭建，体验与本地 Cursor Agent 一致
✅ 团队共享实例，无需个人申请 API Key
✅ 适合快速上手、体验 Cloud Agent 工作流
```

### 适合场景

- 第一次尝试 Cloud Agent，不想折腾环境
- 日常任务量不大，不值得单独维护一套工作流
- 团队演示与协作

### 使用建议

1. 打开 Dashboard，用团队账号登录
2. 创建一个新任务，参考 [M10-03 任务描述模板](./03-using-cloud-agent.md) 写好任务
3. 提交后等待结果，支持异步通知
4. 如果任务较复杂或涉及私有数据，再考虑下方的自建方案

---

## 方案一：Claude Code（推荐）

Claude Code 是 Anthropic 官方的命令行 Agent 工具，在本地或 CI 环境里跑。

### 安装

```bash
npm install -g @anthropic-ai/claude-code
```

### 基本用法

```bash
# 进入你的项目目录
cd /your-project

# 非交互模式（适合脚本 / CI）
claude --print "帮我给 src/auth.js 写单元测试"

# 交互模式（直接在终端对话）
claude

# 指定权限（绕过确认，适合自动化）
claude --permission-mode bypassPermissions --print "..."
```

### 在 CI/CD 里使用

```yaml
# .github/workflows/agent-task.yml
name: Claude Code Agent Task

on:
  workflow_dispatch:       # 手动触发
    inputs:
      task:
        description: '告诉 Agent 要做什么'
        required: true

jobs:
  agent:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: 安装依赖
        run: npm install
      
      - name: 运行 Claude Code Agent
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          npx @anthropic-ai/claude-code \
            --print \
            --permission-mode bypassPermissions \
            "${{ inputs.task }}"
      
      - name: 提交变更（如果有）
        run: |
          git config user.name "Claude Code Agent"
          git config user.email "agent@ci"
          git add -A
          git diff --staged --quiet || git commit -m "chore: agent task - ${{ inputs.task }}"
          git push
```

触发方式：GitHub → Actions → 手动输入任务描述，点 Run。

---

## 方案二：OpenAI Codex（ChatGPT 内置）

Codex 是 ChatGPT 内置的云端编程 Agent，独立沙箱环境。

### 使用方式

```
打开 ChatGPT
  → 左侧边栏找到 "Codex"
  → 连接你的 GitHub 仓库
  → 输入任务
  → Codex 在 OpenAI 云端的隔离环境里执行
```

### 特点

```
✅ 不需要自己配置环境
✅ 支持长任务（几十分钟）
✅ 直接创建 PR 到你的 GitHub
⚠️  代码上传到 OpenAI 服务器
⚠️  需要 ChatGPT Plus 或 Pro
```

### 适合场景

```
- 连接 GitHub 仓库，任务直接变 PR
- 需要较长运行时间的任务
- 不想自己配 CI/CD 的情况
```

---

## 方案三：定时 / 事件触发 Agent 任务

最灵活的自建方案：用脚本把 Claude Code 嵌入你的工作流。

### 结构

```
触发器（cron / Webhook / 消息通知）
    ↓
创建隔离工作目录
    ↓
git clone + 安装依赖
    ↓
运行 Claude Code --print "任务"
    ↓
git commit + push + 创建 PR
    ↓
通知你（Telegram / Slack / 邮件）
```

### 示例脚本

```bash
#!/bin/bash
# agent-task.sh

set -e

TASK="$1"
REPO="git@github.com:your-org/your-repo.git"
BRANCH="agent/task-$(date +%Y%m%d-%H%M%S)"

# 创建临时工作目录
WORKDIR=$(mktemp -d)
trap "rm -rf $WORKDIR" EXIT

# 克隆仓库
git clone "$REPO" "$WORKDIR"
cd "$WORKDIR"
git checkout -b "$BRANCH"

# 安装依赖
npm install

# 运行 Agent
claude --print --permission-mode bypassPermissions "$TASK"

# 提交并推送
git add -A
if git diff --staged --quiet; then
  echo "没有变更，任务可能已完成或无需修改"
  exit 0
fi

git config user.name "Claude Agent"
git config user.email "agent@local"
git commit -m "agent: $TASK"
git push origin "$BRANCH"

echo "✅ 完成！分支 $BRANCH 已推送，请查看 PR"
```

调用方式：

```bash
./agent-task.sh "给 src/api/ 下所有缺少 input validation 的接口添加 Zod 校验"
```

---

## 实用工作流示例

### 每周代码质量报告

```bash
# cron: 每周一 9:00
0 9 * * 1 claude --print "分析 src/ 目录，输出本周代码质量报告：
1. 超过 100 行的函数列表
2. 没有注释的 exported 函数
3. 重复代码片段
以 Markdown 格式输出" > weekly-report.md
```

### PR 自动 Review

```yaml
# .github/workflows/pr-review.yml
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: AI Code Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          git diff origin/main...HEAD > pr.diff
          claude --print "Review 以下代码变更，指出：
          1. 潜在 Bug
          2. 安全问题
          3. 性能问题
          4. 可读性建议
          $(cat pr.diff)" > review.md
          
          # 把 review 结果发到 PR 评论（用 GitHub CLI）
          gh pr comment ${{ github.event.pull_request.number }} --body "$(cat review.md)"
```

---

## 费用参考

用 Claude API 自建的成本（以 Claude Sonnet 为例）：

```
一个中型任务（修改 20 个文件）：
  输入 Token：~50,000（约 ¥0.5）
  输出 Token：~20,000（约 ¥1.0）
  总计：约 ¥1.5 / 次

对比 Devin：约 ¥3,600 / 月
```

自建方案在任务量不大时，成本优势非常明显。

---

## 小结

Cloud Agent 工作流的四种选择：

| 方案 | 适合 | 上手难度 |
|------|------|---------|
| **团队共享实例** [vibe.iamxmm.xyz](https://vibe.iamxmm.xyz/dashboard) | 零配置，快速上手体验 | ⭐（推荐新手） |
| Claude Code + CI/CD | 想集成到 GitHub Actions | ⭐⭐ |
| ChatGPT Codex | 不想自己配置环境 | ⭐⭐ |
| 自定义脚本 | 需要定制触发逻辑 | ⭐⭐⭐ |

**原则：** 从最简单的方案开始——先用团队实例跑通一个任务，再决定是否需要自建。

---

## 参考资源

- [Claude Code 文档](https://docs.anthropic.com/en/docs/claude-code)
- [OpenAI Codex](https://chatgpt.com/codex)
- [GitHub Actions 文档](https://docs.github.com/en/actions)

---

## 模块回顾

完成 M10，你现在了解了：

- ✅ Cloud Agent 是什么、和本地 AI 工具的区别
- ✅ 它的技术原理：沙箱 + 执行循环 + 异步交付
- ✅ 如何用 Cursor Background Agent 高效完成任务
- ✅ 如何自建 Claude Code / Codex 工作流

**下一步推荐：** 挑一个你最近的实际任务，尝试用 Cloud Agent 完成它。
