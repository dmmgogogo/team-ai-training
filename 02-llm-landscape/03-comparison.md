# M2-03 · 模型横向对比与选型指南

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02
>
> 选模型不是选"最强的"，而是选"**在当前预算和约束下，任务成功率最高**的"。
> 本页前半部分是长期有效的选型方法，后半部分是 2026-11 的价格/能力快照。

---

## 一句话结论

2026-11 的默认答案：**编码与长任务用 Claude 5.5 家族，通用/Agent 用 GPT-6 家族，超长上下文与多模态用 Gemini 4，国内合规与性价比用 DeepSeek V4 系列 / Qwen3.8 Max / GLM-5.3 / Kimi K3.1 Pro**。先用中档模型做基线，再用自建评测决定是否升级。

---

## 一、选型方法（长期有效）

### 1. 先定义任务，再谈模型

| 问题 | 为什么重要 |
|------|------------|
| 任务的成功标准是什么？ | "看起来不错"无法比较；要有可判定的 rubric 或测试 |
| 错了的代价多大？ | 决定能否用轻量档、是否需要人工复核 |
| 输入/输出各多少 token？ | 直接决定成本结构（输入贵还是输出贵） |
| 延迟要求？ | 推理档位、Batch、Fast 模式都是钱换时间 |
| 数据能否出内网？ | 直接排除或锁定本地部署 |
| 调用量级？ | 1 万次/天和 10 次/天的最优解完全不同 |

### 2. 候选集控制在 3 个以内

按"**一旗舰 + 一中档 + 一低价/开源自托管**"组候选，例如：

- 编码：Claude Opus 5.5（旗舰）/ GPT-6.1 Sol（中档）/ DeepSeek V4 Pro（国产/自托管）
- 高并发分类：Claude Haiku 5.5 / GPT-6 Luna / DeepSeek V4.1-Flash
- 长文档：Gemini 4 Argon / Kimi K3.1 Pro / Qwen3.8 Max

### 3. 用自建评测做决定（20–50 条就够）

- 从真实业务日志里抽任务，覆盖简单/边界/失败案例。
- 同一 prompt、同一参数、同一评测脚本；记录**成功率、人工修改量、单任务成本、P95 延迟**。
- 榜单只用来"排除明显不行"的模型，不用来"证明谁最好"。

### 4. 算总拥有成本（TCO），不只算 token 单价

```
单任务成本 = (输入 token × 输入价 + 缓存写 × 写价 + 输出 token × 输出价) / 1,000,000
月成本 = 单任务成本 × 日调用量 × 30 + 重试/失败成本 + 人工复核成本 + 集成/运维成本
```

低价模型如果成功率低 10%，重试和人工成本可能远超省下的 token 费。**按"每个成功任务"的成本比较，而不是每百万 token。**

### 5. 上线后持续监控

缓存命中率、单任务 token 数、失败率、成本/成功任务。模型厂商每月都在调价/发新版，**选型是持续动作，不是一次性决策**。

---

## 二、选型决策树（2026-11）

