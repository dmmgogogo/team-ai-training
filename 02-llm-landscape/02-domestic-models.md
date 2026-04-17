# M2-02 · 国内主流大模型

> P26年4月。  
> 本页采用“稳态维护”策略：保留产品定位与选型方法，删除高波动跑分、促销价和营销口径。

---

## 一图总览（长期有效版）

```
国内主流大模型
├── DeepSeek      → 开源与 API 双轨，工程圈采用广
├── Qwen（阿里）  → 开源生态完整，企业云集成强
├── MiniMax       → Agent 与产品化能力突出
├── Kimi（月之暗面）→ 长文本与知识工作流体验好
├── 文心（百度）   → 企业场景和平台化能力成熟
├── 智谱（GLM）    → 学术与开源路线持续推进
├── 豆包（字节）   → 产品化速度快，生态扩展快
└── 混元（腾讯）   → 企业办公与云生态协同
```

---

## 各模型家族的“稳定认知”

## DeepSeek（深度求索）

**定位：**
- 开源模型与 API 双线并行
- 在代码、推理和性价比场景中常被优先考虑

**适合：**
- 预算敏感但质量要求高的团队
- 需要本地部署与私有化能力的项目

**入口：** <https://deepseek.com> / <https://platform.deepseek.com>

---

## 通义千问（Qwen）

**定位：**
- 国内开源生态中覆盖面很广
- 与阿里云（百炼）协同强，企业落地成本低

**适合：**
- 需要稳定云平台能力和企业集成能力
- 需要多尺寸开源模型做分层部署

**入口：** <https://tongyi.aliyun.com> / <https://dashscope.aliyuncs.com>

---

## MiniMax

**定位：**
- 强调 Agent 任务与产品化体验
- 在自动化工作流场景中增长快

**适合：**
- 需要浏览器/研究/工具链协同的 Agent 场景
- 希望“模型 + 产品能力”一体化的团队

**入口：** <https://www.minimaxi.com>

---

## 月之暗面（Kimi）

**定位：**
- 长文本处理和知识工作流能力强
- 在研究、阅读、整理类任务中体验突出

**适合：**
- 文档密集型团队（法务、投研、策略、研发文档）
- 需要长上下文连续交互的使用场景

**入口：** <https://kimi.ai> / <https://platform.moonshot.cn>

---

## 文心（百度）

**定位：**
- 企业平台化能力成熟
- 与百度云与搜索生态结合紧密

**适合：**
- 需要成熟 ToB 服务与平台工具链的企业

**入口：** <https://yiyan.baidu.com> / <https://cloud.baidu.com/product/wenxinworkshop>

---

## 智谱（ChatGLM）

**定位：**
- 开源和学术路线持续推进
- 在教学、研究和垂直应用中常被采用

**适合：**
- 需要开源可控和研究导向的团队

**入口：** <https://chatglm.cn> / <https://open.bigmodel.cn>

---

## 豆包（字节）

**定位：**
- 产品化节奏快，生态扩展快
- 在消费级体验与企业协同间持续迭代

**适合：**
- 需要快速试点和高频交互体验的团队

**入口：** <https://www.doubao.com> / <https://console.volcengine.com/ark>

---

## 国内模型能力速查（去硬编码版）

| 维度 | 优先考虑 |
|------|----------|
| 代码开发 | DeepSeek / Qwen / Kimi Code |
| 推理任务 | DeepSeek / Kimi / Qwen 推理系 |
| Agent 任务 | MiniMax / Kimi / DeepSeek |
| 长文档处理 | Kimi / Qwen 长上下文能力 |
| 开源部署 | DeepSeek / Qwen / GLM |
| 企业集成 | Qwen（阿里云）/ 文心（百度云）/ 混元（腾讯云） |
| 中文对话 | Kimi / 文心 / 豆包 / Qwen |
| 多模态 | Qwen / 文心 / 豆包 / MiniMax |

---

## 合规与数据安全提示

> ⚠️ 使用国内 LLM API 时建议：

- 先明确数据分类（公开 / 内部 / 敏感）
- 敏感数据优先选本地部署或专有网络方案
- 与供应商签订数据处理与保密协议（DPA/NDA）
- 建立审计日志与调用留痕机制，满足事后追踪

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

## 删除说明（本次深度更新）

本页已删除以下高过期风险内容：

- 固定跑分与“谁第一”的结论
- 固定促销价与单次成本估算
- 夸张营销语与不可持续口径

这样做的目标是：降低误导风险，让课程更适合长期维护。

---

## 下一步

- [M2-03 模型横向对比与选型](./03-comparison.md)
- [📚 完整参考资源](../references.md)
