# M2-01 · 国际主流大模型

> 最后更新：2026年4月

---

## 一图总览

```
国际主流大模型
├── OpenAI          → GPT-4o / GPT-4.1 / o3 / o4-mini / GPT-5
├── Anthropic       → Claude Sonnet 4.6 / Opus 4.6
├── Google DeepMind → Gemini 2.0 Flash / Gemini 2.5 Pro
├── Meta            → Llama 4 Scout / Maverick（开源）
├── Mistral AI      → Mistral Large 2 / Codestral（开源友好）
└── xAI             → Grok 3 / Grok 3 mini
```

---

## OpenAI · GPT 系列

### GPT-4 系列（仍广泛使用）

| 模型 | 发布 | 特点 | 适合 |
|------|------|------|------|
| **GPT-4o** | 2024.5 | 多模态（文本/图像/音频），速度快，性价比高 | 日常任务、开发 API |
| **GPT-4o mini** | 2024.7 | 超低成本，替代 GPT-3.5 | 高频简单任务 |
| **GPT-4.1** | 2025.4 | 超长上下文（1M token），代码能力强 | 大文件分析、代码任务 |

### o 系列推理模型

| 模型 | 发布 | 特点 | 适合 |
|------|------|------|------|
| **o3** | 2025.4.16 | 慢思考推理模型，复杂任务首选 | 数学、算法、深度逻辑 |
| **o4-mini** | 2025.4.16 | o3 轻量版，速度快成本低，支持图像输入 | 日常推理、性价比 |

### GPT-5 系列（2025.8 起持续迭代）

| 模型 | 发布 | 特点 | 适合 |
|------|------|------|------|
| **GPT-5.0** | 2025.8.7 | GPT-5 首发版，综合能力全面升级 | 复杂任务基础版 |
| **GPT-5.1** | 2025.11 | 能力增强，更稳定 | 日常高质量任务 |
| **GPT-5.2** | 2025.12.11 | 新增 Thinking 模式（推理增强版） | 需要推理的复杂任务 |
| **GPT-5.3-Codex** | 2026.2 | 代码专项优化版，面向开发者 | 编程、代码生成 |
| **GPT-5.4** | 2026.3.5 🔥 | 最新旗舰，含 Thinking 版；"专业工作最强最高效模型" | 顶级复杂任务 |

