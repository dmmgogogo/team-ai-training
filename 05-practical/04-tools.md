# M5-04 · Tools：工具调用

> LLM 的能力边界 = 模型本身 + 它能调用的工具。学会给 AI 装上"手"。

---

## 什么是 Tool / Function Calling？

LLM 默认只能处理文字——它看不到实时数据，不能操作文件，不能发请求。

**Tool Calling（工具调用）** 让模型能够：

```
用户: "帮我查一下今天上海的天气"

普通 LLM:
→ "根据我的训练数据，上海的天气..." （不知道今天实际天气）

有工具的 LLM:
→ 调用 get_weather(city="上海", date="今天")
→ 获取真实数据 {"temp": 18, "weather": "多云"}
→ "今天上海18°C，多云。"（真实准确）
```

---

## 工具调用的工作流程

```
用户问题
    ↓
LLM 判断：需要调用工具吗？需要哪个工具？参数是什么？
    ↓
LLM 输出结构化的工具调用请求：
{
  "tool": "web_search",
  "parameters": {"query": "上海今天天气"}
}
    ↓
程序执行工具，获取结果
    ↓
把结果发回给 LLM
    ↓
LLM 基于结果生成最终回答
```

---

## 常见工具类型

| 工具类型 | 例子 | 用途 |
|---------|------|------|
| **搜索** | web_search | 获取实时信息 |
| **文件操作** | read_file / write_file | 读写本地文件 |
| **代码执行** | run_python / run_bash | 执行代码，处理数据 |
| **数据库查询** | sql_query | 查询业务数据 |
| **API 调用** | http_request | 调用任意外部服务 |
| **日历/邮件** | get_calendar / send_email | 与日程、邮件集成 |
| **图像处理** | generate_image / analyze_image | 生成或分析图片 |

---

## ChatGPT 内置工具

ChatGPT 已内置多个工具，无需配置直接使用：

| 工具 | 开关位置 | 功能 |
|------|---------|------|
| **联网搜索** | 对话框工具图标 | 搜索最新信息 |
| **代码解释器** | 对话框工具图标 | 执行 Python，处理文件、画图 |
| **DALL-E 图像生成** | 自动触发 | 生成图片 |
| **文件上传** | 对话框附件图标 | 分析 PDF、Excel、代码文件 |

---

## Claude MCP 工具配置

Claude 通过 **MCP（Model Context Protocol）** 连接外部工具。

**配置文件路径：** `~/Library/Application Support/Claude/claude_desktop_config.json`

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
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token"
      }
    }
  }
}
```

**MCP 市场：** [modelcontextprotocol.io/servers](https://modelcontextprotocol.io/servers)

---

## Cursor 内置工具

Cursor Agent 模式内置工具：

```
@文件名       → 文件读取/引用
@目录名       → 目录级引用
@docs         → 搜索已配置的第三方文档
@web          → 实时搜索网络
终端执行       → Agent 自动运行 shell 命令
```

---

## 自己开发工具（Function Calling 示例）

```python
from openai import OpenAI

client = OpenAI()

tools = [
    {
        "type": "function",
        "function": {
            "name": "query_order_status",
            "description": "查询订单状态",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {"type": "string", "description": "订单号"}
                },
                "required": ["order_id"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "查一下订单 ORD-98765"}],
    tools=tools
)
```

---

## 下一步

- [⭐️ M5-04b Skills：技能扩展](./04-skills.md)
- [M4-04 MCP 协议详解](../04-principles/04-mcp.md)
