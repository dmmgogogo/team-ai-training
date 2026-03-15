# ⭐️ M8-02 · 数据库类 MCP

> 让 AI 直接读懂你的数据库结构，写出精准的 SQL，不再靠猜。

---

## MySQL MCP ⭐ 必装（Go + Beego 项目）

**功能：** 连接 MySQL，AI 直接查询和理解表结构

```json
{
  "mysql": {
    "command": "npx",
    "args": ["-y", "mcp-server-mysql"],
    "env": {
      "MYSQL_HOST": "127.0.0.1",
      "MYSQL_PORT": "3306",
      "MYSQL_USER": "readonly_user",
      "MYSQL_PASSWORD": "your_password",
      "MYSQL_DATABASE": "your_db"
    }
  }
}
```

⚠️ **安全建议：** 创建只读账号专门给 AI 使用，不要给 root 权限

**能做什么：**
- 自动读取表结构，生成对应的 Go struct
- 写出准确的 SQL 查询语句
- 分析慢查询，建议索引
- 生成 GORM / Beego ORM 代码

**典型用法：**
```
你：帮我查一下过去 7 天订单量最高的 10 个用户
AI：[读取表结构，直接写出准确的 SQL]

你：帮我写 app_order 表的 Beego Model 定义
AI：[读取表结构，生成完整 Model 代码，字段类型全对]
```

---

## PostgreSQL MCP

```json
{
  "postgres": {
    "command": "npx",
    "args": [
      "-y",
      "@modelcontextprotocol/server-postgres",
      "postgresql://readonly:password@localhost/mydb"
    ]
  }
}
```

功能与 MySQL MCP 类似，适合使用 PostgreSQL 的项目。

---

## Redis MCP

**功能：** 查询和管理 Redis 数据

```json
{
  "redis": {
    "command": "npx",
    "args": ["-y", "mcp-server-redis"],
    "env": {
      "REDIS_URL": "redis://localhost:6379"
    }
  }
}
```

**能做什么：**
- 查看 Key 列表和数据
- 分析内存占用
- 帮你设计缓存策略
- 发现异常 Key（TTL 过长/数据量异常）

**典型用法：**
```
你：我的 Redis 内存快满了，帮我看看哪些 Key 占用最多
AI：[分析 Key 分布，找出问题，给出清理方案]

你：帮我设计用户登录 Token 的缓存结构
AI：[根据业务需求，给出 Key 命名规范和 TTL 策略]
```

---

## SQLite MCP

**功能：** 本地 SQLite 数据库操作

```json
{
  "sqlite": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-sqlite", "--db-path", "/path/to/db.sqlite"]
  }
}
```

**适合场景：**
- 本地开发时的测试数据库
- Flutter App 的本地存储（sqflite）
- 数据分析原型

---

## MongoDB MCP

```json
{
  "mongodb": {
    "command": "npx",
    "args": ["-y", "mcp-server-mongodb"],
    "env": {
      "MONGODB_URI": "mongodb://localhost:27017/mydb"
    }
  }
}
```

**适合场景：** 文档型数据、灵活 Schema 的项目

---

## 数据库 MCP 最佳实践

### 只读账号配置（MySQL 示例）

```sql
-- 创建只读账号给 AI 使用
CREATE USER 'ai_readonly'@'localhost' IDENTIFIED BY 'strong_password';
GRANT SELECT ON your_db.* TO 'ai_readonly'@'localhost';
FLUSH PRIVILEGES;
```

### 生产 vs 开发环境

```
开发环境：可以连接，AI 帮你写代码和调试
测试环境：可以连接，AI 帮你分析数据
生产环境：⚠️ 不建议连接，用表结构导出文件替代
```

### 替代方案：导出表结构给 AI

```bash
# 导出表结构（不含数据）
mysqldump --no-data -u root -p your_db > schema.sql

# 上传 schema.sql 到 Claude Project 或 @引用
```

---

## 下一步

- [M8-03 效率工具类 MCP](./03-productivity.md)
- [M8-04 通用工具类 MCP](./04-utilities.md)
