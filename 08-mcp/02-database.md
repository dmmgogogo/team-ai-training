# ⭐️ M8-02 · 数据库类 MCP

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 让 AI 直接读懂数据库结构、写出精准 SQL。**重点：单库专用服务器多数已归档，2026 年更推荐"一个网关连多种库"或厂商官方远程 MCP。**

---

## 一句话结论

2026-11 的数据库 MCP 有两条主线：

1. **统一网关**：DBHub 用一个进程连 PostgreSQL / MySQL / MariaDB / SQL Server / Oracle / SQLite，默认只加载 2 个工具（约 1.4k token），并自带只读、行数限制、查询超时等护栏。
2. **官方远程 MCP**：Supabase、MongoDB、Redis 等由厂商维护，支持 OAuth / 远程托管 / 功能分组，权限模型更贴近产品本身。

单库社区包的黄金时代已经过去：`@modelcontextprotocol/server-postgres`、`server-sqlite`、`server-redis` 都已被归档。

---

## 2026-11 现状速查

| 方案 | 覆盖数据库 | 形态 | 维护方 | 关键点 |
|------|-----------|------|--------|--------|
| **DBHub** ⭐ | PostgreSQL / MySQL / MariaDB / SQL Server / Oracle / SQLite | 本地单进程 | bytebase | 默认 2 工具 1.4k token；只读模式、行限制、超时；SSH/SSL |
| **Supabase MCP** | Supabase（Postgres） | 远程托管 | Supabase | OAuth 登录；按项目/功能组授权；`read-only` 选项 |
| **Redis MCP** | Redis | 本地/自托管 | Redis 官方 | 读写查询与基础管理命令 |
| **MongoDB MCP** | MongoDB | 本地/官方 | MongoDB 官方 | 集合、文档、聚合；按官方文档配置 |
| **MySQL 社区方案** | MySQL / MariaDB | 本地 | 社区 | 无单一"官方"实现，建议直接用 DBHub |
| ~~PostgreSQL 参考服务器~~ | PostgreSQL | — | — | **已归档**，见历史沿革 |
| ~~SQLite 参考服务器~~ | SQLite | — | — | **已归档**，改用 DBHub |

---

## DBHub ⭐ 首选（多库统一）

**功能：** 极简数据库 MCP 网关，默认只暴露 `execute_sql` 和 `search_objects`，需要时再开 `explain_sql`、`health_check` 或自定义工具。

```bash
# 安装与启动方式以官方文档为准
npx @bytebase/dbhub --dsn "postgres://user:pass@localhost:5432/mydb"
```

**为什么推荐：**

- **省上下文**：默认 2 个工具约 1.4k token，官方对比中 MCP Toolbox 约 19.0k、Supabase MCP 约 19.3k（默认全量工具）。
- **多库一网关**：不用为每种数据库装一个 MCP。
- **有护栏**：只读模式、行数限制、查询超时，适合"让 AI 查生产只读库"。
- **被官方文档引用**：Claude Code 文档里"连接 PostgreSQL"的示例即使用 DBHub。

**典型用法：**

```
你：帮我查过去 7 天订单量最高的 10 个用户
AI：[search_objects 找表 → execute_sql 写查询 → 返回结果]

你：给 app_order 表生成 Go struct
AI：[读列定义与索引，生成字段类型正确的结构体]
```

