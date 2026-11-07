# ⭐️ M9-03 · OpenClaw Skills 与 MCP 接入

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> OpenClaw 的能力扩展有三层：**Skills（技能）→ Plugins（插件）→ MCP（外部工具）**，再叠加 **Automations（自动化）** 把工具串起来。2026 年这三层都经历了明显重构，旧教程里的命令和配置字段需要更新。

---

## 一句话结论

- Skills 的入口从"手写目录 + ClawHub 安装"升级为 **ClawHub + Skill Workshop**（提出、校验、应用、撤销一条链路）。
- MCP 配置从顶层 `mcpServers` 改为 **`mcp.servers`**，支持 Streamable HTTP / SSE / stdio、OAuth、工具过滤、审批与 `mcp doctor --probe`。
- 定时任务统一叫 **Automations**，并新增**事件触发**（MCP Events）；旧的 Heartbeat 机制已迁移。
- 还能反向把 OpenClaw 作为 MCP Server 暴露给别的客户端（`openclaw mcp serve`）。

---

## 一、Skills：给 AI 装上专属技能

### 什么是 Skill

Skill 本质是一组 **Markdown 指令 + 可选资源**，描述"某类任务该怎么做"。OpenClaw 在需要时加载对应 `SKILL.md`，让模型按你的规范执行。

典型 Skill：

| Skill | 用途 |
|-------|------|
| coding-agent | 把复杂编程任务委托给 Claude Code / Codex 等 |
| notion | 读写 Notion 页面与数据库 |
| weather | 查天气 |
| session-logs | 搜索、分析历史会话 |
| nano-pdf | 用自然语言编辑 PDF |

### 获取与安装：ClawHub

- **ClawHub** 是 OpenClaw 的技能市场：浏览、安装、发布、审计、遥测开关。
- 安装命令（以当前版本文档为准）：

```bash
clawhub install <skill-name>
clawhub list
```

- 企业/团队环境建议：先审 `SKILL.md` 内容，再决定是否安装；关注 ClawHub 的安全审计与来源信息。

### 自己写 Skill

在工作区创建技能目录：

```
<workspace>/skills/code-review/
└── SKILL.md
```

`SKILL.md` 示例：

```markdown
# Code Review Skill

当用户要求 code review 时：

1. 先问清楚：后端（Go）还是前端（Vue/Flutter）？
2. 按三个维度审查：
   - 🔴 安全（SQL 注入、权限缺失）
   - 🟡 性能（N+1、无效循环）
   - 🟢 规范（命名、错误处理）
3. 输出：问题描述 + 修复示例。

语气：直接、专业，不废话。
```

### Skill Workshop（2026 新增）

让 agent 参与技能的"改进闭环"：

- 提出修改建议；
- 自动校验（格式、可用性）；
- 应用修改并保留历史；
- 支持**撤销**（Review-wide undo），把技能恢复到修改前。

适合：把团队反复纠正的偏好，沉淀成可复用技能。

---

## 二、MCP：让 AI 操作你的工具

### 配置位置：`mcp.servers`

```json5
{
  mcp: {
    servers: {
      docs: {
        url: "https://mcp.example.com/mcp",
        transport: "streamable-http",
        enabled: true,
        toolFilter: {
          include: ["search", "read_*"]
        }
      }
    }
  }
}
```

支持三种传输：

| 传输 | 适用 | 写法 |
|------|------|------|
| **Streamable HTTP** | 远程 MCP（推荐） | `url` + `transport: "streamable-http"` |
| **SSE** | 旧版远程 MCP（兼容） | `url` + `transport: "sse"` |
| **stdio** | 本地进程 | `command` + `args` + `cwd` |

> 注意：一个服务器定义里不能同时出现 `url` 和 `command`；旧配置如果混写，升级时会告警，需要手动修。

### 三种添加方式

1. **Control UI**：Settings → MCP → Add server（选传输、填 URL/命令）。
2. **聊天里**：`+` → Plugins → Add MCP server…（需要管理员权限；可选本会话或全局）。
3. **CLI**：

```bash
# 本地 stdio
openclaw mcp add local-tools \
  --command node \
  --arg ./dist/mcp-server.js \
  --cwd /srv/openclaw-tools

# 远程 Streamable HTTP，只暴露部分工具
openclaw mcp add docs \
  --url https://mcp.example.com/mcp \
  --transport streamable-http \
  --include 'search,read_*'
```

### 验证与排错

```bash
openclaw mcp status --verbose     # 配置摘要
openclaw mcp doctor <name> --probe # 真正连一次，列出工具
openclaw mcp probe <name>          # 实时能力探测
openclaw mcp login <name>          # HTTP MCP 的 OAuth 登录
```

> 保存配置不等于能连通；`doctor --probe` 才是连通性证据。

### 审批与权限

- MCP 工具和内置工具走**同一套工具策略**，不会因为来自 MCP 就绕过策略。
- Codex MCP 工具的审批跟随会话权限姿态：全权限默认不询问；更严格的模式会对没有安全标注的工具发起审批。
- "Allow Always" 保存的是**针对具体 server + tool** 的授权（即使参数变化），并在下次会话/重启后生效。
- 可用 `openclaw mcp configure <server> --approval approve|prompt|auto` 覆盖单个服务器的审批模式。

