# ⭐️ M5-12 · Agent 自审查与自迭代实战

> 把“目标 Loop、自审查、自迭代”落到日常开发：让 AI 不只是写代码，还能按目标自查、修正、验证，并在该停的时候停。

---

## 适合什么场景？

适合用自迭代闭环的任务：

- 修 Bug：需要定位、修改、跑测试、再修
- 小型功能：需要实现、补测试、更新文档
- 重构：需要保持行为不变
- PR 预审：需要先找明显问题再交给人类
- 文档维护：需要检查链接、目录、时间戳是否一致

不适合完全自动循环的任务：

- 需求还不清楚
- 涉及高风险数据或生产权限
- 没有测试、没有验收标准
- 产品方向需要人做判断

---

## 推荐工作流

```text
1. 写清目标
2. 让 Agent 先出计划
3. 执行最小改动
4. 自审查 diff
5. 运行测试/检查
6. 根据结果最多修 2-3 轮
7. 输出证据，让人最终确认
```

---

## 可复制 Prompt 模板

### 模板 1：通用自迭代任务

```text
请按“目标闭环”完成这个任务：

目标：
[写清楚要完成什么]

约束：
- 先输出简短计划，再动手
- 每轮修改后自查 diff
- 必须运行可用的测试/检查命令
- 最多自我修复 3 轮，超过就停止并说明卡点
- 最终输出：改了什么、验证证据、剩余风险
```

### 模板 2：Bug 修复

```text
请修复这个 Bug，并使用自审查流程：

现象：
[报错/截图/日志]

期望：
[正确行为]

流程：
1. 先定位最可能的原因
2. 做最小必要修改
3. 增加或更新测试
4. 运行测试
5. 如果失败，最多再修 2 轮
6. 最后给出验证证据
```

### 模板 3：PR 交付前自查

```text
请在提交前做一次自审查：

检查维度：
- 是否满足原始需求
- 是否有明显 Bug
- 是否有安全风险
- 是否有不必要的大改
- 是否更新了文档/测试

如果发现问题，请先修复；如果问题需要人工判断，请列入“需要人工确认”。
```

---

## Cursor / Claude Code / Cloud Agent 怎么用？

| 工具 | 推荐方式 |
|------|----------|
| Cursor Agent | 适合短闭环：改代码、跑测试、自查 diff |
| Claude Code | 适合代码库级闭环：跨文件改造、重构、长任务 |
| Cloud Agent | 适合异步闭环：让 Agent 自己跑完并提交 PR |
| GitHub Actions | 适合机器验收：测试、lint、链接检查、格式检查 |

---

## 最小可用规则

如果团队只想先落地一条规则，可以写进 `.cursor/rules/*.mdc` 或项目 `AGENT.md`：

```md
When implementing a task:
1. Restate the goal briefly.
2. Make the smallest safe change.
3. Review your own diff before finalizing.
4. Run available checks.
5. If checks fail, fix at most 3 rounds.
6. Stop and ask for human review if the same failure repeats.
7. Final response must include changed files, validation evidence, and residual risks.
```

---

## 一个具体例子：修接口 Bug

```text
目标：修复 /api/orders 在 user_id 缺失时报 500 的问题。

Agent 闭环：
1. Plan：检查路由、参数校验、错误处理中间件
2. Act：增加 user_id 参数校验
3. Verify：跑 orders API 测试
4. Review：检查是否影响其他接口
5. Revise：若测试失败，只改失败原因
6. Done：输出 diff + 测试结果
```

---

## 验收清单

每个自迭代任务结束前，至少回答：

- [ ] 原始目标是否达成？
- [ ] 改动是否最小？
- [ ] 是否跑了测试/检查？
- [ ] 是否自查过 diff？
- [ ] 是否说明了剩余风险？
- [ ] 是否达到最大迭代轮数？

---

## 避免“自动发疯”的 6 条规则

| 问题 | 规则 |
|------|------|
| 一直修不好 | 最多 3 轮，失败就停 |
| 越改越大 | 每轮只允许改当前失败相关内容 |
| 没证据就说成功 | 必须贴测试/命令/截图/链接证据 |
| 目标漂移 | 每轮 Review 都引用原始目标 |
| 成本爆炸 | 长日志只给路径，不整段粘贴 |
| 风险操作 | 删除数据、改权限、上线部署必须人工确认 |

---

## 和现有章节的关系

- [M4-05 Agent 自审查与自迭代循环](../04-principles/05-agent-self-improvement-loop.md)：原理
- 本章：实战模板和团队规则
- [M5-05 Multi-Agent 多智能体实战](./05-multi-agent.md)：多 Agent 协作实现
- [M5-10 代码审查与质量控制](./10-code-review.md)：审查标准
- [M11-03 Superpowers](../11-dev-tools/03-superpowers.md)：现成工作流工具
- [M11-04 gstack](../11-dev-tools/04-gstack.md)：多角色审查工具

---

## 一句话总结

> 自迭代不是让 AI 无限重试，而是让它在明确目标、明确验收、明确上限的情况下，自己完成“写完以后再检查一遍”的工程习惯。

---

*← 返回 [M5 实战与最佳实践](./README.md) | [课程总览](../README.md)*
