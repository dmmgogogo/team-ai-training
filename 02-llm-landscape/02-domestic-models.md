# M2-02 · 国内主流大模型

> 最后更新：2026年3月。国内 LLM 生态迭代极快，部分已达到或超越国际顶尖水平。

---

## 一图总览

```
国内主流大模型
├── DeepSeek（深度求索）→ V3.1 / R1  ⭐ 性价比之王
├── 阿里云             → Qwen3（2025.4 开源，8种尺寸）
├── MiniMax            → M1 / M2.5  ⭐ Agent + 编程新星（2026.3）
├── 月之暗面           → Kimi k1.5（长文本+推理）
├── 百度               → 文心一言 ERNIE 4.5
├── 智谱 AI            → GLM-4 系列
├── 字节跳动           → 豆包（Doubao）
├── 腾讯               → 混元大模型
└── 百川智能           → Baichuan 4
```

---

## DeepSeek（深度求索）⭐ 重点关注

> 2025年初震惊全球，持续迭代中

| 模型 | 发布时间 | 特点 |
|------|---------|------|
| **DeepSeek V3** | 2025.1 | 综合能力极强，代码/数学顶尖 |
| **DeepSeek R1** | 2025.1 | 推理模型，对标 o1，完全开源 |
| **DeepSeek V3.1-Terminus** | 2025.9 | V3 升级版，SWE-bench 超 V3 40%+ |
| **DeepSeek V3.2-Exp** | 2025.9 | 实验版，使用 Sparse Attention 新架构 |
| **DeepSeek V4** | 即将发布 | 社区消息，预计 2026 年 |

**为什么 DeepSeek 引爆全球？**
- DeepSeek V3 训练成本仅 **557 万美元**，而 GPT-4 约 1 亿美元
- 性能评测接近 GPT-4o，API 价格便宜 **10-30 倍**
- **R1 完全开源**，可本地部署，不受出口限制
- V3.1 在 SWE-bench（代码评测）和 Terminal-bench 上大幅超越前代

**API 价格（2025年2月数据）：**
| | DeepSeek V3 | GPT-4o | Claude Sonnet |
|-|-------------|--------|----------------|
| 输入/百万Token | ~¥4 | ~¥130 | ~¥160 |
| 输出/百万Token | ~¥16 | ~¥520 | ~¥800 |

**入口：** chat.deepseek.com / platform.deepseek.com  
**本地部署：** `ollama pull deepseek-r1`

---

## 阿里云 · 通义千问（Qwen3）

| 模型 | 发布 | 特点 |
|------|------|------|
| **Qwen3 系列** | 2025.4.29 | 开源！8种尺寸，全面升级 |
| **Qwen3-VL** | 2026.1 | 多模态视觉，融合思考/非思考模式 |
| **Qwen2.5-Coder** | 2024 | 代码专用，至今仍广泛使用 |
| **QwQ-32B** | 2025 | 推理增强，对标 R1 |

**Qwen3 的重大意义：**
- 2025年4月29日开源，一次性发布 **8种不同尺寸**的模型
- 阿里已累计开源 **200余个模型**，全球下载量领先
- Qwen3-VL 支持"思考模式"和"非思考模式"切换，适合不同场景

**特点：**
- 中文理解国内顶尖
- 与阿里云生态深度整合（钉钉、阿里云服务）
- API 平台：阿里云百炼（DashScope）

**入口：** tongyi.aliyun.com / dashscope.aliyuncs.com

---

## MiniMax ⭐ 新星崛起

> 2026年3月密集发布，编程和 Agent 能力冲击行业 SOTA

| 模型 | 发布 | 特点 |
|------|------|------|
| **MiniMax M1** | 2026.3 | 开源！全球首个大规模混合架构推理模型，最长 **100万 Token** 上下文 |
| **MiniMax M2** | 2026.3 | Agent 产品，含 Deep Research、代码执行、浏览器控制 |
| **MiniMax M2.5** | 2026.3 🔥 | 编程+Agent SOTA，SWE-bench **80.2%**，成本极低 |

**M2.5 核心亮点：**
- **SWE-bench Verified 80.2%**，Multi-SWE-bench 51.3%，BrowseComp 76.3%，多项刷新行业 SOTA
- 比上一版本 M2.1 完成任务速度快 **37%**
- 成本极低：100 tok/s 连续工作 **1小时仅需 1 美元**；50 tok/s 仅需 0.3 美元
- 定位：**"第一个不需要考虑使用成本可以无限使用的前沿模型"**

**M1 核心亮点：**
- 全球首个开源的大规模混合架构推理模型
- 支持最长 **100 万 Token** 上下文
- 价格比 DeepSeek-R1 更低（32k 以内输入 ¥0.8/百万Token）
- APP 和 Web **不限量免费**使用

