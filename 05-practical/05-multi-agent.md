# M5-05 · Multi-Agent 多智能体实战

> 一个 AI 不够用时，让多个 AI 分工协作。

---

## 为什么需要多 Agent？

单个 Agent 的局限：
- 上下文窗口有限，复杂任务装不下
- 一个模型擅长推理，另一个擅长代码，各有所长
- 长任务容易"跑偏"，中途失去目标
- 串行处理，无法并行提速

**Multi-Agent 解决方案：** 把复杂任务拆解，分配给专业的 Agent 并行处理，再汇总结果。

---

## 核心架构模式

### 模式一：协调者 + 执行者（Orchestrator + Worker）

```
用户需求
    ↓
协调者 Agent（规划、分配任务）
    ├─→ 执行者 A（搜索信息）
    ├─→ 执行者 B（分析数据）
    └─→ 执行者 C（撰写报告）
    ↓
协调者汇总，输出最终结果
```

**适合：** 复杂的研究/分析任务

---

### 模式二：流水线（Pipeline）

```
Agent 1（数据收集）
    ↓ 输出交给下一个
Agent 2（数据清洗）
    ↓
Agent 3（分析）
    ↓
Agent 4（生成报告）
```

**适合：** 步骤明确、顺序固定的处理流程

---

### 模式三：专家团队（Expert Panel）

```
问题 → 并行发给多个专家 Agent
    ├─ 安全专家 Agent
    ├─ 性能专家 Agent
    └─ 架构专家 Agent
        ↓
汇总各方意见 → 最终建议
```

**适合：** 需要多角度评审的任务（代码审查、方案评估）

---

## 实战：Claude Agent Teams（最新）

Claude Opus 4.6 支持原生的 **Agent Teams** 功能：

```python
import anthropic

client = anthropic.Anthropic()

# 主 Agent 可以创建子 Agent 来并行处理任务
response = client.messages.create(
    model="claude-opus-4-6-20260205",
    max_tokens=8096,
    messages=[{
        "role": "user",
        "content": """
        分析我们的竞品情况，需要：
        1. 收集 5 个主要竞品的产品功能
        2. 分析各竞品的定价策略  
        3. 对比我们的优劣势
        4. 提出差异化建议
        请分解任务并并行处理以提升效率。
        """
    }],
    # Agent Teams 模式下，Claude 会自动协调子任务
)
```

---

## 实战：用 AutoGen 构建多 Agent

