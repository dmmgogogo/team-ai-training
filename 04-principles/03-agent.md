# M4-03 · AI Agent（智能体）原理

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：中 ｜ 🔁 下次复核：2027-05
>
> LLM + 工具 + 循环 = 能自主完成任务的 AI。2026 年，这个循环长出了规划、子 Agent 与上下文工程。

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

一个 2026 年广泛采用的定义：

> **Agent = LLM autonomously using tools in a loop**（LLM 在循环中自主使用工具）。

注意关键词是"循环"和"自主"：一次工具调用不叫 Agent，能根据结果调整下一步才叫 Agent。

---

## Agent 的组成（2026 版）

```
Agent = LLM（大脑）
      + Harness（工程外壳：循环、工具执行、权限、日志）
      + Tools（手：读写文件、搜索、执行代码、调 API）
      + Context（工作记忆：系统提示、任务、历史、检索结果）
      + Memory（长期记忆：跨会话的笔记、偏好、项目状态）
```

很多人只盯着"哪个模型强"，但生产环境里 **harness 的差距往往比模型差距更大**：同样的模型，工具设计、上下文管理、权限控制不同，成功率能差出一大截。

---

## 核心循环（ReAct 框架，经典但仍在用）

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

## 2026 进化一：从 ReAct 到 Planning

纯 ReAct 容易"走一步看一步"，在长任务里会绕圈。2026 年的主流做法是**先规划、再执行、定期校准**：

```
1. 理解目标 → 2. 产出计划（Plan）→ 3. 人类/规则审核计划
        ↓
4. 按计划执行（可并行、可派子 Agent）
        ↓
5. 每完成一步，更新计划与待办
        ↓
6. 遇到阻塞：重规划，而不是硬试
        ↓
7. 验收：测试/检查清单通过才算完成
```

落地形态：
- **Plan Mode**：先只读代码、产出计划，人确认后才允许写文件
- **Todo / 任务板**：把计划变成可勾选的状态，避免"做着做着忘了"
- **Spec 驱动**：先写清需求与验收标准，再让 Agent 实现（见 [M5-02](../05-practical/02-workflow.md)）
- **检查点（Checkpoint）**：每阶段 commit / 存档，出错可回滚

---

## 代码结构（极简版）

```python
tools = {
    "web_search": lambda q: search_web(q),
    "read_file": lambda path: read(path),
    "write_file": lambda path, content: write(path, content),
    "run_tests": lambda cmd: run(cmd),
}

def agent_loop(goal, max_steps=30, budget_tokens=2_000_000):
    messages = [{"role": "user", "content": goal}]
    used_tokens = 0

    for step in range(max_steps):
        response = llm.call(
            messages=messages,
            tools=tool_schemas,       # 告诉模型有哪些工具可用
            tool_choice="auto",
        )
        used_tokens += response.usage.total_tokens

        # 预算/步数保护：Agent 最常见的失控点
        if used_tokens > budget_tokens:
            return "预算超限，已停止，请人工接管"

        messages.append(response)

        # 如果模型不再调用工具，说明任务完成
        if response.stop_reason != "tool_use":
            return response.text

        # 执行工具，把结果反馈给模型
        tool_results = []
        for tool_call in response.tool_calls:
            if not is_allowed(tool_call):        # 权限控制
                result = "权限不足，已拒绝"
            else:
                result = tools[tool_call.name](**tool_call.args)
            tool_results.append({
                "tool_use_id": tool_call.id,
                "content": str(result)[:20_000],  # 截断，防止工具输出撑爆上下文
            })

        messages.append({"role": "user", "content": tool_results})
```

这就是 Claude Code、Codex、Cursor Agent 的基本原理。真实产品还会加上：流式输出、并行工具调用、子 Agent、上下文压缩、审批中断、审计日志。

---

## 工具调用（Function Calling / Tool Use）

模型生成"结构化调用指令"：

```json
{
  "type": "tool_use",
  "name": "web_search",
  "input": {
    "query": "DeepSeek V4 1M context"
  }
}
```

程序解析后执行真实的搜索，把结果返回给模型：

