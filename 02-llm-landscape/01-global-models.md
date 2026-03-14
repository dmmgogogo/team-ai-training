# M2-01 · 国际主流大模型

> 最后更新：2026年3月

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

| 模型 | 发布 | 特点 | 适合 |
|------|------|------|------|
| **GPT-4o** | 2024.5 | 多模态（文本/图像/音频），速度快，性价比高 | 日常任务、开发 API |
| **GPT-4.1** | 2025 | 超长上下文（1M token），强代码能力 | 大文件分析、代码任务 |
| **o3** | 2025.4 | 推理增强，慢思考，复杂问题首选 | 数学、代码、逻辑题 |
| **o4-mini** | 2025.4 | o3 的轻量版，速度快成本低，支持图像 | 日常推理、性价比 |
| **GPT-5** | 2026 | 新旗舰，综合能力全面升级 | 顶级复杂任务 |

**特点：**
- 生态最完善，插件/工具最多
- API 最成熟，文档最好
- o3 / o4-mini 推理能力行业领先
- GPT Image 1（2025.3）替代 DALL-E 3，图像生成大幅提升
- 多模态能力强（图像、语音、视频）

**入口：** chatgpt.com / platform.openai.com

---

## Anthropic · Claude 系列

| 模型 | 发布 | 特点 | 适合 |
|------|------|------|------|
| **Claude Sonnet 4.6** | 2026.2 | 最新 Sonnet，代码极强，默认免费可用 | 编程助手、日常任务 |
| **Claude Opus 4.6** | 2026.2 | 旗舰级，1M 上下文，支持 Agent Teams | 复杂分析、长文写作、多 Agent |
| **Claude Opus 4.5** | 2025.11 | 价格下降 67%，输出 token 减少 76% | 高性价比复杂任务 |
| **Claude 3.7 Sonnet** | 2025 | Extended Thinking（慢思考） | 深度推理、代码审查 |
| **Claude Haiku** | - | 极快极便宜 | 高频简单任务 |

**特点：**
- **代码能力极强**，开发者最爱（Cursor 底层默认使用 Claude）
- Opus 4.6 支持 **Infinite Chats**（无上下文限制错误）和 **Agent Teams**（多 Agent 协作）
- 安全和对齐做得好，输出可靠性高
- 擅长长文本写作和结构化输出

**入口：** claude.ai / console.anthropic.com

---

## Google DeepMind · Gemini 系列

| 模型 | 发布 | 特点 | 适合 |
|------|------|------|------|
| **Gemini 2.0 Flash** | 2025 | 速度快、成本低、多模态 | 日常任务、图像理解 |
| **Gemini 2.5 Pro** | 2025.3 | 首个明确的"思维模型"，登顶 LMArena | 复杂推理、大文件分析 |
| **Gemini 2.0 Ultra** | 2025 | 顶级能力 | 企业高端需求 |

**特点：**
- **Gemini 2.5 Pro 是 Google 迄今最强推理模型**，发布即登顶人类偏好榜
- 上下文窗口超大（Gemini 1.5 Pro 可达 200 万 Token）
- 与 Google 生态深度集成（Workspace、搜索、Android）
- 多模态能力强：文本、图像、视频、音频
- 有免费额度，适合个人试用

**入口：** gemini.google.com / ai.google.dev

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

## 综合对比速查（2026年3月）

| 维度 | 最强推荐 |
|------|---------|
| 代码能力 | Claude Sonnet 4.6，o3，DeepSeek V3 |
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
