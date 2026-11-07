# M11-01 · rtk：Token 节省利器

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02
>
> 截至 2026-11：**约 85.8k ⭐**，最新稳定版 **v1.1.0**（2026-10-25）。rtk 已从「Claude Code 的 bash 输出压缩器」升级为**跨 Agent 的 token 优化管线**：压缩、路由、过滤都在一条管线里完成。
>
> GitHub：[rtk-ai/rtk](https://github.com/rtk-ai/rtk) ｜ 官网：[rtk-ai.app](https://www.rtk-ai.app)

---

## 为什么需要它？

AI 编程助手（Claude Code、Codex、Cursor、Copilot 等）在运行命令时，会把**完整的原始输出**塞进上下文：

- `git push` 会输出 15 行进度信息，实际有用的只有最后 1 行
- `cargo test` 失败时输出 200+ 行，AI 只需要看失败的 2 行
- `ls -la` 输出 45 行详细权限信息，AI 只需要文件列表

**rtk 的作用**：在命令执行后、AI 读取前，自动过滤掉噪音，只保留关键信息。官方口径是常见命令输出**最多减少约 90%**，单二进制、100+ 命令、开销 <10ms。

---

## 2026-11 的 rtk 有什么新东西

| 变化 | 说明 |
|------|------|
| **Agent-agnostic** | 不再只服务 Claude Code；支持 Claude Code、Codex、Cursor、Copilot、Gemini、Antigravity、Cline、Windsurf、Kimi、Factory Droid 等 20+ Agent |
| **两种发行版** | `rtk`（Apache-2.0 + BUSL-1.1，含压缩引擎）与 `rtk-oss`（纯 Apache-2.0，无引擎）；另有 `rtk-proxy` |
| **rtk-proxy** | 本地代理，压缩**发给模型厂商的 API 流量**，并把调用路由到更便宜的模型 |
| **100+ 命令** | Git、GitHub CLI、Cargo、npm/pnpm、pytest、Go、Docker、K8s、AWS、Terraform 等 |
| **`rtk gain` 增强** | 汇总、图表、按天、JSON 导出，便于做成本看板 |

> ⚠️ 许可证从早期的单一开源协议变为「Apache-2.0 + BUSL-1.1」双轨（`rtk-oss` 保持纯 Apache-2.0）。商用/二次分发前先看 LICENSE。

---

## 实际节省效果（早期实测，示例）

以一次 30 分钟的 Claude Code 开发会话为例（数据来自 2026 年初版本，仅用于建立量级概念，**不是当前版本承诺**）：

| 操作 | 使用频率 | 原始 token | rtk 后 | 节省 |
|------|---------|-----------|--------|------|
| ls / tree | 10次 | 2,000 | 400 | -80% |
| cat / read | 20次 | 40,000 | 12,000 | -70% |
| grep / rg | 8次 | 16,000 | 3,200 | -80% |
| git status | 10次 | 3,000 | 600 | -80% |
| git diff | 5次 | 10,000 | 2,500 | -75% |
| git add/commit/push | 8次 | 1,600 | 120 | **-92%** |
| cargo test / npm test | 5次 | 25,000 | 2,500 | **-90%** |
| **合计** | | **~118,000** | **~23,900** | **-80%** |

> 当前版本的实际节省取决于项目与命令；用 `rtk gain` 看你自己的数据。

---

## 安装

### macOS / Linux（推荐 Homebrew）

```bash
brew install rtk
```

### Windows

```bash
winget install rtk-ai.rtk
```

### 快速安装脚本

```bash
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh
# 安装到 ~/.local/bin，需要加入 PATH：
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
```

### 验证安装

```bash
rtk --version   # 显示当前版本（2026-11 稳定版为 v1.1.0）
rtk gain        # 查看 token 节省统计
```

> 完整安装方式（Cargo、预编译二进制、WSL、卸载）见[官方安装指南](https://github.com/rtk-ai/rtk#readme)。

---

## 核心用法

### 直接替换常用命令

```bash
# Git 操作
rtk git status          # 紧凑状态
rtk git diff            # 压缩 diff
rtk git log -n 10       # 单行提交记录
rtk git push            # 输出: "ok main"（1行 vs 原来15行）

# 文件操作
rtk ls .                # 目录树（token 优化版）
rtk read file.ts        # 智能读文件
rtk grep "pattern" .    # 分组搜索结果

# 测试输出（只看失败）
rtk test cargo test     # 只显示失败的测试 (-90%)
rtk pytest              # Python 测试 (-90%)
rtk go test             # Go 测试 (-90%)

# 构建与 Lint
rtk tsc                 # TypeScript 错误按文件分组
rtk lint                # ESLint 按规则分组
rtk next build          # Next.js 构建精简输出
```

### 输出对比示例

**git push（原始 vs rtk）：**

```
# 原始输出（15行，~200 tokens）         # rtk 输出（1行，~10 tokens）
Enumerating objects: 5, done.           ok main
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 1.23 KiB...
...
```

---

## 自动拦截 Hook（最推荐的使用方式）

手动在每个命令前加 `rtk` 太麻烦。rtk 提供 Hook 机制，**透明地自动拦截 Bash 命令**，Agent 完全感知不到替换过程。

### 按 Agent 初始化

```bash
rtk init -g                      # Claude Code / Copilot（默认）
rtk init -g --codex              # Codex
rtk init -g --gemini             # Gemini CLI
rtk init -g --agent cursor       # Cursor
rtk init -g --agent windsurf     # Windsurf / Devin Desktop
rtk init --agent cline           # Cline / Roo Code
rtk init --agent antigravity     # Google Antigravity
rtk init --agent kimi            # Kimi
rtk init -g --agent droid        # Factory Droid
```

重启对应 Agent 后生效。

### 覆盖的 Agent 与方式（2026-11）

| Agent | 安装方式 | 机制 |
|-------|---------|------|
| Claude Code | `rtk init -g` | PreToolUse hook |
| GitHub Copilot（VS Code） | `rtk init -g --copilot` | PreToolUse hook |
| Cursor | `rtk init -g --agent cursor` | preToolUse hook（hooks.json） |
| Gemini CLI | `rtk init -g --gemini` | BeforeTool hook |
| Codex | `rtk init -g --codex` | PreToolUse hook + AGENTS.md |
| Windsurf / Devin Desktop | `rtk init -g --agent windsurf` | `.windsurfrules`（项目级） |
| Antigravity | `rtk init --agent antigravity` | `.agents/plugins/rtk/` 插件 |
| Kimi | `rtk init --agent kimi` | `AGENTS.md`（项目级） |

> **注意**：Hook 只对 Bash 工具调用生效。Cursor 的内置 Read、Grep、Glob 工具不经过 Hook；这类场景用 `rtk read` / `rtk grep` 或走 shell 命令。完整列表见 [Supported Agents](https://github.com/rtk-ai/rtk#readme)。

---

## 查看节省统计

```bash
rtk gain                        # 汇总统计
rtk gain --graph                # ASCII 折线图（近 30 天）
rtk gain --daily                # 按天明细
rtk gain --history              # 最近命令历史
rtk gain --all --format json    # JSON 导出（做看板）
```

---

## rtk-proxy：压缩 API 流量（进阶）

`rtk-proxy` 是本地后台代理，位于 Agent 和模型厂商之间，做三件事：

1. **压缩**请求 payload（删掉模型不需要的字节）
2. **路由**部分调用到更便宜的模型
3. 复用 Agent 已有的凭证，统一记入 `rtk gain`

```bash
rtk claude              # 启动 daemon 并让 Claude 走代理
rtk gain                # 命令过滤 + 代理节省并排查看
```

> 适合重度 Agent 用户；团队使用前先评估网关/合规策略。

---

## 适合哪些场景？

| 场景 | 推荐程度 | 说明 |
|------|---------|------|
| 使用 Claude Code 日常开发 | ⭐⭐⭐⭐⭐ | 效果最明显，直接降低 API 费用 |
| Cursor / Codex Agent 模式 | ⭐⭐⭐⭐ | 减少上下文占用，提升响应速度 |
| CI/CD 自动化脚本 | ⭐⭐⭐ | 减少日志噪音 |
| 个人终端使用 | ⭐⭐ | 也可以用，但收益没有 AI 场景大 |

---

## 团队接入建议

1. 每个使用 Agent 的开发同学按自己的 Agent 执行 `rtk init`
2. 无需修改业务代码，零侵入
3. 用 `rtk gain` 定期查看节省，直观感受效果
4. 敏感命令/工具在配置里排除，避免误拦截

```toml
# 示例：排除某些命令（具体路径以当前版本文档为准）
[hooks]
exclude_commands = ["curl", "playwright"]
```

> 配置项随版本变化，以 `rtk --help` 和官方文档为准。

---

## 历史沿革

- **2026-11**：rtk 约 85.8k ⭐，稳定版 v1.1.0；已支持 20+ Agent；新增 `rtk-proxy` 与 JSON 统计导出；许可证为 Apache-2.0 + BUSL-1.1 双轨。
- **2026-10-25**：v1.1.0 发布。
- **2026 年中**：从 Claude Code 专用 hook 扩展为 agent-agnostic 管线，命令数超过 100。
- **2026-03（旧版数据）**：当时 rtk 约 8.9k ⭐、版本 0.30.0，只支持 Claude Code 的 bash hook。本文旧版按当时版本编写，现已作为历史对照保留。

---

## 下一步

- [M5-11 ⭐️ 成本管理与模型选型](../05-practical/11-cost-management.md)
- [M6-01 ⭐️ Cursor Rules 配置指南](../06-ai-project-setup/01-cursorrules.md)
- [M11-05 Claude Code 省 Token 指南](./05-claude-code-token-optimization.md)
