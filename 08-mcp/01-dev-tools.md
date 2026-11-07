# ⭐️ M8-01 · 开发工具类 MCP

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 开发者最高频使用的 MCP Server：代码仓库、浏览器、容器、本地终端。**重点：官方实现已经接管，旧社区包多数归档，别再照旧教程抄包名。**

---

## 一句话结论

2026-11 的开发工具类 MCP 有三个明显趋势：

1. **厂商官方化**：GitHub、GitLab 都推出了官方 MCP Server（GitLab 于 2026-10-15 正式 GA），旧的 `@modelcontextprotocol/server-*` 已被归档。
2. **远程托管优先**：GitHub 官方远程服务器 `https://api.githubcopilot.com/mcp/` 支持 OAuth，不必本地起进程。
3. **工具集（toolset）+ 只读模式**：为了省上下文、降风险，官方服务器普遍支持按工具组裁剪、只读开关。

---

## 2026-11 现状速查

| MCP | 当前形态 | 维护方 | 关键变化 | 建议 |
|-----|----------|--------|----------|------|
| **GitHub MCP** | 官方远程 + 本地（Go/Docker） | GitHub | 远程地址 `api.githubcopilot.com/mcp/`；OAuth 或 PAT；`--toolsets`/`--read-only` | ⭐ 首选远程 + OAuth |
| **GitLab MCP** | 官方内建（SaaS/自建/Dedicated） | GitLab | 2026-10-15 GA；支持工具集选择；GitLab.com 有速率限制（Free 60 次/分，Premium/Ultimate 600 次/分） | 企业 GitLab 用户首选 |
| **Playwright MCP** | `@playwright/mcp`（微软官方） | Microsoft | 基于无障碍树（accessibility tree），不依赖视觉模型；coding agent 场景推荐 CLI+Skills 替代 | ⭐ 前端调试仍推荐 |
| **Docker MCP Gateway** | Docker MCP Catalog & Toolkit | Docker | 用网关统一接入 MCP Catalog 中的服务器，减少逐个配置 | 多 MCP 时值得上 |
| **Filesystem MCP** | 官方参考实现 | MCP 项目组 | 仍在参考服务器列表；路径白名单是核心安全边界 | ⭐ 基础必备 |
| **Desktop Commander** | 社区项目 | wonderwhy-er | 能力大（shell/文件/进程），风险也大 | 只在可信环境开 |

> 官方参考服务器清单与归档列表：[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)。

---

## GitHub MCP ⭐ 首选

**功能：** 让 AI 直接读仓库、查 Issue/PR、看 Actions、审代码、建分支/PR。

### 推荐配置：远程 + OAuth（最省事）

```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}
```

- 首次使用走浏览器 OAuth，不需要自己建 PAT。
- 如果宿主不支持 OAuth，可改用 PAT：

```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${input:github_mcp_pat}"
      }
    }
  }
}
```

### 本地版（Docker）

```json
{
  "mcp": {
    "servers": {
      "github": {
        "command": "docker",
        "args": [
          "run", "-i", "--rm",
          "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
          "ghcr.io/github/github-mcp-server"
        ],
        "env": {
          "GITHUB_PERSONAL_ACCESS_TOKEN": "${input:github_token}"
        }
      }
    }
  }
}
```

### 省上下文：只开需要的工具集

```bash
github-mcp-server --toolsets repos,issues,pull_requests
# 或
GITHUB_TOOLSETS="repos,issues,pull_requests" ./github-mcp-server
```

只读场景加 `--read-only`：写工具会被跳过，即使你在 `--tools` 里显式点名。

**典型用法：**

```
你：帮我看一下 #42 这个 Issue，给出修复方案
AI：[读取 Issue 正文与相关代码，给出方案]

你：最近 3 次 commit 有没有引入回归风险？
AI：[读 commit diff + 相关测试，给出风险评估]
```