```
你的需求是什么？
│
├─ 数据绝对不能出内网？
│   ├─ 中文/低成本 → DeepSeek V4.1-Flash（基于 V4-Flash 的 284B MoE 口径，1M 上下文）
│   ├─ 编程/安全审计 → GLM-5.3（开源权重，1M 上下文）
│   ├─ 长程 Agent → Step 5 Preview（600B/27B 激活）或 Kimi K3.1 Pro（2.8T）
│   └─ 全模态/端侧 → MiMo-V2.6 / Llama 4 / Gemma 4
│
├─ 主要是写代码 / 跑 Coding Agent？
│   ├─ 追求成功率、预算充足 → Claude Opus 5.5
│   ├─ 日常开发循环 → Claude Sonnet 5.5 / GPT-6.1 Sol
│   └─ 预算敏感或国内直连 → DeepSeek V4 Pro / Qwen3.8-Max / GLM-5.3
│
├─ 需要处理超长文档（合同/报告/代码库）？
│   ├─ 国际 → Gemini 4 Argon（1,048,576 统一上下文）/ Claude 5.5（1M）
│   └─ 国内 → Kimi K3.1 Pro（1M）/ Qwen3.8-Max（1M）/ DeepSeek V4（1M）
│
├─ 复杂推理 / 数学 / 科研？
│   ├─ 国际前沿 → Claude Fable 5.1 / GPT-6 Astra / Gemini 4 Carbon（限量）
│   └─ 国内 → DeepSeek V4 Pro / Kimi K3.1 Pro / GLM-5.3
│
├─ 成本敏感、高并发、任务简单？
│   ├─ 国际 → GPT-6 Luna（$0.10/$0.50）/ Claude Haiku 5.5（$0.10/$0.50）
│   └─ 国内 → DeepSeek V4.1-Flash（¥1/¥4 起）/ MiMo-V2.6-Flash（¥1/¥2）/ Qwen Batch
│
├─ 多模态（图/视频/音频/PDF）？
│   ├─ 国际 → Gemini 4 Argon / GPT-6 Astra / Muse Spark 1.3
│   └─ 国内 → Qwen3.8-Max / MiMo-V2.6 / MiniMax M3
│
├─ 必须中文 + 国内合规 + 企业采购？
│   └─ Qwen（阿里云）/ 豆包（火山）/ 混元（腾讯云）/ 文心（百度云）
│
└─ 欧洲合规 / GDPR？
    └─ Mistral Large 4 / Mistral 开源系
```

---

## 三、按场景推荐（2026-11）

| 场景 | 首选 | 备选 | 理由 | 成本提示 |
|------|------|------|------|----------|
| **Coding Agent / 大型重构** | Claude Opus 5.5 | GPT-6 Astra、Kimi K3.1 Pro | 长程编码与工具调用稳定；Kimi 开源可自托管 | Opus 5.5 输出 $20/M，注意 reasoning token |
| **日常编码补全/小改** | Claude Sonnet 5.5 | GPT-6.1 Sol、DeepSeek V4 Pro | 性价比与速度平衡 | 缓存 system prompt + 仓库上下文 |
| **通用问答/办公 Agent** | GPT-6.1 Sol | Claude Sonnet 5.5、Qwen3.8-Max | 工具生态与产品集成成熟 | Batch 5 折适合离线任务 |
| **超长文档分析** | Gemini 4 Argon | Claude Opus 5.5、Kimi K3.1 Pro | 1M 上下文 + 多模态输入 | 注意长上下文溢价与缓存 |
| **复杂推理/科研** | Claude Fable 5.1 | GPT-6 Astra、Gemini 4 Carbon（限量） | 前沿档，慢思考准确率高 | 用 effort 档位控制成本 |
| **高并发分类/抽取/翻译** | Claude Haiku 5.5 | GPT-6 Luna、DeepSeek V4.1-Flash | 单价低、延迟低 | 优先缓存 + Batch；注意 100K 输入分段 |
| **中文内容创作** | Claude Opus 5.5 | Qwen3.8-Max、Kimi K3.1 Pro | 中文表达与风格控制好 | 输出 token 是主要成本 |
| **多模态理解** | Gemini 4 Argon | GPT-6 Astra、MiMo-V2.6 | 原生多模态，输入类型全 | 图片/视频按 token 折算 |
| **国内合规/私有化** | DeepSeek V4.1-Flash | GLM-5.3、Qwen 开源档 | 开放权重、可内网部署 | 算力折旧 + 运维是主要成本 |
| **长程自主 Agent** | Claude Opus 5.5 | Step 5 Preview、Kimi K3.1 Pro | 长任务稳定性与工具使用 | 单任务 token 放大 5–20 倍，务必按任务计量 |
| **欧洲/GDPR** | Mistral Large 4 | Mistral 开源系 | 区域合规与数据驻留 | 能力与三强有差距，按需取舍 |