来源：[dbhub.ai](https://dbhub.ai/)、[bytebase/dbhub](https://github.com/bytebase/dbhub)。

---

## Supabase MCP ⭐（Supabase 用户）

**功能：** 让 AI 直接操作 Supabase 项目：列表、迁移、SQL、日志、Edge Functions、类型生成等。

**远程安装（以 Claude Code 为例）：**

```bash
claude mcp add --scope project --transport http supabase \
  "https://mcp.supabase.com/mcp?features=docs,account,database,debugging,development,functions"
```

```json
{
  "mcpServers": {
    "supabase": {
      "type": "http",
      "url": "https://mcp.supabase.com/mcp?features=docs,account,database,debugging,development,functions"
    }
  }
}
```

**要点：**

- 通过浏览器 OAuth 授权，**不需要 PAT**。
- 建议**按项目限定**（project scoped）；不选项目时所有项目都可访问。
- 支持 **Read-only** 与**功能分组**（Database / Debugging / Development / Edge Functions / Account / Docs / Branching）。
- 官方明确提示：把 LLM 接到 Supabase 项目有安全风险，务必先读安全最佳实践。

来源：[Supabase MCP Server 文档](https://supabase.com/docs/guides/ai-tools/mcp)（更新于 2026-10-30）。

---

## Redis MCP

**功能：** 让 agent 读写 Redis、查询数据、做基础管理。

```json
{
  "mcpServers": {
    "redis": {
      "command": "uvx",
      "args": ["--from", "redis-mcp-server", "redis-mcp-server"],
      "env": {
        "REDIS_HOST": "127.0.0.1",
        "REDIS_PORT": "6379"
      }
    }
  }
}
```

> 包启动方式随版本变化较快，**以上仅为结构示例，命令以 Redis 官方安装页为准**。

**适合：** 查 Key 分布与内存占用、设计缓存 Key 规范与 TTL、排查异常 Key。

**注意：** Redis 默认无鉴权、命令能力强（`FLUSHALL`、`CONFIG`），生产实例务必用 ACL 限制到只读/限定命令的账号，或只连开发库。

来源：[Redis MCP 文档](https://redis.io/docs/latest/integrate/redis-mcp/)、[redis/mcp-redis](https://github.com/redis/mcp-redis)。

---

## MongoDB MCP

**功能：** 让 AI 查询集合、检查文档结构、辅助写聚合管道。

**建议：**

- 使用 MongoDB 官方 MCP Server（本地版 / 官方托管形态），版本与连接参数以 [MongoDB MCP Server 文档](https://www.mongodb.com/docs/mcp-server/) 为准。
- 给 AI 的账号只授予目标库的 `read` 角色；需要写时单独开一个受限库/测试库。
- 文档型数据库没有固定 schema，**先让 AI 采样文档再生成查询**，比直接猜字段可靠。

---

## 数据库 MCP 最佳实践

### 1. 只读账号（MySQL 示例）

```sql
CREATE USER 'ai_readonly'@'localhost' IDENTIFIED BY 'strong_password';
GRANT SELECT ON your_db.* TO 'ai_readonly'@'localhost';
FLUSH PRIVILEGES;
```

### 2. 环境分级

| 环境 | 建议 | 原因 |
|------|------|------|
| 开发 | 可读写 | 快速迭代、让 AI 直接调试 |
| 测试 | 只读或受限写 | 分析数据、复现问题 |
| 生产 | **默认不接**；必要时只读 + 行限制 + 超时 | 误操作代价高；合规与审计要求 |

### 3. 替代方案：导出 schema 给 AI

```bash
mysqldump --no-data -u root -p your_db > schema.sql
# 或 PostgreSQL
pg_dump --schema-only your_db > schema.sql
```

把 `schema.sql` 放进项目或 Claude Project，AI 一样能理解表结构，且**零数据库权限**。

### 4. 防护栏清单

- 只读模式 + 行数上限 + 查询超时（DBHub 自带）
- 禁止 `DROP`/`TRUNCATE`/`UPDATE` 无 `WHERE`（在数据库侧用权限或代理拦截）
- 慢查询与异常查询留痕；敏感表（用户、支付）单独授权或不暴露
- 不要把生产连接串写进 MCP 配置明文；用密钥管理/环境变量

---

## 历史沿革

- **2026-11**：DBHub 成为"多库统一"主流选择；Supabase MCP 按项目/功能组授权；Redis、MongoDB 官方 MCP 稳定。
- **2026 年**：MCP 官方参考服务器中的 PostgreSQL、SQLite、Redis 被归档；数据库类 MCP 从"一库一包"转向"网关 + 官方托管"。
- **~~已过时~~ 早期配置（2026-03 版课程）**：
  - `@modelcontextprotocol/server-postgres`：已归档，改用 DBHub / Supabase MCP
  - `@modelcontextprotocol/server-sqlite`：已归档，改用 DBHub
  - `mcp-server-redis`：改用 Redis 官方 `redis/mcp-redis`
  - `mcp-server-mysql`：社区包维护状态不一，建议改用 DBHub
  - `mcp-server-mongodb`：改用 MongoDB 官方 MCP Server

---

## 下一步

- [M8-03 效率工具类 MCP](./03-productivity.md)
- [⭐️ M8-04 通用工具类 MCP](./04-utilities.md)
- [⭐️ M8-01 开发工具类 MCP](./01-dev-tools.md)
