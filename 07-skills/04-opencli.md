# ⭐️ M7-04 · OpenCLI：把网站与浏览器变成 AI 可调用的 CLI

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 项目仍在活跃维护（2026-11 仍在提交），定位已从"网站 CLI 化"升级为 **通用浏览器自动化 CLI + Agent 工具层**：既能用内置适配器跑确定性命令，也能让 AI Agent 直接操作你已登录的 Chrome。

---

## 一句话结论

| 维度 | 2026-11 现状 |
|------|--------------|
| 项目 | [jackwener/OpenCLI](https://github.com/jackwener/opencli)，Apache-2.0 |
| 版本 | npm 包 `@jackwener/opencli` 最新 **2.0.2**（2026-11 查询） |
| 热度 | GitHub 约 **3.09 万 star**，最近提交 2026-11-05（GitHub API，2026-11-07 查询） |
| 形态 | OpenCLIApp（macOS/Windows）+ npm CLI + Chrome 扩展 |
| 运行要求 | Node.js **>= 20.18.1**（npm 安装时） |
| 覆盖 | 100+ 站点与命令 + 任意网页的浏览器操作原语 |
| 面向 Agent | 提供 **Skills**（`npx skills add jackwener/opencli`）与插件机制 |

> 数字会变，引用时请标注查询日期；以 [GitHub 仓库](https://github.com/jackwener/opencli) 与 [npm](https://www.npmjs.com/package/@jackwener/opencli) 为准。

---

## 一、它解决什么问题

传统做法里，让 AI"操作网站"有三条路，各有痛点：

| 做法 | 痛点 |
|------|------|
| 手工复制网页内容给 AI | 慢、不可复现、易出错 |
| 给每个网站写爬虫 | 维护成本高，登录态难处理 |
| 让 Agent 直接点浏览器 | 不稳定、难调试、无结构化输出 |

OpenCLI 的思路是：**把网站能力变成确定性命令**，同时保留"操作任意页面"的浏览器原语，让 AI 在两者之间选择。

```
网站 / 浏览器会话
   ├─ 内置适配器 → opencli <site> <command>   （确定性、可复用）
   └─ 浏览器原语 → opencli browser ...        （任意页面、临场操作）
```

---

## 二、2026-11 的关键能力

### 1. 内置适配器（100+ 站点）

README 列出的代表性站点包括：小红书、B 站、知乎、Hacker News、Reddit、X/Twitter、LinkedIn、Amazon、Upwork、Midjourney、Notion 相关、Claude / Gemini / NotebookLM 等（完整列表见仓库 `docs/adapters/`）。

```bash
opencli list                        # 列出所有已注册命令
opencli hackernews top --limit 5    # 公共数据
opencli bilibili hot --limit 5      # 复用浏览器登录态
opencli xiaohongshu search "关键词"
```

### 2. 浏览器原语（任意页面）

```bash
opencli browser open https://example.com --session research
opencli browser state   --session research      # 结构化 DOM 快照
opencli browser click   --session research --selector "..."
opencli browser fill    --session research --selector "..." --value "..."
opencli browser extract --session research
opencli browser screenshot --session research
opencli browser close   --session research
```

关键点：Agent 读的是**结构化 DOM**，不是截图，因此更可靠、更省 token。

### 3. 输出格式

命令默认输出 JSON（`{ "ok": true, "data": ... }`），失败返回结构化错误与非零退出码：

```bash
opencli bilibili hot -f json    # 管道给 jq 或 LLM
opencli bilibili hot -f table
opencli bilibili hot -f csv
opencli bilibili hot -f yaml
opencli bilibili hot -f md
```

退出码遵循 `sysexits.h`（0 成功、66 空结果、69 浏览器桥接断开、75 超时、77 需要登录、78 配置错误、130 Ctrl-C），方便 CI/脚本分支处理。

---

## 三、快速上手（2026-11 路径）

### 1) 安装

**方式 A：OpenCLIApp（macOS / Windows 推荐）**

从 <https://opencli.info/download> 下载安装，打开应用后在 System 页安装/修复 `opencli` 命令。

**方式 B：npm（CLI / CI / 服务器）**

```bash
node --version        # 需要 >= 20.18.1
npm install -g @jackwener/opencli
```

### 2) 安装浏览器桥接扩展

- Chrome 网上应用店安装 **OpenCLI** 扩展（推荐）；或
- 从 GitHub Releases 下载 `opencli-extension-v{version}.zip`，`chrome://extensions` 开启开发者模式后加载。

### 3) 验证

```bash
opencli doctor
```

### 4) 跑第一条命令

```bash
opencli list
opencli hackernews top --limit 5
```

### 5) 多 Chrome 配置（可选）

```bash
opencli profile list
opencli profile rename <contextId> work
opencli profile use work
```

---

## 四、与 AI Agent 集成（重点）

### 方式一：安装 Skills（推荐）

```bash
npx skills add jackwener/opencli
```

或只装需要的：

```bash
npx skills add jackwener/opencli --skill opencli-browser
npx skills add jackwener/opencli --skill opencli-adapter-author
npx skills add jackwener/opencli --skill opencli-autofix
npx skills add jackwener/opencli --skill opencli-usage
```

| Skill | 用途 | 示例提问 |
|-------|------|----------|
| **opencli-browser** | 临时操作任意网页（导航、点击、填表、提取） | "帮我看看小红书通知" |
| **opencli-adapter-author** | 为新站点写可复用适配器 | "给抖音热榜写个 adapter" |
| **opencli-autofix** | 内置命令失效时修复适配器 | "`opencli zhihu hot` 返回空了，修一下" |
| **opencli-usage** | 命令与站点速查 | "OpenCLI 有哪些 Twitter 命令？" |

安装后，Agent 会自动发现并调用这些 skill，不需要你手动拼接命令。

> 这套"**能力用 CLI 暴露、知识用 Skill 分发**"的组合，是 2026 年 agent 工具设计的一个典型范式。

### 方式二：写进项目规则

在 `AGENTS.md` 或 `.cursor/rules/` 中约定：

```markdown
## 工具发现
- 需要操作网站或浏览器时，先运行 `opencli list` 探测能力
- 优先使用 `opencli <tool> <command>`，减少手工网页操作
- 输出优先 `-f json`，便于后续处理
```

### 方式三：自己写适配器

```bash
opencli adapter init mysite/search
opencli adapter test mysite/search
opencli adapter eject <site>       # 本地修改官方适配器
opencli plugin install github:user/opencli-plugin-xxx
```

---

## 五、团队接入建议

1. **先选 1–2 个高频场景试点**：热点抓取、内容整理、周报聚合。
2. **统一输出格式**：`-f json` / `-f md`，便于下游处理。
3. **登录态隔离**：用独立 Chrome Profile 或 `--session`，避免误用主账号。
4. **把发现流程写进规则**：让 Agent 固定先 `opencli list`。
5. **合规先行**：只在授权平台和合规范围内使用自动化。

---

## 六、风险与注意事项

| 风险 | 说明 | 建议 |
|------|------|------|
| **平台 ToS** | 自动化可能违反目标站点条款 | 仅用于授权场景，控制频率 |
| **登录态泄露** | Cookie/token 在本机 | 不硬编码进脚本；用独立 Profile |
| **适配器失效** | 站点改版会导致命令失败 | 用 `opencli-autofix` / 及时更新 |
| **供应链** | 第三方插件/适配器可执行代码 | 只用可信来源，审阅后再装 |
| **数据合规** | 抓取内容可能含个人信息 | 最小化采集，注意留存与脱敏 |

---

## 七、历史沿革

| 时间 | 变化 |
|------|------|
| 2026-03 | 课程新增 M7-04《OpenCLI：将网站转换为 CLI 工具》 |
| 2026-04 | 当时 README 记录约 79+ adapters；课程同步"79+ adapters"口径 |
| 2026 年中 | 项目扩展到浏览器自动化原语、插件、Skills 生态 |
| 2026-11 | npm **2.0.2**；GitHub 约 3.09 万 star；提供 OpenCLIApp、100+ 站点、`npx skills add` 集成；README 定位为"通用浏览器自动化 CLI + Agent 工具层" |

> 本文早期版本中的"79+ adapters""Node >= 20"等表述均已过时，已按 2026-11 实际情况更新。

---

## 八、参考

- 项目主页：<https://github.com/jackwener/opencli>
- 中文文档：<https://github.com/jackwener/opencli/blob/main/README.zh-CN.md>
- npm：<https://www.npmjs.com/package/@jackwener/opencli>
- 下载 OpenCLIApp：<https://opencli.info/download>
- Chrome 扩展：<https://chromewebstore.google.com/detail/opencli/ildkmabpimmkaediidaifkhjpohdnifk>
- M11 实战：[`M11-02 OpenCLI：CLI Hub`](../11-dev-tools/02-opencli-cli-hub.md)

---

*← 返回 [M7 Skills 精选](./README.md) | [课程总览](../README.md)*
