# M4-05 · Agent 自审查与自迭代循环

> 从“会调用工具的 Agent”进化到“能围绕目标持续改进的 Agent”，关键是加入目标状态、评审器、验收标准和重试边界。

---

## 为什么需要这一章？

传统 ReAct 循环解决的是：

```text
思考 → 行动 → 观察 → 再行动
```

但真实开发任务只靠这个还不够。因为 Agent 很容易出现：

- 做着做着忘记原始目标
- 工具调用成功，但结果不符合需求
- 代码能跑，但设计不优雅
- 一直修，修不完，进入死循环

所以新的 Agent 工作流会在 ReAct 外面再套一层 **目标闭环（Goal Loop）**：

```text
Goal → Plan → Act → Review → Revise → Verify → Done
```

---

## 核心概念

## 1. Goal Loop：目标闭环

Goal Loop 不是“让模型一直循环”，而是让每一轮都回到同一个问题：

> 当前结果是否已经满足最初目标？

一个健康的目标闭环至少包含：

| 元素 | 作用 |
|------|------|
| Goal | 明确最终要达成什么 |
| Plan | 拆出可执行步骤 |
| Act | 修改代码、调用工具、执行命令 |
| Review | 检查结果是否偏离目标 |
| Verify | 用测试、构建、规则或人工标准验收 |
| Stop | 达标或达到上限就停止 |

---

## 2. Critic / Reviewer：自审查角色

自审查不是让同一个模型简单说“我做得好不好”，而是给它一个不同角色：

```text
Builder：负责生成方案和修改代码
Reviewer：负责找问题、质疑假设、检查边界条件
Verifier：负责跑测试、检查验收标准
```

这可以是：

- 同一个模型的不同 prompt
- 多个子 Agent
- 一个固定检查清单
- 测试和静态分析工具

关键是：**不要让“生成者”直接宣布自己成功**。

---

## 3. Reflexion：反思式迭代

Reflexion 的思想是：Agent 每轮失败后，不只是重试，而是先记录失败原因：

```text
尝试 → 失败 → 反思为什么失败 → 更新策略 → 再尝试
```

在编程场景中可以表现为：

- 测试失败后总结失败原因
- 记录“这次修复为什么不够”
- 下一轮只改最小必要范围
- 避免反复尝试同一种错误方案

---

## 4. Eval-driven Agent：验收驱动

更可靠的 Agent 不靠“感觉完成”，而靠可验证标准：

| 验收方式 | 示例 |
|----------|------|
| 单元测试 | `npm test` / `pytest` |
| 类型检查 | `tsc --noEmit` |
| Lint | `eslint` / `ruff` |
| 安全规则 | 禁止读取 `.env`、禁止硬编码密钥 |
| 产品验收 | 页面字段完整、流程可走通 |
| 人工复核 | PR review、截图确认 |

如果没有 Eval，Agent 的“自迭代”很容易变成“自我感觉良好”。

---

## 标准自迭代架构

```text
用户目标
  ↓
Planner：拆计划
  ↓
Builder：执行修改
  ↓
Verifier：运行测试 / 检查规则
  ↓
Reviewer：找缺陷和偏离
  ↓
是否通过？
  ├─ 是 → 输出结果 / 创建 PR
  └─ 否 → 生成修复计划 → 回到 Builder
```

---

## 伪代码

```python
def goal_loop(goal, max_rounds=3):
    plan = planner(goal)
    history = []

    for round_no in range(max_rounds):
        result = builder(plan, history)
        verification = verifier(result)
        review = reviewer(goal, plan, result, verification)

        if review.passed:
            return {
                "status": "done",
                "result": result,
                "evidence": verification,
            }

        history.append({
            "round": round_no + 1,
            "problem": review.problem,
            "fix_hint": review.fix_hint,
        })
        plan = revise_plan(plan, review)

    return {
        "status": "needs_human_review",
        "reason": "max_rounds_reached",
        "history": history,
    }
```

---

## 必须设置边界

自迭代不是越多越好，必须设置停止条件：

| 风险 | 控制方式 |
|------|----------|
| 无限循环 | `max_rounds`，通常 2-5 轮 |
| 过度修改 | 每轮只允许最小必要改动 |
| 成本失控 | 每轮记录 Token/时间/命令次数 |
| 目标漂移 | 每轮 Review 必须引用原始 Goal |
| 假通过 | 必须附测试、diff、截图或日志证据 |

---

## 和已有章节的关系

- [M4-03 Agent 原理](./03-agent.md)：讲基础 ReAct 循环
- 本章：讲 ReAct 之上的目标闭环、自审查、自迭代
- [M5-12 自审查与自迭代实战](../05-practical/12-agent-self-review-loop.md)：讲如何在日常开发里使用
- [M11-03 Superpowers](../11-dev-tools/03-superpowers.md)：现成工具化工作流示例
- [M11-04 gstack](../11-dev-tools/04-gstack.md)：多角色自审查工作流示例

---

## 一句话总结

> Agent 的下一阶段不是“能不能自动做事”，而是“能不能围绕目标自动检查、自动修正，并知道什么时候该停”。

---

*← 返回 [M4 底层原理深入](./README.md) | [课程总览](../README.md)*
