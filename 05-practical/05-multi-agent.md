# M5-05 · Multi-Agent 多智能体实战

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 一个 AI 不够用时，让多个 AI 分工协作。2026 年的新变化是：多 Agent 从"自己写框架"变成了**客户端原生能力**——Claude Code 有了 Agent Teams，Claude 有了 Cowork / Duet，子 Agent 与并行会话成为日常操作。

---

## 一句话结论

- 多 Agent 的价值不在"多"，而在**上下文隔离 + 并行探索 + 互相挑战**。
- 2026-11 最实用的三种形态：**子 Agent（Subagents）**、**Agent Teams**、**并行会话 / Worktree**。
- 多 Agent 的成本、协调开销和失败模式都是真实的：**先单 Agent，跑不动再拆**。

---

## 一、为什么需要多 Agent？

单个 Agent 的局限：

- 上下文窗口有限，复杂任务装不下；
- 长任务容易"跑偏"，中途失去目标；
- 不同子任务适合不同的模型、工具、权限；
- 串行处理，无法并行提速；
- 单一视角容易"找到一个解释就停"。

**Multi-Agent 的解法**：把任务拆开，让每个 Agent 在自己的上下文里独立工作，再汇总或互相校验。

---

## 二、五种编排形态（2026-11 版）

| 形态 | 谁在协调 | 上下文 | 典型场景 | 2026 工具 |
|------|----------|--------|----------|-----------|
| **单 Agent + 子 Agent** | 主 Agent | 子 Agent 独立，结果回传 | 调研、检索、局部修改 | Claude Code Subagents、Cursor Subagents |
| **Agent Teams** | Team Lead | 每个 teammate 完全独立，可互相通信 | 并行评审、竞争性假设、跨层改动 | Claude Code Agent Teams（实验性） |
| **并行会话 / Worktree** | 人 | 各自独立 | 多个互不干扰的任务同时推进 | Claude Code `--worktree`、git worktree |
| **任务分片（Cowork 式）** | 产品内置 | 按任务分片并行 | 长任务、交付物型工作 | Claude Cowork |
| **图/流水线编排** | 代码 | 由状态显式传递 | 步骤固定、需要回退与分支 | LangGraph、自研编排 |

### 模式一：协调者 + 执行者

```
用户需求
    ↓
协调者 Agent（规划、分配、汇总）
    ├─→ 执行者 A（搜索信息）
    ├─→ 执行者 B（分析数据）
    └─→ 执行者 C（撰写报告）
    ↓
协调者汇总，输出最终结果
```

### 模式二：流水线

```
Agent 1（收集） → Agent 2（清洗） → Agent 3（分析） → Agent 4（成稿）
```

### 模式三：专家评审团 / 对抗辩论

```
问题 → 并行发给多个专家 Agent
    ├─ 安全专家
    ├─ 性能专家
    └─ 架构专家
        ↓
互相挑战 → 汇总 → 最终建议
```

> 2026 年最被低估的是「对抗辩论」：让多个 Agent 各自提出假设并**试图证伪对方**，能显著降低"锚定效应"导致的错误结论。

---

## 三、实战：Claude Code Agent Teams（2026 原生能力）

Claude Code 的 Agent Teams 让多个 Claude Code 实例作为一个团队协作：一个会话当 **Team Lead**，负责拆任务、分配、汇总；其他 **Teammates** 各自在独立上下文里工作，并可以直接互相发消息。