```json
{
  "type": "tool_result",
  "content": "DeepSeek-V4 于 2026-04-24 发布，原生支持 1M 上下文..."
}
```

### 2026 年的工具调用新能力

| 能力 | 解决什么问题 |
|------|-------------|
| **并行工具调用** | 同时读多个文件/查多个源，减少往返 |
| **严格 Schema / 结构化输出** | 参数不合法直接拒，减少"幻觉调用" |
| **Tool Search（工具搜索）** | 工具成百上千时，先检索工具再调用，避免工具列表撑爆上下文 |
| **Programmatic Tool Calling** | 让模型写代码编排工具调用，减少中间结果进入上下文 |
| **MCP** | 工具接入标准化，一次开发到处可用（见 [M4-04](./04-mcp.md)） |
| **Skills** | 把"怎么做某类任务"的流程封装成可加载的技能包 |

---

## 2026 进化二：子 Agent 与多 Agent 协作

一个 Agent 干长任务，上下文很快会爆。2026 年的主流解法是**子 Agent（Sub-agent）**：

```
主 Agent（Orchestrator）
  ├─ 子 Agent A：调研（独立上下文，返回 1-2K Token 摘要）
  ├─ 子 Agent B：改代码（独立上下文，返回 diff + 测试结果）
  └─ 子 Agent C：审查（独立上下文，返回问题清单）
        ↓
主 Agent 汇总、决策、继续
```

好处：
- **上下文隔离**：子 Agent 可以读几万 Token，但只把结论带回主上下文
- **并行**：互不依赖的子任务同时做
- **专业化**：不同子 Agent 用不同提示、工具、模型档位

代价：
- 协调开销、重复劳动、结果冲突
- 成本放大（每个子 Agent 都是一次完整推理）
- 需要清晰的任务边界与写权限划分

Anthropic 在上下文工程文章中提到，子 Agent 常把数万 Token 的探索压缩成 1,000–2,000 Token 的摘要返回，这是"用架构换上下文"的典型（来源：[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)，2026）。

**多 Agent 框架/形态**：Claude Agent SDK、OpenAI Agents SDK、LangGraph、AutoGen、CrewAI；以及 2026 年产品化的 "Agent Teams"（多 Agent 共享任务板/文件系统并行工作）。

---

## 2026 进化三：上下文工程成为 Agent 的核心

Agent 跑得越久，上下文越脏。2026 年大家逐渐接受：**Agent 的瓶颈不是模型智商，而是上下文质量**。

| 技术 | 做法 |
|------|------|
| **Compaction（压缩）** | 接近上限时总结历史，保留决策、未解 Bug、关键实现 |
| **Structured Note-taking** | 让 Agent 维护 `NOTES.md` / 待办清单，跨压缩保持状态 |
| **Just-in-time Retrieval** | 只存文件路径/查询，需要时再读，不预加载全部 |
| **Tool Result Clearing** | 清掉旧的原始工具输出，只留结论 |
| **Sub-agent 隔离** | 把"脏活"放进子上下文，主上下文只收摘要 |

详细方法见 [M4-05 上下文工程](./05-context-engineering.md)。

---

## 内存机制

Agent 需要"记住"之前做了什么：

```
短期记忆（Context Window）
  → 当前对话历史
  → 有 Token 上限，超出则截断/压缩

长期记忆（外部存储）
  → 向量数据库（语义搜索历史经验）
  → 结构化数据库（事实性存储）
  → 文件（NOTES.md、项目文档）

工作记忆（中间状态）
  → 临时文件、任务板、变量
```

> 模型本身是无状态的。"记忆"是 harness 提供的能力，不是模型天生记得你。

---

## Agent 的评测（2026 必修课）

Agent 不像单轮问答那样好测：它多轮、会改环境、结果有随机性。Anthropic 的评测指南给出一套通用词汇（来源：[Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)，2026）：

