# ⭐️ M5-11 · 成本管理与模型选型（2026 版）

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02
>
> AI 用得爽，账单可能吓一跳。2026 年的成本管理，核心不是"找最便宜的模型"，而是**理解 token 的计价结构，把每一分钱花在能提高成功率的地方**。

---

## 一句话结论

同一个任务，用旗舰模型和轻量模型可能差 **40 倍**成本；用错计价方式（长上下文溢价、重复上下文、无缓存、Agent 空转）还会再翻几倍。**先测效果、再算成本、最后才选模型**——这是长期有效的顺序。

---

## 一、Token 到底怎么计费（2026 版）

### 1. 基础换算

- 1 个 token ≈ 0.75 个英文单词
- 中文因分词器而异：1 个汉字通常约 0.5–1 个 token，**1000 个中文字大约 700–1200 token**
- 精确数字请用各厂商的 tokenizer / token 计数接口实测，不要背换算系数

```
"你好世界"   → 约 4 个 token（视分词器而定）
"Hello World" → 约 2–3 个 token
```

### 2. 2026 年的计费公式

```
单次调用费用 =
    未缓存输入 token × 输入单价
  + 缓存命中输入 token × 缓存读单价
  + 缓存写入 token × 缓存写单价
  + 输出 token（含 reasoning token）× 输出单价
  + 工具调用/搜索等附加费
```

**2026 年必须注意的 5 个新变量**：

| 变量 | 影响 | 典型例子 |
|------|------|----------|
| **推理 token（reasoning）** | 输出可能翻几倍，且按输出价计费 | Opus 5.5 高 effort、GPT-6 Astra max |
| **缓存写/读** | 写约 1.25× 输入价，读可低至 5%–10% | 长 system prompt、仓库上下文 |
| **长上下文溢价** | 超过阈值后"整单"进入高价档 | OpenAI >272K、Grok >200K |
| **Batch/Flex** | 约 5 折，但延迟高 | 离线标注、批量摘要 |
| **工具调用** | 按次/按 token 另计 | web search、代码解释器、MCP |

### 3. 价格快照（2026-11，每百万 token）

> 用途：做预算的起点。**下单前必须用官方定价页复核**，本表读取于 2026-11-07。

| 模型 | 输入 | 输出 | 缓存读 | 备注 |
|------|------|------|--------|------|
| Claude Fable 5.1 | $10 | $50 | $0.25 | 前沿档 |
| Claude Opus 5.5 | $4 | $20 | $0.20 | 生产主力 |
| Claude Sonnet 5.5 | $2 | $10 | $0.10 | 日常开发 |
| Claude Haiku 5.5（≤100K） | $0.10 | $0.50 | $0.01 | 高并发首选 |
| GPT-6 Astra | $10 | $50 | $1 | >272K 整单 2×/1.5× |
| GPT-6.1 Sol | $2 | $10 | $0.10 | 性价比档 |
| GPT-6 Luna | $0.10 | $0.50 | $0.01 | 轻量档 |
| Gemini 4 Argon（促销） | $2 | $10 | $0.10 | 促销至 2026-11-30，之后 $4/$20 |
| Grok 4.7（<200K） | $2 | $6 | $0.50 | ≥200K 整单 $4/$12 |
| DeepSeek V4.1-Flash（空闲/高峰） | ¥1 / ¥2 | ¥4 / ¥8 | ¥0.02 / ¥0.04 | 空闲时段 5 折 |
| DeepSeek V4 Pro（空闲/高峰） | ¥4.5 / ¥9 | ¥13.5 / ¥27 | ¥0.15 / ¥0.30 | 旗舰 |
| Qwen3.8-Max | ¥12 | ¥36 | ¥1.5 | Batch 5 折 |
| Kimi K3.1 Pro | $2 | $10 | $0.20 | 开源权重 |
| GLM-5.3（国际站） | $1.4 | $4.4 | $0.26 | 开源权重 |
| MiMo-V2.6-Pro | ¥3 | ¥6 | ¥0.025 | 全模态 |

