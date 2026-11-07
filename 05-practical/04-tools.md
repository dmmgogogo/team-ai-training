# M5-04 · Tools：工具调用

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> LLM 的能力边界 = 模型本身 + 它能调用的工具。2026 年的关键变化是：工具层已经**分层**了——Function Calling 管"怎么调"，MCP 管"接什么"，Skills 管"按什么流程做"，Plugins 管"怎么打包分发"。

---

## 一句话结论

| 层次 | 机制 | 一句话 | 2026-11 现状 |
|------|------|--------|--------------|
| **单次调用约定** | Function Calling / Tool Use | 模型输出结构化调用请求，程序执行后把结果回传 | 所有主流模型 API 的标配 |
| **工具接入协议** | MCP（Model Context Protocol） | 用统一协议把工具/数据源接到任意 AI 客户端 | 开放标准，最新规范 `2026-07-28` |
| **流程知识** | Skills（`SKILL.md`） | 把"多步骤做法"写成按需加载的说明书 | 跨平台开放标准（Agent Skills） |
| **打包分发** | Plugins | 把 skills + 工具 + 命令 + agent 打成一件安装 | Claude / Cursor / OpenAI 都有插件生态 |

> 记住这张表，后面所有内容都是它的展开。

---

## 工具调用的工作流程

```
用户问题
    ↓
LLM 判断：需要调用工具吗？需要哪个工具？参数是什么？
    ↓
LLM 输出结构化的工具调用请求（JSON，受 JSON Schema 约束）
{
  "tool": "web_search",
  "arguments": {"query": "上海今天天气"}
}
    ↓
宿主程序执行工具（本地函数 / 远程 API / MCP Server）
    ↓
把结果（成功或结构化错误）发回给 LLM
    ↓
LLM 基于结果继续推理，或再调用下一个工具，直到给出最终回答
```

2026 年的实现细节里，有三点值得注意：

1. **模型可以一次发起多个工具调用**（并行 tool calls），宿主可以并发执行。
2. **工具结果也会进入上下文**，所以要控制返回体积（分页、截断、摘要）。
3. **工具描述本身消耗 token**，工具越多，每轮请求越贵——这催生了"工具按需发现"（见下文）。

---

## 2026 现状：三个已经稳定的共识

### 共识一：Tool Use 是所有模型的标配

截至 2026-11，工具调用不再是某个平台的特异功能：

