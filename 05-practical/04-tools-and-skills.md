# M5-04 · Tools & Skills：工具调用与技能扩展

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

**代码解释器实用场景：**
```
上传一个 Excel 文件 →
"帮我分析这份销售数据，画出各月趋势折线图，
并找出销售额最高的 Top 5 产品"
→ ChatGPT 直接运行 Python，输出图表和分析
```

---

## Claude 工具使用

Claude 通过 **MCP（Model Context Protocol）** 连接外部工具。

**Claude Desktop 配置 MCP（以文件系统工具为例）：**

配置文件路径：`~/Library/Application Support/Claude/claude_desktop_config.json`

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

配置后，Claude 就能读写你的文件、操作 GitHub 仓库。

**MCP 市场（找现成工具）：** [modelcontextprotocol.io/servers](https://modelcontextprotocol.io/servers)

---

## Cursor 工具扩展

Cursor 的工具能力通过 Agent 模式实现，内置工具包括：

```
文件读取     → @文件名 直接引用
代码搜索     → 语义搜索整个代码库
终端执行     → Agent 可运行 shell 命令
Web 搜索     → @web 实时搜索（部分版本）
文档检索     → @docs 搜索第三方文档
```

**自定义 .cursorrules 扩展行为：**

```
.cursorrules

# 工具使用规范
当需要安装依赖时，使用 poetry add（不用 pip install）
当需要运行测试时，使用 pytest -v --tb=short
当创建 API 接口时，自动生成对应的单元测试
```

---

## 自己开发工具（Function Calling 示例）

用 OpenAI API 给模型添加自定义工具：

```python
from openai import OpenAI

client = OpenAI()

# 定义工具
tools = [
    {
        "type": "function",
        "function": {
            "name": "query_order_status",
            "description": "查询订单状态，输入订单号，返回状态信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "订单号，如 ORD-12345"
                    }
                },
                "required": ["order_id"]
            }
        }
    }
]

# 调用
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "帮我查一下订单 ORD-98765 的状态"}],
    tools=tools
)

# 处理工具调用
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    # tool_call.function.name → "query_order_status"
    # tool_call.function.arguments → '{"order_id": "ORD-98765"}'
    
    # 执行你的业务逻辑
    result = your_db.query_order("ORD-98765")
    
    # 把结果发回给模型
    # ...
```

---

## Skills（技能）的概念

在更高层次上，**Skills** 是封装好的"AI 能力单元"，包含：
- 调用哪些工具
- 用什么 Prompt
- 处理什么类型的任务

**类比：** 就像软件中的函数库，你可以复用别人写好的 Skill。

**常见 Skill 平台：**
- [OpenAI GPT Store](https://chatgpt.com/gpts) — ChatGPT 的 GPT 市场
- [Anthropic Prompt Library](https://www.anthropic.com/prompt-library) — 官方 Prompt 模板
- [MCP Servers](https://modelcontextprotocol.io/servers) — Claude 工具市场

---

## 实用技巧

**技巧 1：组合工具链**
```
搜索最新文档 → 阅读 → 写代码 → 运行测试 → 报告结果
（search → read → code → execute → summarize）
```

**技巧 2：让 AI 自己选工具**
```
"帮我完成这个任务：[描述任务]
你有以下工具可以使用：搜索网络、读写文件、执行代码
请自行判断需要哪些工具，按顺序完成。"
```

**技巧 3：工具调用要有幂等性**
- 搜索、读取 → 安全，可重试
- 写入、发送、删除 → 危险，需要确认

---

## 下一步

- [M5-05 Multi-Agent 多智能体实战](./05-multi-agent.md)
- [M4-04 MCP 协议详解](../04-principles/04-mcp.md)
