# ⭐️ M9-02 · OpenClaw 安装与配置

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 从零到跑起来。**注意：2026 年的安装方式与 1.x 时代不同**——推荐用官方安装脚本或桌面 App，Node 版本要求也提高了。旧步骤保留在文末「历史沿革」。

---

## 一句话结论

2026-11 最省事的路径是：

```bash
# macOS / Linux / WSL2
curl -fsSL https://openclaw.ai/install.sh | bash
```

脚本会自动装 Node、装 OpenClaw、拉起引导（onboarding）；Windows 推荐直接下 **Windows Hub** 客户端，或用 PowerShell 安装脚本。

---

## 前置条件

| 项目 | 要求 |
|------|------|
| 操作系统 | macOS、Linux、Windows（原生或 WSL2） |
| Node.js | **24.16.0+（24.x）或 26.1.0+**；官方强烈推荐 24.22.1+ / 26.12.1+（安全修复）；推荐 Node 26 |
| 包管理器 | 用安装脚本时不需要；源码构建需要 pnpm |
| 模型 | Claude / OpenAI / Gemini / 本地模型等任一 provider 的凭据 |
| 渠道 | 至少一个聊天渠道（Telegram Bot 最简单） |
| 网络 | 能访问模型 API；若用 Webhook/事件触发，需要公网 HTTPS |