| 概念 | 含义 |
|------|------|
| **Task** | 一个测试任务，含输入与成功标准 |
| **Trial** | 对同一任务的一次尝试（要跑多次） |
| **Grader** | 评分器：单测、状态检查、LLM 评审、人工 |
| **Transcript / Trace** | 完整轨迹：工具调用、推理、中间结果 |
| **Outcome** | 最终环境状态（比"模型说完成了"可靠） |
| **pass@k** | k 次里至少成功一次，适合"探索型"任务 |
| **pass^k** | k 次全部成功，适合"必须稳定"的产品 |

实践建议：
- 从 **20–50 个真实失败案例**开始，不要等"完美评测集"
- 优先用**确定性 grader**（单测、状态断言），LLM 评审只做补充
- **读 transcript**：分数不涨时，先怀疑评测而不是模型
- 同时保留 **capability eval**（能做什么）和 **regression eval**（有没有变差）

---

## Agent 的局限与注意事项

| 风险 | 说明 | 对策 |
|------|------|------|
| 无限循环 | 任务无法完成却一直尝试 | 最大步数 + Token 预算 + 超时 |
| 错误放大 | 一步出错，后续全错 | 关键节点人工审核、阶段验收 |
| 幻觉工具调用 | 调用不存在的工具/参数 | 严格 Schema、工具白名单、参数校验 |
| 权限过大 | Agent 删了不该删的文件 / 发了不该发的消息 | 最小权限、沙箱、写操作审批 |
| 成本失控 | 循环太多 + 子 Agent 扇出，Token 爆炸 | 预算上限、缓存、按任务选模型档位 |
| 上下文污染 | 工具输出/网页内容里的恶意指令 | 内容隔离、不信任外部文本、输出过滤 |
| 过度自动化 | 全自动合并/部署，出错无人兜底 | Human-in-the-loop、灰度、可回滚 |

---

## 实用框架推荐

| 框架 | 特点 | 适合 |
|------|------|------|
| **Claude Agent SDK** | 与 Claude Code 同源，工具/子 Agent/权限体系完整 | 生产级编码 Agent |
| **OpenAI Agents SDK** | 官方 Agent 编排，工具/交接/追踪 | OpenAI 生态 |
| **LangChain / LangGraph** | 生态大，图式编排灵活 | 快速原型、复杂流程 |
| **LlamaIndex** | 专注数据与 RAG | 知识型 Agent |
| **AutoGen** | 微软，多 Agent 对话 | 研究/复杂协作 |
| **CrewAI** | 角色扮演式多 Agent | 业务流程模拟 |
| **Dify** | 可视化，国内流行 | 非开发者 |

> 选型建议：先问"我到底需不需要 Agent"。**能用固定工作流解决的，不要上 Agent**——确定性更高、成本更低、更好测。

---

## 参考资源

- [Learn Claude Agents](https://www.anthropic.com/engineering/building-effective-agents) — 从零实现 Agent 循环
- [Building effective agents（Anthropic）](https://www.anthropic.com/engineering/building-effective-agents) — workflow vs agent 的经典区分
- [Demystifying evals for AI agents（Anthropic）](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — Agent 评测方法论
- [Effective context engineering（Anthropic）](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — 长任务上下文管理

---

## 历史沿革

- **2026**：子 Agent / Agent Teams 产品化；规划、上下文工程、评测成为 Agent 工程三件套；MCP 与 Skills 标准化。
- **2025**：ReAct 之后的 planning 模式普及；Agent SDK、MCP、Agentic RAG 爆发；"上下文工程"成为独立学科。
- **2024**：Function Calling 成熟；AutoGen/CrewAI 等多 Agent 框架流行；编码 Agent 开始进入日常开发。
- **2023**：ReAct 论文影响扩大；"LLM + 工具 + 循环"成为 Agent 的标准定义。
- **2022 及以前**：工具调用尚属研究原型，Agent 更多是"自动规划"的学术概念。

---

## 下一步

- [M4-04 MCP 协议](./04-mcp.md) — 工具调用的标准化协议
- [M4-05 上下文工程](./05-context-engineering.md) — Agent 长任务的核心工程
- [M4-06 评测与质量闭环](./06-evaluation.md) — 如何判断 Agent 是否可靠
- [M5-02 Agentic 开发工作流](../05-practical/02-workflow.md) — 实战应用
