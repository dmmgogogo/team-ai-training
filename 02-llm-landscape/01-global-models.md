# M2-01 · 国际主流大模型（深度维护版）

> P26年4月。  
> 本页保留“长期有效信息”（产品定位、适用场景、接入入口），删除易快速过期的硬编码跑分、价格和市场份额。

---

## 为什么这版和以前不一样

过去版本里有很多“看起来很精确”的数字（固定分数、固定价格、固定排名）。这些数据通常几天就会变化，容易误导团队选型。  
本次深度更新采用新原则：

1. **保留决策方法**
2. **删除高波动数字**
3. **把最新数据查询入口放到文档里**

---

## 国际模型生态总览（稳态）

```
国际主流大模型
├── OpenAI          → GPT 系列 / o 系列（通用+推理）
├── Anthropic       → Claude 系列（代码与对齐能力强）
├── Google DeepMind → Gemini 系列（多模态与长上下文）
├── Meta            → Llama 系列（开源、私有化）
├── Mistral AI      → Mistral / Codestral（欧洲生态）
└── xAI             → Grok 系列（与 X 平台联动）
```

---

## 各家模型的“稳定认知”

## OpenAI（GPT / o 系列）

- **强项**：综合能力均衡，产品和 API 生态成熟
- **适合**：通用业务问答、代码生成、复杂推理
- **注意**：模型迭代快，版本命名和能力边界会频繁调整
- **入口**：<https://chatgpt.com> / <https://platform.openai.com/docs>

## Anthropic（Claude 系列）

- **强项**：代码与文档任务表现稳定，对齐和可读性好
- **适合**：代码库改造、文档整理、高质量长输出
- **注意**：不同档位模型在速度与成本差异明显，需按场景分层
- **入口**：<https://claude.ai> / <https://docs.anthropic.com>

## Google（Gemini 系列）

- **强项**：多模态、长上下文、与 Google 生态联动
- **适合**：长文档处理、搜索增强、多模态任务
- **注意**：部分模型生命周期较短，需关注官方弃用公告
- **入口**：<https://gemini.google.com> / <https://ai.google.dev/docs>

## Meta（Llama 系列）

- **强项**：开源与私有化部署灵活
- **适合**：内网部署、可控成本、数据不出网场景
- **注意**：部署和调优门槛高于托管 API
- **入口**：<https://llama.meta.com> / <https://ollama.com>

## Mistral（Mistral / Codestral）

- **强项**：欧洲厂商，合规语境友好，开源生态活跃
- **适合**：多语言场景、GDPR 相关合规项目
- **注意**：不同地区可用性和服务策略存在差异
- **入口**：<https://mistral.ai> / <https://docs.mistral.ai>

## xAI（Grok 系列）

- **强项**：与 X 平台联动，实时信息场景有优势
- **适合**：社交平台动态相关任务
- **注意**：区域可用性与政策限制需提前确认
- **入口**：<https://x.ai> / <https://docs.x.ai>

---

## 任务导向选型（不依赖固定分数）

| 任务类型 | 优先考虑 |
|----------|----------|
| 代码开发与重构 | Claude / OpenAI o 系列 |
| 复杂推理与规划 | OpenAI o 系列 / Gemini Pro |
| 超长上下文文档处理 | Gemini / Claude |
| 多模态（图像+文本） | GPT-4o / Gemini |
| 开源与私有化部署 | Llama / Mistral 开源系 |
| 低延迟高并发基础任务 | 轻量档模型（mini/flash/haiku） |

---

## 动态数据查询入口（替代静态数字）

| 类型 | 入口 |
|------|------|
| 综合质量/速度/价格 | <https://artificialanalysis.ai/leaderboards/models> |
| 人类偏好盲测 | <https://lmarena.ai> |
| 代码修复能力 | <https://www.swebench.com> |
| OpenAI 官方 | <https://platform.openai.com/docs> |
| Anthropic 官方 | <https://docs.anthropic.com> |
| Google 官方 | <https://ai.google.dev/docs> |

---

## 下一步

- [M2-02 国内主流模型](./02-domestic-models.md)
- [M2-03 模型横向对比与选型](./03-comparison.md)
- [📚 完整参考资源](../references.md)
