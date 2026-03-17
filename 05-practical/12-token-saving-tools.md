# M5-12 · Token 节省工具：rtk 实战指南

> AI 编程助手每次调用命令都会消耗大量 token。`rtk`（Rust Token Killer）是一个 CLI 代理工具，将 `git status`、`cargo test`、`ls` 等常见命令的输出压缩过滤后再送给 AI，**单次会话可节省 60-90% 的 token 消耗**。

GitHub：[rtk-ai/rtk](https://github.com/rtk-ai/rtk) · 8.9k ⭐

---

## 为什么需要它？

AI 编程助手（Cursor、Claude Code 等）在运行命令时，会把**完整的原始输出**塞进上下文：

- `git push` 会输出 15 行进度信息，实际有用的只有最后 1 行
- `cargo test` 失败时输出 200+ 行，AI 只需要看失败的 2 行
- `ls -la` 输出 45 行详细权限信息，AI 只需要文件列表

**rtk 的作用**：在命令执行后、AI 读取前，自动过滤掉噪音，只保留关键信息。

---

## 实际节省效果

以一次 30 分钟的 Claude Code 开发会话为例：

| 操作 | 使用频率 | 原始 token | rtk 后 | 节省 |
|------|---------|-----------|--------|------|
| ls / tree | 10次 | 2,000 | 400 | -80% |
| cat / read | 20次 | 40,000 | 12,000 | -70% |
| grep / rg | 8次 | 16,000 | 3,200 | -80% |
| git status | 10次 | 3,000 | 600 | -80% |
| git diff | 5次 | 10,000 | 2,500 | -75% |
| git add/commit/push | 8次 | 1,600 | 120 | **-92%** |
| cargo test / npm test | 5次 | 25,000 | 2,500 | **-90%** |
| **合计** | **~118,000** | **~23,900** | **-80%** | |

---

## 安装

### macOS（推荐 Homebrew）

```bash
brew install rtk
```

### Linux / macOS（快速安装脚本）

```bash
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh
# 安装到 ~/.local/bin，需要加入 PATH：
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
```

### 验证安装

```bash
rtk --version   # 显示 rtk 0.30.0
rtk gain        # 查看 token 节省统计
```

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

**cargo test 失败（原始 vs rtk）：**

```
# 原始输出（200+行）                    # rtk 输出（~20行）
running 15 tests                        FAILED: 2/15 tests
test utils::test_parse ... ok             test_edge_case: assertion failed
test utils::test_format ... ok            test_overflow: panic at utils.rs:18
...（196行省略）...
```

---

## 自动拦截 Hook（最推荐的使用方式）

手动在每个命令前加 `rtk` 太麻烦。rtk 提供 Hook 机制，**透明地自动拦截所有 Bash 命令**，Claude Code 完全感知不到替换过程。

### 安装 Hook

```bash
# 为 Claude Code 安装全局 Hook（推荐）
rtk init --global

# 重启 Claude Code 后生效
```

安装后，AI 执行 `git status` 时，实际运行的是 `rtk git status`，但 AI 看到的指令仍然是原始的 `git status`。

### Hook 覆盖的命令

| 原始命令 | 自动替换为 |
|---------|-----------|
| `git status/diff/log/push/pull` | `rtk git ...` |
| `cat/head/tail <file>` | `rtk read <file>` |
| `rg/grep <pattern>` | `rtk grep <pattern>` |
| `ls` | `rtk ls` |
| `cargo test/build/clippy` | `rtk cargo ...` |
| `pytest / go test / npm test` | `rtk test ...` |
| `tsc / eslint / biome` | `rtk tsc / rtk lint` |
| `docker ps/images/logs` | `rtk docker ...` |

> **注意**：Hook 只对 Bash 工具调用生效。Cursor 的内置 Read、Grep、Glob 工具不经过 Hook，直接用原生实现，无需担心。

---

## 查看节省统计

```bash
rtk gain                        # 汇总统计
rtk gain --graph                # ASCII 折线图（近 30 天）
rtk gain --daily                # 按天明细
rtk discover                    # 发现还没用 rtk 的命令（找节省机会）
```

---

## 适合哪些场景？

| 场景 | 推荐程度 | 说明 |
|------|---------|------|
| 使用 Claude Code 日常开发 | ⭐⭐⭐⭐⭐ | 效果最明显，直接降低 API 费用 |
| Cursor Agent 模式 | ⭐⭐⭐⭐ | 减少上下文占用，提升响应速度 |
| CI/CD 自动化脚本 | ⭐⭐⭐ | 减少日志噪音 |
| 个人终端使用 | ⭐⭐ | 也可以用，但收益没有 AI 场景大 |

---

## 团队接入建议

1. 每个使用 Claude Code 的开发同学都执行 `rtk init --global`
2. 无需修改任何代码，零侵入
3. 用 `rtk gain` 定期查看节省了多少，直观感受效果
4. 如果某个命令不想被拦截，在 `~/.config/rtk/config.toml` 里配置排除

```toml
# ~/.config/rtk/config.toml
[hooks]
exclude_commands = ["curl", "playwright"]  # 这些命令不拦截
```

---

## 下一步

- [M5-11 ⭐️ 成本管理与模型选型](./11-cost-management.md)
- [M6-01 ⭐️ Cursor Rules 配置指南](../06-ai-project-setup/01-cursorrules.md)