---

## 四、能力与规格速查（事实项，非评分）

| 模型 | 上下文 | 最大输出 | 多模态输入 | 开源权重 | 价格档（输入/输出，USD 或 CNY） |
|------|--------|----------|------------|----------|-------------------------------|
| Claude Fable 5.1 | 1M | 128K | 文本+图像 | ❌ | $10 / $50 |
| Claude Opus 5.5 | 1M | 128K | 文本+图像 | ❌ | $4 / $20 |
| Claude Sonnet 5.5 | 1M | 128K | 文本+图像 | ❌ | $2 / $10 |
| Claude Haiku 5.5 | 1M | 128K | 文本+图像 | ❌ | $0.10 / $0.50（≤100K） |
| GPT-6 Astra | 1.05M | 128K | 文本+图像 | ❌ | $10 / $50 |
| GPT-6.1 Sol | 1.05M | 128K | 文本+图像 | ❌ | $2 / $10 |
| GPT-6 Luna | — | — | 文本+图像 | ❌ | $0.10 / $0.50 |
| Gemini 4 Argon | 1,048,576 | 65,536（默认） | 文本/图/视频/音频/PDF | ❌ | $2 / $10（促销至 11-30） |
| Gemini 4 Carbon | 以官网为准 | 以官网为准 | 多模态 | ❌ | $2 / $10（同促销口径） |
| Grok 4.7 | 500K | — | 文本+图像 | ❌ | $2 / $6（<200K） |
| Muse Wonder | 以官网为准 | — | 以官网为准 | ❌ | $4 / $20 |
| Muse Spark 1.3 | 1M | 131K | 文本/图/视频/PDF | ❌ | $1.25 / $4.25（平台价） |
| DeepSeek V4 Pro | 1M | 384K | 文本 | ✅ | ¥4.5 / ¥13.5（空闲） |
| DeepSeek V4.1-Flash | 1M | 384K | 文本+图像 | ✅ | ¥1 / ¥4（空闲） |
| Qwen3.8-Max | 1M | 131K | 文本/图/视频 | 部分 | ¥12 / ¥36 |
| Kimi K3.1 Pro | 1M | — | 文本/图/视频 | ✅ | $2 / $10 |
| GLM-5.3 | 1M | 131K | 文本 | ✅ | $1.4 / $4.4（国际站） |
| MiniMax M3 | 1M | — | 原生多模态 | ✅ | 以官网为准 |
| MiMo-V2.6-Pro | — | — | 全模态 | ✅ | ¥3 / ¥6 |
| Step 5 Preview | 1M | — | 文本+视觉 | ✅ | 自部署 |

> 规格与价格来源见 [M2-01](./01-global-models.md) / [M2-02](./02-domestic-models.md) 对应表格；读取于 2026-11-07，下单前以官网复核。

---

## 五、价格快照（2026-11，每百万 token）

> 同一张表里混了 USD/CNY，**比较前先按当日汇率换算**；这里不写死汇率。

| 档位 | 代表模型 | 输入 | 输出 | 缓存读 | 适用 |
|------|----------|------|------|--------|------|
| 前沿 | Claude Fable 5.1 / GPT-6 Astra | $10 | $50 | $0.25 / $1 | 最难的任务、科研、关键决策 |
| 主力 | Claude Opus 5.5 | $4 | $20 | $0.20 | 长程编码、Agent、生产默认 |
| 中档 | Claude Sonnet 5.5 / GPT-6.1 Sol / Gemini 4 Argon | $2 | $10 | $0.10 | 日常开发、通用业务 |
| 中档（国产） | Qwen3.8-Max | ¥12 | ¥36 | ¥1.5 | 国内合规、中文、多模态 |
| 开源旗舰 | Kimi K3.1 Pro / GLM-5.3 | $2 / $1.4 | $10 / $4.4 | $0.20 / $0.26 | 自托管、数据不出网 |
| 高性价比 | DeepSeek V4.1-Flash | ¥1（空闲） | ¥4（空闲） | ¥0.02 | 高并发、批处理、成本敏感 |
| 轻量 | Claude Haiku 5.5 / GPT-6 Luna | $0.10 | $0.50 | $0.01 | 分类、抽取、路由、翻译 |

