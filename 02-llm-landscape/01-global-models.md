# M2-01 · 国际主流大模型

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02
>
> 本页 = **当前快照（2026-11）** + **历史沿革（2024–2026）**。
> 快照会过期，方法和入口长期有效；每个会过期的数字都带来源和日期，查不到的写"以官网为准"。

---

## 一句话结论

截至 2026-11，国际第一梯队是 **Claude 5.5 家族（Anthropic）、GPT-6 家族（OpenAI）、Gemini 4（Google）** 三强；Meta 以 **Muse Wonder / Muse Spark** 重返前沿，xAI 的 **Grok 4.7** 主打性价比。选型不要背"谁第一"，要背**档位、成本结构、上下文和可用性**。

---

## 当前格局（2026-11 快照）

| 厂商 | 当前旗舰 | 日常/性价比档 | 开源或开放权重 | 官方入口 |
|------|----------|---------------|----------------|----------|
| Anthropic | Claude Fable 5.1 / Opus 5.5 | Sonnet 5.5、Haiku 5.5 | ❌ | [claude.com](https://claude.com) · [docs](https://platform.claude.com/docs/en/home) |
| OpenAI | GPT-6 Astra | GPT-6.1 Sol / Terra、GPT-6 Sol / Luna | ❌（另有 gpt-oss 开源权重） | [openai.com](https://openai.com) · [docs](https://developers.openai.com/api/docs) |
| Google DeepMind | Gemini 4 Carbon（限量）/ Gemini 4 Argon | Gemini 3.8 Flash 等 Flash 档 | Gemma 系列 | [gemini.google.com](https://gemini.google.com) · [ai.google.dev](https://ai.google.dev) |
| Meta | Muse Wonder / Muse Wonder Full | Muse Spark 1.3 | Llama 系列（开放权重） | [ai.meta.com](https://ai.meta.com) |
| xAI（对外品牌 SpaceXAI） | Grok 4.7 | Grok 4.7（原价即为性价比档） | ❌ | [x.ai](https://x.ai) · [docs.x.ai](https://docs.x.ai) |
| Mistral AI | Mistral Large 4 | Small / Codestral 系 | Mistral 开源系 | [mistral.ai](https://mistral.ai) |

> 命名统一约定：**Claude 5.5 家族**（Opus / Sonnet / Haiku 5.5）、**GPT-6 家族**（Astra 旗舰、Sol/Terra 中档、Luna 轻量）、**Gemini 4**（Carbon 前沿限量、Argon 主力）、**Grok 4.x**、**Muse**（Meta）。

---

## 国际模型生态总览（稳定层）

```
国际主流大模型
├── OpenAI          → GPT-6 家族（通用 + 推理 + Agent）
│                     └── gpt-oss（开源权重，私有化备选）
├── Anthropic       → Claude 5.5 家族（编码、长任务、对齐）
│                     └── Fable / Mythos（前沿档）
├── Google DeepMind → Gemini 4（多模态、超长上下文、生态）
│                     └── Gemma（开放权重）
├── Meta            → Muse（前沿闭源）/ Llama（开放权重）
├── xAI             → Grok 4.x（实时信息、X 生态、性价比）
└── Mistral AI      → Mistral / Codestral（欧洲合规、开源）
```

---

## 各家"稳定认知"与当前版本

### Anthropic · Claude 5.5 家族

**稳定认知（长期有效）**
- 编码、长程 Agent、长文档改写是传统强项；指令遵循与"可读性"稳定。
- 产品分层清晰：Fable/Mythos 前沿档 → Opus 主力档 → Sonnet 平衡档 → Haiku 轻量档。
- Prompt caching、batch、effort 档位是控成本的关键旋钮（见下方价格与折扣）。

**当前版本时间线（2026）**

| 版本 | 发布时间 | 关键变化 | 现状（2026-11） |
|------|----------|----------|-----------------|
| Claude Haiku 5.5 | 2026-10-07 | 主打高并发、低成本、低延迟 | 当前轻量档 |
| Claude Sonnet 5.5 | 2026-09-28 | Opus 5.5 的更快更便宜补充 | 当前平衡档 |
| Claude Opus 5.5 | 2026-09-22 | 多数任务达到 Fable 5.1 水平，运行成本比 Opus 5 低 40% | 当前主力档 |
| Claude Fable 5.1 / Mythos 5.1 | 2026-09-01 | 前沿编码与知识工作模型 | 当前前沿档 |
| Claude Opus 5 | 2026-07-24 | 智能接近 Fable 5，价格约其一半 | 仍可用（$5/$25） |
| Claude Sonnet 5 | 2026-06-30 | 更具 Agent 能力的 Sonnet | 仍可用（$2/$10） |

> 来源：[Anthropic 发布说明](https://support.claude.com/zh-CN/articles/12138966-%E5%8F%91%E5%B8%83%E8%AF%B4%E6%98%8E)（更新至 2026-11-06）；[Claude 模型总览](https://platform.claude.com/docs/en/models/overview)、[Pricing](https://platform.claude.com/docs/en/about-claude/pricing)（读取于 2026-11-07）。

**当前规格与价格（每百万 token，USD）**

| 模型 | 上下文 | 最大输出 | 输入 | 输出 | 缓存写（5m/1h） | 缓存读 |
|------|--------|----------|------|------|------------------|--------|
| Fable 5.1 / Mythos 5.1 | 1M | 128K | $10 | $50 | $12.50 / $20 | $0.25 |
| Opus 5.5 | 1M | 128K | $4 | $20 | $5 / $8 | $0.20 |
| Sonnet 5.5 | 1M | 128K | $2 | $10 | $2.50 / $4 | $0.10 |
| Haiku 5.5（≤100K 输入） | 1M | 128K | $0.10 | $0.50 | $0.125 / $0.20 | $0.01 |
| Haiku 5.5（>100K 输入） | 1M | 128K | $0.50 | $2.50 | $0.625 / $1 | $0.05 |

> 来源：[Claude Pricing](https://platform.claude.com/docs/en/about-claude/pricing)（2026-11-07）。Batch 处理约为标准价 5 折（[Batch processing](https://docs.claude.com/en/docs/build-with-claude/batch-processing)）。

---

### OpenAI · GPT-6 家族

**稳定认知**
- 模型产品线最完整：旗舰 Astra、中档 Sol/Terra、轻量 Luna，另按场景分 Cyber、Rosalind 等专用模型。
- Responses API + 工具生态（web search、file search、computer use、MCP）成熟，适合做 Agent 与产品集成。
- 价格梯度大：同代旗舰与轻量档差 100 倍，**分层路由的收益极高**。

**当前版本时间线（2026）**

| 版本 | 发布时间 | 关键变化 | 现状（2026-11） |
|------|----------|----------|-----------------|
| GPT-6 Sol / Luna（10 月版） | 2026-10-07 | 进入 ChatGPT Chat 标签页，配 Intelligent UI | 当前 ChatGPT 默认档 |
| GPT-6.1 Sol | 2026-09-29 | DevDay 发布，定位"接近 Astra、价格低很多" | 当前性价比主力 |
| GPT-6 Astra | 2026-09-03（09-04 起公开；Bedrock 09-08 上市） | 旗舰；1.05M 上下文，ARC-AGI-3 报 98.6%（厂商口径） | 当前旗舰 |
| GPT-6 Sol / Luna（9 月版） | 2026-09 | 面向 Work / Codex 的编码与轻量档 | Work / Codex 在用 |
| GPT-5.6 Sol / Terra / Luna | 2026-07-09 | 公开发布（6 月底预览），分三档 | 上一代，仍可用 |
| GPT-5.4 | 2026-03-05 | 更便宜的编码/专业工作模型 | 仍可用（$2.50/$15） |
| GPT-5.5 / 5.5 Instant | 2026 上半年（最晚 5 月已可用） | 面向编码与专业工作 | 仍可用 |

> 来源：[OpenAI 模型目录](https://developers.openai.com/api/docs/models)（读取于 2026-11-07）；GPT-6 Astra 发布：[The New Stack 2026-09-03](https://thenewstack.io/tns-daily/september-3-2026/)；GPT-6.1 Sol 与取消 GPT-6.1 Astra：[Rai News 2026-09-29](https://www.rainews.it/articoli/2026/09/scienza-tecnologia-tech-intelligenza-artificiale-openai-lancia-gpt-6-1-sol-al-posto-di-gpt-6-1-astra-bf34a832-b12d-4752-ac78-dd323c169557.html)；GPT-6 Sol/Luna 进入 ChatGPT：[gihyo 2026-10-08](https://gihyo.jp/article/2026/10/chatgpt-gpt-6-with-intelligent-ui)；GPT-5.6：[VTV 2026-07-08](https://beta1.vtv.vn/openai-se-ra-mat-gpt-56-sau-khi-duoc-my-chap-thuan-100260708220052431.htm)。

**当前规格与价格（每百万 token，USD，标准档）**

| 模型 | 上下文 | 最大输出 | 输入 | 缓存输入 | 输出 | 备注 |
|------|--------|----------|------|----------|------|------|
| GPT-6 Astra | 1.05M | 128K | $10 | $1 | $50 | >272K 输入按 2x 输入 / 1.5x 输出 |
| GPT-6.1 Sol | 1.05M | 128K | $2 | $0.10 | $10 | 定位接近 Astra 的低价档 |
| GPT-6.1 Terra | — | — | $1 | $0.05 | $5 | 视觉/电脑操作/写作 |
| GPT-6 Sol | — | — | $2 | $0.20 | $10 | 编码与 Agent |
| GPT-6 Luna | — | — | $0.10 | $0.01 | $0.50 | 高并发轻量档 |

> 来源：[OpenAI Pricing](https://developers.openai.com/api/docs/pricing)（2026-11-07）。Batch / Flex 为 5 折，Fast 为 2 倍，Ultrafast 为 6 倍；缓存写为输入价 1.25 倍。

---

### Google DeepMind · Gemini 4

**稳定认知**
- 多模态（文本/图像/视频/音频/PDF）与超长上下文是核心差异点。
- 版本节奏快、Flash 档密集；**生命周期短，必须看弃用公告**。
- 2026 年策略转向"先给受信测试者/防御方，再逐步放开"。

**当前版本时间线（2026）**

| 版本 | 发布时间 | 关键变化 | 现状（2026-11） |
|------|----------|----------|-----------------|
| Gemini 4 Carbon | 2026-10-28 | 面向网络安全防御与长程任务；AA 智能指数报 59（发布口径） | 仅限受信防御方/合作伙伴，尚未全面开放 |
| Gemini 4 Argon | 2026-09-30 发布、2026-10-13 全面可用 | 1,048,576 统一上下文；多模态输入；Vals Index 报第一 | 当前主力可用前沿模型 |
| Gemini 3.8 Flash | 2026-09-02 | Flash 档迭代，另有政府限定的网络安全版本 | 仍可用 |
| Gemini 3.5 / 3.6 / 3.7 Flash | 2026 年内 | Flash 档持续迭代 | 逐步被替代 |
| Gemini 3.1 Pro | 2026-02 | 3.x 代 Pro 升级 | 上一代 |

> 来源：[Gemini 4 Argon 发布（2026-10-13）](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)；[Blockchain.News 2026-10-13](https://blockchain.news/news/google-launches-gemini-4-argon-ai-model-enterprise-developer)；[Gemini 4 Carbon 公告（2026-10-28）](https://blockchain.news/news/google-gemini-4-carbon-cybersecurity-benchmarks)；[Gemini 3.8 Flash 2026-09-02](https://blockchain.news/news/google-gemini-3-8-flash-cyber-release)。

**价格（每百万 token，USD）**

| 模型 | 输入 | 输出 | 缓存输入 | 说明 |
|------|------|------|----------|------|
| Gemini 4 Argon | $2（促销） | $10（促销） | $0.10（约 95% off） | 促销至 2026-11-30；之后 $4 / $20 |
| Gemini 4 Carbon | $2（同 Argon 促销口径） | $10 | 同上 | 尚未全面开放，价格以官网为准 |

> 来源：[Gemini API 定价](https://ai.google.dev/gemini-api/docs/pricing)（以官网为准）；促销与上下文细节：[BenchGecko 2026-10-15](https://benchgecko.ai/blog/gemini-4-argon-on-benchgecko)、[Blockchain.News 2026-10-13](https://blockchain.news/news/google-launches-gemini-4-argon-ai-model-enterprise-developer)。

---

### Meta · Muse

**稳定认知**
- 2026 年以 **Muse** 品牌重返前沿：`Muse Wonder` 主打记忆与长程任务，`Muse Spark` 主打更快更轻。
- Llama 系列仍是开放权重/私有化的重要选项，但前沿能力已由 Muse 承接。

**当前版本（2026）**

| 版本 | 发布时间 | 关键变化 | 现状 |
|------|----------|----------|------|
| Muse Wonder / Wonder Full | 2026-10-12 | 主动记忆、编码与长任务；Wonder Full 仅订阅可用 | 当前前沿档 |
| Muse Spark 1.3 | 2026-09-02 | 1M 上下文，文本/图像/视频/PDF 输入 | 当前轻量 Agent 档 |
| Muse Spark 1.2 / 1.1 | 2026 年内 | 迭代版本 | 逐步被替代 |
| Llama 4 | 2025-04 | 开放权重，长上下文 | 私有化仍在用 |

> 来源：[WION 2026-10-13](https://www.wionews.com/technology/meta-launches-muse-wonder-and-wonder-full-ai-models-how-they-compare-with-gpt-6)（Muse Wonder，$4/$20）；[EmpirioLabs 模型卡](https://docs.empiriolabs.ai/models/muse-spark-1-3)（Muse Spark 1.3：2026-09-02，1M 上下文，$1.25/$4.25，第三方平台报价）。

---

### xAI · Grok 4.x

**稳定认知**
- 与 X 平台实时信息联动；长任务/终端 Agent 是 2026 年的发力点。
- 定价简单透明、同价升级，适合作为"第二供应商"或成本兜底。
- 官方对外品牌在 2026 年出现 **SpaceXAI** 表述，文档仍用 xAI / Grok 命名。

**当前版本（2026）**

| 版本 | 发布时间 | 关键变化 | 现状 |
|------|----------|----------|------|
| Grok 4.7 | 2026-09-21 | 同价升级；500K 上下文；长程编码/终端能力提升 | 当前主力 |
| Grok 4.6 | 2026-08-12 | 主打长时间运行的 Agent 任务 | 仍可用 |
| Grok 4.5 / 4.3 / 4.20 | 2026 年内 | 快速迭代 | 逐步被替代 |

> 来源：[xAI Grok 4.7 发布（2026-09-21）](https://x.ai/news/grok-4-7)，细节与价格整理见 [LLM Stats](https://llm-stats.com/blog/research/grok-4-7-launch)；Grok 4.6：[OrcaRouter 2026-08](https://www.orcarouter.ai/blog/grok-4-6-release-date)。

**价格（每百万 token，USD）**：Grok 4.7 在 <200K 输入时 **$2 输入 / $0.50 缓存 / $6 输出**；≥200K 时整单按 **$4 / $1 / $12** 计。来源同上（2026-09-21）。

---

### Mistral AI（简述）

欧洲厂商，合规语境（GDPR/数据驻留）友好，开源系与 Codestral 代码模型是主要差异点。2026 年前沿能力与三强有差距，更适合作为**欧洲区域合规备选**或**低成本自托管**。入口：<https://mistral.ai> / <https://docs.mistral.ai>（具体版本与价格以官网为准）。

---

## 价格快照（2026-11，USD / 每百万 token）

> 用途：做预算时的**起点**，不是报价承诺。下单前用官方定价页复核。

| 模型 | 输入 | 输出 | 缓存读 | 来源（读取日） |
|------|------|------|--------|----------------|
| Claude Fable 5.1 | $10 | $50 | $0.25 | [Anthropic Pricing](https://platform.claude.com/docs/en/about-claude/pricing)（11-07） |
| Claude Opus 5.5 | $4 | $20 | $0.20 | 同上 |
| Claude Sonnet 5.5 | $2 | $10 | $0.10 | 同上 |
| Claude Haiku 5.5（≤100K） | $0.10 | $0.50 | $0.01 | 同上 |
| GPT-6 Astra | $10 | $50 | $1 | [OpenAI Pricing](https://developers.openai.com/api/docs/pricing)（11-07） |
| GPT-6.1 Sol | $2 | $10 | $0.10 | 同上 |
| GPT-6 Luna | $0.10 | $0.50 | $0.01 | 同上 |
| Gemini 4 Argon（促销） | $2 | $10 | $0.10 | [Gemini Pricing](https://ai.google.dev/gemini-api/docs/pricing)（11-07） |
| Grok 4.7（<200K） | $2 | $6 | $0.50 | [LLM Stats / xAI](https://llm-stats.com/blog/research/grok-4-7-launch)（09-21） |
| Muse Wonder | $4 | $20 | 以官网为准 | [WION](https://www.wionews.com/technology/meta-launches-muse-wonder-and-wonder-full-ai-models-how-they-compare-with-gpt-6)（10-13） |
| Muse Spark 1.3 | $1.25 | $4.25 | $1.00 | [EmpirioLabs](https://docs.empiriolabs.ai/models/muse-spark-1-3)（第三方平台价） |

**缓存与批量折扣（方法论，长期有效）**
- **缓存读**通常是输入价的 5%–10%，缓存写约为输入价的 1.25 倍；固定 system prompt、工具定义、长文档放前面才能命中。
- **Batch**：OpenAI Batch/Flex 5 折、Anthropic Batch 约 5 折、Gemini Batch 档位更便宜；代价是延迟（分钟到小时级）。
- **长上下文溢价**：OpenAI >272K 输入整单 2x 输入 / 1.5x 输出；Grok >200K 整单进入高价档。**"刚好超一点"最贵**。

---

## 榜单口径（2026-10 / 2026-11 快照）

> 榜单是**参考**，不是选型结论。不同榜单测的东西不同，厂商自报数据要打折看。

| 榜单 | 它测什么 | 2026-10/11 快照 | 使用建议 |
|------|----------|------------------|----------|
| **Artificial Analysis Intelligence Index** | 综合智能（多基准合成） | Gemini 4 Carbon (high) 60；Claude Opus 5.5 (max) 59；GPT-6 Astra (max) 57；Claude Sonnet 5.5 (max) 55（[AA 榜单](https://artificialanalysis.ai/leaderboards/models)，读取 11-07） | 看"同 effort 档位"对比，别跨档比 |
| **LMArena** | 人类盲测偏好 | Instruction Following：Gemini 4 Carbon / Argon 1525、Opus 5.5 1522、Fable 5.1 1500、Muse Wonder 1498（[BenchLeader 汇总 LMArena，数据 10-28](https://www.benchleader.com/benchmarks/lmarena_text_if)，读取 11-07） | 贴近"人觉得好不好"，不测硬任务 |
| **Epoch Capabilities Index（ECI）** | 跨基准能力指数 | 榜首 GPT-6 Astra，ECI 169；收录 425 个模型（[Epoch AI](https://epoch.ai/benchmarks?view=graph&tab=eci)，更新 11-07） | 看长期趋势与不确定性区间 |
| **SWE-bench / DeepSWE** | 真实代码修复 | 以实时榜单为准；厂商自报：Grok 4.7 DeepSWE v1.1 71.0%、GLM-5.3 66.9%（均为自报） | 代码选型必须跑自己的仓库评测 |
| **Vals Index** | 金融/法律/编码等经济价值任务 | 公开页最近更新 2026-05-28：Claude Opus 4.8 70.17%、GPT-5.5 67.62%；Google 称 Argon 在 10-13 发布时位列第一 | 更新滞后，引用必须带日期 |

> 结论：**榜单用来缩小候选集，真实评测用来做决定。** 至少用 20–50 条自己业务的任务做 A/B。

---

## 动态查询入口（替代静态排名）

| 类型 | 入口 |
|------|------|
| 综合质量/速度/价格 | <https://artificialanalysis.ai/leaderboards/models> |
| 人类偏好盲测 | <https://arena.ai/leaderboard> |
| 代码修复 | <https://www.swebench.com> |
| 能力指数（ECI） | <https://epoch.ai/benchmarks?view=graph&tab=eci> |
| 经济价值任务 | <https://www.vals.ai/benchmarks> |
| OpenAI 官方 | <https://developers.openai.com/api/docs/models> |
| Anthropic 官方 | <https://platform.claude.com/docs/en/models/overview> |
| Google 官方 | <https://ai.google.dev/gemini-api/docs/models> |
| xAI 官方 | <https://docs.x.ai> |

---

## 历史沿革（2024–2026，倒序）

> 历史层规则：只追加、不回改；已停用/被替代的版本标注 ~~弃用~~。

### Anthropic Claude
- 2026-10-07：Haiku 5.5 发布（Claude 5.5 家族补齐轻量档）
- 2026-09-28：Sonnet 5.5 发布
- 2026-09-22：Opus 5.5 发布（性能接近 Fable 5.1，成本比 Opus 5 低 40%）
- 2026-09-01：Fable 5.1 / Mythos 5.1 发布
- 2026-07-24：Opus 5 发布（接近 Fable 5，价格约一半）
- 2026-07-01：Fable 5 / Mythos 5 访问恢复（6-12 因出口管制暂停）
- 2026-06-30：Sonnet 5 发布；2026-06-09：Fable 5 发布
- 2026-05-28：Opus 4.8；2026-04-16：Opus 4.7
- 2026-02-17：Sonnet 4.6；2026-02-05：Opus 4.6
- 2026-01-16：Opus 4 / 4.1 从 Claude 与 Claude Code 移除 ~~弃用~~
- 2025-11-24：Opus 4.5；2025-10-15：Haiku 4.5；2025-09-29：Sonnet 4.5
- 2025-05-22：Claude 4（Opus 4 / Sonnet 4）
- 2024-06-20：Claude 3.5 Sonnet；2024-03-04：Claude 3 家族

### OpenAI GPT
- 2026-10-07：GPT-6 Sol / Luna（10 月版）进入 ChatGPT
- 2026-09-29：GPT-6.1 Sol 发布；同日确认取消 GPT-6.1 Astra（"频繁忽略指令"）
- 2026-09-03：GPT-6 Astra 发布（09-04 起公开）
- 2026-07-09：GPT-5.6（Sol / Terra / Luna）公开发布
- 2026-05-28 前：GPT-5.5 已可用（Vals Index 当日榜单含 GPT-5.5）
- 2026-03-05：GPT-5.4 发布
- 2025-12：GPT-5.2；2025-11-13：GPT-5.1；2025-08-07：GPT-5
- 2025-04-16：o3 / o4-mini；2025-04-14：GPT-4.1
- 2024-12-17：o1 正式版；2024-05-13：GPT-4o
- 停用节奏：o1/o3/GPT-4 系于 2026-10-23 关停 ~~弃用~~；GPT-4o/4.1 计划 2027-01-14 关停；GPT-5 系计划 2026-12-11 关停

### Google Gemini
- 2026-10-28：Gemini 4 Carbon 发布（限量，防御方优先）
- 2026-10-13：Gemini 4 Argon 全面可用；2026-09-30 首次发布（受信测试者）
- 2026-09-02：Gemini 3.8 Flash
- 2026 年内：3.5 / 3.6 / 3.7 Flash 快速迭代
- 2026-02：Gemini 3.1 Pro
- 2025-11-18：Gemini 3；2025-03：Gemini 2.5；2024-12：Gemini 2.0；2024-02：Gemini 1.5

### Meta
- 2026-10-12：Muse Wonder / Muse Wonder Full 发布
- 2026-09-02：Muse Spark 1.3；2026 年内：1.1 / 1.2
- 2025-04：Llama 4（开放权重）

### xAI
- 2026-09-21：Grok 4.7；2026-08-12：Grok 4.6；2026 年内：4.5 / 4.3 / 4.20
- 2025-07：Grok 4；2025-02：Grok 3

---

## 参考与核实说明

- 本页所有价格读取于 **2026-11-07**；发布说明/榜单页面标注了各自日期。
- 厂商自报的跑分（如 Astra 的 ARC-AGI-3 98.6%、Carbon 的 AA 59）已标注"厂商口径"，未经第三方复现。
- 查不到官方确认的条目（如 Carbon 的完整规格、部分 Flash 版本日期）留白或写"以官网为准"，不做推测。

---

## 下一步

- [M2-02 国内主流模型](./02-domestic-models.md)
- [M2-03 模型横向对比与选型](./03-comparison.md)
- [M5-11 成本管理与模型选型](../05-practical/11-cost-management.md)
- [📚 完整参考资源](../references.md)