> 版本要求可能继续上调，以 [Install 文档](https://docs.openclaw.ai/install) 为准。

---

## 安装

### 方式 A：官方安装脚本（推荐）

```bash
# macOS / Linux / WSL2
curl -fsSL https://openclaw.ai/install.sh | bash

# 只安装、不立即引导
curl -fsSL https://openclaw.ai/install.sh | bash -s -- --no-onboard
```

```powershell
# Windows PowerShell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

### 方式 B：桌面 App

- **Windows**：下载 Windows Hub 安装包（`OpenClawCompanion-Setup-*.exe`）。
- **macOS**：从 GitHub Releases 下载 `OpenClaw-<version>.dmg`，安装并启动 **OpenClaw.app**。

桌面 App 可以在首次启动时**自带一个本地 Gateway**，也可以连接已有的远程 Gateway。

### 方式 C：npm / pnpm / bun（自己管理 Node）

```bash
# npm（npm 12 默认阻止生命周期脚本，需要显式允许）
npm install -g openclaw@latest --allow-scripts=openclaw
openclaw onboard --install-daemon

# pnpm
pnpm add -g --allow-build=openclaw openclaw@latest
openclaw onboard --install-daemon
```

> `--allow-scripts` / `--allow-build` 是必须的：OpenClaw 的 preinstall/postinstall 需要执行；不同 npm 版本的策略不同，详见官方 Install 文档的说明。

### 方式 D：Docker / 服务器部署

官方提供 Docker、Podman、Kubernetes、VPS 一键部署与多个托管平台模板（Fly.io、Railway、Render、Hetzner、DigitalOcean 等）。适合"7×24 在线"的场景。

---

## 引导与验证

```bash
openclaw --version      # 确认 CLI 可用
openclaw doctor         # 检查配置与依赖
openclaw gateway status # 确认 Gateway 在跑
```

引导（`openclaw onboard`）会依次处理：

1. 选择模型 provider、填凭据；
2. 选择聊天渠道；
3. 安装为系统服务（macOS LaunchAgent / Linux systemd user service / Windows 计划任务）。

**托管启动：**

```bash
openclaw onboard --install-daemon   # 或
openclaw gateway install
```

---

## 接入聊天渠道

### Telegram（最简单）

1. 在 Telegram 搜索 `@BotFather` → `/newbot` → 按提示创建；
2. 拿到 Bot Token（形如 `123456789:ABC...`）；
3. 在引导流程或 **Control UI → Settings → Channels** 里选择 Telegram，粘贴 Token；
4. 给你的 Bot 发 `/start`，收到回复即成功。

> 旧版命令 `openclaw channel add telegram` 仍可能可用，但 2.0 后推荐统一走引导 / Control UI，见历史沿革。

### 其他常用渠道

| 渠道 | 接入方式 | 注意事项 |
|------|----------|----------|
| **Discord** | Bot Token + 权限配置 | 注意频道/线程路由与访问控制 |
| **Slack** | App + OAuth / Bot Token | 企业环境需管理员安装；支持审批按钮 |
| **微信 / 企业微信** | 官方渠道插件（WeChat / WeCom） | 个人微信自动化有封号与合规风险，优先企业微信 |
| **飞书** | 飞书应用 + 事件订阅 | 支持动态 agent、卡片消息 |
| **iMessage** | 依赖 macOS + imsg 通道 | 只适合 macOS 宿主机 |
| **WhatsApp / Signal / Matrix / Teams** | 各自官方/插件通道 | 多数需要额外账号或服务端配置 |

完整清单见 [Channels 文档](https://docs.openclaw.ai/channels)。

---

## 配置模型

在 Control UI 的模型设置或配置文件中管理 provider：

- 支持 Anthropic、OpenAI、Google、DeepSeek、Qwen、MiniMax、Moonshot、OpenRouter、Ollama、LM Studio、vLLM 等（完整列表见 [Providers](https://docs.openclaw.ai/providers)）。
- 可配置**主模型 + fallback 链**：主模型限流/失败时自动切换。
- 官方推荐模型列表随版本更新（例如 2026-10 版本推荐里有 Claude Opus 5.5、GPT-6 系列、Gemini 4 Argon 等），**具体 model id 以当前版本 `/models` 或推荐列表为准**。

**建议：**

- 日常对话用便宜快的模型，复杂任务切强模型；
- 给 fallback 设置明确的顺序，避免"静默降智"；
- 把凭据放密钥/环境变量，不要写进会提交的配置文件。

---

## 常用命令（2026-11）

| 命令 | 作用 |
|------|------|
| `openclaw --version` | 查看版本 |
| `openclaw doctor` | 体检；`--fix` 尝试修复 |
| `openclaw gateway status` | 查看 Gateway 状态 |
| `openclaw gateway start/stop/restart` | 控制 Gateway |
| `openclaw onboard` | 重新走引导 |
| `openclaw update` | 更新（可切 stable/dev 通道） |
| `openclaw mcp ...` | 管理 MCP（见 [M9-03](./03-skills-mcp.md)） |

完整命令以 [CLI 参考](https://docs.openclaw.ai/cli) 为准。

---

## Control UI 与工作区

### Control UI

Gateway 启动后会提供 Control UI 地址（安装引导结束也会给出）。可以在里面：

- 直接和 AI 对话、看会话历史；
- 管理渠道、模型、审批；
- 配置 MCP、Skills、Plugins；
- 管理 Automations（定时/事件任务）；
- 查看用量与系统状态。

> 旧版用 `openclaw web` 打开 Web 控制台；2.0 后 Control UI 由 Gateway 统一提供，命令以当前版本文档为准。

### 工作区文件

```
<workspace>/
├── SOUL.md      ← 性格设定
├── USER.md      ← 关于你的信息
├── MEMORY.md    ← 长期记忆
├── AGENTS.md    ← 会话规则与工作流
└── memory/      ← 记忆/日记
```

这些文件仍然有效，但 2.0 后记忆也支持结构化存储与搜索，具体行为以当前版本文档为准。

---

## 排错

| 现象 | 可能原因 | 处理 |
|------|----------|------|
| `openclaw: command not found` | npm 全局 bin 不在 PATH | `npm prefix -g` 查看路径并加入 PATH |
| 引导卡住 / 配置无效 | 配置或存储有问题 | `openclaw doctor --fix` 后重试 |
| Gateway 起不来 | Node 版本不符、端口占用 | 升级 Node；看 Gateway 日志 |
| 渠道连不上 | Token 错误、网络限制、权限不足 | 用 `openclaw doctor` 与渠道文档逐项核对 |
| 模型 401/429 | 凭据错误或限流 | 检查 Key、配置 fallback |

---

## 历史沿革

- **2026-08（OpenClaw 2.0 / v2026.8.1）**：安装与引导重做；会话与转录迁入 SQLite；新增原生 App；npm 安装需要显式允许生命周期脚本。
- **~~已过时~~ 2026-03 版安装步骤（1.x 时代）**：

  ```bash
  # 旧版前置：Node.js 22 LTS（v22.16+）或 Node 24
  npm install -g openclaw@latest
  openclaw onboard --install-daemon
  ```

  旧版配置示例（模型 id 已过时，仅作对照）：

  ```json
  {
    "model": "anthropic/claude-sonnet-4-5",
    "fallbackModel": "openai/gpt-4o",
    "providers": {
      "anthropic": { "apiKey": "sk-ant-xxxxx" },
      "openai": { "apiKey": "sk-xxxxx" }
    }
  }
  ```

  旧版常用命令：

  ```bash
  openclaw gateway start / stop / status / restart
  openclaw channel
  openclaw config
  openclaw status
  openclaw web          # 旧版 Web 控制台
  ```

  旧版工作区默认 `~/clawd`，目录结构（SOUL.md / USER.md / MEMORY.md / AGENTS.md / memory/）在 2.x 仍大体沿用。

---

## 下一步

- [⭐️ M9-03 Skills 与 MCP 接入](./03-skills-mcp.md)
- [M8 MCP 精选](../08-mcp/README.md)
- [M10 AI Cloud Agent](../10-cloud-agent/README.md)