来源：[github/github-mcp-server](https://github.com/github/github-mcp-server)。

---

## GitLab MCP

**功能：** 连接 GitLab.com、自建 GitLab、GitLab Dedicated；访问仓库、MR、流水线，并能调用 GitLab Duo Agent Platform 的 agent/flow。

2026-11 状态：

- GitLab 19.5（2026-10-15）宣布 **GitLab MCP server 正式 GA**，工具目录比早期版本大幅扩展。
- 支持**工具集选择**，避免把全部工具塞进上下文。
- GitLab.com 上按用户限流：Free 60 请求/分钟，Premium/Ultimate 600 请求/分钟；每个重连与重试都计数。
- 新增 `get_artifact_file`（直接读 CI 产物中的单个文件）、`list_groups`、`start_duo_session` 等工具。

**配置思路：** 在 GitLab 侧启用 MCP server，然后在客户端按官方文档填入服务器 URL / 访问令牌；不同版本与部署形态（SaaS / Self-Managed / Dedicated）参数不同，**以 GitLab 官方文档为准**。

来源：[GitLab 19.5 release notes](https://docs.gitlab.com/releases/19/gitlab-19-5-released/)、[GitLab MCP server 文档](https://docs.gitlab.com/user/model_context_protocol/mcp_server/)。

---

## Playwright MCP ⭐ 强推

**功能：** 让 AI 用真实浏览器操作页面、读无障碍树、跑前端流程。

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

**能做什么：**

- 读取页面无障碍快照（比截图更省 token，且不依赖视觉模型）
- 点击、输入、选择、等待、上传文件
- 生成 locator、做基础断言（`--caps=testing`）
- 录制操作、生成 Playwright 代码

**注意：**

- 官方明确提示：**coding agent 场景优先考虑 Playwright CLI + Skills**，因为 CLI 调用比常驻 MCP 工具 schema 更省 token；MCP 更适合需要持续浏览器状态、反复探索的场景。
- `browser_run_code_unsafe` 可在服务器进程里执行任意 JavaScript，**等价于 RCE**，生产/敏感环境不要开。
- 用 `--allowed-hosts`、`--allowed-origins`、`--isolated` 收紧边界。

来源：[microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)。

---

## Docker MCP Gateway

**功能：** 用 Docker 官方的 MCP Catalog + Toolkit + Gateway，把多个 MCP Server 统一挂到一个网关后面，减少 N 个客户端 × N 个服务器的配置爆炸。

适用场景：

- 团队里多人用不同客户端，但想共享同一套 MCP 目录与策略
- 需要集中管理密钥、网络出口与工具白名单
- 本机 MCP 太多，启动慢、端口乱

**建议：** 先用官方 MCP Catalog 找服务器，再用 Gateway 统一接入；具体命令与版本以 [Docker MCP Gateway 文档](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/) 为准。

---

## Filesystem MCP ⭐ 必装

**功能：** 读写本地文件，最基础也最常用的 MCP。

```json
{
  "filesystem": {
    "command": "npx",
    "args": [
      "-y",
      "@modelcontextprotocol/server-filesystem",
      "/Users/你的用户名/Projects"
    ]
  }
}
```

**说明：** 路径参数就是安全边界——只把需要的目录传进去，不要图省事传 `$HOME` 或 `/`。

---

## Desktop Commander MCP

**功能：** 执行 shell、读写文件、管理进程。

⚠️ **安全提示：** 这是权限最大的 MCP 之一，等于把终端交给模型。只在可信项目、可信模型、可信网络下使用；不要把带生产凭据的目录暴露给它。

---

## 安全与权限提醒（开发类 MCP 通用）

| 风险 | 具体表现 | 建议 |
|------|----------|------|
| 令牌过大 | PAT 给了 `repo` + `admin` 全权限 | 用细粒度 PAT / GitHub App；只读场景用 `--read-only` |
| 一键配置投毒 | 点一个链接就往配置里写 `npx 恶意包 && curl ...` | 只从官方仓库复制配置；客户端应展示完整命令再确认 |
| 工具投毒 | 服务器描述里藏指令，诱导模型调用危险工具 | 只装可信来源；开启工具白名单/审批 |
| 上下文膨胀 | 一次挂 10 个 MCP，几十个工具 | 按任务挂载，优先 `--toolsets`/工具过滤 |
| 本地提权 | 浏览器 MCP 可执行任意 JS；终端 MCP 可跑任意命令 | 沙箱、独立目录、最小权限账号 |

> 协议级安全要求见 [MCP Security Best Practices（2026-07-28）](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)。

---

## 历史沿革

- **2026-11**：GitLab MCP server 于 GitLab 19.5 GA（2026-10-15）；GitHub 官方 MCP 推荐远程 + OAuth；Playwright MCP 明确"coding agent 优先 CLI+Skills"。
- **2026-07-28**：MCP 规范大改（无状态、`server/discover`、MRTR、Roots/Sampling/Logging 弃用），旧版服务器需要适配或继续走兼容路径。
- **2025 年下半年—2026 年**：官方参考服务器批量归档：GitHub、GitLab、Google Drive、PostgreSQL、Redis、Slack、SQLite、Puppeteer、Sentry 等迁入 [servers-archived](https://github.com/modelcontextprotocol/servers-archived)，由厂商官方实现接替。
- **~~已过时~~ 早期配置（2026-03 版课程）**：
  - `@modelcontextprotocol/server-github`（已归档）→ 改用 `github/github-mcp-server` 或远程 `api.githubcopilot.com/mcp/`
  - `@modelcontextprotocol/server-gitlab`（已归档）→ 改用 GitLab 官方 MCP
  - `@executeautomation/playwright-mcp-server`（社区包）→ 改用微软官方 `@playwright/mcp`
  - `@docker/mcp-server`（旧入口）→ 改用 Docker MCP Catalog/Toolkit + MCP Gateway

---

## 下一步

- [⭐️ M8-02 数据库类 MCP](./02-database.md)
- [M8-03 效率工具类 MCP](./03-productivity.md)
- [⭐️ M8-04 通用工具类 MCP](./04-utilities.md)
