# M4-03 · AI Agent（智能体）原理

> LLM + 工具 + 循环 = 能自主完成任务的 AI

---

## 什么是 Agent？

普通 LLM 对话：
```
用户问 → 模型答 → 结束
（一次性，被动响应）
```

**Agent**：
```
目标 → 模型规划 → 调用工具 → 观察结果 → 继续行动 → ... → 完成目标
（多步骤，主动执行）
```

---

## Agent 三要素

```
Agent = LLM（大脑）+ Tools（手）+ Memory（记忆）

LLM:    决策中心，理解目标，规划步骤
Tools:  执行单元，读写文件，调用 API，搜索网络
Memory: 状态记录，对话历史，中间结果
```

---

## 核心循环（ReAct 框架）

最经典的 Agent 模式叫 **ReAct（Reasoning + Acting）**：

```
用户目标
    ↓
THINK:  模型思考（"我需要先搜索，再整理..."）
    ↓
ACT:    调用工具（搜索、读文件、执行代码...）
    ↓
OBSERVE: 观察工具返回结果
    ↓
THINK:  根据结果继续思考
    ↓
ACT:    继续行动...
    ↓
（循环直到任务完成）
    ↓
ANSWER: 给用户最终答案
```

---

## 代码结构（极简版）

```python
tools = {
    "web_search": lambda q: search_web(q),
    "read_file": lambda path: open(path).read(),
    "write_file": lambda path, content: write(path, content),
    "run_python": lambda code: exec(code),
}

def agent_loop(goal):
    messages = [{"role": "user", "content": goal}]
    
    while True:
        response = llm.call(
            messages=messages,
            tools=tool_schemas,  # 告诉模型有哪些工具可用
        )
        
        messages.append(response)
        
        # 如果模型不再调用工具，说明任务完成
        if response.stop_reason != "tool_use":
            return response.text
        
        # 执行工具，把结果反馈给模型
        tool_results = []
        for tool_call in response.tool_calls:
            result = tools[tool_call.name](**tool_call.args)
            tool_results.append({
                "tool_use_id": tool_call.id,
                "content": str(result)
            })
        
        messages.append({"role": "user", "content": tool_results})
        # 继续循环...
```

这就是 Cursor Agent、Claude Code 的基本原理。

---

## 工具调用（Function Calling / Tool Use）

模型生成"结构化调用指令"：

```json
{
  "type": "tool_use",
  "name": "web_search",
  "input": {
    "query": "DeepSeek R1 最新版本特性"
  }
}
```

程序解析后执行真实的搜索，把结果返回给模型：

```json
{
  "type": "tool_result",
  "content": "DeepSeek R1 于 2025 年 1 月发布，参数 671B..."
}
```

---

## Agent 类型

| 类型 | 特点 | 例子 |
|------|------|------|
| **工具调用 Agent** | 调用外部 API/工具 | ChatGPT 插件、Claude Tools |
| **代码执行 Agent** | 写代码并运行 | Cursor Agent、Claude Code |
| **浏览器 Agent** | 控制网页、自动操作 | Browser Use、Playwright Agent |
| **多 Agent** | 多个 AI 分工协作 | AutoGen、CrewAI |
| **规划 Agent** | 先制定计划再执行 | OpenAI o3 模式 |

---

## 内存机制

Agent 需要"记住"之前做了什么：

```
短期记忆（Context Window）
  → 当前对话历史
  → 有 Token 上限，超出则截断

长期记忆（外部存储）
  → 向量数据库（语义搜索历史经验）
  → 结构化数据库（事实性存储）

工作记忆（中间状态）
  → 临时文件
  → 变量存储
```

---

## 多 Agent 协作

复杂任务可以拆分给多个专业 Agent：

```
用户: 帮我分析竞品并写一份报告

协调 Agent（Orchestrator）
    ├─ 搜索 Agent: 搜集竞品信息
    ├─ 分析 Agent: 整理数据、对比
    └─ 写作 Agent: 撰写报告
         ↓
    汇总输出
```

**框架：**
- **AutoGen**（微软）— 多 Agent 对话
- **CrewAI** — 角色扮演式多 Agent
- **LangGraph** — 有向图工作流

---

## Agent 的局限与注意事项

| 风险 | 说明 | 对策 |
|------|------|------|
| 无限循环 | 任务无法完成却一直尝试 | 设置最大步数限制 |
| 错误放大 | 一步出错，后续全错 | 关键节点人工审核 |
| 幻觉工具调用 | 调用不存在的工具/参数 | 严格的工具 Schema |
| 权限过大 | Agent 删了不该删的文件 | 最小权限原则 |
| 成本失控 | 循环太多，Token 消耗爆炸 | 预算限制 + 监控 |

---

## 实用框架推荐

| 框架 | 特点 | 适合 |
|------|------|------|
| **LangChain** | 最全，最多示例 | 快速原型 |
| **LlamaIndex** | 专注数据，简洁 | RAG + Agent |
| **AutoGen** | 微软，多 Agent | 复杂协作任务 |
| **Dify** | 可视化，国内流行 | 非开发者 |
| **n8n** | 工作流自动化 | 业务流程集成 |

---

## 参考资源

- [Learn Claude Agents](https://learn-claude-agents.vercel.app/zh/s01/) — 从零实现 Agent 循环
- Anthropic 文档：Tool Use 章节

---

## 下一步

- [M4-04 MCP 协议](./04-mcp.md) — 工具调用的标准化协议
- [M5-02 AI 辅助开发工作流](../05-practical/02-workflow.md) — 实战应用
