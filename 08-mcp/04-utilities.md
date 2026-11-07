# ⭐️ M8-04 · 通用工具类 MCP

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 搜索、记忆、推理、时间——这些 MCP 提升的是 AI 的**基础能力**而不是某个垂直场景。此外本篇还负责回答两个问题：**去哪找 MCP**、**装在哪**。

---

## 一句话结论

- **Brave Search MCP** 已由 Brave 官方接手（`@brave/brave-search-mcp-server`），官方参考实现归档。
- **Memory / Sequential Thinking / Time / Fetch / Filesystem / Git** 仍是 MCP 项目组维护的官方参考实现，定位是"教学与参考"，不是生产级产品。
- 找 MCP 的第一站是 **官方 Registry**（仍在 preview），但对终端用户更实用的是下游市场（mcp.so、awesome-mcp-servers、glama 等）。
- 安装位置因客户端而异；2026 年新增/固化了几种标准写法（VS Code 的 `.vscode/mcp.json`、Claude Code 的 `claude mcp add`、Codex 的 `config.toml`）。

---

## 2026-11 现状速查

| MCP | 状态 | 维护方 | 说明 |
|-----|------|--------|------|
| **Brave Search** | 官方接管 | Brave | 包名改为 `@brave/brave-search-mcp-server`；需 API Key |
| **Memory** | 官方参考实现 | MCP 项目组 | 知识图谱式持久记忆，适合演示与轻量使用 |
| **Sequential Thinking** | 官方参考实现 | MCP 项目组 | 强制分步思考；对推理型任务有帮助，但不是万能 |
| **Time** | 官方参考实现 | MCP 项目组 | 提供时区换算与当前时间 |
| **Fetch** | 官方参考实现 | MCP 项目组 | 网页抓取（见 [M8-03](./03-productivity.md)） |
| **Git** | 官方参考实现 | MCP 项目组 | 读/搜/改本地 Git 仓库 |
| ~~`@modelcontextprotocol/server-brave-search`~~ | — | — | **已归档**，改用 Brave 官方包 |

> 官方参考服务器列表与归档说明：[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)。

---

## Brave Search MCP ⭐ 常用

**功能：** 给 AI 一个联网搜索入口，补足知识截止日期。

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@brave/brave-search-mcp-server"],
      "env": {
        "BRAVE_API_KEY": "your_brave_api_key"
      }
    }
  }
}
```

**获取 API Key：** [brave.com/search/api](https://brave.com/search/api/)（免费额度以官网为准）。

**能做什么：**

- 查最新版本、发布说明、changelog
- 查报错与社区讨论
- 做竞品/技术方案调研

**典型用法：**

```
你：Go 最新稳定版有什么变化？
AI：[搜索官方发布说明 → 给出版本与要点，而不是凭记忆回答]
```

⚠️ **注意：** 搜索结果同样是不可信内容，可能被 SEO 投毒或包含注入指令。涉及"按网页指示执行操作"时必须人工确认。

来源：[brave/brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server)。

---

## Memory MCP ⭐ 推荐

**功能：** 给 AI 一个可持久化的"记忆本"（知识图谱）。

```json
{
  "memory": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-memory"]
  }
}
```

**能做什么：**

- 记住你的偏好、项目决策、术语表
- 跨会话保持上下文
- 构建实体-关系型知识图谱

**典型用法：**

```
你：记住，我们项目主键统一用 bigint，不用 int
AI：[写入记忆]

