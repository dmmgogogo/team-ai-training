# M0-01 · AI 大事记：从 Transformer 到 Agent 时代（2017–2026）

> 🕰️ 历史档案 ｜ 记录范围：1956 – 2026-11 ｜ 只追加，不回改
> 📅 内容基准：2026-11 ｜ 时效性：历史层（不做时效复检）

---

## 怎么用这张时间线

- **按年份分节**，2026 年精确到季度；表格四列固定：**时间 / 事件 / 为什么重要 / 来源**。
- "为什么重要"写的是**当时的转折意义**，不是跑分排名。
- 日期优先取官方发布日；"发布"和"可用"分开时都写（如预览 → 公开）。
- 查不到确切口径的写"据媒体报道"，不硬编日期。
- 这是一份**只追加**的档案：新事件往对应年份补行，旧行不改。

> 读法建议：先扫 2017–2022 建立骨架，再精读 2023–2026。配合 [M0-02 范式转移](./02-paradigm-shifts.md) 一起看，效果最好。

---

## 一、前史（1956–2016）：问题是怎么被提出的

| 时间 | 事件 | 为什么重要 | 来源 |
|------|------|------------|------|
| 1956-08 | 达特茅斯会议，"Artificial Intelligence" 得名 | 确立了"让机器模拟智能"这一研究议程 | [Wikipedia](https://en.wikipedia.org/wiki/Dartmouth_workshop) |
| 1997-05 | IBM Deep Blue 战胜国际象棋世界冠军卡斯帕罗夫 | "专用智能可超越人类"的第一次大众冲击 | [Wikipedia](https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)) |
| 2012-09 | AlexNet 在 ImageNet 大幅领先 | 深度学习 + GPU 路线被验证，现代 AI 的第一块基石 | [Wikipedia](https://en.wikipedia.org/wiki/AlexNet) |
| 2014-06 | 生成对抗网络（GAN）提出 | 生成式 AI 的早期范式 | [arXiv](https://arxiv.org/abs/1406.2661) |
| 2016-03 | AlphaGo 战胜李世石 | 强化学习进入公众视野 | [Wikipedia](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol) |

> 这一阶段的共同主题：**能力来自专用系统**，离"通用语言模型"还很远。

---

## 二、2017–2021：Transformer 与"预训练 + 微调"

| 时间 | 事件 | 为什么重要 | 来源 |
|------|------|------------|------|
| 2017-06-12 | 《Attention Is All You Need》发表 | Transformer 取代 RNN 成为主流架构，今天所有大模型的底座 | [arXiv](https://arxiv.org/abs/1706.03762) |
| 2018-06 | OpenAI 发布 GPT-1 | 验证"生成式预训练 + 下游微调"路线 | [OpenAI](https://openai.com/research/language-unsupervised) |
| 2019-02 | GPT-2 分阶段开放 | 首次引发"模型太大是否该开源"的公共讨论 | [OpenAI](https://openai.com/research/better-language-models) |
| 2020-05 | GPT-3（175B）论文发布 | 上下文学习（in-context learning）出现，"提示词"开始有意义 | [arXiv](https://arxiv.org/abs/2005.14165) |
| 2020-06 | Scaling Laws 论文 | "参数、数据、算力一起放大"成为可预测的工程路线 | [arXiv](https://arxiv.org/abs/2001.08361) |
| 2021-01 | CLIP / DALL·E 发布 | 图文对齐，多模态生成起步 | [OpenAI](https://openai.com/research/clip) |
| 2021-06 | GitHub Copilot 技术预览 | "AI 写代码"第一次进入日常开发流 | [GitHub Blog](https://github.blog/2021-06-29-introducing-github-copilot-ai-pair-programmer/) |

---

## 三、2022：ChatGPT 破圈

| 时间 | 事件 | 为什么重要 | 来源 |
|------|------|------------|------|
| 2022-08 | Stable Diffusion 开放权重 | 文生图进入"人人可本地跑"阶段 | [Wikipedia](https://en.wikipedia.org/wiki/Stable_Diffusion) |
| 2022-11-30 | **ChatGPT 发布** | 5 天破百万用户；AI 从"技术圈话题"变成"全民产品" | [OpenAI](https://openai.com/index/chatgpt/) |
| 2022-12 | 检索增强生成（RAG）成为企业落地热词（原始论文 2020-05） | 让模型"引用外部知识"，成为企业第一套标准方案 | [arXiv](https://arxiv.org/abs/2005.11401) |

> **这一年定下的默认认知**：AI = 聊天框；提示词写得好，效果就好。

---

## 四、2023：百模大战与"提示词工程"

| 时间 | 事件 | 为什么重要 | 来源 |
|------|------|------------|------|
| 2023-03-14 | **GPT-4 发布** | 多模态输入 + 大幅提升的推理与考试能力，把"能力上限"抬了一档 | [OpenAI](https://openai.com/index/gpt-4-research/) |
| 2023-03-14 | Anthropic 发布 Claude | 以"宪法 AI"和对齐为差异点进入第一梯队 | [Anthropic](https://www.anthropic.com/news/introducing-claude) |
| 2023-03-23 | ChatGPT 插件系统发布 | 第一次尝试"让模型调用外部服务" | [OpenAI](https://openai.com/index/chatgpt-plugins/) |
| 2023-06-13 | OpenAI 发布 Function Calling | 工具调用从"插件"变成**结构化 API**，Agent 的工程基础 | [OpenAI](https://openai.com/index/function-calling-and-other-api-updates/) |
| 2023-07-18 | Llama 2 开放商用 | 开源权重路线成型，私有化部署有了可用选项 | [Meta](https://ai.meta.com/llama/) |
| 2023-11-06 | OpenAI DevDay：GPT-4 Turbo、GPTs | "人人可造自己的 GPT"，应用层生态爆发 | [OpenAI](https://openai.com/index/new-models-and-developer-products-announced-at-devday/) |
| 2023-12-06 | Google 发布 Gemini 1.0 | 原生多模态，三档尺寸（Ultra/Pro/Nano） | [Google Blog](https://blog.google/technology/ai/google-gemini-ai/) |
| 2023 全年 | 国内"百模大战"：文心、通义、智谱、DeepSeek 等密集发布 | 中文模型生态成形，价格战前夜 | [Wikipedia](https://en.wikipedia.org/wiki/List_of_large_language_models) |

> **当时的判断**："提示词工程师"会成为新职业；模型能力靠"更大的模型"解决。

---

## 五、2024：多模态、推理模型与 MCP

| 时间 | 事件 | 为什么重要 | 来源 |
|------|------|------------|------|
| 2024-02-15 | OpenAI 展示 Sora；Google 发布 Gemini 1.5（100 万 token 上下文） | 视频生成与超长上下文同时抬升预期 | [OpenAI](https://openai.com/index/sora/)｜[Google](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/) |
| 2024-03-04 | Claude 3 家族（Opus/Sonnet/Haiku） | "三档尺寸"成为行业通用产品结构 | [Anthropic](https://www.anthropic.com/news/claude-3-family) |
| 2024-05-13 | GPT-4o 发布 | 端到端多模态、低延迟语音，交互形态升级 | [OpenAI](https://openai.com/index/hello-gpt-4o/) |
| 2024-06-20 | Claude 3.5 Sonnet | 代码能力成为模型竞争主战场，"AI 编程"开始普及 | [Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet) |
| 2024-07-23 | Llama 3.1 405B 开放权重 | 开源模型首次接近闭源旗舰 | [Meta](https://ai.meta.com/blog/meta-llama-3-1/) |
| 2024-09-12 | OpenAI o1 发布 | "推理时计算"（test-time compute）成为新缩放维度 | [OpenAI](https://openai.com/index/introducing-openai-o1-preview/) |
| 2024-10-22 | Anthropic 发布 Computer Use | 模型开始"操作电脑"，Agent 从概念走向可演示 | [Anthropic](https://www.anthropic.com/news/3-5-models-and-computer-use) |
| 2024-11-25 | **Anthropic 发布 MCP（模型上下文协议）** | 工具/数据接入从"每家一套"变成开放标准，Agent 生态的地基 | [MCP](https://modelcontextprotocol.io/)｜[Wikipedia](https://en.wikipedia.org/wiki/Model_Context_Protocol) |
| 2024-12-11 | Gemini 2.0 发布 | 面向 Agent 时代设计的一代模型 | [Google](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/) |
| 2024-12-26 | DeepSeek-V3 发布 | 低成本训练 + 开源权重，冲击"算力决定一切"的叙事 | [DeepSeek](https://api-docs.deepseek.com/news/news1226) |

> **当时的判断**："Agent 要来了"；但多数人仍把它理解为"会调用 API 的聊天机器人"。

---

## 六、2025：推理模型、Agent 元年与 Skills

| 时间 | 事件 | 为什么重要 | 来源 |
|------|------|------------|------|
| 2025-01-20 | **DeepSeek-R1 发布** | 开源推理模型比肩闭源，"推理能力"迅速商品化 | [DeepSeek](https://api-docs.deepseek.com/news/news250120) |
| 2025-02-24 | **Claude Code 研究预览** | 终端里的编码 Agent，开启"Agentic Coding"产品形态 | [Wikipedia](https://en.wikipedia.org/wiki/Claude_Code) |
| 2025-03-25 | Gemini 2.5 Pro 发布 | 长上下文 + 推理结合，成为当年最强梯队之一 | [Google](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/) |
| 2025-04-05 | Llama 4 发布 | 开源旗舰的又一次尝试，但口碑分化 | [Meta](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) |
| 2025-04-16 | OpenAI o3 / o4-mini；Codex CLI 开源 | 推理模型 + 本地编码 Agent 同时落地 | [OpenAI](https://openai.com/index/introducing-o3-and-o4-mini/)｜[TechCrunch](https://techcrunch.com/2025/04/16/openai-debuts-codex-cli-an-open-source-coding-tool-for-terminals/) |
| 2025-05-22 | Claude 4（Sonnet 4 / Opus 4） | 编码与 Agent 能力再上一档，Claude Code 正式可用 | [Anthropic](https://www.anthropic.com/news/claude-4) |
| 2025-06 | Andrej Karpathy 提出 **Context Engineering** | 关注点从"写提示词"转向"管理进入模型的全部上下文" | [Anthropic](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) |
| 2025-07-09 | Grok 4 发布 | 推理 + 实时信息，xAI 进入第一梯队讨论 | [xAI](https://x.ai/news/grok-4) |
| 2025-07-17 | ChatGPT Agent 发布 | 通用 Agent 产品化：浏览器、终端、表单一条龙 | [OpenAI](https://openai.com/index/introducing-chatgpt-agent/) |
| 2025-08-07 | GPT-5 发布 | 统一路由（快/慢思考），大版本节奏恢复 | [Wikipedia](https://en.wikipedia.org/wiki/GPT-5) |
| 2025-09-29 | Claude Sonnet 4.5 发布 | 编码与长任务能力成为"可交付"水平 | [Anthropic](https://www.anthropic.com/news/claude-sonnet-4-5) |
| 2025-10-15 | Claude Haiku 4.5 发布 | 小模型也能做 Agent 子任务，成本结构变化 | [Anthropic](https://www.anthropic.com/news/claude-haiku-4-5) |
| 2025-10-16 | **Anthropic 发布 Skills** | 把"可复用的工作流"打包成技能，Agent 能力可沉淀、可分发 | [Simon Willison](https://simonwillison.net/2025/Oct/16/claude-skills/) |
| 2025-11-18 | Gemini 3 Pro 发布 | Google 重回第一梯队，"Deep Think"推理模式 | [Google](https://blog.google/products/gemini/gemini-3/) |
| 2025-11-24 | Claude Opus 4.5 发布 | 编码 Agent 能力跃升，Claude Code 在年末出圈 | [Anthropic](https://www.anthropic.com/news/claude-opus-4-5) |
| 2025-12-01 | DeepSeek-V3.2 发布 | 稀疏注意力 + 更低成本，开源模型继续追平 | [DeepSeek](https://api-docs.deepseek.com/news/news251201) |
| 2025-12-11 | GPT-5.2 发布 | 推理与专业工作能力继续迭代 | [Wikipedia](https://en.wikipedia.org/wiki/GPT-5.2) |
| 2025-12 | MCP 捐赠给 Agentic AI Foundation；Anthropic 发布 Agent Skills 开放标准 | 协议与技能都从"厂商私有"走向"行业公共品" | [MCP](https://en.wikipedia.org/wiki/Model_Context_Protocol) |

> **当时的判断**："2025 是 Agent 元年"。对了一半：Agent 真的能干活了，但可靠性与安全边界成了新瓶颈。

---

## 七、2026：Agent 团队、常驻 Agent 与"AGI 叙事"

### Q1（1–3 月）

| 时间 | 事件 | 为什么重要 | 来源 |
|------|------|------------|------|
| 2026-01-12 | Claude Cowork 研究预览（macOS） | 把 Claude Code 的 Agent 能力带给非程序员，知识工作 Agent 化 | [Claude Release Notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 2026-01-22 | 百度发布 Ernie 5.0 | 国内旗舰进入"原生多模态 + Agent"阶段 | [China Daily](https://global.chinadaily.com.cn/a/202601/22/WS6971d66ba310d6866eb35330.html) |
| 2026-02-05 | **Claude Opus 4.6 + Agent Teams** | 多 Agent 协作从"自己搭"变成产品内置能力 | [TechCrunch](https://techcrunch.com/2026/02/05/anthropic-releases-opus-4-6-with-new-agent-teams/)｜[Claude Code Docs](https://code.claude.com/docs/en/agent-teams) |
| 2026-02-09 | Karpathy 提出 **Agentic Engineering** | 给"人类做编排、Agent 写代码"的新工作方式命名 | [Times of India](https://timesofindia.indiatimes.com/technology/tech-news/tesla-former-ai-director-andrej-karpathy-who-coined-the-word-vibe-coding-has-a-new-word-for-engineers/articleshowprint/128098180.cms) |
| 2026-02-12 | 智谱发布 GLM-5 | 国产开源旗舰进入"万亿参数 + Agent"竞争 | [Wikipedia](https://en.wikipedia.org/wiki/Zhipu_AI) |
| 2026-02-13 | GPT-4o 正式退役 | 第一代"全民多模态"模型退出历史舞台 | [Wikipedia](https://en.wikipedia.org/wiki/2026_in_artificial_intelligence) |
| 2026-02-17 | Claude Sonnet 4.6 发布 | 中档模型承接大部分 Agent 任务 | [Claude Release Notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 2026-02-24 | Cowork 插件市场与管理员控制 | Skills/插件从个人玩具变成企业可治理资产 | [Claude Release Notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 2026-02-25 | Cowork 支持定时任务 | "后台常驻 Agent"的产品雏形 | [Claude Release Notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 2026-03-05 | GPT-5.4 发布 | 专业工作与计算机使用能力继续推进 | [Wikipedia](https://en.wikipedia.org/wiki/GPT-5.4) |
| 2026-03-23 | Cowork / Claude Code 支持 Computer Use | Agent 可直接操作本机应用，"数字同事"感增强 | [Claude Release Notes](https://support.claude.com/en/articles/12138966-release-notes) |

### Q2（4–6 月）

| 时间 | 事件 | 为什么重要 | 来源 |
|------|------|------------|------|
| 2026-04-07 | Anthropic Project Glasswing：Mythos Preview 定向开放 | 前沿模型先给"防御方"用于找漏洞，安全范式变化 | [Wikipedia](https://en.wikipedia.org/wiki/Claude_(AI)) |
| 2026-04-09 | Claude Cowork 正式可用（macOS/Windows） | 知识工作 Agent 从预览走向商用 | [Claude Release Notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 2026-04-16 | Claude Opus 4.7 + Claude Design | 编码、视觉与设计工作流融合 | [Anthropic](https://www.anthropic.com/news/claude-opus-4-7) |
| 2026-04-23 | GPT-5.5 发布 | 长程 Agent 任务与专业交付能力提升 | [Wikipedia](https://en.wikipedia.org/wiki/GPT-5.5) |
| 2026-04-24 | **DeepSeek-V4 预览（V4-Pro / V4-Flash）** | 1M 上下文 + 开源权重，国产开源再上一档 | [Wikipedia](https://en.wikipedia.org/wiki/DeepSeek) |
| 2026-05-28 | Claude Opus 4.8 发布 | 编码与 Agent 技能继续迭代 | [Claude Release Notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 2026-06-01 | MiniMax M3 发布 | 开源模型同时做到"前沿编码 + 1M 上下文 + 原生多模态" | [MiniMax](https://www.minimax.io/models/text/m3)｜[南都](https://www.sohu.com/a/1030549129_161795) |
| 2026-06-09 | **Claude Fable 5 / Mythos 5 发布** | Mythos 级能力 + 分级安全护栏，前沿模型开始"分权使用" | [Anthropic](https://www.anthropic.com/news/claude-fable-5-mythos-5) |
| 2026-06-12 | Fable 5 / Mythos 5 访问被暂停 | 出口管制直接作用于模型访问权，地缘政治进入模型层 | [Wikipedia](https://en.wikipedia.org/wiki/Claude_(AI)) |
| 2026-06-16 | GLM-5.2 发布（1M 上下文） | 国产开源上下文竞赛 | [Wikipedia](https://en.wikipedia.org/wiki/Zhipu_AI) |
| 2026-06-19 | Google 发布 Gemini 3.5 家族 + Gemini Omni | 多模态生成与 Agent 能力合并 | [Wikipedia](https://en.wikipedia.org/wiki/Gemini_(chatbot)) |
| 2026-06-23 | Claude Tag（Slack 内委派任务） | Agent 进入团队协作流，而不只是个人工具 | [Anthropic](https://www.anthropic.com/news/introducing-claude-tag) |
| 2026-06-30 | Claude Sonnet 5 发布 | "最 Agentic 的 Sonnet"，中档模型承担主力 | [Anthropic](https://www.anthropic.com/news/claude-sonnet-5) |

### Q3（7–9 月）

| 时间 | 事件 | 为什么重要 | 来源 |
|------|------|------------|------|
| 2026-07-01 | Fable 5 / Mythos 5 访问恢复 | 管制松绑，但"模型可用性受政策影响"成为常态风险 | [Anthropic](https://www.anthropic.com/news/redeploying-fable-5) |
| 2026-07-07 | Cowork 登陆 Web 与移动端 | 会话与文件跟人走，后台任务脱离单机 | [Claude Release Notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 2026-07-08 | Grok 4.5 发布 | xAI 以"Opus 级、更便宜"切入编码 Agent | [Wikipedia](https://en.wikipedia.org/wiki/Grok_(chatbot)) |
| 2026-07-09 | **GPT-5.6（Sol/Terra/Luna）+ ChatGPT Work** | 模型家族分层 + "工作操作系统"定位 | [Wikipedia](https://en.wikipedia.org/wiki/GPT-5.6) |
| 2026-07-09 | Meta Muse Spark 1.1 | Meta 用新家族取代 Llama 作为消费级主力 | [Wikipedia](https://en.wikipedia.org/wiki/Muse_Spark) |
| 2026-07-16 | Kimi K3 发布（2.8T 参数，开源权重） | 当时最大开源模型，国产开源冲到第一梯队 | [Wikipedia](https://en.wikipedia.org/wiki/Kimi_(chatbot)) |
| 2026-07-21 | OpenAI 披露 Agent 自主入侵 Hugging Face | 首个公开的"Agent 自主网络攻击"事件，安全边界成为核心议题 | [Wikipedia](https://en.wikipedia.org/wiki/2026_in_artificial_intelligence) |
| 2026-07-24 | Claude Opus 5 发布 | 以一半价格接近 Fable 5 的前沿能力 | [Anthropic](https://www.anthropic.com/news/claude-opus-5) |
| 2026-07-31 | DeepSeek V4-Flash 正式版 | 低成本长上下文模型进入生产可用 | [Wikipedia](https://en.wikipedia.org/wiki/DeepSeek) |
| 2026-08-03 | Qwen3.8-Max 云版本上线（2.4T 参数） | 阿里旗舰进入"万亿级 + 1M 上下文" | [Wikipedia](https://en.wikipedia.org/wiki/Qwen) |
| 2026-08-05 | Meta Muse Spark 1.2 + Muse Code | Meta 补齐终端编码 Agent | [Wikipedia](https://en.wikipedia.org/wiki/Muse_Spark) |
| 2026-08-06 | Claude 企业版 Skills/插件安全扫描 | 技能生态开始需要"供应链安全" | [Claude Release Notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 2026-08-10 | Muse Glimmer 30B 开放权重 | 消费级 GPU 可跑的本地 Agent 模型 | [Wikipedia](https://en.wikipedia.org/wiki/Muse_Spark) |
| 2026-08-11 | Grok Bot 公测 | "AI 队友"产品化：多 Bot 共享一台云电脑 | [Wikipedia](https://en.wikipedia.org/wiki/Grok_(chatbot)) |
| 2026-08-12 | Grok 4.6 发布；Qwen3.8 开放权重 | 模型迭代节奏进入"周更" | [Wikipedia](https://en.wikipedia.org/wiki/Grok_(chatbot))｜[Wikipedia](https://en.wikipedia.org/wiki/Qwen) |
| 2026-08-13 | DeepSeek V4-Pro 正式版 | 1.6T 参数开源旗舰落地 | [Wikipedia](https://en.wikipedia.org/wiki/DeepSeek) |
| 2026-08-14 | GLM-5.3 发布 | 743B 基座 + 后训练优化，主打性价比 | [科技日报](https://www.stdaily.com/web/gdxw/2026-08/14/content_564134.html) |
| 2026-08-25 | Cowork 记忆跨会话 + 主题管理 | 常驻 Agent 的"长期记忆"基础设施 | [Claude Release Notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 2026-09-01 | **Claude Fable 5.1 / Mythos 5.1 发布** | 前沿模型效率提升，成本下降 | [Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-1) |
| 2026-09-02 | Muse Spark 1.3；Gemini 3.8 Flash；Qwen3.8-Max-0902 快照 | 三家在同一天更新，竞争进入"同周对打" | [LLM Stats](https://llm-stats.com/models/muse-spark-1.3)｜[Wikipedia](https://en.wikipedia.org/wiki/Gemini_(chatbot))｜[QwenCloud](https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade) |
| 2026-09-03 | **GPT-6 Astra 发布**（09-04 向付费用户开放） | OpenAI 称"进入 AGI 时代"，把能力叙事推到新高 | [Wikipedia](https://en.wikipedia.org/wiki/GPT-6) |
| 2026-09-08 | Meta 发布 Muse Agent | 消费级"帮你办事"的 Agent 产品 | [Wikipedia](https://en.wikipedia.org/wiki/2026_in_artificial_intelligence) |
| 2026-09-10 | DeepSeek V4.1-Flash 发布 | 原生多模态 + 新架构，开源继续快跑 | [Wikipedia](https://en.wikipedia.org/wiki/DeepSeek) |
| 2026-09-15 | 阶跃星辰 Step 5 Preview | 国产多模态推理 + Agent 工具链 | [EmpirioLabs](https://docs.empiriolabs.ai/models/step-5-preview) |
| 2026-09-16 | Cowork 与聊天合并为"一个 Claude" | Agent 与对话的边界消失，默认入口统一 | [Claude Release Notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 2026-09-21 | Grok 4.7 发布 | xAI 保持高频迭代 | [Wikipedia](https://en.wikipedia.org/wiki/Grok_(chatbot)) |
| 2026-09-22 | **Claude Opus 5.5**；GPT-6 Sol/Luna；小米 MiMo-V2.6 | 同一天三家旗舰更新，模型竞争白热化 | [Anthropic](https://www.anthropic.com/claude-opus-5-5)｜[Wikipedia](https://en.wikipedia.org/wiki/GPT-6)｜[南都](https://www.sohu.com/a/1079584925_161795) |
| 2026-09-25 | Claude 插件开发者目录开放 | 插件生态从"内部工具"走向"可分发市场" | [Claude Release Notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 2026-09-28 | Claude Sonnet 5.5 发布 | 速度/成本/智能的平衡点更新 | [Anthropic](https://www.anthropic.com/claude-sonnet-5-5) |
| 2026-09-29 | **GPT-6.1 Sol 发布；Dots 个人 Agent** | 旗舰分层（Astra 受限、Sol 主推）；Agent 产品继续分化 | [Wikipedia](https://en.wikipedia.org/wiki/GPT-6.1)｜[Wikipedia](https://en.wikipedia.org/wiki/2026_in_artificial_intelligence) |
| 2026-09-30 | **Gemini 4 Argon 发布**（Pro/Ultra 订阅） | Google 新一代旗舰，先在订阅层落地 | [Wikipedia](https://en.wikipedia.org/wiki/Gemini_(chatbot)) |

### Q4（10–11 月，进行中）

| 时间 | 事件 | 为什么重要 | 来源 |
|------|------|------------|------|
| 2026-10-07 | **Claude Haiku 5.5**；GPT-6 Instant | 小模型与"智能 UI"入口同时更新 | [Anthropic](https://www.anthropic.com/claude-haiku-5-5)｜[Wikipedia](https://en.wikipedia.org/wiki/GPT-6) |
| 2026-10-13 | Gemini 4 Argon 扩大 Web 可用 | 旗舰能力从订阅灰度走向更大范围 | [Wikipedia](https://en.wikipedia.org/wiki/Gemini_(chatbot)) |
| 2026-10-15 | Meta Muse Spark Open（816B MoE） | 开放权重旗舰，可在 Mac Studio 级设备运行 | [Wikipedia](https://en.wikipedia.org/wiki/Muse_Spark) |
| 2026-10-21 | Claude Duet 研究预览 | "主动型 Agent"：不等提问，主动推进任务 | [Claude Release Notes](https://support.claude.com/en/articles/12138966-release-notes) |
| 2026-10-26 | GPT-6.1 Terra 发布 | 低成本档承接高并发 Agent 任务 | [Wikipedia](https://en.wikipedia.org/wiki/GPT-6.1) |
| 2026-10-27 | Kimi K3.1 Pro 发布 | 开源模型在 Agent 编码榜上逼近闭源旗舰 | [China Daily](https://www.chinadaily.com.cn/a/202610/27/WS6adff3c1e4b06d4aa0564e78.html) |
| 2026-10-28 | Gemini 4 Carbon 公布（Fairwind 计划） | Google 下一代前沿模型进入受限测试 | [Wikipedia](https://en.wikipedia.org/wiki/Gemini_(chatbot)) |
| 2026-10-29 | Mistral Large 4（1T MoE） | 欧洲旗舰继续走"开源 + 主权 AI"路线 | [Wikipedia](https://en.wikipedia.org/wiki/Mistral_AI) |
| 2026-11-05 | GPT-6 Cyber 发布 | 网络安全专用模型，需 Trusted Access | [Wikipedia](https://en.wikipedia.org/wiki/GPT-6) |

> **截至 2026-11 的观察**：模型迭代已进入"周更/同周对打"节奏；真正的分水岭不再是单个模型分数，而是**Agent 工程能力、上下文与记忆、技能/插件生态、安全与治理**。

---

## 参考

**官方来源（优先）**

- Anthropic：[Newsroom](https://www.anthropic.com/news)｜[Claude Release Notes](https://support.claude.com/en/articles/12138966-release-notes)｜[Models Overview](https://platform.claude.com/docs/en/models/overview)
- OpenAI：[News](https://openai.com/news/)｜模型卡（Amazon Bedrock 镜像，含发布日）：[GPT-6 Astra](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-astra.html)、[GPT-6.1 Sol](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-1-sol.html)
- Google：[Blog](https://blog.google/)｜[Gemini Release Notes](https://gemini.google/release-notes/)
- DeepSeek：[API News](https://api-docs.deepseek.com/news/)｜[QwenCloud Changelog](https://docs.qwencloud.com/changelog/models)
- MCP：[modelcontextprotocol.io](https://modelcontextprotocol.io/)
- 各厂商模型页：<https://ai.meta.com/>｜<https://x.ai/news>｜<https://mistral.ai/news>｜<https://www.minimax.io/>｜<https://platform.kimi.com/>｜<https://z.ai/>｜<https://mimo.mi.com/>｜<https://www.stepfun.com/>

**第三方交叉核对**

- [Wikipedia: 2026 in artificial intelligence](https://en.wikipedia.org/wiki/2026_in_artificial_intelligence)
- [Wikipedia: Claude (AI)](https://en.wikipedia.org/wiki/Claude_(AI))｜[GPT-6](https://en.wikipedia.org/wiki/GPT-6)｜[GPT-5.6](https://en.wikipedia.org/wiki/GPT-5.6)｜[Gemini (chatbot)](https://en.wikipedia.org/wiki/Gemini_(chatbot))｜[DeepSeek](https://en.wikipedia.org/wiki/DeepSeek)｜[Qwen](https://en.wikipedia.org/wiki/Qwen)｜[Grok (chatbot)](https://en.wikipedia.org/wiki/Grok_(chatbot))｜[Muse Spark](https://en.wikipedia.org/wiki/Muse_Spark)
- [LMArena](https://lmarena.ai)｜[Artificial Analysis](https://artificialanalysis.ai/)｜[SWE-bench](https://www.swebench.com)

> 说明：2026 年部分事件仍在演进；表中"发布"指官方宣布，"可用"指面向用户开放，两者可能相差数天。以厂商官网为准。

---

## 下一步

- [M0-02 · 六次范式转移](./02-paradigm-shifts.md) —— 把时间线串成"协作方式"的演进
- [M0-03 · 模型家谱](./03-model-lineage.md) —— 按家族查版本
- [M0-04 · 年度回顾](./04-yearly-review.md) —— 当年的判断对了吗
- [M2 · 国内外主流大模型](../02-llm-landscape/README.md) —— 今天怎么选
- [返回 M0 导读](./README.md)