[AutoGen](https://github.com/microsoft/autogen)（微软出品）是最成熟的多 Agent 框架之一。

```python
import autogen

# 配置模型
config_list = [{"model": "gpt-4o", "api_key": "your_key"}]
llm_config = {"config_list": config_list}

# 定义 Agent 角色
user_proxy = autogen.UserProxyAgent(
    name="用户",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    code_execution_config={"work_dir": "workspace", "use_docker": False}
)

programmer = autogen.AssistantAgent(
    name="程序员",
    llm_config=llm_config,
    system_message="你是一个 Python 专家，负责编写和调试代码。"
)

reviewer = autogen.AssistantAgent(
    name="代码审查员",
    llm_config=llm_config,
    system_message="你是一个代码审查专家，负责检查代码质量、安全性和性能。"
)

# 发起多 Agent 对话
user_proxy.initiate_chat(
    programmer,
    message="写一个爬虫，抓取 Hacker News 今日热榜，提取标题和链接，保存到 CSV"
)

# 审查员介入
user_proxy.initiate_chat(
    reviewer,
    message=f"请审查以下代码：\n{programmer.last_message()}"
)
```

---

## 实战：用 CrewAI 构建专业团队

[CrewAI](https://github.com/crewAIInc/crewAI) 用"角色扮演"方式定义 Agent 团队：

```python
from crewai import Agent, Task, Crew

# 定义团队成员
researcher = Agent(
    role="AI 市场研究员",
    goal="收集和分析 AI 工具市场的最新动态",
    backstory="你是一个专注 AI 领域的市场研究员，擅长信息收集和整理",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool]  # 可以使用搜索工具
)

writer = Agent(
    role="技术文档作者",
    goal="将研究结果整理成结构清晰、易于理解的文档",
    backstory="你是一个经验丰富的技术写作者，擅长将复杂内容转化为清晰文档",
    verbose=True,
    allow_delegation=False
)

# 定义任务
research_task = Task(
    description="调研 2026 年最热门的 5 个 AI 编程工具，包括功能、价格、优缺点",
    expected_output="包含 5 个工具详细信息的结构化数据",
    agent=researcher
)

writing_task = Task(
    description="基于研究结果，撰写一篇面向开发者的 AI 工具推荐报告",
    expected_output="一篇 1000 字左右的 Markdown 格式报告",
    agent=writer
)

# 组建团队并执行
crew = Crew(agents=[researcher, writer], tasks=[research_task, writing_task])
result = crew.kickoff()
```

---

## 实战：LangGraph 有向图工作流

[LangGraph](https://github.com/langchain-ai/langgraph) 用图结构控制复杂 Agent 流程：

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict

class State(TypedDict):
    query: str
    search_result: str
    code: str
    review_result: str
    final_output: str

# 定义每个节点（Agent 步骤）
def search_node(state):
    result = web_search(state["query"])
    return {"search_result": result}

def code_node(state):
    code = llm.generate_code(state["search_result"])
    return {"code": code}

def review_node(state):
    review = llm.review_code(state["code"])
    return {"review_result": review}

def should_revise(state):
    # 根据 review 结果决定是否重新生成代码
    if "需要修改" in state["review_result"]:
        return "code"  # 回到代码生成节点
    return END

# 构建图
workflow = StateGraph(State)
workflow.add_node("search", search_node)
workflow.add_node("code", code_node)
workflow.add_node("review", review_node)

workflow.set_entry_point("search")
workflow.add_edge("search", "code")
workflow.add_edge("code", "review")
workflow.add_conditional_edges("review", should_revise)

app = workflow.compile()
result = app.invoke({"query": "用 FastAPI 实现 JWT 认证"})
```

---

## Cursor 中的多 Agent 实践

Cursor 的 Agent 模式本身就支持多步骤任务链：

```
实用工作流：

1. 架构设计 Agent：
   "根据需求文档 @docs/requirements.md，设计系统架构图（文字版）和数据库 Schema"

2. 代码生成 Agent：
   "根据上面的架构设计，生成 @src/models/ 下的所有数据库模型"

3. 测试生成 Agent：
   "为 @src/models/ 中的每个模型，生成完整的单元测试"

4. 审查 Agent：
   "@src/ 对整个项目做一次安全和性能审查，输出问题清单"
```

---

## 多 Agent 注意事项

| 风险 | 说明 | 对策 |
|------|------|------|
| **成本爆炸** | 多个 Agent 并行，Token 消耗成倍增加 | 设置预算上限，先小规模测试 |
| **错误传播** | A 的错误输出传给 B，雪球越滚越大 | 关键节点加人工审核 |
| **死循环** | Agent 互相等待或反复调用 | 设置最大轮次限制 |
| **状态不一致** | 多 Agent 并行修改同一资源 | 加锁或顺序化 |
| **调试困难** | 多 Agent 交互链路长，排错难 | 开启详细日志，记录每步输入输出 |

---

## 框架选型建议

| 框架 | 地址 | 适合场景 |
|------|------|---------|
| **AutoGen** | [github.com/microsoft/autogen](https://github.com/microsoft/autogen) | 多 Agent 对话，代码执行 |
| **CrewAI** | [github.com/crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 角色明确的专业团队 |
| **LangGraph** | [github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 复杂有状态工作流 |
| **Claude Agent Teams** | 原生支持，无需框架 | 简单多 Agent 协作 |
| **Dify** | [dify.ai](https://dify.ai) | 可视化编排，非开发者友好 |

---

## 下一步

- [M5-06 Cursor 正确配置与使用](./06-cursor-setup.md)
- [M5-07 ChatGPT 正确配置与使用](./07-chatgpt-setup.md)
- [M5-08 Claude 正确配置与使用](./08-claude-setup.md)