**特点：**
- 短时间内密集发布，迭代速度极快
- Agent 能力突出（Deep Research、浏览器控制、代码执行）
- 定价激进，主打极致性价比
- 国内 APP 免费使用门槛极低

**入口：** minimaxi.com / hailuo.ai（视频生成）

---

## 月之暗面 · Kimi

| 模型 | 特点 |
|------|------|
| **Kimi** | 超长上下文（200万 Token） |
| **Kimi k1.5** | 推理增强，长思维链，对标 o1 |
| **Kimi Code** | 开源代码模型，支持自部署 |

**特点：**
- **长文本处理能力国内最强**，200万 Token 上下文
- k1.5 是国内首批对标 o1 的推理模型
- **Kimi Code 已开源**，可自部署，是 AI 编程工具的新选择
- 对话体验流畅，有联网搜索
- 适合：读长报告、分析合同、整理大量文档

**入口：** kimi.ai

---

## 百度 · 文心一言（ERNIE）

| 模型 | 特点 |
|------|------|
| **ERNIE 4.5** | 最新旗舰，中文理解深 |
| **ERNIE Speed** | 快速低成本 |

**特点：**
- 国内第一批发布的 LLM，产品化成熟
- 百度搜索、知识图谱结合，信息检索准确
- 企业级应用（百度智能云·千帆平台）生态完善

**入口：** yiyan.baidu.com / cloud.baidu.com

---

## 智谱 AI · ChatGLM / GLM-4

| 模型 | 特点 |
|------|------|
| **GLM-4** | 综合能力，清华背景 |
| **GLM-4V** | 多模态视觉 |
| **CogVideoX** | 视频生成 |

**特点：**
- 清华大学背景，学术积累深厚
- 开源历史悠久，GLM 系列是早期国内开源标杆
- 适合学术研究和需要开源模型的场景

**入口：** chatglm.cn / open.bigmodel.cn

---

## 字节跳动 · 豆包（Doubao）

**特点：**
- 字节旗下，产品化体验好
- 与飞书整合，企业办公场景有优势
- API 价格便宜，有大量补贴
- 面向 C 端增长很快

**入口：** doubao.com / console.volcengine.com

---

## 国内模型能力速查（2026年3月）

| 维度 | 推荐 |
|------|------|
| 代码开发 | MiniMax M2.5（SWE-bench 80.2%）、DeepSeek V3.1、Kimi Code |
| 推理/数学 | DeepSeek R1、MiniMax M1、Kimi k1.5、QwQ-32B |
| Agent 任务 | MiniMax M2/M2.5、Kimi k1.5 |
| 长文档处理 | Kimi（200万Token）、MiniMax M1（100万Token）|
| 极致性价比 | MiniMax M2.5（$1/小时）、DeepSeek V3 |
| 开源部署 | DeepSeek R1、Qwen3、MiniMax M1、Kimi Code |
| 企业集成 | 千问（阿里云）、文心（百度云）、混元（腾讯云）|
| 中文对话 | Kimi、文心 4.5、豆包 |
| 多模态 | Qwen3-VL、文心、Hailuo（MiniMax 视频）|

---

## 合规与数据安全提示

> ⚠️ 使用国内 LLM API 时注意：

- 大多数国内模型**数据存在国内服务器**，有利于数据合规
- 涉及敏感业务数据时，优先考虑**本地部署开源模型**（DeepSeek R1 / Qwen3）
- **Kimi Code** 是新兴的可自部署代码模型，值得关注
- 了解各平台的数据使用协议，企业用户建议签订数据保密协议

---

## 官方文档入口

| 模型 | 使用入口 | 开发者 API |
|------|---------|-----------|
| DeepSeek | [deepseek.com](https://www.deepseek.com) | [platform.deepseek.com](https://platform.deepseek.com) |
| 通义千问 | [tongyi.aliyun.com](https://tongyi.aliyun.com) | [dashscope.aliyuncs.com](https://dashscope.aliyuncs.com) |
| MiniMax | [minimaxi.com](https://www.minimaxi.com) | [platform.minimaxi.com](https://platform.minimaxi.com) |
| Kimi | [kimi.ai](https://kimi.ai) | [platform.moonshot.cn](https://platform.moonshot.cn) |
| 文心一言 | [yiyan.baidu.com](https://yiyan.baidu.com) | [cloud.baidu.com](https://cloud.baidu.com/product/wenxinworkshop) |
| 豆包 | [doubao.com](https://www.doubao.com) | [console.volcengine.com](https://console.volcengine.com/ark) |
| ChatGLM | [chatglm.cn](https://chatglm.cn) | [open.bigmodel.cn](https://open.bigmodel.cn) |

---

## 下一步

- [M2-03 模型横向对比与选型](./03-comparison.md)
- [📚 完整参考资源](../references.md)