> 官方文档：[Orchestrate teams of Claude Code sessions](https://code.claude.com/docs/en/agent-teams)（访问于 2026-11）。**Agent Teams 目前是实验性功能，默认关闭。**

### 开启

```json
// ~/.claude/settings.json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

开启后，用自然语言描述任务和你想要的队友即可：

```text
I'm designing a CLI tool that helps developers track TODO comments across
their codebase. Spawn three teammates to explore this from different angles:
one on UX, one on technical architecture, one playing devil's advocate.
```

### 它由什么组成

| 组件 | 作用 |
|------|------|
| **Team Lead** | 主会话，创建任务、分配、汇总 |
| **Teammates** | 独立 Claude Code 实例，各有自己的上下文窗口 |
| **共享任务列表** | 任务有 pending / in progress / completed 三态，可设置依赖；认领时用文件锁防并发冲突 |
| **Mailbox** | Agent 之间的消息系统，存放于 `~/.claude/teams/{team}/inboxes/*.json` |

### 两种显示模式

| 模式 | 说明 | 要求 |
|------|------|------|
| **in-process**（默认） | 所有 teammate 跑在主终端，用方向键切换、Enter 查看/对话 | 任意终端 |
| **split panes** | 每个 teammate 一个窗格 | tmux 或 iTerm2 + `it2` CLI |

### 两种典型用法

```text
// 并行代码审查：每个 teammate 一个视角
Spawn three teammates to review PR #142:
- One focused on security implications
- One checking performance impact
- One validating test coverage
Have them each review and report findings.
```

```text
// 竞争性假设：让它们互相证伪
Users report the app exits after one message instead of staying connected.
Spawn 5 agent teammates to investigate different hypotheses. Have them talk to
each other to try to disprove each other's theories, like a scientific debate.
```

### 官方给出的实践建议（原文要点）

1. **先从研究与评审开始**：边界清晰、不写代码，最容易体现并行价值。
2. **团队规模 3–5 人起步**：token 成本随 teammate 线性增长，3 个专注的队友常胜于 5 个分散的。
3. **每个 teammate 5–6 个任务**：任务太小协调开销大于收益，太大容易跑偏。
4. **避免文件冲突**：两个 teammate 改同一个文件会互相覆盖，按文件/模块切分工作。
5. **及时监控与干预**：不要让团队长时间无人看管。
6. **给足上下文**：teammate 不继承 lead 的对话历史，spawn prompt 要自带任务细节。

### 已知限制（务必知道）

| 限制 | 影响 |
|------|------|
| 实验性功能，默认关闭 | 需要显式开启；行为可能变化 |
| 会话恢复不保留 in-process teammate | `/resume`、`/rewind` 后队友可能"消失" |
| 任务状态可能滞后 | teammate 忘记标记完成会阻塞依赖任务 |
| 一个会话只能有一个 team | 不能创建多个命名团队，也不能跨会话共享 |
| 不支持嵌套团队 | teammate 不能再创建 teammate |
| Lead 固定 | 不能把 teammate 提升为 lead |
| spawn 时不能单独设置权限模式 | teammate 继承 lead 的权限模式 |
| split panes 需要 tmux/iTerm2 | 部分终端不支持 |

> 这些限制会随版本变化，使用前请以[官方文档](https://code.claude.com/docs/en/agent-teams)为准。

---

## 四、Subagents vs Agent Teams：别用错

这是官方文档里的核心对比，直接决定成本和效果：

| | 子 Agent（Subagents） | Agent Teams |
|--|----------------------|-------------|
| **上下文** | 独立上下文，结果返回调用方 | 独立上下文，完全独立 |
| **通信** | 向调用方返回结果 | teammate 之间可直接互发消息 |
| **协调** | 主 Agent 管理全部工作 | 自协调 + 共享任务列表 |
| **适合** | 只需要结果的聚焦任务 | 需要讨论、协作、互相挑战的复杂任务 |
| **token 成本** | 较低（结果摘要回主上下文） | 较高（每个 teammate 是独立实例） |

**选择原则**：

```
只需要一个结果？         → 子 Agent
需要多个角色讨论/互评？   → Agent Teams
需要隔离运行环境？       → Worktree + 独立会话
步骤固定、要可回退？      → 图编排（LangGraph 等）
```

---

## 五、Context 隔离：多 Agent 的真正难点

多 Agent 系统的成败，80% 取决于上下文管理，而不是模型选型。

| 问题 | 表现 | 做法 |
|------|------|------|
| **上下文不继承** | teammate 不知道 lead 刚讨论过什么 | spawn prompt 自带背景、目标、约束、交付格式 |
| **信息发霉** | 早期结论没同步，后续基于旧信息工作 | 共享任务列表 + 明确的"事实文件"（如 findings.md） |
| **文件冲突** | 两个 Agent 改同一文件 | 按文件/目录切分；或用 git worktree 隔离 |
| **上下文膨胀** | 所有中间结果都塞回主会话 | 子 Agent 只回摘要；大结果落盘给路径 |
| **责任不清** | 多 Agent 互相等待 | 明确 owner、依赖关系、完成标准 |

Claude Code 中，每个 teammate 启动时会加载与普通会话相同的项目上下文（CLAUDE.md、MCP、skills），但**不会加载 lead 的对话历史**——这条规则值得所有多 Agent 系统借鉴。

---

## 六、Claude Cowork 与 Duet：2026 的"产品化多 Agent"

除了开发者自己编排，2026 年 Anthropic 还把多 Agent 做进了产品：

| 产品 | 形态 | 关键点 |
|------|------|--------|
| **Claude Cowork** | 桌面/网页/移动端的"任务执行器" | 处理你指定的文件夹与工具；一个任务会拆成多个分片并行（边起草边调研）；可定时无人值守运行；内置独立浏览器 |
| **Claude Duet** | 主动型 agent（research preview） | 由 Opus 5.5 驱动；每天主动汇报、起草下一步，需要时等你确认；Pro/Max/Ultra，美国先行 |

> 说明：Claude Cowork 已并入 Claude 主产品（"Claude Cowork is now just Claude"），入口在 Claude 应用内。Duet 仍为研究预览（来源：[Claude Cowork](https://claude.com/product/cowork)、[Claude Duet](https://claude.com/product/claude-duet)，访问于 2026-11）。

**对团队的启示**：未来大多数同事接触到的"多 Agent"，不是他在写编排代码，而是产品在后台自动分片并行。理解分片、审批、成本，比会写框架更重要。

---

## 七、成本与失败模式

| 风险 | 说明 | 对策 |
|------|------|------|
| **成本爆炸** | token 随 teammate 数量线性增长 | 设预算上限；先 3 个；例行任务用单 Agent |
| **协调开销** | 沟通、任务分配、冲突处理本身耗时间 | 任务粒度适中（5–6 个/人）；减少不必要的通信 |
| **错误传播** | A 的错误输出被 B 当真 | 关键节点人工审核；要求给出证据/来源 |
| **死循环 / 空转** | Agent 反复调用、互相等待 | 最大轮次；超时；明确完成标准 |
| **任务状态滞后** | 依赖任务被永久阻塞 | 定期检查任务列表；必要时手动更新状态 |
| **文件冲突** | 并行写同一文件互相覆盖 | 按 owner 切分文件；worktree 隔离 |
| **过早收敛** | lead 认为完成，实际有任务没做完 | 显式验收清单；用 hook 做质量门禁 |
| **调试困难** | 链路长，难以复现 | 记录每步输入输出；保留中间产物 |

### 什么时候**不该**用多 Agent

- 任务本身是线性的、强依赖的；
- 大部分工作要改同一批文件；
- 预算敏感、时效要求高；
- 你还没把单 Agent 的提示词和上下文调好。

> 经验法则：**单 Agent + 好上下文**能解决 80% 的任务；剩下 20% 里，一半用子 Agent 就够，真正需要 Agent Teams 的是"需要多视角互相挑战"的场景。

---

## 八、经典框架（2023–2025 主流，现在仍然可用）

这些框架是多 Agent 工程化的"必修历史"，也是自研编排时最好的参考实现。API 可能随版本变化，示例仅示意，请以官方文档为准。

### AutoGen（微软）

以"多 Agent 对话"为核心，适合代码执行、角色对话类任务。

```python
import autogen

config_list = [{"model": "<你的模型>", "api_key": "..."}]
llm_config = {"config_list": config_list}

user_proxy = autogen.UserProxyAgent(
    name="用户",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    code_execution_config={"work_dir": "workspace", "use_docker": False},
)

programmer = autogen.AssistantAgent(
    name="程序员",
    llm_config=llm_config,
    system_message="你是 Python 专家，负责编写和调试代码。",
)

reviewer = autogen.AssistantAgent(
    name="代码审查员",
    llm_config=llm_config,
    system_message="你是代码审查专家，检查质量、安全与性能。",
)

user_proxy.initiate_chat(programmer, message="写一个抓取 Hacker News 热榜并保存 CSV 的脚本")
```

### CrewAI

用"角色扮演"定义团队：role / goal / backstory / tools。

```python
from crewai import Agent, Task, Crew

researcher = Agent(
    role="AI 市场研究员",
    goal="收集 AI 工具市场的最新动态",
    backstory="专注 AI 领域的市场研究员，擅长信息收集与整理",
    tools=[search_tool],
)

writer = Agent(
    role="技术文档作者",
    goal="把研究结果整理成结构清晰的文档",
    backstory="经验丰富的技术写作者",
)

research_task = Task(
    description="调研 2026 年最热门的 5 个 AI 编程工具",
    expected_output="包含 5 个工具信息的结构化数据",
    agent=researcher,
)
writing_task = Task(
    description="基于研究结果写一篇开发者推荐报告",
    expected_output="1000 字左右的 Markdown 报告",
    agent=writer,
)

crew = Crew(agents=[researcher, writer], tasks=[research_task, writing_task])
result = crew.kickoff()
```

### LangGraph

用有向图 + 显式状态控制流程，适合需要回退、分支、人工介入的复杂工作流。

```python
from typing import TypedDict
from langgraph.graph import StateGraph, END

class State(TypedDict):
    query: str
    search_result: str
    code: str
    review_result: str

def search_node(state):
    return {"search_result": web_search(state["query"])}

def code_node(state):
    return {"code": llm.generate_code(state["search_result"])}

def review_node(state):
    return {"review_result": llm.review_code(state["code"])}

def should_revise(state):
    return "code" if "需要修改" in state["review_result"] else END

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

### 框架选型（2026-11 视角）

| 方案 | 适合场景 | 备注 |
|------|----------|------|
| **Claude Code Agent Teams** | 需要讨论、互评、并行探索 | 实验性；原生集成最好 |
| **Claude Code Subagents** | 聚焦子任务、结果回传 | 成本更低，优先考虑 |
| **AutoGen** | 多 Agent 对话、代码执行 | 经典框架，注意版本变化 |
| **CrewAI** | 角色分工明确的团队 | 上手快，适合原型 |
| **LangGraph** | 复杂有状态工作流 | 可控性强，学习曲线陡 |
| **Dify** | 可视化编排、非开发者 | 适合业务同学 |
| **自研** | 有特殊合规/集成要求 | 建议先参考上面框架的设计 |

---

## 九、历史沿革

| 时间 | 事件 |
|------|------|
| 2023 | AutoGen、CrewAI 等框架兴起，"多 Agent 对话"成为研究热点 |
| 2024 | LangGraph 等"图编排"方案成熟，强调状态与可控性 |
| 2025 | 编码 Agent 普及，子 Agent / 并行会话进入日常开发 |
| 2025–2026 | 多 Agent 从"框架能力"变成"客户端原生能力" |
| 2026 | Claude Code Agent Teams（实验性）、Claude Cowork 任务分片、Claude Duet 主动型 agent 出现 |
| 2026-11 | Agent Teams 仍需显式开启；多 Agent 的成本与协调问题被官方明确写入文档 |

---

## 十、下一步

- [M5-06 Cursor 正确配置与使用](./06-cursor-setup.md)
- [M5-07 ChatGPT 正确配置与使用](./07-chatgpt-setup.md)
- [M5-08 Claude 正确配置与使用](./08-claude-setup.md)
- [⭐️ M5-11 成本管理与模型选型](./11-cost-management.md)
