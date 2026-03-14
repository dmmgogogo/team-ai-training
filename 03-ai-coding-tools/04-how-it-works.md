# M3-04 · AI 编程工具底层原理

> 理解了原理，才能用好工具，也能理解它的局限。

---

## 整体架构

```
你写的代码
    +
你的问题/指令
    ↓
[上下文构建] ← 这是核心，下面详细讲
    ↓
[LLM API 请求]（Claude / GPT-4o / DeepSeek）
    ↓
[模型生成回复]
    ↓
[差异对比 + 应用修改]
    ↓
你的代码被修改 / 你得到回答
```

---

## 关键技术一：上下文构建

AI 编程工具最重要的工作，就是**决定把什么内容发给 LLM**。

上下文包含：
```
1. 系统提示词（System Prompt）
   - "你是一个专业的代码助手..."
   - 当前语言/框架信息

2. 当前文件内容
   - 光标所在文件的代码

3. 相关文件（RAG 检索）
   - 根据你的问题，自动检索项目里相关的文件
   
4. 你的问题/指令

5. 对话历史
```

**为什么这很重要？**

LLM 不知道你的项目长什么样。工具的核心价值，就是把最相关的代码"喂"给模型，让它能给出准确答案。

---

## 关键技术二：代码库索引（Embedding）

当你打开项目时，Cursor 等工具会在后台：

```
1. 读取项目所有文件（排除 .gitignore）
       ↓
2. 把每个文件/函数切成小块（Chunk）
       ↓
3. 把每个 Chunk 转化为 Embedding（向量）
       ↓
4. 存储在本地向量数据库
```

当你问问题时：

```
你的问题 → 转化为 Embedding
       ↓
在向量数据库中搜索最相关的代码块
       ↓
把相关代码块 + 你的问题一起发给 LLM
```

这就是为什么 Cursor 能"理解整个项目"——它用语义搜索找到了相关代码。

**这个技术叫做 RAG（Retrieval-Augmented Generation）**

---

## 关键技术三：代码补全（FIM）

Tab 补全用的是特殊的技术叫 **FIM（Fill-In-the-Middle）**：

```
[PREFIX] 光标前的代码
[SUFFIX] 光标后的代码
[MIDDLE] ← 模型预测这里应该填什么
```

示例：
```python
def process_user(user_id):
    user = db.get(user_id)
    [模型在这里填入代码]
    return result
```

模型看到前后文，才能填入合适的内容。

**为什么补全这么快？**
- 专用的小模型（不是 GPT-4 这种大模型）
- 量化压缩，本地或边缘节点运行
- 预填充技术减少延迟

---

## 关键技术四：Agent 循环

Cursor Agent / Claude Code 能"自动完成任务"，背后是 **Agent 循环**：

```python
while True:
    response = llm.call(messages, tools=TOOLS)
    
    if response.stop_reason != "tool_use":
        break  # 任务完成，退出循环
    
    # 执行工具调用
    for tool_call in response.tool_calls:
        if tool_call.name == "read_file":
            result = read_file(tool_call.path)
        elif tool_call.name == "write_file":
            result = write_file(tool_call.path, tool_call.content)
        elif tool_call.name == "run_command":
            result = run_terminal(tool_call.command)
    
    messages.append(tool_results)
    # 继续循环...
```

**工具清单（以 Cursor 为例）：**
- `read_file` — 读取文件
- `write_file` — 写入/修改文件
- `search_codebase` — 搜索代码库
- `run_terminal` — 执行终端命令
- `search_web` — 搜索网络（部分工具有）

**模型决定调用哪个工具、传什么参数，然后根据结果继续工作**，直到任务完成。

---

## 关键技术五：Diff 应用

当 LLM 生成修改建议时，工具需要把它变成可视化的"接受/拒绝"界面：

```
原始代码：          LLM 生成：
def foo():    →    def foo():
    x = 1              x = 2      ← 修改
    return x           y = x + 1  ← 新增
                       return y    ← 修改
```

工具计算差异（Diff），高亮显示变化，让你选择接受或拒绝。

---

## 为什么有时候它会"出错"？

理解原理后，你就能理解局限：

| 问题 | 原因 |
|------|------|
| 不了解你的业务逻辑 | 它只看到代码，看不到需求背景 |
| 生成过时的库用法 | 训练数据有截止日期 |
| 跨文件任务出错 | 上下文窗口装不下所有相关代码 |
| 修改了不该改的代码 | Agent 判断失误，工具调用错误 |
| 重复生成类似内容 | 缺乏记忆，不知道已经做了什么 |

---

## 本地 vs 云端的区别

| 维度 | 云端模型（Claude/GPT） | 本地模型（Ollama）|
|------|----------------------|-----------------|
| 质量 | 更强 | 受限于硬件 |
| 速度 | 受网络影响 | 极快（本地） |
| 隐私 | 代码发给第三方 | 完全本地 |
| 成本 | 按 Token 计费 | 一次性硬件投入 |
| 适合 | 大多数场景 | 数据安全要求高 |

---

## 实用结论

1. **工具质量 = 上下文质量**：给 AI 提供越精准的代码片段，答案越好
2. **大文件拆分**：如果文件太大，超出上下文，AI 可能看不完整
3. **明确的 @引用**：用 `@文件名` 手动指定，比让工具自动猜更准
4. **Agent 模式要监督**：自动任务可能误改，保持 git 干净，随时可回滚
5. **写好 `.cursorrules`**：告诉 AI 你的项目规范，减少返工

---

## 下一步

- [M4-02 RAG 检索增强生成](../04-principles/02-rag.md) — 深入理解代码库索引
- [M4-03 Agent 原理](../04-principles/03-agent.md) — 深入 Agent 循环
- [M5-02 AI 辅助开发工作流](../05-practical/02-workflow.md) — 实战流程