- **OpenAI**：GPT-6 家族（GPT-6 Sol、GPT-6 Pro / Astra）与 GPT-5.6 家族（Sol / Terra / Luna）都通过 API 的 tools 机制调用外部函数（来源：[OpenAI 模型说明](https://help.openai.com/en/articles/20001354-gpt-6-and-other-models-in-chatgpt)，2026-11）。
- **Anthropic**：Claude 5.5 家族（Opus 5.5 / Sonnet 5.5 / Haiku 5.5）把 agentic coding 与工具使用作为核心能力；Opus 5.5 于 2026-09-22 发布（来源：[Anthropic 发布说明](https://www.anthropic.com/claude-opus-5-5)，2026-09）。
- **其他平台**：Gemini、国内 Qwen / DeepSeek / GLM 等也都提供 function calling 或等价机制（具体接口以各家官网为准）。

**结论**：不要再问"哪个模型支持工具调用"，要问"哪个模型在长链路工具调用上更稳、更省"。

### 共识二：MCP 成为工具接入的事实标准

MCP 用 JSON-RPC 定义 Host（AI 应用）、Client、Server 之间的通信，把"工具/资源/提示"标准化（来源：[MCP 规范 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28)，2026-07）。

2026-11 的生态状态：

| 维度 | 现状 |
|------|------|
| 规范版本 | `2026-07-28`（最新） |
| 传输方式 | stdio、Streamable HTTP；SSE 在部分客户端已标注为过渡方案 |
| 授权 | OAuth 2.0，支持动态客户端注册；Claude Code 等客户端可限制 OAuth scopes |
| 扩展 | MCP Apps（工具返回可交互 UI）等扩展机制 |
| 目录 | 官方目录/Registry 可检索；Claude、Cursor 等内置市场入口 |
| 采用方 | Claude（Desktop / Code / Cowork）、Cursor、VS Code、Codex 等 |

**结论**：给团队做工具集成，优先做 MCP Server，而不是给每个客户端写一套私有插件。

### 共识三：工具定义也要"省着用"

工具一多，模型每轮都要读一遍工具清单，成本上升、准确率下降。2026 年的主流做法是**按需发现**：

- Claude Code 的 MCP 支持 **tool search**：不必把所有工具一次性塞进上下文，模型需要时再检索工具。
- 客户端的"工具/插件上下文成本"开始被显式度量（例如 Claude Code 的 `/plugin` 会显示 Context cost 估算）。

**结论**：工具不是越多越好；先问"这个工具真的需要常驻吗"。

---

## 常见工具类型

| 工具类型 | 例子 | 用途 | 2026 年的变化 |
|---------|------|------|---------------|
| **搜索** | web_search | 获取实时信息 | 逐渐与"深度研究"类 agent 融合 |
| **文件操作** | read_file / write_file / edit | 读写本地文件 | 成为编码 agent 的基础能力 |
| **代码执行** | run_python / run_bash | 执行代码、跑测试 | 普遍加沙箱与审批 |
| **数据库查询** | sql_query | 查询业务数据 | 推荐只读账号 + 连接串隔离 |
| **API 调用** | http_request | 调用任意外部服务 | 越来越多以 MCP Server 形式提供 |
| **浏览器** | browser / playwright | 打开页面、填表、截图 | MCP Apps、浏览器桥接（如 OpenCLI）兴起 |
| **日历/邮件** | calendar / email | 日程与邮件集成 | 通过官方 connector / MCP 接入 |
| **图像处理** | generate_image / analyze_image | 生成或分析图片 | 多模态工具调用常态化 |

---

## 各平台怎么用（2026-11 快照）

### ChatGPT

| 能力 | 入口 | 说明 |
|------|------|------|
| 内置工具 | 对话框工具/模式选择 | 搜索、代码解释器、图像生成、文件分析 |
| **Plugins** | 侧边栏 **Plugins** / [插件目录](https://chatgpt.com/plugins) | 2026 年接替自定义 GPT：插件可包含 Skills（流程说明）和 Connected apps（连接外部服务） |
| **Apps / Connectors** | 插件内或单独连接 | 连接 Slack、Google Drive 等外部服务并授权 |

> ⚠️ 2026 年的重要变化：OpenAI 正在**退役自定义 GPT**，工作流迁移到 **Plugins + Skills**。详见 [M7-01](../07-skills/01-chatgpt-gpts.md)（来源：[OpenAI 帮助中心](https://help.openai.com/en/articles/8554407-gpts-in-chatgpt)，2026-11）。

### Claude

| 能力 | 入口 | 说明 |
|------|------|------|
| Connectors（MCP） | 设置 → Connectors / 目录 | 远程 MCP 服务，OAuth 授权 |
| Skills | Customize → Skills | 按需加载的流程说明 |
| Plugins | Customize → Plugins | 打包 skills + connectors + commands + agents |
| 本地 MCP | `claude_desktop_config.json`（Claude Desktop） | 传统本机配置文件 |

**Claude Desktop 本机 MCP 配置示例**（路径以 macOS 为例，其他平台以官网为准）：

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/你的用户名/Documents"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

> 用 `${VAR}` 引用环境变量，不要把 token 直接写进配置文件。

### Claude Code（命令行）

```bash
# 添加远程 HTTP MCP（推荐）
claude mcp add --transport http notion https://mcp.notion.com/mcp

# 添加本地 stdio MCP
claude mcp add db --env DB_DSN=postgresql://readonly:pass@host:5432/db -- npx -y @bytebase/dbhub

# 查看状态
claude mcp list
```

项目级配置写在仓库根目录的 `.mcp.json`，可提交给团队共享（首次使用需要信任工作区并批准）。详见 [M6-03](../06-ai-project-setup/03-mcp-integration.md)。

### Cursor

- Agent 内置工具：`@文件名`、`@目录`、`@docs`、`@web`、终端执行。
- 自定义 MCP：`mcp.json` 或 Customize → MCP，支持 stdio / SSE / Streamable HTTP（来源：[Cursor MCP 文档](https://cursor.com/docs/mcp)，2026-11）。
- 规则/技能：`.cursor/rules/*.mdc` 与 `.agents/skills/`，见 [M6-01](../06-ai-project-setup/01-cursorrules.md)。

---

## 工具设计原则（给要写工具的人）

工具设计得好不好，直接决定 agent 能不能稳定完成任务。以下 7 条是团队实践里最值钱的：

### 1. 名字和描述要"能被检索"

```json
// ❌ 太抽象
{"name": "process", "description": "处理数据"}

// ✅ 说清对象、动作、边界
{
  "name": "query_order_status",
  "description": "按订单号查询订单当前状态。只读。订单不存在时返回 not_found 错误。"
}
```

模型是根据名称 + 描述决定"要不要用、用哪个"的，描述就是检索关键词。

### 2. 参数少而明确，用 JSON Schema 约束

```json
{
  "type": "object",
  "properties": {
    "order_id": {"type": "string", "description": "订单号，形如 ORD-98765"},
    "include_history": {"type": "boolean", "default": false}
  },
  "required": ["order_id"],
  "additionalProperties": false
}
```

- 必填项越少越好；
- 枚举值写 `enum`，不要让模型猜；
- 关闭 `additionalProperties`，避免模型编造字段。

### 3. 返回结构化、可判别成功/失败

```json
{"ok": false, "error": {"code": "not_found", "message": "订单不存在", "hint": "确认订单号是否正确"}}
```

错误信息要**可行动**（告诉模型下一步怎么做），而不是抛一段堆栈。

### 4. 输出要有体积上限

工具返回 10 万行日志，上下文直接爆掉。做法：分页、字段裁剪、摘要、把大结果落盘返回路径。

### 5. 写操作要幂等、可回滚

- 用业务幂等键，避免重试造成重复下单；
- 破坏性操作提供 dry-run；
- 记录审计日志（谁、什么时候、调了什么、结果如何）。

### 6. 一个工具只做一件事

"万能工具"（一个函数干十件事）会让模型难以选择、难以组合、难以调试。宁可多几个小工具。

### 7. 权限最小化

工具能读什么、能写什么，在服务端就限制死，不要依赖"模型会自觉"。

---

## 权限与安全（2026 年的重点）

工具越强，风险越大。2026 年最常见的几类事故：

| 风险 | 场景 | 对策 |
|------|------|------|
| **提示注入** | 工具返回的网页/Issue/邮件里藏指令，诱导模型执行危险操作 | 把工具输出当不可信数据；危险操作强制人工确认；限制工具组合 |
| **权限过大** | 数据库连接用 root、文件工具指向整个 home | 只读账号、路径白名单、最小 scope |
| **密钥泄露** | token 硬编码进配置或日志 | 环境变量/密钥管理；日志脱敏 |
| **供应链** | 安装来源不明的 MCP/插件/skill | 只从可信市场安装；审阅脚本；锁定版本 |
| **误操作** | 删除文件、改生产配置 | dry-run、审批模式、沙箱、可回滚 |
| **越权串联** | A 工具读到的数据被 B 工具发出去 | 按数据域隔离工具；限制网络出口 |

给团队的三条硬规则：

1. **写操作默认需要人批准**：Claude Code 的 permission modes、Cursor 的审批、ChatGPT 的动作确认都是这个思路。
2. **生产环境只读**：数据库、监控、日志类工具默认只读账号。
3. **插件/Skill 安装要审**：插件和 skill 可以携带脚本，等于在你机器上执行代码。

---

## 自己开发工具：一个最小示例

### 方式一：Function Calling（平台内函数）

```json
{
  "name": "query_order_status",
  "description": "按订单号查询订单当前状态。只读。",
  "parameters": {
    "type": "object",
    "properties": {
      "order_id": {"type": "string", "description": "订单号，形如 ORD-98765"}
    },
    "required": ["order_id"],
    "additionalProperties": false
  }
}
```

Python 侧（OpenAI 风格，**模型 ID 与调用细节以官网为准**）：

```python
from openai import OpenAI

client = OpenAI()

resp = client.responses.create(
    model="<当前 GPT-6 系列模型 ID>",
    input="查一下订单 ORD-98765 的状态",
    tools=[{
        "type": "function",
        "name": "query_order_status",
        "description": "按订单号查询订单当前状态。只读。",
        "parameters": {
            "type": "object",
            "properties": {"order_id": {"type": "string"}},
            "required": ["order_id"],
            "additionalProperties": False,
        },
    }],
)

# 解析模型返回的 tool call，执行本地函数，再把结果回传（略）
```

### 方式二：MCP Server（推荐，跨客户端复用）

MCP Server 本质上是一个说 JSON-RPC 的进程/服务，暴露 tools / resources / prompts。写一次，Claude、Cursor、VS Code 等都能接。

```python
# 伪代码：暴露一个只读查询工具
from mcp.server import Server

server = Server("order-tools")

@server.tool()
def query_order_status(order_id: str) -> dict:
    """按订单号查询订单状态（只读）。"""
    ...
```

> 具体 SDK 用法以 [MCP 官方文档](https://modelcontextprotocol.io/docs/develop/build-server) 为准。

---

## 历史沿革

| 时间 | 事件 | 意义 |
|------|------|------|
| 2023-03 | OpenAI 推出 ChatGPT Plugins | 第一次让模型"调用外部服务"产品化 |
| 2023-06 | OpenAI 推出 Function Calling | 工具调用变成 API 能力，成为行业接口 |
| 2024-11 | Anthropic 开源 MCP | 工具接入从"每家一套"走向统一协议 |
| 2025 | MCP 被主流客户端广泛采用；Claude Skills 出现 | 工具层与"流程层"开始分离 |
| 2025–2026 | Agent 长任务普及，工具调用从"单次"走向"长链路 + 并行" | 权限、审批、沙箱成为刚需 |
| 2026-07 | MCP 规范更新至 `2026-07-28` | 传输、授权、扩展机制进一步稳定 |
| 2026-09 | Claude Marketplace 上线，聚合 2000+ connectors/plugins | 工具与插件的分发渠道成型 |
| 2026-11 | OpenAI 退役自定义 GPT，转向 Plugins + Skills | 工具/技能生态完成一次代际切换 |

---

## 参考

- [MCP 规范（2026-07-28）](https://modelcontextprotocol.io/specification/2026-07-28)
- [OpenAI：GPT-6 家族与模型说明](https://help.openai.com/en/articles/20001354-gpt-6-and-other-models-in-chatgpt)
- [OpenAI：Function calling 文档](https://developers.openai.com/api/docs/guides/function-calling)
- [Claude Code：MCP 接入](https://code.claude.com/docs/en/mcp)
- [Cursor：MCP 文档](https://cursor.com/docs/mcp)
- [Claude Opus 5.5 发布说明](https://www.anthropic.com/claude-opus-5-5)

---

## 下一步

- [⭐️ M5-04b Skills：技能扩展](./04-skills.md)
- [M4-04 MCP 协议详解](../04-principles/04-mcp.md)
- [M6-03 MCP 项目集成](../06-ai-project-setup/03-mcp-integration.md)
