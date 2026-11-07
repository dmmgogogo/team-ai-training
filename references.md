# 📚 参考资源与链接索引

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02
>
> 本页汇总课程引用的外部资源。链接由 `scripts/check_docs.py --links` 定期体检，仍可能有站点改版/反爬导致的失效；如遇失效欢迎提 Issue。
>
> 具体模型版本、价格、榜单数据变化很快，**以官方页面当日内容为准**。

---

## 🏆 模型评测与榜单

| 排行榜 | 地址 | 说明 |
|--------|------|------|
| **LMArena / Arena.ai** | [lmarena.ai](https://lmarena.ai) | 人类盲测偏好榜（Elo 式评分），看综合体验 |
| **SWE-bench** | [swebench.com](https://www.swebench.com) | 真实 GitHub Issue 修复，代码能力常用基准 |
| **Artificial Analysis** | [artificialanalysis.ai](https://artificialanalysis.ai/leaderboards/models) | 智能指数 + 速度 + 价格综合对比 |
| **Epoch AI** | [epoch.ai](https://epoch.ai) | 综合能力指数（ECI）与长期趋势 |
| **Vals AI** | [vals.ai](https://vals.ai) | 金融/法律/税务/编码等职业任务评测 |
| **Terminal-Bench** | [tbench.ai](https://www.tbench.ai) | 终端与 Agent 执行能力 |
| **HuggingFace 开源榜** | [huggingface.co/open-llm-leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) | 开源模型学术基准 |

> 读榜方法见 [M4-06 评测与质量闭环](./04-principles/06-evaluation.md)。

---

## 🌐 官方模型平台

### 国际模型

| 公司/模型 | 官网 | API / 开发者平台 | 发布说明 / 文档 |
|-----------|------|------------------|------------------|
| **OpenAI** | [openai.com](https://openai.com) | [platform.openai.com](https://platform.openai.com) | [platform.openai.com/docs](https://platform.openai.com/docs) · [模型发布说明](https://help.openai.com/en/articles/9624314-model-release-notes) |
| **Anthropic / Claude** | [claude.com](https://claude.com) | [console.anthropic.com](https://console.anthropic.com) | [docs.claude.com](https://docs.claude.com/en/docs/intro) · [产品更新日志](https://support.claude.com/en/articles/12138966-release-notes) |
| **Google Gemini** | [gemini.google.com](https://gemini.google.com) | [ai.google.dev](https://ai.google.dev) | [Gemini API 文档](https://ai.google.dev/gemini-api/docs) · [Google AI 博客](https://blog.google/technology/ai/) |
| **Meta / Muse** | [ai.meta.com](https://ai.meta.com) | [llama.com](https://www.llama.com) | [Llama 文档](https://www.llama.com/docs/overview) |
| **Mistral AI** | [mistral.ai](https://mistral.ai) | [console.mistral.ai](https://console.mistral.ai) | [docs.mistral.ai](https://docs.mistral.ai) |
| **xAI / Grok** | [x.ai](https://x.ai) | [console.x.ai](https://console.x.ai) | [docs.x.ai](https://docs.x.ai) |

### 国内模型

| 公司/模型 | 官网 | API 平台 | 文档 |
|-----------|------|---------|------|
| **DeepSeek** | [deepseek.com](https://www.deepseek.com) | [platform.deepseek.com](https://platform.deepseek.com) | [API 文档](https://api-docs.deepseek.com) |
| **通义千问 Qwen** | [tongyi.aliyun.com](https://tongyi.aliyun.com) | [dashscope.aliyuncs.com](https://help.aliyun.com/zh/model-studio) | [阿里云百炼](https://help.aliyun.com/zh/model-studio) |
| **MiniMax** | [minimaxi.com](https://www.minimaxi.com) | [platform.minimaxi.com](https://platform.minimaxi.com) | [文档](https://platform.minimaxi.com) |
| **Kimi / 月之暗面** | [kimi.ai](https://kimi.ai) | [platform.moonshot.cn](https://platform.moonshot.cn) | [文档](https://platform.moonshot.cn/docs) |
| **文心 / 百度** | [yiyan.baidu.com](https://yiyan.baidu.com) | [千帆平台](https://cloud.baidu.com/product/wenxinworkshop) | [ERNIE 发布页](https://ernie.baidu.com/) · [ERNIE 5.5 Flash Base](https://ernie.baidu.com/release/ernie-5-5-flash-base/) · [Hugging Face](https://huggingface.co/baidu/ERNIE-5.5-Flash-Base) |
| **智谱 GLM** | [chatglm.cn](https://chatglm.cn) | [open.bigmodel.cn](https://open.bigmodel.cn) | [文档](https://open.bigmodel.cn/dev/api) |
| **豆包 / 字节** | [doubao.com](https://www.doubao.com) | [火山方舟](https://console.volcengine.com/ark) | [文档](https://www.volcengine.com/docs/82379) |
| **腾讯混元** | [hunyuan.tencent.com](https://hunyuan.tencent.com) | [腾讯云混元](https://cloud.tencent.com/product/hunyuan) | [文档](https://cloud.tencent.com/document/product/1729) · [Hy4 发布说明](https://cloud.tencent.cn/developer/article/2776227) |
| **小米 MiMo** | [github.com/XiaomiMiMo](https://github.com/XiaomiMiMo) | — | — |
| **阶跃 StepFun** | [stepfun.com](https://www.stepfun.com) | [platform.stepfun.com](https://platform.stepfun.com) | [文档](https://platform.stepfun.com/docs) |

> 版本演进与家族关系见 [M0-03 模型家谱](./00-history/03-model-lineage.md)。

---

## 🛠️ AI 编程工具

| 工具 | 官网 | 文档 / GitHub |
|------|------|---------------|
| **Cursor** | [cursor.com](https://cursor.com) | [docs.cursor.com](https://docs.cursor.com) · [Cursor 3 发布](https://cursor.com/blog/cursor-3) |
| **Claude Code** | [claude.com/product/claude-code](https://claude.com/product/claude-code) | [code.claude.com/docs](https://code.claude.com/docs) · [Agent Teams](https://code.claude.com/docs/en/agent-teams) |
| **OpenAI Codex** | [openai.com/codex](https://openai.com/codex) | [github.com/openai/codex](https://github.com/openai/codex) |
| **GitHub Copilot** | [github.com/features/copilot](https://github.com/features/copilot) | [docs.github.com/en/copilot](https://docs.github.com/en/copilot) |
| **Gemini CLI** | [github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | [Gemini CLI 文档](https://github.com/google-gemini/gemini-cli#readme) |
| **Google Antigravity** | [antigravity.google](https://antigravity.google) | [文档](https://antigravity.google/docs) |
| **Windsurf** | [windsurf.com](https://windsurf.com) | [docs.windsurf.com](https://docs.windsurf.com) |
| **Kiro** | [kiro.dev](https://kiro.dev) | [docs.kiro.dev](https://kiro.dev/docs) |
| **Aider** | [aider.chat](https://aider.chat) | [github.com/Aider-AI/aider](https://github.com/Aider-AI/aider) |
| **Cline** | [cline.bot](https://cline.bot) | [github.com/cline/cline](https://github.com/cline/cline) |
| **Continue** | [continue.dev](https://www.continue.dev) | [docs.continue.dev](https://docs.continue.dev) |
| **OpenCode** | [opencode.ai](https://opencode.ai) | [github.com/sst/opencode](https://github.com/sst/opencode) |
| **v0** | [v0.app](https://v0.app) | — |
| **Kimi Code** | [kimi.ai](https://kimi.ai) | [github.com/MoonshotAI](https://github.com/MoonshotAI) |

---

## 🚀 开发提效与 Agent 工作流工具

| 工具/资源 | 地址 | 说明 |
|-----------|------|------|
| **rtk** | [github.com/rtk-ai/rtk](https://github.com/rtk-ai/rtk) | 减少无效 token 消耗的 CLI 代理 |
| **OpenCLI** | [github.com/jackwener/opencli](https://github.com/jackwener/opencli) | 把网站/本地工具统一成 CLI |
| **Superpowers** | [github.com/obra/superpowers](https://github.com/obra/superpowers) | AI 编程 Agent 的完整开发工作流 |
| **gstack** | [github.com/garrytan/gstack](https://github.com/garrytan/gstack) | YC CEO 的 AI 软件工厂（角色化 Slash 命令） |
| **Claude Code 省 Token 指南** | [11-dev-tools/05](./11-dev-tools/05-claude-code-token-optimization.md) | 课程内文章 |

---

## 🔌 MCP 与 Skills

| 资源 | 地址 | 说明 |
|------|------|------|
| **MCP 官网** | [modelcontextprotocol.io](https://modelcontextprotocol.io) | 规范、SDK、生态入口 |
| **MCP 规范** | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) | 当前协议版本与变更 |
| **MCP Registry** | [registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io) | 官方服务器注册表 |
| **Awesome MCP Servers** | [github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 社区 MCP 服务器清单 |
| **Claude Skills / 插件** | [claude.com/blog](https://claude.com/blog) | Skills / plugins 发布说明 |
| **Claude 插件目录** | [claude.com/plugins](https://claude.com/plugins) | 官方插件市场 |
| **Cursor Rules** | [docs.cursor.com/context/rules](https://docs.cursor.com/context/rules) | `.cursor/rules` 语法 |
| **AGENTS.md** | [agents.md](https://agents.md) | 跨工具的项目规则约定 |
| **Awesome Cursor Rules** | [github.com/PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | 社区规则集 |

---

## ☁️ Cloud Agent 与常驻 Agent

| 资源 | 地址 | 说明 |
|------|------|------|
| **Claude Cowork** | [claude.com/product/cowork](https://claude.com/product/cowork) | 桌面/网页/移动端常驻 Agent |
| **Claude Code 远程** | [code.claude.com/docs](https://code.claude.com/docs) | 云端/远程会话 |
| **OpenAI Codex Cloud** | [openai.com/codex](https://openai.com/codex) | 云端委派任务 |
| **Thinking Machines** | [thinkingmachines.ai](https://thinkingmachines.ai/) | Inkling 系列模型 |
| **GitHub Copilot coding agent** | [docs.github.com/en/copilot](https://docs.github.com/en/copilot) | Issue → PR 自动化 |
| **Google Jules** | [jules.google](https://jules.google) | Google 的异步编程 Agent |
| **Devin** | [devin.ai](https://devin.ai) | 自主软件工程 Agent |

---

## 🖥️ 本地部署与开源

| 工具 | 地址 | 用途 |
|------|------|------|
| **Ollama** | [ollama.com](https://ollama.com) | 最简单的本地模型运行 |
| **LM Studio** | [lmstudio.ai](https://lmstudio.ai) | 带 GUI 的本地模型 |
| **vLLM** | [github.com/vllm-project/vllm](https://github.com/vllm-project/vllm) | 生产级高并发推理 |
| **Hugging Face** | [huggingface.co](https://huggingface.co) | 开源模型与数据集 |
| **OpenClaw** | [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw) | 自托管 AI 网关 |

---

## 📖 学习资源与论文

| 资源 | 地址 | 说明 |
|------|------|------|
| **Learn Claude Agents** | [learn-claude-agents.vercel.app/zh](https://www.anthropic.com/engineering/building-effective-agents) | 从零实现 Agent，中文 |
| **OpenAI Cookbook** | [cookbook.openai.com](https://cookbook.openai.com) | 官方示例代码 |
| **Anthropic Engineering** | [anthropic.com/engineering](https://www.anthropic.com/engineering) | Agent / 上下文工程等工程博客 |
| **Anthropic Prompt Library** | [docs.claude.com/en/resources/prompt-library](https://docs.claude.com/en/resources/prompt-library) | Prompt 模板 |
| **Attention Is All You Need**（2017） | [arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762) | Transformer 原始论文 |
| **GPT-3**（2020） | [arxiv.org/abs/2005.14165](https://arxiv.org/abs/2005.14165) | 规模法则与上下文学习 |
| **InstructGPT / RLHF**（2022） | [arxiv.org/abs/2203.02155](https://arxiv.org/abs/2203.02155) | 人类反馈对齐 |
| **FlashAttention**（2022） | [arxiv.org/abs/2205.14135](https://arxiv.org/abs/2205.14135) | 长上下文的关键工程优化 |
| **Lost in the Middle**（2023） | [arxiv.org/abs/2307.03172](https://arxiv.org/abs/2307.03172) | 长上下文注意力问题 |
| **DeepSeek R1**（2025） | [arxiv.org/abs/2501.12948](https://arxiv.org/abs/2501.12948) | 开源推理模型与低成本训练 |
| **Context Rot**（2025） | [research.trychroma.com/context-rot](https://research.trychroma.com/context-rot) | 上下文变长导致性能下降的实证 |

### 追踪 AI 动态

| 资源 | 地址 | 说明 |
|------|------|------|
| **LLM Stats** | [llm-stats.com](https://llm-stats.com) | 模型发布与基准追踪 |
| **DataLearner 发布追踪** | [datalearner.com/ai-models/release-tracker](https://www.datalearner.com/ai-models/release-tracker) | 未发布模型传闻与官宣预告 |
| **Daily Diff** | [github.com/dboeter/daily-diff](https://github.com/dboeter/daily-diff) | 每日 AI 模型/实验室更新摘要 |
| **Arxiv CS.AI** | [arxiv.org/list/cs.AI/recent](https://arxiv.org/list/cs.AI/recent) | 最新论文预印本 |
| **Hacker News** | [news.ycombinator.com](https://news.ycombinator.com) | 工程圈讨论与发布信息 |

---

## 💰 API 价格入口

| 平台 | 地址 | 说明 |
|------|------|------|
| **OpenAI Pricing** | [openai.com/api/pricing](https://openai.com/api/pricing) | 官方价格与缓存/批量折扣 |
| **Anthropic Pricing** | [claude.com/pricing](https://claude.com/pricing) | 官方价格（含 API 与订阅） |
| **Google AI Pricing** | [ai.google.dev/pricing](https://ai.google.dev/pricing) | Gemini API 价格 |
| **DeepSeek Pricing** | [api-docs.deepseek.com/quick_start/pricing](https://api-docs.deepseek.com/quick_start/pricing) | 官方价格 |
| **阿里云百炼价格** | [help.aliyun.com/zh/model-studio](https://help.aliyun.com/zh/model-studio) | Qwen 系列价格 |
| **Artificial Analysis 价格对比** | [artificialanalysis.ai/models](https://artificialanalysis.ai/models) | 跨厂商价格/速度对比 |

---

## 🧰 课程维护入口

- [MAINTAINING.md](./MAINTAINING.md) — 维护规范与更新节奏
- [CHANGELOG.md](./CHANGELOG.md) — 变更日志
- [scripts/check_docs.py](./scripts/check_docs.py) — 文档体检脚本
- [reports/docs-check-report.md](./reports/docs-check-report.md) — 最近一次体检报告

---

*链接失效或有更好的资源？欢迎提 Issue / PR，或在团队群反馈。*