> 来源：[OpenAI Pricing](https://developers.openai.com/api/docs/pricing)、[Claude Pricing](https://platform.claude.com/docs/en/about-claude/pricing)、[Gemini Pricing](https://ai.google.dev/gemini-api/docs/pricing)、[DeepSeek 模型 & 价格](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)、[Qwen3.8-Max](https://www.qianwenai.com/models/qwen3.8-max)、[Kimi (heise 2026-10-26)](https://www.heise.de/news/Chinesisches-Open-Weight-Modell-Kimi-K3-1-Pro-rueckt-an-US-Spitzenmodelle-heran-11500459.html)、[GLM-5.3](https://www.alibabacloud.com/help/ja/model-studio/glm-5-3-by-zhipu)、[MiMo](https://mimo.mi.com/docs/en-US/price/pay-as-you-go)（均读取于 2026-11-07）。
>
> ⚠️ 币种不同，比较前按当日汇率换算；表中不含税、不含工具调用附加费。

**官方定价页入口**（收藏这几个就够了）：

| 平台 | 官方价格页 |
|------|-----------|
| OpenAI | <https://developers.openai.com/api/docs/pricing> |
| Anthropic | <https://platform.claude.com/docs/en/about-claude/pricing> |
| Google Gemini | <https://ai.google.dev/gemini-api/docs/pricing> |
| DeepSeek | <https://api-docs.deepseek.com/zh-cn/quick_start/pricing> |
| 千问 AI 平台 | <https://platform.qianwenai.com/pricing/api> |
| Kimi | <https://platform.kimi.ai/docs/pricing/chat> |
| 智谱 GLM | <https://z.ai/pricing> |
| MiniMax | <https://platform.minimax.io/docs/pricing/overview> |

---

## 二、五个成本杠杆（按收益排序）

### 杠杆 1：Prompt Caching（缓存）——收益最大，最容易被忽略

**原理**：把固定不变的前缀（system prompt、工具定义、长文档、代码库上下文）缓存起来，后续请求命中缓存时按"缓存读价"计费。

| 厂商 | 缓存读折扣 | 缓存写 | 备注 |
|------|-----------|--------|------|
| Anthropic | 约为输入价 **5%**（Opus 5.5：$0.20 vs $4） | 约 1.25× 输入价，有 5 分钟/1 小时 TTL | 显式 `cache_control` |
| OpenAI | 约为输入价 **5%–10%**（Astra $1 vs $10；Sol $0.10 vs $2） | 1.25× 输入价 | 自动前缀缓存，≥1024 token 起效 |
| Gemini | 约 **95% off**（Argon 缓存读 $0.10 vs $2） | 按官方文档 | 隐式缓存为主 |
| DeepSeek | 缓存命中 ¥0.02 vs 未命中 ¥1（Flash） | 自动 | 无需配置 |
| Qwen | 缓存命中 ¥1.5 vs ¥12 | 显式缓存创建 ¥15 | 控制台/参数开启 |

**实操要点**
1. 稳定的内容放**最前面**，变量放最后；前缀一变，缓存全失效。
2. 缓存有最小 token 门槛和 TTL，短对话/低频调用可能不划算。
3. 长文档问答、代码库 Agent、固定人设的客服，是缓存收益最大的三个场景。
4. 监控**缓存命中率**；低于 50% 说明 prompt 结构有问题。

### 杠杆 2：Batch / Flex / 空闲时段——确定性 5 折

- OpenAI Batch / Flex：标准价 **5 折**；Anthropic Batch：约 **5 折**；Gemini 也有 Batch/Flex 档。
- DeepSeek：**空闲时段（非工作日全天 + 工作日非高峰）价格为高峰的一半**。
- 适合：离线标注、批量摘要、数据清洗、评测集跑分、内容审核。
- 不适合：实时对话、需要工具往返的交互式 Agent。

> 来源：[OpenAI Pricing（Batch/Flex 说明）](https://developers.openai.com/api/docs/pricing)、[Anthropic Batch](https://docs.claude.com/en/docs/build-with-claude/batch-processing)、[DeepSeek 价格页](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)。

### 杠杆 3：模型路由（Model Routing）——便宜模型做 80% 的活

```
用户请求
  │
  ├─ 复杂度判定（规则/小模型）
  │     ├─ 简单：分类、抽取、格式转换、翻译 → 轻量档（Haiku 5.5 / GPT-6 Luna / DeepSeek Flash）
  │     ├─ 中等：多步推理、长文档 → 中档（Sonnet 5.5 / GPT-6.1 Sol / Qwen3.8-Max）
  │     └─ 困难：架构设计、长程 Agent → 旗舰（Opus 5.5 / GPT-6 Astra / Fable 5.1）
  │
  └─ 失败升级：中档失败/低置信 → 自动升级旗舰重试（只对失败样本付费）
```

**落地建议**
- 用评测集确定"中档模型在哪些任务上已经够用"，不要凭感觉。
- 路由本身要便宜：规则优先，小模型兜底；不要用旗舰做路由判断。
- 记录每次请求的"路由理由"，方便复盘和调参。

### 杠杆 4：上下文工程——少发 token 比降价更有效

- **压缩 system prompt**：删掉客套话和重复约束，"你是资深 Python 工程师，简洁专业"就够了。
- **只传相关上下文**：用检索/摘要代替整文件、整库塞入。
- **裁剪工具输出**：工具返回的 JSON 只留需要的字段；日志只留错误行。
- **会话压缩**：长对话定期总结，丢弃无关历史；Anthropic 的上下文压缩、各家的"记忆"功能可减少重发。
- **避免长上下文溢价**：OpenAI >272K、Grok >200K 会整单涨价，能拆就拆。

### 杠杆 5：输出控制——输出通常比输入贵 2–5 倍

- 设 `max_tokens`，别让模型"自由发挥"。
- 用 effort / thinking 档位：简单任务关掉或调低推理强度。
- 要求结构化输出（JSON Schema），减少解释性文字。
- 流式输出 + 提前终止：拿到需要的部分就停。
- 让模型"先给结论，再按需展开"，避免一次性生成超长文档。

---

## 三、Agent 任务的 token 放大（2026 年最大的成本坑）

### 为什么会放大

普通问答是"一问一答"；Agent 是"多轮循环"，每一轮都要把**历史上下文重新发一遍**：

```
第 1 轮：system + 任务                 → 5K 输入
第 2 轮：+ 上轮结果 + 工具输出          → 12K 输入
第 3 轮：+ 更多结果                     → 20K 输入
...
第 30 轮：                              → 60K+ 输入
```

放大来源：
1. **上下文重发**：轮数越多，累计输入近似平方增长。
2. **工具输出**：网页、日志、文件内容动辄数万 token。
3. **推理 token**：高 effort 下输出 token 翻倍。
4. **重试/反思**：失败重来、自我检查、多 Agent 互评都额外计费。
5. **多 Agent 编排**：子 Agent 各自带上下文，成本叠加。

### 用"每任务成本"而不是"每百万 token 价格"来比较

Artificial Analysis 用统一任务集测过"每任务成本"（2026-11 页面数据）：

| 模型（effort） | 每任务成本（USD） | 说明 |
|----------------|-------------------|------|
| Claude Opus 5.5 (max) | $10.04 | 高 effort 旗舰，成本最高档 |
| Gemini 4 Carbon (high) | $7.76 | 前沿档 |
| GPT-6 Astra (max) | $6.24 | 前沿档 |
| Claude Opus 5.5 (high) | $3.46 | 降 effort 后明显下降 |
| GPT-6 Astra (high) | $3.24 | 同上 |
| GPT-6.1 Sol (max) | $1.27 | 中档模型高 effort，性价比突出 |
| Kimi K3.1 Pro | 约 $2.11 | 开源权重，接近中档闭源 |

> 来源：[Artificial Analysis LLM Leaderboard](https://artificialanalysis.ai/leaderboards/models)（读取 2026-11-07）；Kimi K3.1 Pro 任务成本见 [heise 2026-10-26](https://www.heise.de/news/Chinesisches-Open-Weight-Modell-Kimi-K3-1-Pro-rueckt-an-US-Spitzenmodelle-heran-11500459.html) 引用的 AA 数据。
>
> 注意：这是 AA 的标准任务，不代表你的业务；但"任务成本 ≠ token 单价"这个结论是通用的。

### Agent 成本控制清单

- **设最大步数/最大 token 预算**，超限就停并报警。
- **工具输出截断/摘要**：网页只留正文，日志只留关键行。
- **上下文缓存**：把 system prompt、工具定义、项目规范放前缀。
- **升级策略**：默认中档，失败再升级；不要一开始就全量旗舰。
- **按任务计量**：记录每个任务的轮数、输入/输出 token、是否重试。
- **多 Agent 审慎**：先证明单 Agent 不够，再上多 Agent。

**一个粗算例子（Claude Opus 5.5）**：编码 Agent 平均 30 轮，累计输入 600K token、输出 60K token。
- 不用缓存：600K × $4/M + 60K × $20/M = **$2.4 + $1.2 = $3.6/任务**
- 80% 输入命中缓存：480K × $0.20/M + 120K × $4/M + 60K × $20/M ≈ **$0.10 + $0.48 + $1.2 = $1.78/任务**

> 结论：**输出和重发的上下文才是大头**；缓存能砍掉近一半，但降 effort、缩短轮数往往更有效。

---

## 四、成本监控：把"月底吓一跳"变成"每天看得见"

### 必看的 6 个指标

| 指标 | 定义 | 健康信号 |
|------|------|----------|
| 单任务成本 | 总成本 / 成功任务数 | 稳定或下降 |
| 缓存命中率 | 缓存读 token / 总输入 token | >50%（长上下文场景 >80%） |
| 每任务 token 数 | 输入+输出 / 任务 | 不随版本升级无故上涨 |
| 重试率 | 重试次数 / 总调用 | <10% |
| 失败成本占比 | 失败任务花费 / 总花费 | <5% |
| P95 延迟 | 95 分位响应时间 | 满足业务 SLA |

### 工具与做法

1. **先用厂商自带账单/用量页**
   - OpenAI：Dashboard → Usage / Limits，设置月度预算上限。
   - Anthropic：Console → Usage & Cost；2026-11 起企业版支持**按项目标签（cost code）追踪支出**（beta）。
2. **给每次调用打标签**：`team`、`feature`、`env`、`model`、`task_type`；没有标签就无法归因。
3. **用网关统一观测**：OpenRouter / LiteLLM / 自建网关可统一记录模型、token、成本、延迟，并做预算与降级。
4. **接入 OpenTelemetry**：把 LLM 调用纳入现有可观测体系（trace + metrics + log）。
5. **设置三级告警**：日预算 50% / 80% / 100%；异常突增（同比 2 倍）单独告警。
6. **每月复盘**：Top 5 花钱功能、Top 5 失败任务、缓存命中率变化、是否有更便宜的等价模型。

> 参考：[Anthropic 发布说明（2026-11-06 项目标签）](https://support.claude.com/zh-CN/articles/12138966-%E5%8F%91%E5%B8%83%E8%AF%B4%E6%98%8E)、[OpenAI Usage](https://platform.openai.com/usage)。

---

## 五、实战：1000 条/天情感分析，选哪个模型？

**假设**：每条 150 输入 token + 50 输出 token，30 天/月；价格用上文 2026-11 快照。

```
单条成本 = 150 × 输入价 / 1,000,000 + 50 × 输出价 / 1,000,000
```

| 方案 | 模型 | 单条成本 | 日成本 | 月成本 | 相对倍数 |
|------|------|----------|--------|--------|----------|
| A | Claude Opus 5.5 | $0.0016 | $1.60 | $48.00 | 40× |
| B | Claude Sonnet 5.5 | $0.0008 | $0.80 | $24.00 | 20× |
| C | Claude Haiku 5.5 | $0.00004 | $0.04 | $1.20 | 1× |
| D | DeepSeek V4.1-Flash（空闲） | ¥0.00035 | ¥0.35 | ¥10.50 | 约 1/6（按汇率粗算） |
| E | 本地小模型 | 电费+折旧 | — | 视硬件 | 固定成本 |

**怎么选？**
- 如果 Haiku 5.5 在自建评测上的准确率与 Opus 5.5 差距 <2%，直接选 C，省 40 倍。
- 如果差距大，用**路由**：80% 简单样本走 Haiku，20% 疑难样本走 Sonnet/Opus，综合成本约为全量 Opus 的 1/5。
- 如果数据不能出网，选 D（本地/国内 API）或 E（自托管）。

> 这组数字会过期，但**方法**不会：固定评测集 → 算单任务成本 → 算"每个成功任务"成本 → 再决定。

---

## 六、五个长期有效的原则

1. **先小后大**：先用轻量档跑评测，不够再升级；不要一上来就旗舰。
2. **按成功任务付费**：便宜但失败率高，等于更贵。
3. **缓存优先**：固定前缀不缓存，是在给厂商送钱。
4. **能批处理就批处理**：离线任务没有理由付实时价。
5. **每季度复核**：模型和价格每季度都在变，去年的最优解今年可能贵 3 倍。

---

## 七、常见误区

| 误区 | 现实 |
|------|------|
| "单价最低就是最省" | 任务成本 = 单价 × token 量 × 重试次数；长上下文/低质量模型可能更贵 |
| "上下文越长越好" | 超阈值会整单溢价，且准确率未必提升 |
| "缓存会自动生效" | 前缀结构不对、内容变动、低于最小 token 都不会命中 |
| "Agent 只是多调几次 API" | 上下文重发导致近似平方增长，成本可能是问答的 10–50 倍 |
| "开源 = 免费" | GPU、电费、运维、人力都是成本；小规模时通常比 API 贵 |
| "价格表可以一次写好" | 2026 年厂商月内多次调价/促销，必须带日期并定期复核 |

---

## 八、成本优化 Checklist（可直接贴到项目里）

- [ ] 有固定评测集（20–50 条），能量化"效果"
- [ ] 知道每个功能的单任务成本与月成本
- [ ] system prompt / 工具定义 / 长文档已启用缓存
- [ ] 离线任务走 Batch/Flex 或空闲时段
- [ ] 简单任务路由到轻量档，失败才升级
- [ ] 设了 `max_tokens` 和最大 Agent 步数
- [ ] 每次调用带 `team/feature/model/task_type` 标签
- [ ] 配了日/月预算告警
- [ ] 每月复盘 Top 花钱功能与缓存命中率
- [ ] 每季度复核官方定价页与模型版本

---

## 历史沿革

- **2023**：成本 ≈ 输入/输出 token 数 × 单价，团队主要靠"少贴代码"省钱。
- **2024**：prompt caching、batch API 出现；长上下文开始有溢价。
- **2025**：推理模型的 thinking token 计入输出，"同样的答案更贵了"；模型路由成为常规手段。
- **2026**：effort 档位、缓存读写分层、Agent 多轮 token 放大成为主要成本变量；成本管理从"省 token"变成"按任务核算 + 预算告警 + 定期复核定价"。

---

## 下一步

- [⭐️ M2-03 模型横向对比与选型](../02-llm-landscape/03-comparison.md)
- [⭐️ M5-09 AI 安全与数据隐私](./09-security-privacy.md)
- [M11-01 rtk：Token 节省利器](../11-dev-tools/01-rtk-token-killer.md)
- [M11-05 Claude Code 省 Token 指南](../11-dev-tools/05-claude-code-token-optimization.md)
