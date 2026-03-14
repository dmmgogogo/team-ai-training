# M3-03 · 其他主流 AI 编程工具

---

## GitHub Copilot

> 微软/GitHub 出品，全球用户最多

**基本信息：**
- 底层模型：GPT-4o
- 价格：$10/月，学生/开源免费
- 支持：VS Code、JetBrains 全家桶、Neovim、Visual Studio

**核心功能：**
- 代码补全（Ghost Text）
- Copilot Chat（问答）
- Copilot Workspace（从 Issue 到 PR 全流程）
- PR 自动审查

**优势：**
- GitHub 深度集成，PR 审查、Issue 关联
- 企业版数据隐私保护好
- 对 JetBrains 用户最友好（Cursor 只有 VS Code 体验）

**劣势：**
- 代码补全质量略逊于 Cursor
- 多文件协作任务不如 Cursor Agent

---

## Windsurf（by Codeium）

> 2024 年底崛起的强力竞争者

**基本信息：**
- 底层模型：Claude + DeepSeek
- 价格：$15/月，有免费计划
- 支持：独立 IDE（VS Code 系）

**核心亮点：**

**Cascade 模式** — 最大特色：
```
你说："添加用户权限系统"
Cascade 自动：
  1. 读取整个项目结构
  2. 制定修改计划
  3. 一次性修改所有相关文件
  4. 运行测试验证
```

**优势：**
- 自动任务能力接近 Cursor Agent
- 价格比 Cursor 低
- 支持 DeepSeek，成本控制好

**适合：** 想要 Cursor 能力但预算更少的团队

---

## Claude Code（CLI）

> Anthropic 官方命令行工具，技术深度最强

**安装：**
```bash
npm install -g @anthropic-ai/claude-code
cd your-project
claude
```

**核心特点：**

直接在终端里与 Claude 对话，且能：
- 读写文件
- 运行命令（git、npm、python...）
- 理解整个代码库
- 持续迭代直到任务完成

**场景示例：**
```
> 分析这个项目的性能瓶颈，并提出优化建议

> 帮我把所有的 API 错误处理统一成同一种格式

> 根据 README 的要求，实现缺失的功能
```

**优势：**
- 不依赖 IDE，适合后端/DevOps
- 可以集成到 CI/CD 流水线
- 对整个代码库的理解比 Cursor 更深
- 支持自动化脚本，无人值守跑任务

**劣势：**
- 纯命令行，没有 GUI
- 按 API 用量计费，大量使用成本高

---

## Aider

> 开源 CLI，支持几乎所有模型

**安装：**
```bash
pip install aider-chat
aider --model deepseek/deepseek-chat  # 用 DeepSeek
aider --model ollama/llama3.3         # 用本地模型
```

**核心特点：**
- **完全开源**，可私有化部署
- 支持 GPT、Claude、DeepSeek、Ollama 等 100+ 模型
- 自动 git commit 每次修改
- 适合不想依赖闭源工具的团队

**场景：**
```bash
aider --model deepseek/deepseek-chat
> /add src/auth.py src/models.py
> 给这个认证系统添加双因素验证
# Aider 修改文件并自动 git commit
```

---

## Continue.dev

> 开源 VS Code / JetBrains 插件，连接本地模型

**特点：**
- **免费开源**
- 支持 Ollama（本地模型）
- 可以用 DeepSeek API、OpenAI、Claude
- 数据完全在本地（如果用 Ollama）

**配置示例（~/.continue/config.json）：**
```json
{
  "models": [
    {
      "title": "DeepSeek V3",
      "provider": "deepseek",
      "model": "deepseek-chat",
      "apiKey": "your-key"
    },
    {
      "title": "Local Llama (Ollama)",
      "provider": "ollama",
      "model": "llama3.3"
    }
  ]
}
```

**适合：** 数据安全要求高、不想付费订阅的团队

---

## v0 by Vercel

> 前端 UI 生成神器

**入口：** v0.dev

**功能：**
- 用自然语言描述 UI → 生成 React + Tailwind 代码
- 可以迭代修改
- 直接复制代码到项目

**示例：**
```
"帮我做一个数据仪表盘，左侧导航，
 右侧有用户统计卡片和折线图，
 深色主题，用 shadcn/ui 组件"
```

输出：完整可运行的 React 代码

**适合：** 前端开发、快速原型验证

---

## JetBrains AI Assistant

**特点：**
- 直接内置在 IntelliJ IDEA、PyCharm 等 JetBrains IDE
- 理解 JetBrains 的代码语义（类、方法、重构）
- 对 Java/Kotlin/Python 等类型系统理解更深

**适合：** 已经在用 JetBrains 系列 IDE 的后端开发

---

## 工具对比汇总

| 工具 | 优势场景 | 价格 | 数据隐私 |
|------|---------|------|---------|
| **Cursor** | 综合最强，日常开发 | $20/月 | 可关闭学习 |
| **Windsurf** | 自动任务，性价比 | $15/月 | 一般 |
| **Copilot** | JetBrains，企业 | $10/月 | 企业版好 |
| **Claude Code** | 代码库级任务，自动化 | API 计费 | 好 |
| **Aider** | 开源，多模型，灵活 | 免费+模型费 | 极好 |
| **Continue** | 本地模型，隐私优先 | 免费 | 最好 |
| **v0** | 前端 UI 生成 | 免费额度 | 一般 |

---

## 下一步

- [M3-04 AI 编程工具底层原理](./04-how-it-works.md)