**折扣叠加顺序（经验）**：缓存 → Batch → 档位/effort → 供应商比价 → 自托管。
通常"缓存 + Batch + 轻量档"三步就能把成本降到旗舰的 1/10 以下。

**官方定价页入口**：[OpenAI](https://developers.openai.com/api/docs/pricing) · [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing) · [Gemini](https://ai.google.dev/gemini-api/docs/pricing) · [DeepSeek](https://api-docs.deepseek.com/zh-cn/quick_start/pricing) · [Qwen](https://platform.qianwenai.com/pricing/api) · [Kimi](https://platform.kimi.ai/docs/pricing/chat) · [GLM](https://z.ai/pricing) · [MiniMax](https://platform.minimax.io/docs/pricing/overview) · [MiMo](https://mimo.mi.com/docs/en-US/price/pay-as-you-go)。

---

## 六、本地部署参考配置（2026）

> 以下是**工程估算**，不是厂商承诺。实际显存取决于量化方式、上下文长度、并发数和推理框架。

### 显存估算公式

```
权重显存 ≈ 参数量 × 每参数字节数
  FP16 = 2 字节；FP8 = 1 字节；INT4 ≈ 0.5 字节（含量化开销略高）
KV Cache ≈ 层数 × 2 × hidden × 上下文长度 × 并发数 × 字节数
总显存 ≈ 权重 + KV Cache + 框架开销（约 10–20%）
```

### 参考配置

| 模型/规模 | 精度 | 权重显存（估算） | 最低配置 | 推荐配置 | 适用场景 |
|-----------|------|------------------|----------|----------|----------|
| 7–8B 小模型 | INT4 | 4–5 GB | 8 GB 显存 | 16 GB 显存 | 分类、补全、端侧 |
| 32B 稠密 | INT4 / FP8 | 18–20 GB / 32 GB | 24 GB 显存 | 48–80 GB 显存 | 中文对话、轻量 Agent |
| 70B 稠密 | INT4 | 38–42 GB | 48 GB 显存 | 2× 80 GB | 通用私有化 |
| DeepSeek V4.1-Flash（按 V4-Flash 284B/13B 口径，官方未单独公布） | FP8 / INT4 | 约 284 GB / 约 150 GB | 4× H100 80GB | 8× H100/H200 | 高吞吐私有化 |
| Step 5 Preview（600B/27B 激活） | FP8 / INT4 | 约 600 GB / 约 320 GB | 8× H100 80GB | 8× H200 141GB | 长程 Agent |
| Kimi K3.1 Pro（2.8T/104B 激活） | INT4 | 约 1.4 TB+ | 多机集群 | 16× H200 以上 | 前沿能力私有化 |
| DeepSeek V4 Pro（1.6T/49B 激活） | FP8 / INT4 | 约 1.6 TB / 约 800 GB | 多机集群 | 16× H200 以上 | 旗舰自托管 |

> 参数来源：DeepSeek V4 系列（[官方](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)）、Step 5（[极客公园](https://www.geekpark.net/news/372400)）、Kimi K3.1 Pro（[heise](https://www.heise.de/news/Chinesisches-Open-Weight-Modell-Kimi-K3-1-Pro-rueckt-an-US-Spitzenmodelle-heran-11500459.html)）。显存为按公式估算，务必以实测为准。

### 工具选型

| 工具 | 适合 | 说明 |
|------|------|------|
| **Ollama** | 本地开发、单机 | 一条命令跑模型，适合 7–70B |
| **LM Studio** | 非开发者、桌面 | GUI，模型下载/量化方便 |
| **vLLM** | 生产 API | 高并发、PagedAttention、OpenAI 兼容 |
| **SGLang** | 生产 API | 结构化生成/前缀缓存强，Step 5 官方推荐之一 |
| **llama.cpp** | 端侧/CPU | 量化格式全，适合边缘设备 |

### 自托管前的三笔账

1. **算力账**：GPU 采购/租用 + 电费 + 机房；一张 H100 的月租通常高于大多数团队一个月的 API 账单。
2. **运维账**：推理框架升级、模型更新、监控、故障处理都要人。
3. **能力账**：开源模型与闭源前沿通常有 3–12 个月差距，关键任务要接受这个差距。

**结论**：月 API 支出 < 约 2 万元人民币、且无强合规要求时，通常**不值得自建**；数据不出网、超大规模、或需要深度定制时才自托管。

---

## 七、榜单怎么用（2026-11 快照）

| 榜单 | 参考价值 | 注意事项 |
|------|----------|----------|
| Artificial Analysis Intelligence Index | 快速看综合档位 | 同 effort 档位比较；成本/任务也要看 |
| LMArena | 人类偏好 | 不测硬任务，容易被风格影响 |
| SWE-bench / DeepSWE | 代码修复 | 与 harness 强相关，跨 harness 不可比 |
| Epoch ECI | 长期能力趋势 | 有不确定性区间，别拿小数点排名 |
| Vals Index | 经济价值任务 | 更新可能滞后，引用带日期 |

具体 2026-10/11 数据与来源见 [M2-01 榜单口径](./01-global-models.md#榜单口径2026-10--2026-11-快照)。

---

## 八、快速决策总结

```
数据不出网        → DeepSeek V4.1-Flash / GLM-5.3 / Step 5 / Kimi K3.1 Pro / 混元 Hy4 / ERNIE 5.5 Flash Base
编码 Agent        → Claude Opus 5.5；省钱用 Sonnet 5.5 / GPT-6.1 Sol
超长文档          → Gemini 4 Argon / Claude 5.5 / Kimi K3.1 Pro
复杂推理          → Claude Fable 5.1 / GPT-6 Astra / Gemini 4 Carbon（限量）
高并发简单任务    → Claude Haiku 5.5 / GPT-6 Luna / DeepSeek V4.1-Flash
中文 + 国内合规   → Qwen3.8-Max / DeepSeek V4 / GLM-5.3 / 豆包 / 混元
多模态            → Gemini 4 / Qwen3.8-Max / MiMo-V2.6 / MiniMax M3
欧洲合规          → Mistral Large 4
```

**最后一句**：先跑 20 条真实任务的自建评测，再谈选型；没有评测的"最强模型"只是别人的结论。

> 📌 **2026-11 第一周补录**：混元 Hy4（11-04）、ERNIE 5.5 Flash Base（11-05，开放权重）、豆包 Seed-Evolving（11-02）、Inkling 2 Small（11-05，权重待发）已加入可选项；Qwen4 仅预热、尚未发布。新模型先确认许可证与可用性，再进评测。

---

## 历史沿革

- **2023**：选型主要看"单个最强模型"（GPT-4），场景差异不大。
- **2024**：模型数量爆发、价格战开始，出现"按任务选模型"和"大小模型分层"。
- **2025**：推理模型（o 系列 / DeepSeek R1）让"思考档位"成为选型维度；长上下文与 RAG 的取舍开始被讨论。
- **2026**：模型普遍多档位、Agent 化；选型重点转向"任务成本 + 自建评测 + 可替换性"，而不是榜单名次。

---

## 下一步

- [M2-01 国际主流模型](./01-global-models.md)
- [M2-02 国内主流模型](./02-domestic-models.md)
- [M5-11 成本管理与模型选型](../05-practical/11-cost-management.md)
- [M3-01 AI 编程工具概览](../03-ai-coding-tools/01-overview.md) — 开发者专属工具
- [M5-01 Prompt 工程入门](../05-practical/01-prompt-engineering.md) — 用好模型的关键
