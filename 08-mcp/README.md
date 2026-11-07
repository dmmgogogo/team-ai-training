# M8 · MCP 精选

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 开发、数据库、效率、通用工具类 MCP 的**当前快照 + 历史沿革**。旧条目保留在文末，标注 `~~已过时~~`，方便对照生态变化。

---

## 一句话结论

截至 2026-11，MCP 已从"社区玩具"进入**协议重构 + 官方服务器接管**阶段：

- 协议最新版为 **2026-07-28**，核心变化是**无状态化**（去掉会话与 initialize 握手）、`server/discover`、订阅模型 `subscriptions/listen`、多轮请求 MRTR；Roots、Sampling、Logging 被标记为**弃用**。
- **官方 Registry 仍在预览**（preview），定位是"元数据中枢"，主要供下游市场/聚合器消费，不直接面向终端用户。
- 大量"官方参考服务器"（GitHub、GitLab、Postgres、Redis、Slack、Google Drive 等）已**归档**，改由各厂商维护的官方 MCP 接管。
- 安全成为主线：OAuth 2.1 + CIMD、token 不得透传、scope 最小化、本地 MCP 一键配置需显式同意。

> 协议原理请看 [M4-04 MCP 模型上下文协议](../04-principles/04-mcp.md)；项目级集成请看 [M6-03 MCP 项目集成](../06-ai-project-setup/03-mcp-integration.md)。

---

## 本模块文件

| 编号 | 文件 | 内容概述 |
|------|------|----------|
| [M8-01 ⭐️](./01-dev-tools.md) | **开发工具类 MCP** | GitHub / GitLab / Playwright / Docker 等开发向 MCP 的 2026-11 现状 |
| [M8-02 ⭐️](./02-database.md) | **数据库类 MCP** | DBHub、Supabase、Redis、MongoDB 等；只读与权限实践 |
| [M8-03](./03-productivity.md) | **效率工具类 MCP** | Slack、Notion、Google Workspace 官方 MCP 与抓取工具 |
| [M8-04 ⭐️](./04-utilities.md) | **通用工具类 MCP** | 搜索、记忆、推理、时间；Registry 与发现渠道；安装位置汇总 |

---

## 怎么读这一章

1. **先看每篇开头的"2026-11 现状"表**：确认某个 MCP 是否还在维护、是否改名、是否归档。
2. **再看配置示例**：示例只保证"结构正确"，包名与参数请以对应官方文档为准。
3. **最后看"历史沿革"**：里面是被替换掉的旧包名、旧配置、旧判断——排查"为什么我照着旧教程配不上"时最有用。

---

## 历史沿革

- **2026-11**：本模块按"当前快照 + 历史沿革"重写：MCP 规范更新到 2026-07-28，官方服务器接管主流条目。
- **2026-07-28**：MCP 规范无状态化重构（去除会话与 initialize 握手、新增 `server/discover` 与 MRTR）。
- **2026-03（课程初版）**：模块以"官方参考服务器 + 社区包"为主，GitHub / GitLab / PostgreSQL / Redis / Slack 等配置均来自 `@modelcontextprotocol/server-*`；这些包后来多数归档。

---

*← 返回 [课程总览](../README.md)*
