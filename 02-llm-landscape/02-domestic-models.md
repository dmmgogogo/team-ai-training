# M2-02 · 国内主流大模型

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02
>
> 本页 = **当前快照（2026-11）** + **历史沿革（2024–2026）**。
> 国内模型迭代比国际更快、命名更杂，选型时优先看**当前在售版本 + 开源许可 + 官方定价页**，不要按旧版本名做判断。

---

## 一句话结论

截至 2026-11，国内形成"**DeepSeek、通义千问（Qwen）、Kimi、智谱（GLM）** 四强 + **MiniMax、小米 MiMo、阶跃 StepFun** 特色补位"的格局。共同趋势：**1M 上下文普及、旗舰全面 Agent 化、头部模型陆续开放权重**。开源模型里，Kimi K3.1 Pro 的公开评测（AA 智能指数 55）已接近国际一线。

---

## 当前格局（2026-11 快照）

| 厂商 | 当前旗舰 | 性价比/轻量档 | 开源 | 官方入口 |
|------|----------|---------------|------|----------|
| DeepSeek 深度求索 | DeepSeek V4 Pro（0813） | DeepSeek V4.1-Flash（1017） | ✅ 开放权重 | [platform.deepseek.com](https://platform.deepseek.com) · [API Docs](https://api-docs.deepseek.com/zh-cn/) |
| 阿里 · 通义千问 | Qwen3.8-Max（0902） | Qwen3.8 系列轻量档 | 部分开源 | [qianwenai.com](https://www.qianwenai.com) · [平台](https://platform.qianwenai.com) |
| 月之暗面 · Kimi | Kimi K3.1 Pro | Kimi K3.1 Pro Highspeed | ✅ 开放权重 | [kimi.ai](https://kimi.ai) · [platform.kimi.ai](https://platform.kimi.ai) |
| 智谱 · GLM | GLM-5.3 | GLM-5.3-Flash | ✅ 开放权重 | [z.ai](https://z.ai) · [bigmodel.cn](https://bigmodel.cn) |
| MiniMax | MiniMax M3 | MiniMax M3.1 Flash | ✅ 开放权重 | [minimax.io](https://www.minimax.io) · [平台](https://platform.minimax.io) |
| 小米 · MiMo | MiMo-V2.6-Pro | MiMo-V2.6-Flash | ✅ 开放权重 | [mimo.mi.com](https://mimo.mi.com) |
| 阶跃星辰 · StepFun | Step 5 Preview | —（开源权重） | ✅ 开放权重 | [stepfun.com](https://www.stepfun.com) |
| 字节 · 豆包 | 豆包 Seed-Evolving（2026-11-02） | 豆包轻量档 | ❌ | [volcengine.com/ark](https://console.volcengine.com/ark) |
| 腾讯 · 混元 | 混元 Hy4（2026-11-04，770B/49B） | Hy4 Flash（待发） | 权重近期开源 | [hunyuan.tencent.com](https://hunyuan.tencent.com) |
| 百度 · 文心 | ERNIE 5.5 Flash Base（2026-11-05，280B/14B） | ERNIE 5.5 Flash（待发） | ✅ 开放权重 | [ernie.baidu.com](https://ernie.baidu.com) |

> 命名统一约定：**DeepSeek V4 系列**（V4 Pro / V4.1-Flash）、**Qwen3.8 Max**、**Kimi K3.1 Pro**、**GLM-5.3**、**MiniMax M3**、**MiMo-V2.6**、**Step 5 Preview**、**混元 Hy4**、**ERNIE 5.5 Flash Base**、**豆包 Seed-Evolving**。

### 2026-11 第一周增量（11-02 ~ 11-06，发布后补录）

| 日期 | 模型 | 厂商 | 关键点 | 来源 |
|------|------|------|--------|------|
| 2026-11-04 | **混元 Hy4 正式版** | 腾讯 | 770B 总参 / 49B 激活；1M 上下文；首次加入视觉 + Computer Use；¥6/¥18（缓存 ¥0.3）；权重近期开源，Hy4 Flash 待发 | [腾讯云](https://cloud.tencent.cn/developer/article/2776227) |
| 2026-11-05 | **ERNIE 5.5 Flash Base** | 百度 | 280B 总参 / 14B 激活；1M 上下文；33.5T tokens 训练；开放权重；完整 ERNIE 5.5 Flash 待发 | [ERNIE 发布页](https://ernie.baidu.com/release/ernie-5-5-flash-base/) · [Hugging Face](https://huggingface.co/baidu/ERNIE-5.5-Flash-Base) |
| 2026-11-02 | **豆包 Seed-Evolving** | 字节 | 深度思考档，火山方舟最新模型 | [火山方舟](https://console.volcengine.com/ark/region:cn-beijing/docs/latest-model) |
| 2026-11-05 | Nanbeige4.3-33B | 南贝 | 开放权重，AA 智能指数 20，对标 Qwen3.8 27B | [AA 分析](https://artificialanalysis.ai/articles/nanbeige-has-released-nanbeige4-3-33b-scoring-20-on-the-intelligence-index) |
| 2026-11-06 | Qwen4 系列（预热，未发布） | 阿里 | 官方预热"鲲"，预计 Max/Plus/Flash/27B，11–12 月陆续发布，旗舰或超 3 万亿参数 | [DataLearner 追踪](https://www.datalearner.com/ai-models/release-tracker) |

> 注意：Qwen4 截至 2026-11-07 **尚未发布**，不要当作可用模型选型；发布后以阿里官方为准。


### DeepSeek · V4 系列

**稳定认知**
- 开源 + API 双轨，工程圈采用广；价格低、推理/代码强，适合预算敏感与私有化。
- 版本命名规则：`deepseek-v4-pro` 走旗舰；`deepseek-flash` 是轻量档的**别名**，背后版本会滚动升级。
- 空闲时段价格是高峰的一半——**批处理任务排到夜间/周末能直接省钱**。

**当前版本（2026-11）**

| 模型 ID | 实际版本 | 发布时间 | 上下文 | 输出上限 | 备注 |
|---------|----------|----------|--------|----------|------|
| `deepseek-v4-pro` | DeepSeek V4 Pro（0813） | 2026-08-13 GA | 1M | 384K | 旗舰，文本；不支持图像理解 |
| `deepseek-flash` | DeepSeek V4.1-Flash-1017 | 2026-10-17 | 1M | 384K | 轻量档，支持图像理解；旧名 `deepseek-v4-flash` 仍可调用但已下线 |

**价格（人民币 / 每百万 token，官方文档）**

| 模型 | 输入（缓存命中） | 输入（未命中） | 输出 |
|------|------------------|----------------|------|
| `deepseek-flash`（空闲/高峰） | ¥0.02 / ¥0.04 | ¥1 / ¥2 | ¥4 / ¥8 |
| `deepseek-v4-pro`（空闲/高峰） | ¥0.15 / ¥0.30 | ¥4.5 / ¥9 | ¥13.5 / ¥27 |

> 来源：[DeepSeek 模型 & 价格](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)（2026-11-07）。高峰时段：北京时间周一至周五 9:00–12:00、14:00–18:00（不含法定节假日）；其余为空闲时段。Search / Fetch 均为 ¥5 / 1000 次成功请求。

**DeepSeek 历史沿革**
- 2026-10-17：V4.1-Flash-1017 发布（性能/成本 Pareto 改进，开放权重）
- 2026-09-10：V4.1-Flash 发布
- 2026-08-21：V4-Flash-Vision-Exp（视觉实验版）
- 2026-08-13：V4-Pro 正式 GA
- 2026-04-24：V4 Preview 发布（V4 Pro 1.6T 总参 / 49B 激活；V4 Flash 284B / 13B 激活，研究预览）
- 2025-12-01：V3.2；2025-09-29：V3.2-Exp；2025-08-21：V3.1
- 2025-05-28：R1-0528；2025-03-25：V3-0324；2025-01-20：R1
- 2024-12-26：DeepSeek-V3；2024-09-05：V2.5
- ~~V4-Flash / V4-Flash-Vision-Exp 已下线~~，请求由 V4.1-Flash-1017 承接并按 Flash 价格计费

> 来源：[DeepSeek News 时间线](https://api-docs.deepseek.com/zh-cn/news/news261017)（侧栏列出 2024–2026 全部版本）；V4 参数：[ETV Bharat 2026-04-27](https://www.etvbharat.com/en/technology/deepseek-launched-v4-flash-and-v4-pro-llms-challenging-gpt-5-dot-2-and-gemini-3-dot-0-pro-enn26042701407)（媒体转述官方发布）。

---

### 阿里 · 通义千问 Qwen3.8 Max

**稳定认知**
- 国内开源生态覆盖最广（尺寸档位多），与阿里云/百炼集成深，企业落地成本低。
- Max 档走旗舰闭源/半开放路线，轻量档走开源，可做**同一家族内的分层部署**。

**当前版本（2026-11）**
- `qwen3.8-max` 默认指向 **qwen3.8-max-0902** 快照（2026-09-02 快照，2026-09-05 起自动切换）。
- 2.4 万亿参数 MoE 旗舰；1M 上下文（最大输入 991K、最大输出 131K、思维链上限 262K）；原生视觉理解；支持函数调用、结构化输出、Context Cache、Batch、联网搜索。

**价格（人民币 / 每百万 token，官方模型页）**

| 计费项 | 价格 |
|--------|------|
| 输入 | ¥12 |
| 输出 | ¥36 |
| 输入（缓存命中） | ¥1.5 |
| Batch File 输入 / 输出 | ¥6 / ¥18 |
| 显式缓存创建 / 命中 | ¥15 / ¥1 |

> 来源：[Qwen3.8-Max 模型页](https://www.qianwenai.com/models/qwen3.8-max)（2026-11-07）；[升级通知](https://platform.qianwenai.com/docs/changelog/model-updates/qwen3.8-max-upgrade)（2026-09-05）。

**Qwen 历史沿革**
- 2026-09-02：Qwen3.8-Max（0902 快照），09-05 成为默认版本
- 2026 年内：Qwen3.5 Max → Qwen3.6 Plus → Qwen3.7 Max（快速迭代，具体日期以官网更新日志为准）
- 2025-09：Qwen3-Max；2025-04：Qwen3 开源系列
- 2024-09：Qwen2.5 系列
- 更早：Qwen2 / Qwen1.5（2024 年）

> 来源：[千问 AI 平台更新日志](https://platform.qianwenai.com/docs/changelog/model-updates)（2026-11-07）。

---

### 月之暗面 · Kimi K3.1 Pro

**稳定认知**
- 长文本/知识工作起家，2026 年转向**开放权重 + 长程 Agent**。
- K3.1 Pro 是目前公开评测中最强的国产开源权重模型之一（AA 智能指数 55，发布时第 4）。

**当前版本（2026-11）**
- **Kimi K3.1 Pro**：MoE 2.8T 总参 / 104B 激活；1M 上下文；文本、图像、视频输入；支持 3D 建模、CAD/Blender 脚本、金融分析等长任务。
- 开源权重 2026-11-04 起放出；同步推出 **Kimi Hosted Agents** 托管智能体服务（2026-11-05）。
- API 价格：**$2 输入 / $10 输出**（每百万 token），缓存命中 $0.20；Highspeed 档 $4 / $20（速度约 2–3 倍）。
- 公开评测（发布时）：Terminal-Bench 4.0 67%、GDPval-AA 1846 Elo（第 3）、HLE 52%；幻觉率（AA-Omniscience）从 53% 降到 44%。

> 来源：[heise 2026-10-26](https://www.heise.de/news/Chinesisches-Open-Weight-Modell-Kimi-K3-1-Pro-rueckt-an-US-Spitzenmodelle-heran-11500459.html)（发布、参数、价格、AA 数据）；[搜狐/中国城市报 2026-11-06](https://www.sohu.com/a/1098125406_122512986)（开放权重与 Hosted Agents）。

**Kimi 历史沿革**
- 2026-11-04/05：K3.1 Pro 开放权重 + Hosted Agents
- 2026-10-27：Kimi K3.1 Pro 发布（北京时间；欧洲媒体 10-26 报道）
- 2026-07：Kimi K3 发布（2.8T MoE / 104B 激活，1M 上下文）
- 2026 上半年：Kimi K2.6（Vals Index 2026-05-28 榜单在列）
- 2025-07：Kimi K2；2025-01：Kimi k1.5
- 更早：Kimi 长文本系列（2023–2024）

> 来源：同上；K2.6 见 [Vals Index](https://www.vals.ai/benchmarks/vals_index_v1_1)（2026-05-28）。

---

### 智谱 · GLM-5.3

**稳定认知**
- 开源 + 学术路线，编程与 Agent 能力在国产开源中靠前；2026 年强化"后训练 Scaling"。
- 安全能力（代码审计/漏洞发现）是差异点，但**高风险能力需受信访问**。

**当前版本（2026-11）**
- **GLM-5.3**：2026-08-14 发布；1M 上下文、最大输出 131K；文本输入/输出；支持函数调用、结构化输出、缓存；**开放权重**（发布两周后开源）。
- 公开基准（官方自报）：Terminal-Bench 3.0 28.3（前代 4.6）、DeepSWE v1.1 66.9（前代 46.2）、Agents' Last Exam 28.5、GDPval-AA v2 1769。
- 安全：CyberGym 84.5%（高于 Mythos 5 的 83.8%、GPT-5.6 Sol 的 83.6%）；ExploitBench 54.4%，仍落后闭源前沿。
- 参考价格：阿里云百炼国际站 **$1.4 输入 / $4.4 输出**（每百万 token），隐式缓存 $0.26；官方 Z.ai 价格以官网为准。

> 来源：[智谱 GLM-5.3 发布（2026-08-14）](https://www.zhipuai.cn/zh/research/162)；[阿里云 Model Studio 模型信息（更新 2026-10-30）](https://www.alibabacloud.com/help/ja/model-studio/glm-5-3-by-zhipu)（第三方云平台价）。

**GLM 历史沿革**
- 2026-08-14：GLM-5.3（开源）
- 2026 年内：GLM-5.2 → GLM-5.1 → GLM-5（Vals Index 2026-05-28 榜单含 GLM 5.1）
- 2025：GLM-4.5 / GLM-4.6 系列
- 2024：GLM-4 / ChatGLM 系列

---

### MiniMax · M3

**稳定认知**
- 产品化与 Agent 体验强，2026 年转向"开源 + 1M 上下文 + 原生多模态"。
- M3 是首个同时具备"前沿编码 + 百万上下文 + 原生多模态"的开放权重模型（官方口径）。

**当前版本（2026-11）**
- **MiniMax M3**：2026-09-22 发布；1M 上下文（保证至少 512K）；原生多模态；开放权重；BrowseComp 83.5（官方称超过 Opus 4.7 的 79.3）。
- 最新轻量档：**MiniMax M3.1 Flash**（官方文档 2026-11 已上线，具体规格以官网为准）。
- API 价格以官方定价页为准（本页未获取到稳定公开数字，避免写错）。

> 来源：[MiniMax M3 模型页](https://www.minimax.io/models/text/m3)（2026-11-07）；[MiniMax 定价总览](https://platform.minimax.io/docs/pricing/overview)。

**MiniMax 历史沿革**
- 2026-11：M3.1 Flash 上线
- 2026-09-22：MiniMax M3（开放权重）
- 2026 上半年：MiniMax M2.7 等（Vals Index 2026-05-28 榜单在列）
- 2025：MiniMax M1 / M2 系列
- 2024：abab 系列

---

### 小米 · MiMo-V2.6

**稳定认知**
- 2026 年以"开源 + 全模态 + 极低价格"切入，适合成本敏感的高并发任务。
- 与小米生态/端侧结合是长期看点。

**当前版本（2026-11）**
- **MiMo-V2.6-Pro / V2.6-Flash**：2026-09-22 发布并开源；原生支持图片、视频、音频、文本全模态输入。
- 发布时 Artificial Analysis 综合智能指数 46，官方称位列开源权重模型第一（当时代际）。
- 价格（人民币 / 每百万 token）：Pro 输入 ¥3（缓存命中 ¥0.025）/ 输出 ¥6；Flash 输入 ¥1 / 输出 ¥2；Batch 5 折。
- 注意：`mimo-v2.5-pro` / `mimo-v2.5` 已于 **2026-10-21 下线**。

> 来源：[北京日报 2026-09-22](http://xinwen.bjd.com.cn/content/s6ab282a7e4b039a8e2f16ebd.html)；[MiMo 官方价格页（更新 2026-10-21）](https://mimo.mi.com/docs/en-US/price/pay-as-you-go)。

**MiMo 历史沿革**
- 2026-10-21：V2.5 系列下线 ~~弃用~~
- 2026-09-22：MiMo-V2.6-Pro / Flash（开源）
- 2026 年内：MiMo-V2.5-Pro / V2.5
- 更早：MiMo-7B 等开源小模型（2025）

---

### 阶跃星辰 · Step 5 Preview

**稳定认知**
- 面向长程 Agent 的稀疏 MoE 模型，开放权重、许可宽松但**不是 Apache 2.0**。
- 在 OpenRouter 的 Token 用量榜上曾冲到全球第二（2026-10-15），说明开发者采用度高。

**当前版本（2026-11）**
- **Step 5 Preview**：600B 总参 / 27B 激活；1M 上下文；92 层窄深架构；原生文本 + 视觉；支持 vLLM / SGLang 部署。
- 2026-09 开放 API；**2026-10-15 开放权重**（BF16 / FP8，Hugging Face + ModelScope）。
- 许可：StepFun Model License 1.0（允许使用/修改/分发；大规模商业用途需注意署名与另签条款）。

> 来源：[极客公园 2026-10-15](https://www.geekpark.net/news/372400)；[沙丘社区 2026-10-15](https://www.shaqiu.cn/tracking/model:stepfun:step5-preview-weights-20261015)。

---

### 其他厂商（简述）

| 厂商 | 2026 动态 | 选型提示 |
|------|-----------|----------|
| 字节 · 豆包 | 豆包 Seed-Evolving（2026-11-02，深度思考档）；豆包 2.0（2026-02-14） | 消费级/企业协同场景可试点；价格与版本以火山方舟为准 |
| 腾讯 · 混元 | **Hy4 正式版（2026-11-04）**：770B/49B、1M 上下文、视觉 + Computer Use、¥6/¥18；权重近期开源，Hy4 Flash 待发 | 腾讯云生态项目的默认候选之一；Computer Use 场景值得实测 |
| 百度 · 文心 | **ERNIE 5.5 Flash Base（2026-11-05 开放权重）**：280B/14B、1M、33.5T tokens；完整版待发 | 需要开源 + 中文知识增强的政企场景 |
| 商汤 / 讯飞 / 零一万物等 | 垂直行业与政企场景 | 按行业合规与交付能力选，不只看跑分 |

> 来源：[央广网 2026-02-14](https://tech.cnr.cn/ycbd/20260214/t20260214_527526982.shtml)（豆包 2.0）；[中央社 2026-11-04](https://www.cna.com.tw/news/ait/202611040339.aspx)（混元 Hy4）。

---

## 价格快照（2026-11，每百万 token）

> 币种不同，**不要直接把人民币和美元数字放一起比**；先换算再比较，并注意高峰/空闲、缓存、Batch 差异。

| 模型 | 输入 | 输出 | 缓存读 | 币种 | 来源（日期） |
|------|------|------|--------|------|--------------|
| DeepSeek V4.1-Flash（空闲） | ¥1 | ¥4 | ¥0.02 | CNY | [DeepSeek 官方](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)（11-07） |
| DeepSeek V4.1-Flash（高峰） | ¥2 | ¥8 | ¥0.04 | CNY | 同上 |
| DeepSeek V4 Pro（空闲） | ¥4.5 | ¥13.5 | ¥0.15 | CNY | 同上 |
| DeepSeek V4 Pro（高峰） | ¥9 | ¥27 | ¥0.30 | CNY | 同上 |
| Qwen3.8-Max | ¥12 | ¥36 | ¥1.5 | CNY | [Qwen 模型页](https://www.qianwenai.com/models/qwen3.8-max)（11-07） |
| GLM-5.3（国际站） | $1.4 | $4.4 | $0.26 | USD | [阿里云 Model Studio](https://www.alibabacloud.com/help/ja/model-studio/glm-5-3-by-zhipu)（10-30） |
| Kimi K3.1 Pro | $2 | $10 | $0.20 | USD | [heise](https://www.heise.de/news/Chinesisches-Open-Weight-Modell-Kimi-K3-1-Pro-rueckt-an-US-Spitzenmodelle-heran-11500459.html)（10-26） |
| MiMo-V2.6-Pro | ¥3 | ¥6 | ¥0.025 | CNY | [MiMo 官方](https://mimo.mi.com/docs/en-US/price/pay-as-you-go)（10-21） |
| MiMo-V2.6-Flash | ¥1 | ¥2 | ¥0.02 | CNY | 同上 |
| 混元 Hy4 | ¥6 | ¥18 | ¥0.3 | CNY | [腾讯云 11-04](https://cloud.tencent.cn/developer/article/2776227) |
| ERNIE 5.5 Flash Base | 开放权重（自部署） | — | — | — | [ERNIE 发布页](https://ernie.baidu.com/release/ernie-5-5-flash-base/) |
| MiniMax M3 | 以官网为准 | 以官网为准 | — | — | [MiniMax 定价](https://platform.minimax.io/docs/pricing/overview) |
| Step 5 Preview | 开源自部署 | — | — | — | [官方](https://www.stepfun.com/step-5-preview) |

**官方定价页入口**

| 平台 | 官方价格页 |
|------|-----------|
| DeepSeek | <https://api-docs.deepseek.com/zh-cn/quick_start/pricing> |
| 千问 AI 平台 | <https://platform.qianwenai.com/pricing/api> |
| Kimi | <https://platform.kimi.ai/docs/pricing/chat> |
| 智谱 GLM | <https://z.ai/pricing> |
| MiniMax | <https://platform.minimax.io/docs/pricing/overview> |
| 小米 MiMo | <https://mimo.mi.com/docs/en-US/price/pay-as-you-go> |
| 火山方舟（豆包） | <https://www.volcengine.com/pricing?product=ark> |
| 百度千帆 | <https://cloud.baidu.com/product/wenxinworkshop> |
| 腾讯云 TokenHub | <https://cloud.tencent.com/product/tokenhub> |

---

## 开源与本地部署（速查）

| 模型 | 总参数 / 激活 | 上下文 | 许可 | 适合 |
|------|---------------|--------|------|------|
| DeepSeek V4.1-Flash | 官方未在定价页给出；V4-Flash 为 284B / 13B | 1M | 开放权重 | 单机/小集群私有化、高吞吐 |
| DeepSeek V4 Pro | 1.6T / 49B | 1M | 开放权重 | 多机集群旗舰推理 |
| Kimi K3.1 Pro | 2.8T / 104B | 1M | 开放权重（具体条款以模型卡为准） | 高端私有化/研究 |
| GLM-5.3 | 官方未公开总参 | 1M | 开放权重 | 编程/安全审计 |
| MiniMax M3 | 官方未在模型页给出 | 1M | 开放权重 | 多模态 Agent |
| MiMo-V2.6-Pro | 官方未公开 | — | 开放权重 | 全模态、低成本 |
| Step 5 Preview | 600B / 27B | 1M | StepFun License 1.0（非 Apache） | 长程 Agent 自部署 |

> 显存/硬件详细配置见 [M2-03 本地部署参考配置](./03-comparison.md#六本地部署参考配置2026)。

---

## 合规与数据安全提示（长期有效）

- 先做数据分类（公开 / 内部 / 敏感 / 个人信息），再选部署形态。
- 敏感数据优先**本地部署或专有网络**；调用公有 API 时确认数据是否用于训练、留存多久。
- 与供应商签 DPA/NDA，保留审计日志与调用留痕。
- 涉及生成式 AI 服务合规（备案、内容安全、标识）时，优先选已完成合规手续的大厂平台。
- 开源 ≠ 无约束：Step 5 等模型的许可是"可用但非 Apache"，商用前读模型卡。

---

## 历史沿革（2024–2026，倒序）

### DeepSeek
- 2026-10-17 V4.1-Flash-1017；2026-09-10 V4.1-Flash；2026-08-21 V4-Flash-Vision-Exp
- 2026-08-13 V4-Pro GA；2026-04-24 V4 Preview（1.6T Pro）
- 2025-12-01 V3.2；2025-09-29 V3.2-Exp；2025-08-21 V3.1
- 2025-05-28 R1-0528；2025-03-25 V3-0324；2025-01-20 R1
- 2024-12-26 V3；2024-09-05 V2.5

### 通义千问
- 2026-09-02 Qwen3.8-Max（0902）
- 2026 年内 Qwen3.5 Max / 3.6 Plus / 3.7 Max
- 2025-09 Qwen3-Max；2025-04 Qwen3
- 2024-09 Qwen2.5

### Kimi
- 2026-11-05 开放权重 + Hosted Agents；2026-10-27 K3.1 Pro；2026-07 K3
- 2026 上半年 K2.6；2025-07 K2；2025-01 k1.5

### GLM
- 2026-08-14 GLM-5.3
- 2026 年内 GLM-5.2 / 5.1 / 5
- 2025 GLM-4.5 / 4.6；2024 GLM-4 / ChatGLM

### MiniMax
- 2026-11 M3.1 Flash；2026-09-22 M3
- 2026 上半年 M2.7；2025 M1 / M2；2024 abab

### MiMo
- 2026-10-21 V2.5 下线 ~~弃用~~；2026-09-22 V2.6-Pro / Flash
- 2026 年内 V2.5；2025 MiMo-7B 等

### StepFun
- 2026-10-15 Step 5 Preview 开放权重；2026-09 开放 API
- 2025 Step 3 / Step-Audio 等

### 腾讯混元
- 2026-11-04 Hy4 正式版（770B/49B，视觉 + Computer Use，权重近期开源）；Hy4 Flash 待发
- 2026-08 Hy4 preview；2026-04-24 Hy3 preview；2026-07-07 Hy3 开放权重

### 百度文心
- 2026-11-05 ERNIE 5.5 Flash Base 开放权重（280B/14B，1M，33.5T tokens）；完整 ERNIE 5.5 Flash 待发
- 2026-04-29 ERNIE 5.1 开源；2026-01-22 ERNIE 5.0

### 字节豆包
- 2026-11-02 豆包 Seed-Evolving（深度思考档）
- 2026-02-14 豆包 2.0

> 以上早期版本日期为公开资料整理；如需引用到正式材料，建议回链各厂商官方发布页复核。

---

## 参考与核实说明

- 价格与版本读取于 **2026-11-07**，均给出来源链接；MiniMax M3 未获取到稳定公开价格，明确写"以官网为准"。
- 2026-11-02 ~ 11-06 的新模型（混元 Hy4、ERNIE 5.5 Flash Base、豆包 Seed-Evolving、Nanbeige4.3-33B）为发布后补录；Qwen4 仅为预热，未发布。
- 国产模型更新极快，**超过 2 个月的"最新版本"判断都可能过期**；每季度复核一次。
- 本文不收录营销口径的"全面超越/第一"，只保留带日期的官方或第三方数据。

---

## 下一步

- [M2-01 国际主流模型](./01-global-models.md)
- [M2-03 模型横向对比与选型](./03-comparison.md)
- [M5-11 成本管理与模型选型](../05-practical/11-cost-management.md)
- [📚 完整参考资源](../references.md)
