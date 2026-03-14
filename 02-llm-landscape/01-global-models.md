# M2-01 · 国际主流大模型

> 认识 OpenAI、Anthropic、Google、Meta 的主力产品。

---

## 一图总览

```
国际主流大模型
├── OpenAI          → GPT-4o / o3 / o4-mini
├── Anthropic       → Claude 3.5 / 3.7 Sonnet, Claude Opus
├── Google DeepMind → Gemini 2.0 Flash / Ultra
├── Meta            → Llama 3.3 / 4（开源）
├── Mistral AI      → Mistral Large / Codestral（开源友好）
└── xAI             → Grok 3
```

---

## OpenAI · GPT 系列

| 模型 | 特点 | 适合 |
|------|------|------|
| **GPT-4o** | 多模态（文本/图像/音频），速度快，性价比高 | 日常任务、开发 API |
| **o3 / o4-mini** | 推理增强，慢思考，解决复杂问题 | 数学、代码、逻辑题 |
| **GPT-4.1** | 长上下文（1M token），强代码能力 | 大文件分析、代码任务 |

**特点：**
- 生态最完善，插件/工具最多
- API 最成熟，文档最好
- 价格相对较高，但 mini 系列亲民
- 多模态能力强（图像、语音）

**入口：** chatgpt.com / platform.openai.com

---

## Anthropic · Claude 系列

| 模型 | 特点 | 适合 |
|------|------|------|
| **Claude 3.5 Sonnet** | 代码最强，指令跟随好 | 编程助手、文档写作 |
| **Claude 3.7 Sonnet** | Extended Thinking（慢思考）| 复杂推理、代码审查 |
| **Claude Opus 4** | 顶级质量，最强理解力 | 复杂分析、长文写作 |
| **Claude Haiku** | 极快极便宜 | 高频简单任务 |

**特点：**
- **代码能力极强**，开发者最爱
- 长上下文最高 200K Token
- 安全和对齐做得好，输出可靠性高
- 擅长长文本写作和结构化输出
- **Cursor、Claude Code 底层用的就是 Claude**

**入口：** claude.ai / console.anthropic.com

---

## Google DeepMind · Gemini 系列

| 模型 | 特点 | 适合 |
|------|------|------|
| **Gemini 2.0 Flash** | 速度快、成本低、多模态 | 日常任务、图像理解 |
| **Gemini 2.5 Pro** | 超长上下文（1M Token），推理强 | 大文件分析、复杂任务 |
| **Gemini Ultra** | 顶级能力，对标 GPT-4 | 企业高端需求 |

**特点：**
- **上下文窗口最大**（Gemini 1.5 Pro 可达 200 万 Token！）
- 与 Google 生态深度集成（Workspace、搜索）
- 多模态能力强：文本、图像、视频、音频
- 有免费额度，适合个人试用

**入口：** gemini.google.com / ai.google.dev

---

## Meta · Llama 系列（开源）

| 模型 | 参数量 | 特点 |
|------|--------|------|
| **Llama 3.3 70B** | 70B | 开源中质量最高，对标 GPT-4 |
| **Llama 3.1 405B** | 405B | 旗舰级，可本地私有化部署 |
| **Llama 4**（2025） | 多专家混合 | 新架构，多模态 |

**特点：**
- **完全开源**，可下载本地跑
- **可私有化部署**，数据不出内网
- 通过 Ollama、vLLM 等框架部署
- 生态活跃，大量基于 Llama 的微调版本
- 企业版需遵守 Meta 许可协议

**本地运行：** ollama pull llama3.3

---

## Mistral AI · Mistral 系列（欧洲开源）

| 模型 | 特点 |
|------|------|
| **Mistral Large** | 欧洲最强闭源模型 |
| **Mistral Small** | 高效轻量 |
| **Codestral** | 专为代码优化 |
| **Mixtral 8x7B** | MoE（混合专家）架构，开源 |

**特点：**
- 欧洲公司，GDPR 友好，数据合规好
- MoE 架构效率高（激活部分参数）
- 代码模型 Codestral 对标 Claude

---

## xAI · Grok 系列

| 模型 | 特点 |
|------|------|
| **Grok 3** | 推理能力强，实时联网（X/Twitter 数据）|
| **Grok 3 mini** | 轻量快速 |

**特点：**
- 马斯克旗下，整合 X（Twitter）实时数据
- 对政治话题更开放
- 中国大陆访问受限

---

## 综合对比速查

| 维度 | 最强 |
|------|------|
| 代码能力 | Claude 3.5/3.7 Sonnet，o3 |
| 推理/数学 | o3，DeepSeek R1，Claude 3.7（Thinking）|
| 创意写作 | Claude Opus，GPT-4o |
| 长文本 | Gemini 1.5 Pro（200万Token），Claude（200K）|
| 速度 | GPT-4o mini，Claude Haiku，Gemini Flash |
| 多模态（图像/视频） | GPT-4o，Gemini |
| 开源/私有化 | Llama 3，Mistral，DeepSeek |
| 性价比 | DeepSeek V3，Gemini Flash，Claude Haiku |

---

## 下一步

- [M2-02 国内主流模型](./02-domestic-models.md) — 了解国产 LLM
- [M2-03 模型横向对比与选型](./03-comparison.md) — 怎么选适合自己的模型
