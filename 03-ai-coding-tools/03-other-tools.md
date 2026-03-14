# M3-03 · 其他主流 AI 编程工具

> 最后更新：2026年3月

---

## GitHub Copilot

> 微软/GitHub 出品，全球用户最多，入门最便宜

**基本信息：**
- 底层模型：GPT-4o
- 价格：$10/月，学生/开源免费
- 支持：VS Code、JetBrains 全家桶、Neovim、Visual Studio

**核心功能：**
- 代码补全（Ghost Text）
- Copilot Chat（问答）
- Copilot Workspace（从 Issue 到 PR 全流程）
- PR 自动审查 + 代码安全扫描

**优势：**
- GitHub 深度集成，PR 审查、Issue 关联
- 企业版数据隐私保护好（可完全关闭数据学习）
- $10/月是有 Git 集成的工具里最便宜的
- 对 JetBrains 用户友好

**适合：** 预算有限、已用 JetBrains、企业合规要求高的团队

---

## Windsurf（by Codeium）

> 个人免费，agentic 能力强，性价比最优

**基本信息：**
- 底层模型：Claude + DeepSeek
- 价格：**个人版免费**，Pro $15/月
- 支持：独立 IDE（VS Code 系）

**核心亮点：**

**Cascade + Supercomplete 模式：**
```
Cascade：你说"添加用户权限系统"
→ 自动读取整个项目结构
→ 制定修改计划
→ 一次性修改所有相关文件
→ 运行测试验证

Supercomplete：预测多行意图，不只补全一行
→ 根据你的编写意图预测接下来几行
```

**优势：**
- **个人用户完全免费**，对学习者友好
- agentic 自动任务能力接近 Cursor
- 支持 DeepSeek，成本控制好
- 市场定位：agentic IDE 类别最佳性价比

**适合：** 个人开发者、想要 Cursor 能力但预算有限的团队

---

## Claude Code（CLI）

> SWE-bench 评测第一（80.9%），代码能力最强的 CLI 工具

**安装：**
```bash
npm install -g @anthropic-ai/claude-code
cd your-project
claude
```

**核心特点：**
- 终端内与 Claude 对话，能读写文件、运行命令
- **SWE-bench 得分 80.9%**，代码理解和修复能力业界第一
- 理解整个代码库（不只是当前文件）
- 支持自动化：可集成到 CI/CD 流水线

**场景示例：**
```
> 分析这个项目的性能瓶颈，并给出优化建议
> 把所有的 API 错误处理统一成同一种格式
> 根据 README 要求，实现还未完成的功能
> 对比这两个实现方案，告诉我哪个更好
```

**优势：**
- 代码库级别的理解和修改，不依赖 IDE
- 适合后端/DevOps/自动化场景
- 无人值守跑复杂任务

**适合：** 需要处理整个代码库的复杂任务，自动化流水线

---

## OpenAI Codex CLI

> o3/o4-mini 驱动，速度最快（240+ tok/s）

**特点：**
- 底层用 o3/o4-mini，推理能力强
- Terminal-Bench 评测 77.3%，行业第二
- 速度极快（240+ tokens/秒）
- 支持图像输入（可截图 bug 发给它）

**适合：** 需要快速推理的命令行任务，o 系列推理能力场景

---

## Gemini CLI

> Google 出品，完全免费开源

**特点：**
- **完全免费，开源**，是唯一零成本 CLI 工具
- 底层用 Gemini 模型，长上下文优势
- 可自部署，数据完全掌控
- 国内访问需代理

**安装：**
```bash
npm install -g @google/gemini-cli
gemini
```

**适合：** 预算为零、数据安全要求高、已有 Google 账号

---

## Aider

> 开源 CLI，支持 100+ 模型

**安装：**
```bash
pip install aider-chat
aider --model deepseek/deepseek-chat    # 用 DeepSeek
aider --model ollama/llama4             # 用本地模型
```

**核心特点：**
- **完全开源**，100+ 模型支持（GPT、Claude、DeepSeek、Ollama...）
- 自动 git commit 每次修改
- 数据完全私有（用本地模型时）

---

## Antigravity ⭐ 新兴

> 完全免费（预览期），值得关注

**特点：**
- 预览期**完全免费，无付费计划**
- 新架构，市场定位差异化
- 具体能力持续观察中

**适合：** 预算为零、愿意尝鲜的开发者

---

## Kimi Code ⭐ 国内新兴

> 月之暗面出品，开源，可自部署

**特点：**
- **开源**，国内团队可私有化部署
- 月之暗面出品，长上下文能力延续
- 适合数据合规要求高的国内企业
- 是 Gemini CLI 之外另一个开源 AI 编程工具

**适合：** 数据不能出境、需要开源代码模型的国内团队

---

## Continue.dev

> 开源 VS Code / JetBrains 插件，连接本地模型

**特点：**
- **免费开源**，支持 Ollama 本地模型
- 可配置 DeepSeek API、Claude、Gemini
- 数据完全本地（用 Ollama 时）

**配置示例：**
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
      "title": "Local Llama 4",
      "provider": "ollama",
      "model": "llama4"
    }
  ]
}
```

---

## v0 by Vercel

> 前端 UI 生成神器

**入口：** v0.dev

**功能：**
- 用自然语言描述 UI → 生成 React + Tailwind 代码
- 迭代修改，直接复制到项目
- 支持 shadcn/ui 组件

**适合：** 前端开发、快速原型验证

---

## 2026年工具对比汇总

| 工具 | 优势场景 | 价格 | 数据隐私 |
|------|---------|------|---------|
| **Cursor** | 综合最强，日常开发 | $20/月 | 可关闭学习 |
| **Windsurf** | 自动任务，个人免费 | 免费/$15月 | 一般 |
| **Copilot** | JetBrains，企业合规 | $10/月 | 企业版好 |
| **Claude Code** | 代码库级任务，SWE榜第一 | API 计费 | 好 |
| **Codex CLI** | 速度极快，推理能力强 | API 计费 | 好 |
| **Gemini CLI** | 零成本，开源 | **完全免费** | 极好 |
| **Aider** | 多模型，本地部署 | 免费+模型费 | 极好 |
| **Antigravity** | 零成本，新兴 | **完全免费** | 观察中 |
| **Kimi Code** | 国内开源，合规 | 开源 | 极好 |
| **v0** | 前端 UI 生成 | 免费额度 | 一般 |

---

## 下一步

- [M3-04 AI 编程工具底层原理](./04-how-it-works.md)
