# ⭐️ M5-11 · 成本管理与模型选型

> AI 用得爽，账单可能吓一跳。学会合理选模型、控制 Token 消耗，效果不变、成本砍半。

---

## Token 是什么？怎么计费？

### Token 基础
- 1 个 Token ≈ 0.75 个英文单词 ≈ 0.5 个中文汉字
- **1000 个中文字 ≈ 约 1500-2000 个 Token**

```
"你好世界" → 约 4 个 Token
"Hello World" → 约 3 个 Token
```

### 计费方式
每次 API 调用费用 = **输入 Token × 输入单价** + **输出 Token × 输出单价**

### 主流模型价格对比（更新至 2026-04，按官方定价页）

| 模型 | 输入（/1M tokens） | 输出（/1M tokens） | 适用场景 |
|------|-----------------|-----------------|---------|
| **GPT-4o** | $2.5 | $10 | 通用复杂任务 |
| **GPT-4o mini** | $0.15 | $0.6 | 简单任务首选 |
| **Claude Sonnet 4** | $3 | $15 | 复杂推理、长文本 |
| **Claude Haiku 4.5** | $1 | $5 | 快速、低成本 |
| **Gemini 2.5 Flash** | $0.30 | $2.50 | 低成本、支持 thinking budget |
| **DeepSeek-V3.2（deepseek-chat）** | $0.28（cache miss） / $0.028（cache hit） | $0.42 | 中文场景性价比高（API） |

> 定价更新说明：以上为各家**官方定价页**的标准档（Standard）公开价格，随时可能调整；以官方页面为准。

> 同等效果下，选对模型可以节省 **10-30倍** 成本。

---

## 什么任务用什么模型

### 按任务复杂度选型

**✅ 用便宜模型（mini/flash/haiku）就够用：**
- 代码补全、简单生成
- 分类、打标签
- 格式转换（JSON ↔ Markdown）
- 简单问答
- 翻译
- 摘要提取

**🔵 用中档模型（GPT-4o / Sonnet）：**
- 复杂代码生成和 debug
- 多步骤推理
- 长文档理解
- 需要高准确率的任务

**🔴 用旗舰模型（o1 / Claude Opus）：**
- 数学/逻辑推理
- 复杂架构设计
- 需要反复思考的任务
- 对准确率要求极高的场景

### 决策树
```
任务简单（分类/格式化/翻译）？
  → 是 → GPT-4o mini / Gemini Flash（最便宜）

需要复杂推理或长上下文？
  → 是 → GPT-4o / Claude Sonnet

中文场景为主，预算有限？
  → 是 → DeepSeek V3 / Qwen（国内价格更低）

极度追求准确率，预算不限？
  → 是 → o1 / Claude Opus
```

---

## Token 消耗优化技巧

### 1. 压缩 System Prompt
```
# 臃肿版（浪费 Token）
你是一个非常专业的、经验丰富的 Python 开发工程师，
你有超过 10 年的开发经验，熟悉各种设计模式，
你会用清晰简洁的方式解答问题...

# 精简版（效果相同）
你是资深 Python 工程师，简洁专业地回答问题。
```

### 2. 只传必要的上下文
```python
# 错误：把整个文件都传给 AI
with open("10000_line_file.py") as f:
    context = f.read()  # 几万 Token

# 正确：只传相关的函数/类
context = extract_relevant_section(file, target_function)
```

### 3. 用缓存（Cache）
- OpenAI 和 Anthropic 都支持 Prompt Cache
- 相同的 System Prompt 被缓存后，**缓存部分费用降低 75-90%**
- 把固定内容放在 prompt 开头，利用缓存

### 4. 流式输出 + 提前终止
```python
# 如果只需要前几行结果，用 stream + 提前停止
# 不需要等 AI 生成完整响应
```

### 5. 批处理
```python
# 错误：一次处理一条
for item in items:
    result = call_ai(item)  # N 次 API 调用，N 倍开销

# 正确：批量处理
results = call_ai(f"处理以下 {len(items)} 条数据：{items}")
```

---

## API 成本优化进阶

### 用量监控
```python
# 每次调用后记录 Token 用量
response = client.chat.completions.create(...)
print(f"本次消耗: {response.usage.total_tokens} tokens")
print(f"估算费用: ${response.usage.total_tokens / 1000000 * price:.4f}")
```

### 设置预算告警
- OpenAI：Dashboard → Settings → Limits → 设置月度上限
- Anthropic：Console → Settings → 消费告警

### 本地模型降成本
**适合本地化的场景：**
- 代码补全（Continue.dev + 本地模型）
- 敏感数据处理
- 高频调用的简单任务

```bash
# Ollama 本地运行
ollama run deepseek-coder:6.7b  # 代码补全，6GB 显存
ollama run qwen2.5:7b           # 中文对话，8GB 显存
```

---

## 成本计算器（实战案例）

**场景：每天处理 1000 条用户反馈，做情感分析**

| 方案 | 模型 | 每条 Token | 日成本 | 月成本 |
|------|------|-----------|--------|--------|
| 方案A | GPT-4o | 200 tokens | $0.50 | $15 |
| 方案B | GPT-4o mini | 200 tokens | $0.03 | $0.9 |
| 方案C | Gemini Flash | 200 tokens | $0.015 | $0.45 |
| 方案D | 本地模型 | - | $0 | $0 |

> 同样的任务，方案A vs 方案B 相差 **16倍**。

---

## 总结：选模型的三个原则

1. **先用小模型试** — 很多任务小模型完全够用
2. **按效果付费** — 效果不够再升级，不要一上来就用旗舰
3. **中文场景考虑国内模型** — DeepSeek / Qwen 价格低且中文效果好

---

## 下一步

- [⭐️ M5-09 AI 安全与数据隐私](./09-security-privacy.md)
- [M2-03 模型横向对比与选型指南](../02-llm-landscape/03-comparison.md)