> 📌 **来源：** [Wikipedia - ChatGPT](https://en.wikipedia.org/wiki/ChatGPT) · [TechCrunch - GPT-5.4 发布](https://techcrunch.com/2026/03/05/openai-launches-gpt-5-4-with-pro-and-thinking-versions/)

**GPT-5 系列特点：**
- 迭代节奏极快，平均每 1-2 个月发布新版本
- 每代都有标准版和 **Thinking（推理）版** 两种模式
- GPT-5.3-Codex 是编程专项，开发者重点关注
- GPT-5.4 是当前（2026.3）最新旗舰

**其他产品：**
- GPT Image 1（2025.3）：替代 DALL-E 3，图像生成大幅提升
- Sora 2：视频生成模型

**入口：** [chatgpt.com](https://chatgpt.com) / [platform.openai.com](https://platform.openai.com)

---

## Anthropic · Claude 系列

### Claude 3 系列（2024，仍在使用）

| 模型 | 发布 | 特点 |
|------|------|------|
| **Claude 3.5 Sonnet** | 2024.6 | 代码能力突破，开发者广泛使用 |
| **Claude 3.7 Sonnet** | 2025.2 | 首次引入 Extended Thinking（慢思考）|

### Claude 4 系列（2025-2026，当前主力）

| 模型 | 发布 | 特点 | 适合 |
|------|------|------|------|
| **Claude Sonnet 4.0** | 2025 | Claude 4 代首发 Sonnet | 日常编程、文档 |
| **Claude Opus 4.1** | 2025 | Claude 4 代首发 Opus，旗舰 | 复杂分析 |
| **Claude Opus 4.5** | 2025.11.24 | 价格降 67%，输出 token 减 76% | 高性价比旗舰任务 |
| **Claude Sonnet 4.5** | 2025 | 性能提升，SWE-bench 进步显著 | 编程助手 |
| **Claude Opus 4.6** | 2026.2.5 | 1M 上下文，Agent Teams，Infinite Chats | 大型任务、多 Agent |
| **Claude Sonnet 4.6** | 2026.2.17 🔥 | 最新，SWE-bench **79.6%**，接近 Opus 4.6 水平 | 日常编程首选 |
| **Claude Haiku** | - | 极快极便宜 | 高频简单任务 |

> 📌 **来源：** [Anthropic Claude 版本时间线](https://www.scriptbyai.com/anthropic-claude-timeline/) · [Claude Sonnet 4.6 评测](https://www.digitalapplied.com/blog/claude-sonnet-4-6-benchmarks-pricing-guide)

**Anthropic 特点：**
- **代码能力行业顶尖**，Sonnet 4.6 SWE-bench 79.6%（编码评测第二）
- Cursor 底层默认使用 Claude
- Opus 4.6 新增 **Infinite Chats**（无上下文限制错误）和 **Agent Teams**
- 安全和对齐做得最好，输出可靠性高

**入口：** [claude.ai](https://claude.ai) / [console.anthropic.com](https://console.anthropic.com)

---

## Google DeepMind · Gemini 系列

### Gemini 2.0 系列（2025 上半年主力）

| 模型 | 发布 | 特点 |
|------|------|------|
| **Gemini 2.0 Flash** | 2025.2 | 速度极快，多模态，低成本 |
| **Gemini 2.0 Flash-Lite** | 2025 | 超轻量，最低延迟 |
| **Gemini 2.0 Ultra** | 2025 | 顶级旗舰 |

### Gemini 2.5 系列（2025 下半年，当前主力）

| 模型 | 发布 | 特点 | 适合 |
|------|------|------|------|
| **Gemini 2.5 Pro** | 2025.3.25 | Google 首个"思维模型"，发布即登顶 LMArena | 复杂推理、大文件分析 |
| **Gemini 2.5 Flash** | 2025 | 2.5 代轻量版，速度/质量均衡 | 日常任务、API 调用 |
| **Gemini 2.5 Flash Image** | 2025.8（GA 2025.10）| 专项图像生成/编辑 | 图像处理工作流 |
| **Gemini 2.5 Flash-Lite** | 2025.9 | 超轻量，⚠️ 2026.3.31 停止服务 | — |

### Gemini 3 系列（2026，最新一代）

| 模型 | 发布 | 特点 |
|------|------|------|
| **Gemini 3 Flash** | 2026.1 | 最新一代轻量模型 |
| **Gemini 3.1 Pro** | 2026.3 🔥 | SWE-bench **80.6%**，代码能力直逼 Claude Opus |

> 📌 注意：Gemini 2.5 Pro 和 2.5 Flash 计划于 **2026.6.17 停用**，届时将由新版本替代。
>
> 📌 **来源：** [Wikipedia - Gemini](https://en.wikipedia.org/wiki/Gemini_(language_model)) · [Google AI Developers Forum](https://discuss.ai.google.dev/t/clarification-on-stable-replacement-models-for-gemini-2-5-flash-and-gemini-2-5-pro-before-june-2026-deprecation/130009)

**Google 特点：**
- **上下文窗口最大**（Gemini 1.5 Pro 可达 200 万 Token）
- Gemini 2.5 Pro 是首个明确的"思维模型"，复杂推理行业领先
- 与 Google Workspace、搜索、Android 深度整合
- 多模态能力最强：文本、图像、视频、音频全覆盖
- 有免费额度，适合个人试用

**入口：** [gemini.google.com](https://gemini.google.com) / [ai.google.dev](https://ai.google.dev)

---

## Meta · Llama 4（开源）

| 模型 | 发布 | 参数 | 上下文 | 特点 |
|------|------|------|--------|------|
| **Llama 4 Scout** | 2025.4 | 109B总/17B激活 | **1000万 Token** | 超长上下文，效率极高 |
| **Llama 4 Maverick** | 2025.4 | 400B总/17B激活 | 100万 Token | 旗舰级，对标顶尖闭源 |

**特点：**
- **原生多模态**，文本+图像统一架构
- MoE（混合专家）架构，激活参数少但质量高
- **完全开源**，可私有化部署，数据不出内网
- Llama 4 Scout 的 **1000 万 Token 上下文**是业界最长之一
- 通过 Ollama、vLLM 等框架本地部署

**本地运行：** `ollama pull llama4`

---

## Mistral AI · Mistral 系列（欧洲开源）

| 模型 | 特点 |
|------|------|
| **Mistral Large 2** | 欧洲最强闭源模型，多语言强 |
| **Mistral Small 3** | 高效轻量，性价比高 |
| **Codestral** | 专为代码优化，支持 80+ 编程语言 |
| **Mixtral 8x22B** | MoE 架构，开源旗舰 |

**特点：**
- 欧洲公司，**GDPR 友好**，数据合规优先
- 代码模型 Codestral 对标 DeepSeek Coder
- 开源模型质量在同规模中领先

---

## xAI · Grok 系列

| 模型 | 发布 | 特点 |
|------|------|------|
| **Grok 3** | 2025.2 | 推理能力强，实时接入 X/Twitter 数据 |
| **Grok 3 mini** | 2025 | 轻量快速，免费用户可用 |
| **Grok Imagine** | 2026.2 | 图像+视频生成，v1.0 支持音频 |

**特点：**
- 马斯克旗下，整合 X（Twitter）实时数据，信息时效性强
- 对部分话题限制较少
- 2026年初美国市场份额快速增长（17.8%）
- 中国大陆访问受限

---

## 📊 权威评测榜单

> 以下为可独立核实的真实评测平台，数据由第三方或社区维护，非模型厂商自评：

| 榜单 | 地址 | 评测内容 |
|------|------|---------|
| **LMArena 人类偏好榜** | [lmarena.ai](https://lmarena.ai) | 真实用户盲测投票，600万+次评分，衡量模型综合表现 |
| **SWE-bench 代码榜** | [swebench.com](https://www.swebench.com) | 解决真实 GitHub Issue，代码能力黄金标准 |
| **Artificial Analysis** | [artificialanalysis.ai/leaderboards/models](https://artificialanalysis.ai/leaderboards/models) | 质量/速度/价格综合排名，100+ 模型横向对比 |
| **HuggingFace 开源榜** | [huggingface.co/spaces/open-llm-leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) | 开源模型专项，含 MMLU-Pro、GPQA、MATH |

---

## 综合对比速查（2026年4月）

| 维度 | 最强推荐 |
|------|---------|
| 代码能力 | Claude Opus 4.5（80.9%）、Gemini 3.1 Pro（80.6%）、MiniMax M2.5（80.2%） |
| 推理/数学 | o3，Gemini 2.5 Pro，DeepSeek R1 |
| 创意写作 | Claude Opus 4.6，GPT-4o |
| 超长文本 | Llama 4 Scout（1000万Token），Gemini 2.5 Pro |
| 速度/响应 | GPT-4o mini，Gemini 2.0 Flash，Claude Haiku |
| 多模态（图像/视频） | GPT-4o，Gemini 2.0，Llama 4 |
| 开源/私有化 | Llama 4，DeepSeek R1，Qwen2.5 |
| 性价比 | DeepSeek V3，o4-mini，Gemini Flash |
| 多 Agent 协作 | Claude Opus 4.6（Agent Teams） |

---

## 官方文档入口

| 模型 | 使用入口 | 开发者 API |
|------|---------|-----------|
| GPT 系列 | [chatgpt.com](https://chatgpt.com) | [platform.openai.com](https://platform.openai.com) |
| Claude 系列 | [claude.ai](https://claude.ai) | [console.anthropic.com](https://console.anthropic.com) |
| Gemini 系列 | [gemini.google.com](https://gemini.google.com) | [ai.google.dev](https://ai.google.dev) |
| Llama 系列 | 本地部署 [ollama.com](https://ollama.com) | [llama.meta.com](https://llama.meta.com) |
| Grok 系列 | [x.ai](https://x.ai) | [console.x.ai](https://console.x.ai) |

---

## 下一步

- [M2-02 国内主流模型](./02-domestic-models.md)
- [M2-03 模型横向对比与选型](./03-comparison.md)
- [📚 完整参考资源](../references.md)