### 反向：把 OpenClaw 当 MCP Server

```bash
openclaw mcp serve
```

把 OpenClaw 的渠道会话暴露给其他 MCP 客户端（注意权限与数据边界）。

### MCP Relay（可选插件）

默认关闭。开启后可以让 ChatGPT / Claude 连接你的 OpenClaw 会话，而不必把 Gateway 端口暴露到公网。注意：中继方能读到经过它的内容，只授权可信应用与可信中继。

---

## 三、Automations：定时 + 事件触发

### 定时任务（cron）

在 **Control UI → Automations** 中新建任务：填 cron 表达式 + 指令 + 投递渠道即可。

> CLI 侧旧版命令是 `openclaw cron add --schedule ... --message ...`；2.0 后统一到 Automations，**具体子命令以当前版本 `openclaw --help` / 官方文档为准**，不要照旧教程硬套。

常见用法：

```
每天早上 9 点 → 日程摘要
每周一 10 点 → 读 GitHub 一周 commits，生成周报
每 30 分钟（工作时间）→ 检查新 PR / Issue
```

### 事件触发（MCP Events，2026-10 新增）

- 支持的 MCP Server 上报事件时，直接触发自动化，不用等定时轮询。
- 需要**公网 HTTPS 回调**，只转发回调路由（如 `/plugins/mcp-events/callback/`），不要把整个 Gateway 暴露出去。
- 注意：收到事件 ≠ 任务完成；上游事件可能丢失。

### Heartbeat（旧机制）

早期用工作区 `HEARTBEAT.md` + 心跳轮询让 AI 周期性检查。该机制已迁移到 Automations，旧文件仅作历史参考（见文末）。

---

## 四、与 M7 / M8 的关系

```
Skills（M7 的思路）→ OpenClaw 技能库（ClawHub / Skill Workshop）
MCP（M8 的服务器）→ OpenClaw `mcp.servers`
Automations        → 定时/事件触发上面这些工具
Plugins            → 扩展渠道、模型、工具、UI
```

组合示例：

```
你：检查 GitHub 今天的新 Issue，整理到 Notion
AI：[GitHub MCP 读 Issue] + [Notion MCP 写入] + [Skill 格式化输出]
```

---

## 五、安全与治理

| 风险 | 建议 |
|------|------|
| 第三方 Skill / Plugin 供应链 | 先审内容再装；关注 ClawHub 审计；企业环境白名单 |
| MCP 工具越权 | 用 `toolFilter` 只暴露需要的工具；高风险工具设 `prompt` |
| OAuth 凭据泄露 | 用 OpenClaw 的密钥机制，不要把 token 写进配置明文 |
| 事件回调暴露 | 只暴露回调路由；校验签名/来源 |
| 多用户共享 | 用多用户模式或独立 Gateway；互不信任的用户必须隔离 |

---

## 历史沿革

- **2026-11**：`mcp.servers` + OAuth + 审批 + `mcp doctor`；Automations 统一；MCP Events 事件触发。
- **2026-10**：MCP Relay 插件；远程工作区 Files/Memory/Skills；Advisor 实验特性。
- **2026-08（2.0）**：Skills 全链路重构（ClawHub + Skill Workshop），插件可从 Control UI 管理。
- **~~已过时~~ 2026-03 版配置（1.x 时代）**：

  顶层 `mcpServers` 写法：

  ```json
  {
    "model": "anthropic/claude-sonnet-4-5",
    "mcpServers": {
      "filesystem": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/你的用户名/Projects"]
      },
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxx" }
      }
    }
  }
  ```

  旧版技能安装与定时任务：

  ```bash
  clawhub install weather
  clawhub list
  openclaw cron add --schedule "0 9 * * 1-5" --message "..."
  ```

  旧版 `HEARTBEAT.md`：

  ```markdown
  # HEARTBEAT.md
  - 每天早上 9 点：提醒今日日程
  - 有重要邮件：立即通知
  - 没有要紧事：保持安静（HEARTBEAT_OK）
  ```

  ⚠️ 以上写法对应 1.x；升级到 2.x 后请迁移到 `mcp.servers` 与 Automations，旧的 `@modelcontextprotocol/server-github` 也已归档（见 [M8-01](../08-mcp/01-dev-tools.md)）。

---

## 更多资源

- 官方文档：[docs.openclaw.ai](https://docs.openclaw.ai)
- MCP 接入：[Connect MCP servers](https://docs.openclaw.ai/tools/mcp)
- Skills：[Skills](https://docs.openclaw.ai/tools/skills)
- 技能市场：[ClawHub](https://docs.openclaw.ai/clawhub)
- 自动化：[Automations](https://docs.openclaw.ai/automation/cron-jobs)
- 代码仓库：[github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)

---

## 下一步

- [M8 MCP 精选](../08-mcp/README.md)
- [M7 Skills 精选](../07-skills/README.md)
- [M10 AI Cloud Agent](../10-cloud-agent/README.md)
- [⭐️ M9-01 什么是 OpenClaw](./01-intro.md)
