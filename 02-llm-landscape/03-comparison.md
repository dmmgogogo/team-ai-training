# M2-03 · 模型横向对比与选型指南

> 选模型不是选"最好的"，而是选"最适合场景的"。

---

## 选型决策树

```
你的需求是什么？
│
├─ 数据必须留在内网？
│   └─ YES → 本地部署 → Llama 3.x / DeepSeek R1 / Qwen3
│
├─ 主要是写代码？
│   ├─ 需要编辑器内嵌 → Cursor / Copilot / Windsurf
│   └─ 需要 API 调用 → Claude Sonnet 4.x / DeepSeek V3.1
│
├─ 需要处理超长文档？
│   ├─ 国内首选 → Kimi（200万Token）/ MiniMax M1（100万Token）
│   └─ 国际首选 → Gemini 2.5 Pro（200万Token）
│
├─ 复杂推理/数学？
│   ├─ 国际 → o3 / Claude 3.7 Sonnet（Extended Thinking）
│   └─ 国内 → DeepSeek R1 / MiniMax M1 / QwQ-32B
│
├─ 成本敏感？
│   ├─ 国内低成本 → MiniMax M2.5 / DeepSeek V3.1 / Qwen3-Plus
│   └─ 国际低成本 → Gemini 2.0 Flash / Claude Haiku / GPT-4o mini
│
└─ 多模态（图片/视频）？
    ├─ 国际 → GPT-4o / Gemini 2.5
    └─ 国内 → Qwen3-VL / Hailuo（MiniMax视频）
```

---

## 能力雷达图（主观评分，满分 5）

| 维度 | GPT-4o | Claude Sonnet | Gemini 2.x | DeepSeek V3.1 | Qwen3 |
|------|--------|---------------|------------|---------------|-------|
| 代码 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 推理 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 中文 | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 创意写作 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| 长文本 | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 速度 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 价格 | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 开源 | ❌ | ❌ | ❌ | ✅（R1） | ✅ |
| 国内可用 | ⚠️需代理 | ⚠️需代理 | ⚠️需代理 | ✅ | ✅ |

---

## 按使用场景推荐

### 👨‍💻 开发者日常编码

**首选：** Claude Sonnet 4.x（通过 Cursor）  
**备选：** DeepSeek V3.1 / MiniMax M2.5（性价比，国内直连）  
**理由：** Claude 代码能力最强，Cursor 集成最好；DeepSeek/MiniMax 性价比极高

---

### 📊 数据分析 / 报告生成

**首选：** GPT-4o / Claude Sonnet  
**国内首选：** DeepSeek V3 / 通义千问  
**理由：** 结构化输出好，能处理表格和复杂分析

---

### 📄 长文档分析（合同、报告、书籍）

**首选：** Kimi（200万Token，国内直连）/ MiniMax M1（100万Token）  
**国际首选：** Gemini 2.5 Pro  
**理由：** 超长上下文是核心能力

---

### 🔢 数学 / 复杂推理

**首选：** o3 / DeepSeek R1  
**备选：** Claude 3.7 Extended Thinking / MiniMax M1  
**理由：** 专为推理优化，慢思考大幅提升准确率

---

### ✍️ 内容创作 / 写作

**首选：** Claude Opus / GPT-4o  
**国内首选：** Kimi / DeepSeek V3  
**理由：** 文笔好，风格多样，中文写作通顺

---

### 🏢 企业私有化部署

**首选：** DeepSeek R1（开源，免费）  
**备选：** Llama 3.3 70B / Qwen2.5-72B  
**工具：** Ollama（本地）/ vLLM（服务器部署）  
**理由：** 数据不出内网，可完全定制

---

## API 价格参考（动态维护）

价格波动非常快（厂商常在月内多次调价），本课程不再维护硬编码价格数字，避免“看起来精确、实际过期”。

建议直接使用以下权威入口做最新比价：

| 入口 | 用途 |
|------|------|
| [Artificial Analysis 价格页](https://artificialanalysis.ai/models) | 跨厂商横向对比（质量/速度/价格） |
| [OpenAI Pricing](https://openai.com/api/pricing) | OpenAI 官方定价 |
| [Anthropic Pricing](https://www.anthropic.com/pricing) | Anthropic 官方定价 |
| [Google AI Pricing](https://ai.google.dev/gemini-api/docs/pricing) | Gemini API 官方定价 |
| [DeepSeek Pricing](https://platform.deepseek.com/api-docs/pricing) | DeepSeek 官方定价 |
| [阿里云百炼定价](https://help.aliyun.com/zh/model-studio/product-overview/billing-overview) | 通义千问/百炼官方定价 |

---

## 本地部署参考配置

| 模型 | 最低配置 | 推荐配置 |
|------|---------|---------|
| 7B 模型（量化） | 8GB 内存 | 16GB 内存 |
| 32B 模型（量化） | 24GB 显存 | 32GB 显存（A100） |
| 70B 模型（量化） | 48GB 显存 | 80GB 显存 × 2 |
| 671B（DeepSeek V3）| 需集群 | 8× H100 |

**本地工具推荐：**
- **Ollama** — 最简单，一条命令跑模型
- **LM Studio** — 有 GUI，适合非开发者
- **vLLM** — 生产级，支持高并发 API 服务

---

## 快速决策总结

```
预算有限 + 国内使用 → MiniMax M2.5 / DeepSeek V3.1
代码开发 → Claude Sonnet 4.x（via Cursor）
推理/数学 → DeepSeek R1 或 o3
长文档 → Kimi / MiniMax M1
数据合规/私有化 → 本地部署 DeepSeek R1 / Qwen3
多模态 → GPT-4o 或 Gemini 2.5
```

---

## 下一步

- [M3-01 AI 编程工具概览](../03-ai-coding-tools/01-overview.md) — 开发者专属工具
- [M5-01 Prompt 工程入门](../05-practical/01-prompt-engineering.md) — 用好模型的关键
