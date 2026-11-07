# M0-03 · 模型家谱：每个家族是怎么迭代到今天的

> 🕰️ 历史档案 ｜ 记录范围：2023 – 2026-11 ｜ 只追加，不回改
> 📅 内容基准：2026-11 ｜ 时效性：历史层（不做时效复检）

---

## 怎么读这份家谱

- **一条家族一条线**：按"版本 → 发布时间 → 关键变化 → 现状"读，能看出这个家族的节奏和取舍。
- **现状列**只表示"截至 2026-11 的公开状态"，分四档：

| 标签 | 含义 |
|------|------|
| **活跃** | 当前主推，官方仍在售/可用 |
| **旧版** | 仍可能可用，但已被新版本取代，不建议新项目选用 |
| **弃用** | 官方已下线或宣布退役 |
| **受限** | 仅特定客户/计划/地区可用（安全、合规或预览） |
| **预览** | 研究预览，API/行为可能变化 |

> 模型迭代极快，状态以厂商官网为准；本表只做"演进脉络"，不做实时报价。选型请看 [M2-03 模型横向对比](../02-llm-landscape/03-comparison.md)。

---

## 一、国际家族

### 1. OpenAI · GPT / o 系列

**主线：** 通用对话 → 多模态 → 推理模型 → Agent 模型 → "GPT-6 家族分层"。
**来源：** [OpenAI News](https://openai.com/news/)｜[GPT-6](https://en.wikipedia.org/wiki/GPT-6)｜[GPT-5.6](https://en.wikipedia.org/wiki/GPT-5.6)｜Bedrock 模型卡（含发布日）

| 版本 | 发布时间 | 关键变化 | 现状 |
|------|----------|----------|------|
| GPT-3.5 / ChatGPT | 2022-11-30 | 对话式 AI 破圈 | 弃用 |
| GPT-4 | 2023-03-14 | 多模态输入、推理大幅提升 | 弃用 |
| GPT-4o | 2024-05-13 | 端到端多模态、低延迟语音 | 2026-02-13 退役 |
| o1 | 2024-09-12 | 推理时计算，先想再答 | 旧版 |
| GPT-4.5 | 2025-02 | 更大规模、更强的写作与常识 | 弃用 |
| o3 / o4-mini | 2025-04-16 | 推理模型产品化，工具调用增强 | 旧版 |
| GPT-5 | 2025-08-07 | 统一快/慢思考路由 | 旧版 |
| GPT-5.1 | 2025-11-12 | 对话体验与指令遵循改进 | 旧版 |
| GPT-5.2 | 2025-12-11 | 推理与专业工作能力提升 | 旧版 |
| GPT-5.4 | 2026-03-05 | 计算机使用、长上下文工作流 | 旧版 |
| GPT-5.5 | 2026-04-23 | 长程 Agent 任务、专业交付 | 旧版 |
| **GPT-5.6 Sol / Terra / Luna** | 2026-07-09 | 三档分层；Sol 主打编码与 Agent | 活跃（Terra/Luna 为低成本档） |
| **GPT-6 Astra** | 2026-09-03（09-04 公开） | 旗舰，主打推理、编码、计算机使用；"AGI 时代"叙事 | 活跃（受限） |
| **GPT-6 Sol / Luna** | 2026-09-22 | 主力档与高性价比档 | 活跃 |
| **GPT-6 Instant** | 2026-10-07 | "智能 UI"入口，交互形态变化 | 活跃 |
| **GPT-6.1 Sol** | 2026-09-29 | 接近 Astra 的能力、更低价格 | 活跃 |
| **GPT-6.1 Terra** | 2026-10-26 | 低成本高并发档 | 活跃 |
| **GPT-6 Cyber** | 2026-11-05 | 网络安全专用，需 Trusted Access | 受限 |

> 备注：OpenAI 在 2026-09 同时保留 Astra（强但受限）与 6.1 Sol（主推），形成"能力上限 + 可用性"的双轨。此前的 GPT-4o 于 2026-02-13 退役，标志第一代"全民多模态"退场。

---

### 2. Anthropic · Claude

**主线：** 对齐与长文本 → 编码 → Agent → "Fable/Mythos 分级" → 5.5 家族。
**来源：** [Claude Release Notes](https://support.claude.com/en/articles/12138966-release-notes)｜[Models Overview](https://platform.claude.com/docs/en/models/overview)｜[Wikipedia](https://en.wikipedia.org/wiki/Claude_(AI))

| 版本 | 发布时间 | 关键变化 | 现状 |
|------|----------|----------|------|
| Claude 1 / 2 | 2023-03 / 2023-07 | 长上下文与"宪法 AI"对齐路线 | 弃用 |
| Claude 3（Opus/Sonnet/Haiku） | 2024-03-04 | 三档尺寸成为行业模板 | 弃用 |
| Claude 3.5 Sonnet | 2024-06-20 | 编码能力跃升 | 弃用 |
| Claude 3.7 Sonnet | 2025-02 | 混合推理（可切换思考） | 弃用 |
| Claude 4（Sonnet 4 / Opus 4） | 2025-05-22 | 编码 Agent、工具使用增强 | 弃用（2026-01 移除） |
| Claude Opus 4.1 | 2025-08 | 小幅升级 | 弃用 |
| Claude 4.5 家族 | 2025-09-29 / 10-15 / 11-24 | Sonnet 4.5、Haiku 4.5、Opus 4.5；编码 Agent 出圈 | 旧版 |
| Claude Opus 4.6 | 2026-02-05 | **Agent Teams**、PowerPoint 集成 | 旧版 |
| Claude Sonnet 4.6 | 2026-02-17 | 1M 上下文（beta）、全面升级 | 旧版 |
| Claude Mythos Preview | 2026-04-07 | Project Glasswing，仅定向开放找漏洞 | 受限（已升级） |
| Claude Opus 4.7 | 2026-04-16 | 软件工程、视觉增强；Claude Design | 旧版 |
| Claude Opus 4.8 | 2026-05-28 | 编码与 Agent 技能改进 | 旧版 |
| **Claude Fable 5 / Mythos 5** | 2026-06-09 | Mythos 级能力 + 分级护栏；Fable 公开、Mythos 受限 | 旧版（6-12 曾暂停，7-01 恢复） |
| Claude Sonnet 5 | 2026-06-30 | "最 Agentic 的 Sonnet" | 旧版 |
| Claude Opus 5 | 2026-07-24 | 以一半价格接近 Fable 5 | 旧版 |
| **Claude Fable 5.1 / Mythos 5.1** | 2026-09-01 | 前沿能力 + 效率提升（成本降约 25%） | 活跃（Mythos 受限） |
| **Claude Opus 5.5** | 2026-09-22 | 编码/知识工作领先；运行成本约降 40% | 活跃 |
| **Claude Sonnet 5.5** | 2026-09-28 | 速度/成本/智能平衡 | 活跃 |
| **Claude Haiku 5.5** | 2026-10-07 | 高并发、低成本小模型 | 活跃 |

> 备注：2026 年 Anthropic 把"最强能力"和"可公开使用"拆成 Fable / Mythos 两条线，是前沿模型治理的一次重要产品化尝试。基准与价格请看 [M2-01](../02-llm-landscape/01-global-models.md)。

---

### 3. Google · Gemini

**主线：** 原生多模态 → 长上下文 → 推理（Deep Think）→ Agent 化 → Gemini 4。
**来源：** [Google Blog](https://blog.google/)｜[Gemini Release Notes](https://gemini.google/release-notes/)｜[Wikipedia](https://en.wikipedia.org/wiki/Gemini_(chatbot))

| 版本 | 发布时间 | 关键变化 | 现状 |
|------|----------|----------|------|
| Gemini 1.0 | 2023-12-06 | 原生多模态，Ultra/Pro/Nano 三档 | 弃用 |
| Gemini 1.5 | 2024-02-15 | 100 万 token 上下文、MoE | 弃用 |
| Gemini 2.0 | 2024-12-11 | 面向 Agent 时代设计 | 弃用 |
| Gemini 2.5 Pro / Flash | 2025-03 / 2025-06 | 推理 + 长上下文，当年第一梯队 | 旧版 |
| Gemini 3 Pro | 2025-11-18 | 重回第一梯队，Deep Think 推理模式 | 旧版 |
| Gemini 3 Deep Think（升级） | 2026-02-12 | ARC-AGI-2 77.1%、SWE-bench 80.6% | 旧版 |
| Gemini 3.5 家族 + Gemini Omni | 2026-06-19 | 多模态生成 + Agent 能力合并 | 旧版（部分型号仍用） |
| **Gemini 3.8 Flash** | 2026-09-02 | 高性价比 Flash 线 | 活跃 |
| **Gemini 4 Argon** | 2026-09-30 | 新一代旗舰，先向 AI Pro/Ultra 开放 | 活跃（订阅优先） |
| **Gemini 4 Carbon** | 2026-10-28 | 下一代前沿模型，Fairwind 计划受限测试 | 受限 |

> 备注：Google 的节奏是"先订阅层灰度，再扩大可用"；Gemini 4 Argon 于 10-13 扩大 Web 可用。

---

### 4. Meta · Llama → Muse

**主线：** 开源 Llama → 被 Muse Spark 取代为消费级主力 → 开源/闭源双轨。
**来源：** [Meta AI](https://ai.meta.com/)｜[Wikipedia: Llama](https://en.wikipedia.org/wiki/Llama_(language_model))｜[Wikipedia: Muse Spark](https://en.wikipedia.org/wiki/Muse_Spark)

| 版本 | 发布时间 | 关键变化 | 现状 |
|------|----------|----------|------|
| Llama 2 | 2023-07-18 | 开放商用，私有化部署起点 | 弃用 |
| Llama 3 / 3.1 / 3.2 / 3.3 | 2024 | 405B 开放权重、多模态、轻量版 | 旧版 |
| Llama 4（Scout/Maverick） | 2025-04-05 | MoE、超长上下文；口碑分化 | 旧版（被 Muse 取代） |
| Muse Spark 1.1 | 2026-07-09 | Meta Superintelligence Labs 新家族，多模态推理/编码 | 旧版 |
| Muse Spark 1.2 + Muse Code | 2026-08-05 | 终端编码 Agent | 旧版 |
| Muse Glimmer 30B | 2026-08-10 | 开源权重，24GB 消费级 GPU 可跑 | 活跃（开源） |
| Muse Agent | 2026-09-08 | 消费级"帮你办事"Agent 产品 | 活跃（产品） |
| **Muse Spark 1.3** | 2026-09-02 | 长程协作、多 Agent、编码增强；1M 上下文 | 活跃 |
| **Muse Spark Open（816B MoE）** | 2026-10-15 | 开放权重旗舰，Mac Studio 级可运行 | 活跃（开源） |

> 备注：2026 年 Meta 把消费级主力从 Llama 迁到 Muse，Llama 更多留在开源/研究语境。

---

### 5. xAI · Grok

**主线：** 实时信息 + 推理 → 编码 Agent → 多 Bot 协作。
**来源：** [xAI News](https://x.ai/news)｜[Wikipedia](https://en.wikipedia.org/wiki/Grok_(chatbot))

| 版本 | 发布时间 | 关键变化 | 现状 |
|------|----------|----------|------|
| Grok-1 | 2023-11 | 首代模型，后开源 | 弃用 |
| Grok-2 | 2024-08 | 图像生成、实时信息 | 弃用 |
| Grok 3 | 2025-02 | 推理能力提升 | 弃用 |
| Grok 4 / 4 Heavy | 2025-07-09 | 推理 + 多 Agent 雏形 | 旧版 |
| Grok 4.1 / 4.1 Fast | 2025-11-17 | 推理、多模态、情商改进 | 旧版 |
| Grok 4.5 | 2026-07-08 | 编码 Agent（Grok Build），"Opus 级、更便宜" | 旧版 |
| Grok 4.6 | 2026-08-12 | 迭代加速，进入 Copilot/Bedrock 等平台 | 旧版 |
| **Grok 4.7** | 2026-09-21 | 当前主力 | 活跃 |
| Grok Bot | 2026-08-11 | 多 Bot 共享云电脑、互相消息 | 活跃（beta） |

> 备注：xAI 在 2026 年与 SpaceX 体系整合（对外使用 SpaceXSI 名称），模型迭代节奏明显加快。

---

### 6. Mistral AI

**主线：** 欧洲开源/主权 AI，Large 系列 + 代码/文档专用模型。
**来源：** [Mistral News](https://mistral.ai/news)｜[Wikipedia](https://en.wikipedia.org/wiki/Mistral_AI)｜[Bedrock 模型卡](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-mistral-ai-mistral-large-3.html)

| 版本 | 发布时间 | 关键变化 | 现状 |
|------|----------|----------|------|
| Mistral 7B / Mixtral 8x7B | 2023-09 / 2023-12 | 开源小模型与 MoE 路线 | 旧版（开源） |
| Mistral Large 2 | 2024-07 | 旗舰闭源，多语言 | 旧版 |
| Codestral / Devstral | 2024–2025 | 代码专用线 | 旧版 |
| Mistral Large 3 | 2025-12-02 | MoE 旗舰，欧洲主权 AI 代表 | 旧版 |
| Mistral Medium 3.5 / Small 4 | 2026 | 中/小档更新 | 活跃 |
| **Mistral Large 4（1T MoE）** | 2026-10-29 | 当前最大公开模型，52B 激活 | 活跃 |

> 备注：Mistral 的差异点是"开放权重 + 欧洲合规 + 本地部署"，不是绝对能力榜。

---

## 二、国内家族

### 7. DeepSeek · V 系列 / R 系列

**主线：** 开源权重 + 极致性价比 → 推理模型 → 百万上下文 → 原生多模态。
**来源：** [DeepSeek API News](https://api-docs.deepseek.com/news/)｜[Wikipedia](https://en.wikipedia.org/wiki/DeepSeek)

| 版本 | 发布时间 | 关键变化 | 现状 |
|------|----------|----------|------|
| DeepSeek LLM / V2 | 2023-11 / 2024-05 | 开源、MoE、低价 API | 旧版 |
| DeepSeek-V3 | 2024-12-26 | 低成本训练，冲击算力叙事 | 旧版 |
| **DeepSeek-R1** | 2025-01-20 | 开源推理模型比肩闭源 | 旧版 |
| DeepSeek-V3.1 | 2025-08-21 | 混合推理、Agent 能力 | 旧版 |
| DeepSeek-V3.2 | 2025-12-01 | 稀疏注意力、成本再降 | 旧版 |
| DeepSeek-V4 预览（Pro/Flash） | 2026-04-24 | 1M 上下文、MIT 许可；Pro 1.6T / Flash 284B | 被正式版替代 |
| **DeepSeek-V4-Flash** | 2026-07-31 | 正式版，低成本长上下文 | 活跃 |
| **DeepSeek-V4-Pro** | 2026-08-13 | 正式版，1.6T 开源旗舰 | 活跃 |
| **DeepSeek-V4.1-Flash** | 2026-09-10 | 新架构（causal encoder-decoder）、原生多模态 | 活跃 |

> 备注：DeepSeek 的发布节奏是"先预览、后正式"，V4 系列从 4 月预览到 8 月正式，跨度约 4 个月。

---

### 8. 阿里 · Qwen（通义千问）

**主线：** 开源全尺寸 → Qwen3 → 万亿 MoE → 3.8 多模态/长上下文。
**来源：** [Qwen](https://qwen.ai/)｜[QwenCloud Changelog](https://docs.qwencloud.com/changelog/models)｜[Wikipedia](https://en.wikipedia.org/wiki/Qwen)

| 版本 | 发布时间 | 关键变化 | 现状 |
|------|----------|----------|------|
| Qwen / Qwen2 / Qwen2.5 | 2023-04 → 2024-09 | 开源全尺寸家族，生态最完整 | 旧版 |
| Qwen3 | 2025-04-28 | 思考/非思考双模式，Apache 2.0 | 旧版 |
| Qwen3-Max | 2025-09 | 闭源旗舰（>1T） | 旧版 |
| Qwen3.5 / 3.5-Plus | 2026-02 | 开源 + 闭源双轨，可操作桌面/移动应用 | 旧版 |
| Qwen3.6 / 3.6-Plus | 2026-04 | 多模态与 Agent 能力 | 旧版 |
| Qwen3.7-Max / Plus | 2026-05 / 06 | 闭源旗舰迭代 | 旧版 |
| **Qwen3.8-Max** | 2026-08-03（09-02 快照，09-05 起默认） | 2.4T 参数、1M 上下文、约 95B 激活 | 活跃（闭源） |
| **Qwen3.8-2.4T-A95B** | 2026-08-12 | 开放权重（部分功能省略） | 活跃（开源） |
| **Qwen3.8-27B** | 2026-08-14 | Apache 2.0，图像输入 + 非思考模式 | 活跃（开源） |
| **Qwen3.8-Flash / Flash-Next** | 2026-08-26 | 高性价比 + 多模态开源权重 | 活跃 |
| **Qwen3.8-Omni-Flash** | 2026-09-18 | 文本/图像/音频/视频输入 | 活跃 |

> 备注：Qwen 的"同代多尺寸 + 开源/闭源并行"是它生态强的核心原因。

---

### 9. MiniMax

**主线：** 产品化（Talkie/海螺）→ Agent 模型 → M3 开源旗舰。
**来源：** [MiniMax](https://www.minimax.io/)｜[M3](https://www.minimax.io/models/text/m3)｜[Wikipedia](https://en.wikipedia.org/wiki/MiniMax_(company))

| 版本 | 发布时间 | 关键变化 | 现状 |
|------|----------|----------|------|
| abab 系列 | 2022–2024 | 早期文本模型 | 弃用 |
| MiniMax-M1 | 2025-06 | 开源推理模型 | 旧版 |
| MiniMax-M2 | 2025-10 | Agent/编码能力 | 旧版 |
| MiniMax-M2.5 / Lightning | 2026-02 | 速度与成本优化 | 旧版 |
| MiniMax-M2.7 | 2026-03 | 迭代版 | 旧版 |
| **MiniMax-M3** | 2026-06-01 | MSA 稀疏注意力、1M 上下文、原生多模态；开源 | 活跃 |

> 备注：M3 的定位是"开源模型里同时做到前沿编码 + 1M 上下文 + 原生多模态"。

---

### 10. 月之暗面 · Kimi

**主线：** 长文本 → 开源 K 系列 → K3 万亿开源 → K3.1 Pro。
**来源：** [Kimi Platform](https://platform.kimi.com/)｜[Wikipedia](https://en.wikipedia.org/wiki/Kimi_(chatbot))｜[China Daily](https://www.chinadaily.com.cn/a/202610/27/WS6adff3c1e4b06d4aa0564e78.html)

| 版本 | 发布时间 | 关键变化 | 现状 |
|------|----------|----------|------|
| Kimi（Moonshot） | 2023-11 | 128K 长上下文起家 | 旧版 |
| Kimi K1.5 | 2025-01 | 推理模型 | 旧版 |
| Kimi K2 | 2025-07 | 开源 MoE，编码与 Agent | 旧版 |
| Kimi K2.5 | 2026-01 | 1T MoE、多模态、Agent 能力 | 旧版 |
| Kimi K2.6 | 2026-04 | 迭代版 | 旧版 |
| Kimi K2.7 Code | 2026-06 | 代码专用 | 旧版 |
| **Kimi K3** | 2026-07-16 | 2.8T 参数，当时最大开源模型；Swarm 多子 Agent | 活跃 |
| **Kimi K3.1 Pro** | 2026-10-27 | 编码/金融/3D 增强；安全上主动限制网攻能力 | 活跃（权重计划 11-04 开放） |

---

### 11. 智谱 · GLM（Z.ai）

**主线：** 学术开源 → GLM-4.5/4.6 → 万亿 GLM-5 → 5.3。
**来源：** [Z.ai](https://z.ai/)｜[Wikipedia](https://en.wikipedia.org/wiki/Zhipu_AI)｜[科技日报](https://www.stdaily.com/web/gdxw/2026-08/14/content_564134.html)

| 版本 | 发布时间 | 关键变化 | 现状 |
|------|----------|----------|------|
| ChatGLM / GLM-4 | 2023–2024 | 学术开源起家 | 弃用 |
| GLM-4.5 | 2025-07 | 开源旗舰，Agent 能力 | 旧版 |
| GLM-4.6 | 2025-09 | 国产芯片适配 | 旧版 |
| GLM-4.7（含 4.6V） | 2025-12 | 多模态 | 旧版 |
| GLM-5 | 2026-02-12 | 新一代基座 | 旧版 |
| GLM-5.1 | 2026-03 | 开源，API 提价 10% | 旧版 |
| GLM-5.2 | 2026-06-16 | 1M 上下文 | 旧版 |
| **GLM-5.3** | 2026-08-14 | 743B 基座 + 后训练优化，主打性价比 | 活跃 |

> 备注：GLM 在 2026 年 8 月被 CAISI 评为"开源权重中网络安全能力最强"之一（媒体口径，需以原始报告为准）。

---

### 12. 百度 · 文心 ERNIE

**主线：** 中文知识增强 → 4.5 开源 → 5.0 原生多模态 → 5.1。
**来源：** [Baidu](https://ernie.baidu.com/)｜[Wikipedia](https://en.wikipedia.org/wiki/Ernie_Bot)｜[China Daily](https://global.chinadaily.com.cn/a/202601/22/WS6971d66ba310d6866eb35330.html)

| 版本 | 发布时间 | 关键变化 | 现状 |
|------|----------|----------|------|
| ERNIE 3.0 / 4.0 | 2021 / 2023-10 | 中文知识增强 | 弃用 |
| ERNIE 4.5 / X1 | 2025-03-16 | 多模态 + 推理双线；4.5 开源 | 旧版 |
| ERNIE 5.0 | 2026-01-22 | 原生多模态 | 旧版 |
| **ERNIE 5.1** | 2026-04-29 | 开源（Apache 2.0） | 活跃 |

---

### 13. 字节 · 豆包 Doubao

**主线：** 产品驱动（豆包 App）→ Seed 模型。
**来源：** [豆包](https://www.doubao.com/)｜[Wikipedia](https://en.wikipedia.org/wiki/Doubao)

| 版本 | 发布时间 | 关键变化 | 现状 |
|------|----------|----------|------|
| Doubao 1.0 | 2024-05 | 低价 API + 国民级 App | 旧版 |
| Doubao Seed 1.6 | 2025 | 综合能力升级 | 旧版 |
| **Doubao Seed 2.0** | 2026-02-14 | 当前主力，产品/API 同步 | 活跃 |

> 备注：豆包的核心优势是产品入口与流量，而非单一模型分数；2026 年 7 月起按新规下线拟人化智能体功能。

---

### 14. 小米 · MiMo

**主线：** 开源小模型 → 全模态 V2.5 → V2.6 旗舰。
**来源：** [MiMo 开放平台](https://mimo.mi.com/)｜[南都](https://www.sohu.com/a/1079584925_161795)｜[Wikipedia](https://en.wikipedia.org/wiki/Xiaomi)

| 版本 | 发布时间 | 关键变化 | 现状 |
|------|----------|----------|------|
| MiMo-7B | 2025-04 | 开源推理小模型 | 旧版（开源） |
| MiMo-V2 系列 | 2026 上半年 | 端侧/云端并行，API 平台上线 | 旧版 |
| MiMo-V2.5 / V2.5-Pro | 2026-04 | 主力迭代（2026-10-21 退役） | 弃用 |
| **MiMo-V2.6-Pro / Flash** | 2026-09-22 | 全模态、开源；Pro 登顶开源榜（厂商/媒体口径） | 活跃 |

> 备注：MiMo 走"开源 + 高性价比 + 端侧生态"路线，训练成本公开（RL 后训练约 347 万美元）是其传播点。

---

### 15. 阶跃星辰 · StepFun

**主线：** 多模态基座 → Step 3 → Step 5 Preview。
**来源：** [StepFun](https://www.stepfun.com/)｜[Wikipedia](https://en.wikipedia.org/wiki/StepFun)｜[EmpirioLabs](https://docs.empiriolabs.ai/models/step-5-preview)

| 版本 | 发布时间 | 关键变化 | 现状 |
|------|----------|----------|------|
| Step-1 / Step-2 | 2023 / 2024-07 | 多模态基座，Step-2 万亿参数 | 旧版 |
| Step-3 | 2025-07 | 多模态推理 | 旧版 |
| Step 3.5 Flash | 2026-02 | 196B MoE、Apache 2.0 | 旧版 |
| Step 3.7 Flash | 2026-05 | 迭代版 | 旧版 |
| **Step 5 Preview** | 2026-09-15 | 1M 上下文、图文视频输入、并行工具调用 | 预览 |

> 备注：StepFun 的差异化在"多模态 + 国产芯片适配 + 开源小模型"。

---

## 三、横向观察（截至 2026-11）

1. **版本节奏**：头部厂商从"季度发"变成"月发/同周对打"；同代多档（旗舰/主力/轻量）成为标准结构。
2. **开源与闭源并行**：中国厂商普遍"同代开源权重 + 闭源旗舰"双轨；美国厂商更倾向闭源 + 分级访问。
3. **上下文**：1M token 已从卖点变成标配；竞争转向"长上下文下的有效召回"。
4. **多模态**：原生多模态（文本/图像/音频/视频）成为旗舰门槛。
5. **Agent 能力**：编码、工具调用、计算机使用、长程任务，是 2026 年真正的分水岭。
6. **安全分级**：前沿模型开始按"能力/用途"分级开放（Mythos 受限、GPT-6 Cyber 需 Trusted Access）。

---

## 参考

- Anthropic：[Models Overview](https://platform.claude.com/docs/en/models/overview)｜[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)
- OpenAI：模型卡镜像 [GPT-6 Astra](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-astra.html)｜[GPT-6.1 Sol](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-1-sol.html)
- Google：[Gemini Release Notes](https://gemini.google/release-notes/)｜[Blog](https://blog.google/)
- DeepSeek：[API News](https://api-docs.deepseek.com/news/)
- Qwen：[QwenCloud Changelog](https://docs.qwencloud.com/changelog/models)｜[Qwen3.8-Max 更新公告](https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade)
- MiniMax：[M3](https://www.minimax.io/models/text/m3)
- Kimi：[K3.1 Pro 文档](https://platform.kimi.com/docs/guide/kimi-k3-1-pro-quickstart)
- 智谱：[Z.ai](https://z.ai/)
- 文心：[ernie.baidu.com](https://ernie.baidu.com/)
- 豆包：[doubao.com](https://www.doubao.com/)
- MiMo：[mimo.mi.com](https://mimo.mi.com/)
- StepFun：[stepfun.com](https://www.stepfun.com/)
- Meta：[ai.meta.com](https://ai.meta.com/)
- xAI：[x.ai/news](https://x.ai/news)
- Mistral：[mistral.ai/news](https://mistral.ai/news)
- 第三方交叉核对：[2026 in artificial intelligence](https://en.wikipedia.org/wiki/2026_in_artificial_intelligence)｜[LMArena](https://lmarena.ai)｜[Artificial Analysis](https://artificialanalysis.ai/)

> 说明：本页是"演进脉络"，不是实时价目表。具体价格、上下文、跑分请查对应厂商模型页；状态列可能随厂商调整而变化。

---

## 下一步

- [M0-01 · 大事记](./01-timeline.md) —— 版本发布的完整时间线
- [M0-02 · 六次范式转移](./02-paradigm-shifts.md) —— 能力变化如何改变协作方式
- [M0-04 · 年度回顾](./04-yearly-review.md) —— 哪些家族真正改变了格局
- [M2-01 国际主流模型](../02-llm-landscape/01-global-models.md)｜[M2-02 国内主流模型](../02-llm-landscape/02-domestic-models.md) —— 今天怎么选
- [返回 M0 导读](./README.md)
