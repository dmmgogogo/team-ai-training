# 🤖 AI 技术培训课程

> 面向技术团队，帮助大家了解 AI 大模型原理、主流工具及实战应用。
>
> 📌 本课程持续更新，建议收藏。欢迎提 Issue 反馈或补充内容。

---

## 课程目标

- 理解 AI 大模型的工作原理，不再"黑盒"
- 掌握国内外主流模型的特点和选型方法
- 上手主流 AI 编程工具，提升开发效率
- 具备基本的 Prompt 工程能力
- 了解 AI 使用中的安全、成本与质量控制

---

## 课程模块

| 编号 | 模块 | 内容概述 | 适合人群 |
|------|------|----------|----------|
| [M1](./01-llm-basics/) | **AI 大模型基础** | 什么是 LLM、Transformer、训练过程、核心概念 | 所有人 |
| [M2](./02-llm-landscape/) | **国内外主流大模型** | GPT/Claude/Gemini/DeepSeek 等横向对比 | 所有人 |
| [M3](./03-ai-coding-tools/) | **AI 编程工具全景** | Cursor、Copilot、Claude Code 等工具使用 | 开发同学 |
| [M4](./04-principles/) | **底层原理深入** | Attention 机制、RAG、Agent、MCP | 有兴趣深入的同学 |
| [M5](./05-practical/) | **实战与最佳实践** | Prompt 工程、工具调用、Skills、Multi-Agent、安全隐私、成本管理 | 所有人 |
| [M6](./06-ai-project-setup/) | **AI 项目配置规范** | .cursorrules、项目上下文文档、MCP 集成 | 开发同学 |
| [M7](./07-skills/) | **Skills 精选** | GPT Store、Claude Projects、Cursor Rules 社区精选 | 所有人 |
| [M8](./08-mcp/) | **MCP 精选** | 开发/数据库/效率/通用工具类 MCP 完整指南 | 开发同学 |
| [M9](./09-openclaw/) | **OpenClaw 小🦞** | 自托管 AI 网关：Telegram/Discord 随时用 AI | 所有人 |

---

## 学习路径推荐

```
入门路线（非技术 / 管理）:
  M1-01 → M1-04 → M2-01 → M2-02 → M5-01

开发路线（技术同学）:
  M1（全） → M2（全） → M3（全） → M4 → M5 → M6

深度路线（想深入研究）:
  全部模块顺序学习
```

---

## 各模块文件索引

### M1 · AI 大模型基础
- [M1-01 什么是大语言模型](./01-llm-basics/01-what-is-llm.md)
- [M1-02 Transformer 架构](./01-llm-basics/02-transformer.md)
- [M1-03 训练过程：预训练、微调与 RLHF](./01-llm-basics/03-training.md)
- [M1-04 核心概念速查](./01-llm-basics/04-key-concepts.md)

### M2 · 国内外主流大模型
- [M2-01 国际主流模型](./02-llm-landscape/01-global-models.md)
- [M2-02 国内主流模型](./02-llm-landscape/02-domestic-models.md)
- [M2-03 模型横向对比与选型](./02-llm-landscape/03-comparison.md)

### M3 · AI 编程工具全景
- [M3-01 AI 编程工具概览](./03-ai-coding-tools/01-overview.md)
- [M3-02 Cursor 使用指南](./03-ai-coding-tools/02-cursor.md)
- [M3-03 其他主流工具](./03-ai-coding-tools/03-other-tools.md)
- [M3-04 AI 编程工具底层原理](./03-ai-coding-tools/04-how-it-works.md)

### M4 · 底层原理深入
- [M4-01 Attention 机制详解](./04-principles/01-attention.md)
- [M4-02 RAG 检索增强生成](./04-principles/02-rag.md)
- [M4-03 AI Agent 智能体原理](./04-principles/03-agent.md)
- [M4-04 MCP 模型上下文协议](./04-principles/04-mcp.md)

