# M5-08 · Claude 正确配置与高效使用

> Claude 是开发者首选 AI，代码能力行业顶尖。但很多人只用了聊天功能。

---

## 账号与计划

**入口：** [claude.ai](https://claude.ai)

| 计划 | 价格 | 核心权益 |
|------|------|---------|
| **Free** | 免费 | Claude Sonnet 有限次，基础功能 |
| **Pro** | $20/月 | Sonnet 无限 + Opus 访问 + Projects + 更多上传 |
| **Team** | $25/人/月 | Pro 功能 + 团队管理 + 数据不训练 |
| **Enterprise** | 按需 | 私有化部署、SSO、合规 |

> 💡 **开发者强烈推荐 Pro**：Projects 功能可以存储项目上下文，Claude 是代码任务首选。

---

## 核心配置：Projects（项目记忆）

**Claude 最重要的功能**，让它记住你的项目上下文。

**位置：** 左侧边栏 → Projects → 新建项目

### 配置步骤

**第一步：创建项目并设置指令**

```
项目名：后端服务开发

项目指令：
你是我们团队的高级后端工程师助手。

【项目信息】
- 这是一个 B2B SaaS 平台，用于企业人力资源管理
- 后端：Python 3.11 + FastAPI + SQLAlchemy 2.0
- 数据库：PostgreSQL 15，使用 Alembic 做迁移
- 测试：pytest + factory-boy
- 部署：Docker + AWS ECS

【代码规范】
- 所有函数必须有 type hints 和 docstring
- 使用 async/await 处理所有 IO 操作
- 错误统一使用自定义异常类（见 src/exceptions.py）
- 日志使用 structlog，格式化为 JSON

【回答要求】
- 代码示例使用 Python，且符合上述规范
- 给出代码时，同时给出使用示例
- 发现潜在的安全或性能问题时主动指出
- 用中文回答
```

**第二步：上传项目文档**

可以上传这些文件让 Claude 更了解你的项目：
```
✅ 推荐上传：
- README.md（项目说明）
- 数据库 Schema（DDL 文件）
- API 设计文档
- 编码规范文档

❌ 不要上传：
- 含真实用户数据的文件
- 包含密钥的配置文件
- 超过 10MB 的大文件
```

---

## 模型选择

Claude 系列各有侧重，对话框左下角可切换：

| 模型 | 适合场景 | 速度 | 成本 |
|------|---------|------|------|
| **Claude Sonnet 4.6** | 日常编码、文档、分析 | 快 | 中 |
| **Claude Opus 4.6** | 复杂架构、深度推理、重要决策 | 慢 | 高 |
| **Claude Haiku** | 快速简单任务、高频使用 | 极快 | 低 |

**选择原则：**
- 80% 的任务用 Sonnet 就够了
- 遇到 Sonnet 给出错误或不完整答案，换 Opus 试试
- 批量简单任务（如格式转换）用 Haiku

---

## Extended Thinking（扩展思考）

Claude 3.7 Sonnet 和 Opus 系列支持"慢思考"模式：

**开启方式：** 对话框右下角 → 思考模式（灯泡图标）

**适合场景：**
```
✅ 复杂 Bug 的根本原因分析
✅ 算法设计（动态规划、图算法）
✅ 架构方案比较和决策
✅ 数学推导和证明
✅ 安全漏洞分析

❌ 不需要思考模式：
日常编码、文档生成、简单问答
```

**使用示例：**
```
开启思考模式，然后问：

"我们的系统在高并发下偶尔出现数据不一致：
一个用户同时发起两次下单请求，库存被扣减两次。
数据库用的 PostgreSQL，应用层是无状态的 FastAPI。
请深入分析根本原因，并给出三种解决方案，
对比各方案的优缺点和适用场景。"
```

---

## Artifacts（输出物）

Claude 会把长代码、文档、图表等放在右侧 **Artifacts** 面板：

**使用技巧：**
```
代码类 Artifact：
- 右上角可以一键复制
- 可以继续对话修改，会实时更新
- 支持"预览"按钮（HTML/CSS 可以直接看效果）

文档类 Artifact：
- 可以导出为 Markdown
- 继续追问会追加内容，不是重新生成

网页 Artifact：
- 可以直接在右侧看网页效果
- 适合快速验证 UI 原型
```

---

## 文件上传技巧

Claude Pro 支持上传多种文件，用于分析：

| 文件类型 | 使用场景 |
|---------|---------|
| **PDF** | 分析技术文档、论文、合同 |
| **代码文件** | 代码审查、解释、重构 |
| **图片** | 分析 UI 设计稿、架构图、截图报错 |
| **CSV/数据** | 数据分析和可视化（配合代码生成）|

**高效用法：**
```
上传一张系统架构图（截图）→
"根据这个架构图，分析可能的性能瓶颈，并给出优化建议"

上传一份 API 文档（PDF）→
"根据这个文档，帮我写所有接口的 Python SDK，包含错误处理"

上传报错截图 →
"这个错误是什么原因，如何修复？"
```

---

## Claude API 配置（开发者）

如果要在代码中调用 Claude，通过 [console.anthropic.com](https://console.anthropic.com) 获取 API Key。

**基础调用示例：**

```python
import anthropic

client = anthropic.Anthropic(api_key="your_api_key")

# 普通对话
message = client.messages.create(
    model="claude-sonnet-4-5-20251022",
    max_tokens=1024,
    system="你是一个 Python 专家，代码示例要包含类型注解和错误处理",
    messages=[
        {"role": "user", "content": "写一个异步的 Redis 缓存装饰器"}
    ]
)
print(message.content[0].text)
```

**带工具调用：**

```python
tools = [
    {
        "name": "get_weather",
        "description": "获取指定城市的当前天气",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "城市名"}
            },
            "required": ["city"]
        }
    }
]

response = client.messages.create(
    model="claude-sonnet-4-5-20251022",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "上海今天天气怎么样？"}]
)
```

**流式输出（适合长文本）：**

```python
with client.messages.stream(
    model="claude-sonnet-4-5-20251022",
    max_tokens=2048,
    messages=[{"role": "user", "content": "写一篇技术文章..."}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

---

## Claude Desktop + MCP 配置

**下载：** [anthropic.com/claude](https://www.anthropic.com/claude)（下载桌面版）

配置文件位置：
- Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

**推荐 MCP 配置：**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", 
               "/Users/你的用户名/Projects"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_URL": "postgresql://user:pass@localhost/devdb"
      }
    }
  }
}
```

配置后 Claude Desktop 可以：
- 读写你项目目录的文件
- 操作 GitHub（查 PR、创建 Issue）
- 查询本地开发数据库

**MCP 工具市场：** [modelcontextprotocol.io/servers](https://modelcontextprotocol.io/servers)

---

## 高效使用场景示例

### 场景一：代码审查

```
上传代码文件，然后：

"对这个代码文件做全面审查，按优先级列出问题：
1. 安全漏洞（高）
2. 潜在 Bug（高）
3. 性能问题（中）
4. 代码规范问题（低）

每个问题给出：位置、问题说明、修复建议"
```

### 场景二：技术选型

```
"我需要为系统添加消息队列，候选方案：Kafka、RabbitMQ、Redis Pub/Sub。
我们的场景：日均消息 100 万条，需要消息持久化，团队 5 人，运维能力一般。
请帮我做技术选型决策，给出推荐和理由。"
```

### 场景三：文档生成

```
上传代码文件 →

"根据这个模块的代码，生成完整的 API 文档，包含：
- 接口说明
- 请求/响应格式（JSON Schema）
- 错误码说明
- 使用示例
输出为 Markdown 格式"
```

---

## 注意事项

| 场景 | 注意 |
|------|------|
| 生产数据 | 脱敏后再上传，不要有真实用户信息 |
| API Key | 不要粘贴到对话，Claude 不会索要 |
| 长上下文 | 对话太长时，开新对话并附上背景摘要 |
| 重要决策 | 用 Opus 或开启思考模式，结果要人工验证 |

---

## 参考链接

- 官方文档：[docs.anthropic.com](https://docs.anthropic.com)
- Prompt 库：[anthropic.com/prompt-library](https://www.anthropic.com/prompt-library)
- MCP 工具：[modelcontextprotocol.io/servers](https://modelcontextprotocol.io/servers)
- API Console：[console.anthropic.com](https://console.anthropic.com)
