# ⭐️ M5-04b · Skills：技能扩展（重要）

> Skills 是 AI 的"能力单元"——封装好的 Prompt + 工具 + 流程。会用 Skills，效率翻倍。

---

## 什么是 Skills？

**Skills（技能）** 是在工具调用之上的更高层抽象：

| 层次 | 说明 | 例子 |
|------|------|------|
| **LLM** | 基础能力 | 理解语言、生成文本 |
| **Tools** | 单个工具 | 搜索、读文件、执行代码 |
| **Skills** | 封装好的能力单元 | "代码审查专家"、"文档生成器" |

**类比：**
- Tools = 函数
- Skills = 封装好的模块/类库

---

## Skills 的组成

一个完整的 Skill 通常包含：

```
Skill: 代码审查专家
├── System Prompt（角色设定）
│   "你是一个资深代码审查专家，关注安全、性能、可维护性..."
├── Tools（可用工具）
│   - read_file: 读取代码文件
│   - search_codebase: 搜索代码库
│   - run_tests: 运行测试
├── Workflow（工作流程）
│   1. 分析代码结构
│   2. 检查安全漏洞
│   3. 检查性能问题
│   4. 检查代码规范
│   5. 生成审查报告
└── Output Format（输出格式）
    Markdown 报告，按优先级排序
```

---

## ChatGPT GPTs（自定义 GPT）

ChatGPT 的 Skills 实现形式是 **GPTs**。

**创建方式：** 右上角 → 我的 GPT → 创建

**GPT 组成：**
- **指令（Instructions）**：System Prompt
- **知识库（Knowledge）**：上传参考文档
- **功能（Capabilities）**：联网、代码解释器、DALL-E
- **操作（Actions）**：自定义 API 调用

**实用示例：团队技术助手 GPT**
```
名称：XX公司技术助手

指令：
你是我们公司的内部技术助手。
技术栈：Python/FastAPI/PostgreSQL/AWS
代码规范见上传的文档。
回答时优先考虑我们的实际场景。

上传知识库：
- 编码规范.pdf
- API设计指南.md
- 常见问题FAQ.md
```

**GPT Store：** [chatgpt.com/gpts](https://chatgpt.com/gpts)

---

## Claude Projects（项目技能）

Claude 的 Skills 实现是 **Projects**。

**创建方式：** 左侧栏 → Projects → 新建

**Project 组成：**
- **项目指令**：长期有效的 System Prompt
- **上传文档**：项目背景资料
- **所有对话**：继承项目上下文

**优势：** 比单次对话的上下文更持久，适合长期项目。

---

## Cursor .cursorrules（编码技能）

Cursor 的 Skills 实现是 **.cursorrules** 文件。

每个项目一个，自动加载：

```markdown
# .cursorrules

# 角色
你是一个 Python FastAPI 专家。

# 技术栈约束
- 使用 SQLAlchemy 2.0 新式 API
- 所有 IO 操作用 async/await
- 测试用 pytest + factory-boy

# 工作流程
- 生成代码时同时生成测试
- 发现安全问题主动提示
- 遵循 PEP8 规范
```

---

## MCP Servers（Claude 技能市场）

预封装好的工具+能力，一键安装：

**热门 MCP Servers：**

| Server | 功能 |
|--------|------|
| **filesystem** | 读写本地文件 |
| **github** | 操作 GitHub 仓库 |
| **postgres** | 查询数据库 |
| **brave-search** | 网络搜索 |
| **puppeteer** | 控制浏览器 |
| **memory** | 持久化记忆 |

**市场地址：** [modelcontextprotocol.io/servers](https://modelcontextprotocol.io/servers)

---

## Anthropic Prompt Library

Anthropic 官方的 Prompt 模板库，可直接复用：

**热门模板：**
- 代码审查专家
- SQL 生成器
- 会议纪要提取
- 文档写作助手
- 数据分析师

**地址：** [anthropic.com/prompt-library](https://www.anthropic.com/prompt-library)

---

## 如何设计好的 Skill

### 原则一：明确角色定位
```
❌ "你是一个 AI 助手"
✅ "你是一个有 10 年经验的 Python 后端架构师，专注于高并发系统设计"
```

### 原则二：明确输入输出
```
输入：用户提供的代码文件
输出：Markdown 格式的审查报告，按优先级排列
```

### 原则三：定义工作流程
```
Step 1: 分析代码结构，理解功能
Step 2: 检查安全漏洞（SQL注入、XSS等）
Step 3: 检查性能问题（N+1查询、内存泄漏）
Step 4: 检查代码规范（命名、注释、格式）
Step 5: 生成总结报告
```

### 原则四：设置边界
```
可以做：代码分析、提出建议、解释原理
不可以做：直接修改生产代码、处理敏感数据
不确定时：明确说明需要人工确认
```

---

## 团队共享 Skills 的最佳实践

```
团队 Skills 仓库
├── prompts/
│   ├── code-review.md       # 代码审查 Prompt
│   ├── api-doc-gen.md       # API 文档生成
│   └── incident-analysis.md # 故障分析
├── cursorrules/
│   ├── backend.cursorrules  # 后端项目规则
│   └── frontend.cursorrules # 前端项目规则
└── mcp-configs/
    └── team-tools.json      # 团队通用 MCP 配置
```

**版本控制**：Skills 文件提交到 Git，团队共享，持续迭代。

---

## 下一步

- [⭐️ M5-05 Multi-Agent 多智能体实战](./05-multi-agent.md)
- [⭐️ M5-01 Prompt 工程入门](./01-prompt-engineering.md)