[下次会话]
你：帮我设计用户表
AI：[自动使用 bigint 主键]
```

**说明：** 这是参考实现，数据一般落在本地文件；团队共享记忆请用数据库/知识库方案，别把多人记忆混在一个文件里。

---

## Sequential Thinking MCP

**功能：** 让模型把复杂问题拆成显式的思考步骤。

```json
{
  "sequential-thinking": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
  }
}
```

**适合：** 架构设计、多步骤排障、需要"先列假设再验证"的问题。

**不适合：** 简单问答——强行分步只会增加 token 与时延。

> 2026-07-28 规范把 Sampling、Roots、Logging 标记为弃用，但 Sequential Thinking 本身不依赖这些特性，仍可正常使用。

---

## Time MCP

**功能：** 提供当前时间与时区换算。

```json
{
  "time": {
    "command": "uvx",
    "args": ["mcp-server-time"]
  }
}
```

**场景：** 生成带日期的日报/周报、计算跨时区会议时间、给版本号打日期。

**注意：** 很多客户端已经把"当前时间"注入系统提示，先确认是否真的需要再装。

---

## 发现更多 MCP

| 资源 | 说明 |
|------|------|
| [registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io) | 官方 Registry（**preview**），按命名空间校验来源 |
| [modelcontextprotocol.io/registry/about](https://modelcontextprotocol.io/registry/about) | Registry 的定位、server.json 格式与信任模型 |
| [mcp.so](https://mcp.so) | 社区 MCP 搜索 |
| [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | GitHub 精选列表 |
| [glama.ai/mcp/servers](https://glama.ai/mcp/servers) | 评分与使用量排行 |
| [Smithery](https://smithery.ai) | 带托管能力的 MCP 目录 |

### 关于官方 Registry（2026-11）

- 状态：**preview**，官方明确说 GA 前可能有破坏性变更或数据重置。
- 定位：**元数据仓库**，不是代码仓库；指向 npm/PyPI/Docker 等包。
- 信任：用反向 DNS 命名空间 + GitHub/DNS 验证来源；**不做代码安全扫描**，扫描交给包仓库与下游市场。
- 不支持私有服务器；私有场景建议自建 registry。
- 官方建议：终端 host 应用不要直接消费 Registry，而应消费下游市场（它们实现同一套 OpenAPI）。

来源：[MCP Registry](https://modelcontextprotocol.io/registry/about)。

---

## MCP 安装位置汇总（2026-11）

| 客户端 | 配置位置 / 命令 |
|--------|----------------|
| Claude Desktop | `claude_desktop_config.json`（macOS：`~/Library/Application Support/Claude/`） |
| Claude Code | `claude mcp add <name> ...`，或项目内 `.mcp.json` |
| Cursor | Settings → MCP → Add new MCP Server |
| VS Code (Copilot) | 项目级 `.vscode/mcp.json`，或命令面板 `MCP: Add Server` |
| Codex | `~/.codex/config.toml` 的 `[mcp_servers.<name>]`，或 `codex mcp add` |
| OpenClaw | 配置 `mcp.servers`（见 [M9-03](../09-openclaw/03-skills-mcp.md)） |

> 各客户端字段名不完全一致（`mcpServers` / `servers` / `mcp.servers`），复制配置时先看目标客户端的文档。

---

## 推荐组合方案

### 开发者日常最小配置

```json
{
  "mcpServers": {
    "filesystem": { "...": "只挂项目目录" },
    "github": { "...": "远程 + OAuth" },
    "brave-search": { "...": "搜索" },
    "dbhub": { "...": "只读连开发库" }
  }
}
```

### 全栈开发完整配置

```json
{
  "mcpServers": {
    "filesystem": { "...": "项目目录" },
    "github": { "...": "远程 + 只读工具集" },
    "playwright": { "...": "@playwright/mcp" },
    "dbhub": { "...": "多库网关" },
    "redis": { "...": "只连开发实例" },
    "fetch": { "...": "读文档" },
    "memory": { "...": "项目约定记忆" }
  }
}
```

**别一次全开**：工具越多，模型选错工具、上下文被 schema 占满的概率越高。按任务"临时挂载"更稳。

---

## 安全提醒（通用类 MCP）

| 风险 | 说明 | 建议 |
|------|------|------|
| 一键配置注入 | 恶意配置在启动命令里夹带 `curl`/`rm` | 客户端必须展示完整命令并二次确认；自己只从官方仓库复制 |
| 工具投毒 | 服务器在工具描述里藏指令 | 只装可信来源；用工具白名单/审批；关注 Registry 命名空间 |
| 供应链 | npm 包被劫持、仿冒包名 | 核对官方仓库链接；优先官方 scope（`@brave/`、`@playwright/`） |
| 数据外泄 | 搜索/抓取把内部信息带出去 | 敏感数据脱敏；限制可访问域名 |
| 权限过大 | 本地 MCP 以你的用户权限运行 | 沙箱、独立目录、最小权限账号 |

协议级要求见 [MCP Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) 与 [Authorization 规范](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)。

---

## 历史沿革

- **2026-11**：Brave 官方包取代归档的参考实现；官方 Registry 仍处 preview；客户端配置格式趋于稳定。
- **2026-07-28**：MCP 规范重构（无状态化、MRTR、`subscriptions/listen`），`server/discover` 成为服务器必须实现的 RPC；Roots / Sampling / Logging 进入弃用期（至少 12 个月）。
- **2026 年**：官方参考服务器批量归档，Registry 从"目录页"升级为"元数据中枢"。
- **~~已过时~~ 早期配置（2026-03 版课程）**：
  - `@modelcontextprotocol/server-brave-search` → 改用 `@brave/brave-search-mcp-server`
  - 发现入口 `modelcontextprotocol.io/servers` → 改为 Registry / 下游市场
  - 早期 Memory / Sequential Thinking 的 `npx -y @modelcontextprotocol/server-*` 写法仍可用，但请核对包是否已迁移

---

## 下一步

- [⭐️ M8-01 开发工具类 MCP](./01-dev-tools.md)
- [⭐️ M8-02 数据库类 MCP](./02-database.md)
- [M8-03 效率工具类 MCP](./03-productivity.md)