### M5 · 实战与最佳实践
- [M5-01 ⭐️ Prompt 工程入门](./05-practical/01-prompt-engineering.md)
- [M5-02 AI 辅助开发工作流](./05-practical/02-workflow.md)
- [M5-03 避坑指南与注意事项](./05-practical/03-pitfalls.md)
- [M5-04 Tools：工具调用](./05-practical/04-tools.md)
- [M5-04b ⭐️ Skills：技能扩展（重要）](./05-practical/04-skills.md)
- [M5-05 ⭐️ Multi-Agent 多智能体实战](./05-practical/05-multi-agent.md)
- [M5-06 ⭐️ Cursor 正确配置与高效使用](./05-practical/06-cursor-setup.md)
- [M5-07 ChatGPT 正确配置与高效使用](./05-practical/07-chatgpt-setup.md)
- [M5-08 Claude 正确配置与高效使用](./05-practical/08-claude-setup.md)
- [M5-09 ⭐️ AI 安全与数据隐私](./05-practical/09-security-privacy.md)
- [M5-10 ⭐️ 代码审查与质量控制](./05-practical/10-code-review.md)
- [M5-11 ⭐️ 成本管理与模型选型](./05-practical/11-cost-management.md)

### M6 · AI 项目配置规范
- [M6-01 ⭐️ .cursorrules 配置指南](./06-ai-project-setup/01-cursorrules.md)
- [M6-02 ⭐️ 给 AI 喂上下文：项目文档规范](./06-ai-project-setup/02-ai-context.md)
- [M6-03 MCP 项目集成](./06-ai-project-setup/03-mcp-integration.md)
- [M6-04 ⭐️ 真实案例：全栈项目 AI 配置实战](./06-ai-project-setup/04-real-world-template.md)

### M7 · Skills 精选
- [M7-01 ⭐️ ChatGPT GPT Store 精选（开发向）](./07-skills/01-chatgpt-gpts.md)
- [M7-02 ⭐️ Claude Projects 开发最佳实践](./07-skills/02-claude-projects.md)
- [M7-03 ⭐️ Cursor Rules 社区精选](./07-skills/03-cursor-rules.md)

### M8 · MCP 精选
- [M8-01 ⭐️ 开发工具类 MCP](./08-mcp/01-dev-tools.md)
- [M8-02 ⭐️ 数据库类 MCP](./08-mcp/02-database.md)
- [M8-03 效率工具类 MCP](./08-mcp/03-productivity.md)
- [M8-04 ⭐️ 通用工具类 MCP](./08-mcp/04-utilities.md)

### M9 · OpenClaw 小🦞
- [M9-01 ⭐️ 什么是 OpenClaw](./09-openclaw/01-intro.md)
- [M9-02 ⭐️ 安装与配置](./09-openclaw/02-setup.md)
- [M9-03 ⭐️ Skills 与 MCP 接入](./09-openclaw/03-skills-mcp.md)

### M10 · AI Cloud Agent

- [M10-01 ⭐️ 什么是 AI Cloud Agent](./10-cloud-agent/01-what-is-cloud-agent.md)
- [M10-02 ⭐️ Cloud Agent 工作原理](./10-cloud-agent/02-how-it-works.md)
- [M10-03 ⭐️ 如何使用 Cloud Agent（实战）](./10-cloud-agent/03-using-cloud-agent.md)
- [M10-04 自建 Cloud Agent 工作流](./10-cloud-agent/04-build-your-own.md)

---

## 参考资源

> 所有链接均经过验证，可直接访问。完整链接库见 [📚 参考资源页](./references.md)。

### 评测榜单（第三方，客观中立）
- [LMArena](https://lmarena.ai) — 人类偏好排行榜，600万+真实用户投票
- [SWE-bench](https://www.swebench.com) — AI 代码能力黄金评测
- [Artificial Analysis](https://artificialanalysis.ai/leaderboards/models) — 速度/质量/价格综合对比

### 官方文档
- [OpenAI 文档](https://platform.openai.com/docs) — GPT 系列
- [Anthropic 文档](https://docs.anthropic.com) — Claude 系列
- [Google AI](https://ai.google.dev) — Gemini 系列
- [DeepSeek 开放平台](https://platform.deepseek.com) — DeepSeek 系列
- [阿里云百炼](https://help.aliyun.com/zh/model-studio) — 通义千问 Qwen

### 学习资源
- [Learn Claude Agents](https://learn-claude-agents.vercel.app/zh/s01/) — Agent 开发入门（本课程参考）
- [OpenAI Cookbook](https://cookbook.openai.com) — 官方代码示例
- [Papers with Code](https://paperswithcode.com) — 最新 AI 论文与代码

---

*课程持续更新中。AI 领域发展迅速，建议每季度复习一次。*
