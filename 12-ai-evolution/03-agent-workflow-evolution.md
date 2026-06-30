# M12-03 · Agent 工作流演进

> Agent 的发展不是从“不会做事”突然变成“全自动工程师”，而是经历了多个工作流阶段。理解这些阶段，团队才能判断新工具到底先进在哪里。
>
> 最后更新：2026年6月

---

## 阶段 1：单轮问答

```text
用户提问 → 模型回答
```

代表：

- ChatGPT 早期使用方式
- 普通问答助手

问题：

- 不能主动调用工具
- 不能验证答案
- 不能持续完成任务

---

## 阶段 2：工具调用

```text
用户目标 → 模型选择工具 → 调用工具 → 返回答案
```

代表：

- Function Calling
- Tools
- MCP

价值：

- 模型能查资料、读文件、调 API
- 从“只会说”变成“能动手”

新问题：

- 调错工具
- 工具结果没验证
- 工具太多导致上下文膨胀

---

## 阶段 3：ReAct 循环

```text
Reason → Act → Observe → Reason → Act ...
```

代表：

- Cursor Agent
- Claude Code
- 大多数 Coding Agent

价值：

- 能多步骤完成任务
- 能根据工具结果继续行动

新问题：

- 可能跑偏
- 可能无限循环
- 可能宣布成功但没有证据

---

## 阶段 4：Plan-and-Act

```text
先计划 → 再执行 → 再根据结果调整
```

代表：

- Plan Mode
- 复杂任务拆解
- Cloud Agent 异步执行

价值：

- 降低盲目动手带来的返工
- 更适合跨文件、跨模块任务

新问题：

- 计划可能过大
- 执行中仍会偏离目标
- 需要中途检查点

---

## 阶段 5：Goal Loop / 自审查 / 自迭代

```text
Goal → Plan → Act → Review → Revise → Verify → Done
```

这是当前最值得团队理解的新阶段。

它解决的是：

- Agent 做完后没人检查
- Agent 改错方向后继续错
- Agent 没有测试证据也说完成
- Agent 长任务中忘记原始目标

核心机制：

| 机制 | 作用 |
|------|------|
| Goal | 每轮都回到原始目标 |
| Critic / Reviewer | 独立找问题 |
| Reflexion | 失败后总结原因再重试 |
| Eval | 用测试/规则/人工标准验收 |
| Stop Condition | 限制最大轮次，避免死循环 |

---

## 阶段 6：角色化 Agent Team

```text
PM / Architect / Builder / Reviewer / QA / Security
```

代表：

- gstack
- Superpowers
- Agent Teams

价值：

- 把软件开发流程拆成多个角色
- 让 AI 不只是“写代码”，还参与计划、审查、测试、发布

风险：

- 多 Agent 成本更高
- 编排复杂
- 如果没有验收标准，只是“多个 AI 一起胡说”

---

## 判断一个新 Agent 工具先进不先进

不要只看它说“全自动”。看这 6 点：

1. 是否能明确保存目标？
2. 是否有计划阶段？
3. 是否能调用真实工具？
4. 是否有自审查或 Reviewer？
5. 是否有可验证 Eval？
6. 是否有停止条件和人工接管点？

如果没有第 4-6 点，它只是普通 Agent，不是真正可靠的工程工作流。

---

## 和课程其他模块的关系

- [M4-03 Agent 原理](../04-principles/03-agent.md)：ReAct 基础循环
- [M4-05 Agent 自审查与自迭代循环](../04-principles/05-agent-self-improvement-loop.md)：Goal Loop 原理
- [M5-12 Agent 自审查与自迭代实战](../05-practical/12-agent-self-review-loop.md)：团队落地模板
- [M10 AI Cloud Agent](../10-cloud-agent/)：异步执行和 PR 交付
- [M11 Superpowers / gstack](../11-dev-tools/)：现成工具案例

---

## 一句话总结

> Agent 技术的演进主线，是从“能回答”到“能执行”，再到“能围绕目标自我检查并交付可验证结果”。

---

## 下一步

- [M12-04 新版本评估模板](./04-release-review-template.md)
