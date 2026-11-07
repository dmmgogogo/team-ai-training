# M5-08 · Claude 正确配置与高效使用

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02
>
> Claude 是开发者首选 AI 之一。2026 年的 Claude 已经不只是聊天：Projects、Cowork、Skills、Plugins、Claude Code、Claude in Chrome 都是正式入口。

---

## 账号与计划（2026-11）

**入口：** [claude.ai](https://claude.ai)

| 计划 | 价格（2026-11） | 核心权益 |
|------|----------------|---------|
| **Free** | $0 | 基础对话、联网、文件、Artifacts、记忆 |
| **Pro** | $20/月（年付 $17/月，一次性 $200） | 更多用量、Projects、Claude Code、Claude Science、更多模型 |
| **Max** | $100/月 | 5× Pro 用量；Fable 最多用到周额度一半；$100 API credits |
| **Ultra** | $200/月 | 10× Pro 周用量；无 5 小时限制（验证账号）；$200 API credits |
| **Team** | Standard $20/座/月（年付；月付 $25）；Premium $100/座/月（月付 $125） | 团队管理、SSO、Claude Code / Cowork、最多 $500 池化 API credits |
| **Enterprise** | $20/座/月 + API 用量（年付，20 座起） | SCIM、审计日志、数据保留控制、角色权限 |

> 💡 **开发者首选 Pro**：Claude Code 已包含在所有付费计划里，和聊天共用同一份额度；重度编码再上 Max。
>
> 来源：[claude.com/pricing](https://claude.com/pricing)（2026-11 核对），价格不含税，**以官网为准**。

---

## 模型选择（2026-11）

| 模型 | 定位 | 适合场景 | 价格（每百万 token） |
|------|------|---------|---------------------|
| **Claude Fable 5.1** | 最强、长程 Agent | 超长任务、复杂科研/工程 | 输入 $10 / 输出 $50 |
| **Claude Opus 5.5** | 日常旗舰 | 复杂编码、架构、重要决策 | 输入 $4 / 输出 $20；缓存读 $0.20 |
| **Claude Sonnet 5.5** | 性价比主力 | 日常编码、文档、分析 | 输入 $2 / 输出 $10；缓存读 $0.10 |
| **Claude Haiku 5.5** | 最快最省 | 高频简单任务、子 Agent、浏览器 | 输入 $0.10 / 输出 $0.50（≤100K 提示） |

**选择原则：**
- 80% 的任务用 Sonnet 5.5 就够
- 遇到 Sonnet 给出错误或不完整答案，换 Opus 5.5
- 需要极限长程 Agent，再用 Fable 5.1
- 批量简单任务（格式转换、分类、子 Agent）用 Haiku 5.5

> 模型名与价格变化很快，客户端/官网为准。Opus 5.5 于 2026-09-22、Sonnet 5.5 于 2026-09-28、Haiku 5.5 于 2026-10-07 发布。

---

## 核心配置：Projects（项目记忆）

**Claude 最重要的功能之一**，让它记住你的项目上下文。

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

> 2026 年 Projects 还能挂接 **Claude Code 的云端会话**：一个项目里协调多个并行会话。

---

## Claude Cowork：把任务交给 Claude（2026）

> **重要变化**：2026 年 Cowork 已并入 Claude 本体——「Claude Cowork is now just Claude」，用自然语言提需求即可，Claude 会自动调用 Cowork 能力。

**是什么：** 给 Claude 一个目标，它在**你指定的文件夹和工具**里直接干活，交付可审阅的成品（表格、文档、幻灯片、研究报告）。

**关键能力：**
- 直接操作本地文件夹和连接的工具（Drive、Microsoft 365 等）
- 浏览器在 Cowork 侧边栏打开，不抢你的浏览器
- 任务可拆分并行；可定时（每天/每周/每月）自动运行
- 关掉电脑也会继续跑（云端）
- Web、桌面、移动是同一个 Claude

**可用计划：** Pro / Max / Ultra / Team（Enterprise 由管理员在组织设置里开启）

**适合：** 周报/月报、表格对账、合同初审、批量资料分析等「重复但有判断」的工作。

来源：[Claude Cowork 页面](https://claude.com/product/cowork)、[Claude 定价](https://claude.com/pricing)（2026-11）。

---

## Skills 与 Plugins（2026）

### Skills（技能）

把可复用的工作流打包成 Skill，Claude 在需要时自动加载。适合：

- 团队固定的代码审查清单
- 固定的周报模板
- 某个内部系统的操作流程

在 Claude Code 里用 `/skill-name` 调用；在 Claude 应用里由 Claude 自动判断是否加载。

### Plugins（插件）

**位置：** [claude.com/marketplace/plugins](https://claude.com/marketplace/plugins)（2026-11 约 529 个插件）

插件把 **Skills + Connectors + 子 Agent** 打包，一次安装就让 Claude 变成某个领域的「专家」。团队可以：

- 用官方/第三方插件快速接入 Supabase、Slack、前端设计等
- 建自己的私有插件市场（Team / Enterprise）

> 对开发团队：**Skills 管流程，Plugins 管集成**，两者配合比单纯写长 Prompt 稳定得多。

---

## Claude Code（开发者必看）

Claude Code 现在是「终端 + IDE + 桌面 + Web + 移动 + Slack」的多入口 Agent：

| 入口 | 适合 |
|------|------|
| 终端 CLI | 本地开发、脚本、CI |
| VS Code / JetBrains 扩展 | 在编辑器里看 diff、@引用 |
| 桌面 App | 多会话并排、可视化 diff、定时任务 |
| Web（claude.ai/code） | 没本地环境、并行云端任务 |
| 移动 / Slack | 随时派活、看进度 |

**核心配置：**
- `CLAUDE.md`：项目根目录的长期指令（也支持 `AGENTS.md`）
- `settings.json`：权限、环境变量、模型
- Hooks：工具调用前后自动执行（格式化、lint）
- Skills / Plugins：复用工作流与集成
- 权限与沙箱：allow / deny、路径范围、审批模式

**Agent Teams（实验）：**
- 一个 lead 协调多个 teammate，共享任务列表、可互相消息
- 需要 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` 开启
- token 成本显著高于单会话，**只适合能独立切分的任务**

详见 [M11-05 Claude Code 省 Token 指南](../11-dev-tools/05-claude-code-token-optimization.md) 与 [官方文档](https://code.claude.com/docs/en/overview)。

---

## 扩展思考 / Effort（2026 写法）

Claude 5.5 系列用 **effort（努力程度）** 控制思考深度，不再只有「开/关思考模式」：

- **Low / Medium**：日常编码、快速迭代（更省钱）
- **High**：复杂 Bug、架构方案
- **Max / xhigh**：难题、长程任务（更慢更贵）

**适合开高 effort 的场景：**
```
✅ 复杂 Bug 的根本原因分析
✅ 算法设计（动态规划、图算法）
✅ 架构方案比较和决策
✅ 数学推导和证明
✅ 安全漏洞分析
```

**不需要高 effort：**
日常编码、文档生成、简单问答。

> 在 Claude Code 里切换 effort 时，Opus 5.5 / Sonnet 5.5 / Haiku 5.5 / Fable 5.1 默认**不会破坏缓存**（2026-11 文档口径）；切模型才会。

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

2026 年 Claude 还提供 **Design / Slides / Docs** 等成品形态，Artifacts 与它们是同一套输出体系。

---

## 文件上传技巧

| 文件类型 | 使用场景 |
|---------|---------|
| **PDF** | 分析技术文档、论文、合同 |
| **代码文件** | 代码审查、解释、重构 |
| **图片** | 分析 UI 设计稿、架构图、截图报错 |
| **CSV/数据** | 数据分析和可视化（配合代码生成） |

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

在 [platform.claude.com](https://platform.claude.com) 获取 API Key。

**基础调用示例：**

```python
import anthropic

client = anthropic.Anthropic(api_key="your_api_key")

message = client.messages.create(
    model="claude-opus-5-5",      # 具体 model id 以官方文档为准
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
    model="claude-opus-5-5",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "上海今天天气怎么样？"}]
)
```

**流式输出：**

```python
with client.messages.stream(
    model="claude-opus-5-5",
    max_tokens=2048,
    messages=[{"role": "user", "content": "写一篇技术文章..."}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

> 2026 年的 API 还提供 prompt caching、batch（省 50%）、fast mode（Opus 5.5 最高 2.5× 速度，2× 价格）等能力，按需使用。

---

## Claude Desktop + MCP 配置

**下载：** [claude.com/download](https://claude.com/download)（桌面版）

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

**MCP 工具市场：** [modelcontextprotocol.io](https://modelcontextprotocol.io)

> 2026 年的替代方案：在 Claude 的 **Connectors / Plugins** 里一键安装，比手写 JSON 更简单。

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
| 重要决策 | 用 Opus 5.5 / Fable 5.1 或高 effort，结果要人工验证 |
| Cowork / Dots 类 Agent | 先收紧权限与目录范围，敏感操作保持人工确认 |

---

## 历史沿革

- **2026-11**：计划更新为 Pro $20 / Max $100 / Ultra $200 / Team $20 起；模型更新为 Claude 5.5 家族 + Fable 5.1；新增 Cowork、Skills/Plugins 章节。
- **2026-10-07**：Claude Haiku 5.5 发布（比 Haiku 4.5 便宜约 75%）。
- **2026-09-28**：Claude Sonnet 5.5 发布（Terminal-Bench 4.0 70.6%，$2/$10）。
- **2026-09-22**：Claude Opus 5.5 发布（比 Opus 5 便宜 40%，$4/$20）。
- **2026**：Claude Cowork 并入 Claude；Claude Code 扩展到桌面/Web/移动/Slack；Agent Teams 进入实验。
- **2025**：Claude 4 系列；Skills、MCP、Claude Code 普及。
- **2024 及以前**：Claude 3 / 3.5 / 3.7 Sonnet；本文旧版以 Opus 4.6 / Sonnet 4.6 / Haiku + Pro $20 / Team $25 编写。

---

## 参考链接

- 官方定价：[claude.com/pricing](https://claude.com/pricing)
- 官方文档：[docs.anthropic.com](https://docs.anthropic.com)
- Claude Code 文档：[code.claude.com/docs](https://code.claude.com/docs/en/overview)
- Prompt 库：[claude.com/prompt-library](https://docs.claude.com/en/resources/prompt-library)
- 插件市场：[claude.com/marketplace/plugins](https://claude.com/marketplace/plugins)
- API Console：[platform.claude.com](https://platform.claude.com)

---

## 下一步

- [M3-03 其他主流工具](../03-ai-coding-tools/03-other-tools.md)
- [M11-05 Claude Code 省 Token 指南](../11-dev-tools/05-claude-code-token-optimization.md)
