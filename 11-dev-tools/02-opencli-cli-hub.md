# M11-02 · OpenCLI：把网站和浏览器变成 CLI Hub

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02
>
> 截至 2026-11：**约 30.9k ⭐**，最新版 **v2.0.2**（2026-10-20）。定位已从「网站 → CLI」扩展为 **面向 AI Agent 的通用浏览器自动化 CLI**，可作为 agent-browser 的替代。
>
> GitHub: [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) ｜ npm: [`@jackwener/opencli`](https://www.npmjs.com/package/@jackwener/opencli)

---

## 这是什么？为什么放在 M11

M11 关注「开发提效工具」。OpenCLI 2026 年的核心价值是：

1. **统一入口**：把网站操作、浏览器操作、本地 CLI 收敛到一个命令入口 `opencli ...`
2. **AI 友好**：Agent 可以通过固定命令发现并执行能力，减少「手工点网页」的重复劳动
3. **可脚本化**：命令可直接接到 Shell、自动化流程、CI
4. **浏览器状态复用**：直接使用你已登录的 Chrome 会话，不需要在脚本里存账号密码

一句话：OpenCLI 不是单点工具，而是一个面向 Agent 的 **浏览器/CLI 能力层**。

---

## 2026-11 的 OpenCLI 有什么新东西

| 变化 | 说明 |
|------|------|
| **通用浏览器自动化** | 无需站点适配器，也能 navigate / click / fill / extract / screenshot |
| **`opencli browser` 原语** | Agent 直接操作任意网页：打开、读取网络请求、截图、描述页面 |
| **Agent 技能** | `opencli-browser`（操作网页）、`opencli-adapter-author`（写适配器）可装进 Claude Code / Cursor |
| **适配器体系** | 内置 Bilibili、知乎、小红书、Reddit、HackerNews、Twitter/X 等站点命令 |
| **统一 JSON 契约** | 默认输出 `{ "ok": true, "data": ... }`；失败 `{ "ok": false, "error": {...} }`，日志走 stderr |
| **Chrome 扩展上架** | 可直接从 Chrome Web Store 安装浏览器桥接扩展 |

> ⚠️ v2 有**破坏性变更**：命令语法与 JSON 输出结构变了（如 `analyze` / `discover` 被 `state --diagnostics` / `network --static` 替代）。升级前先读迁移说明。

---

## 核心能力（团队视角）

- **Website → CLI**：把网站能力包装成命令
- **Browser Use**：在已登录的 Chrome 上执行任意网页操作
- **Local CLI Hub**：注册并透传本地 CLI（如 `gh`、`docker`）统一被 AI 发现
- **浏览器会话复用**：复用 Chrome/Chromium 登录状态
- **AI Skills 集成**：配合 Claude Code / Cursor 的技能体系
- **机器可读输出**：`json` / `csv` / `md` / `yaml`

---

## 快速上手（官方推荐路径）

### 1) 安装浏览器桥接扩展

1. 打开 [Chrome Web Store 的 OpenCLI 扩展](https://chromewebstore.google.com/detail/opencli/ildkmabpimmkaediidaifkhjpohdnifk)
2. 安装并确认与 CLI 连通

（也可以从 GitHub Releases 下载 `opencli-extension.zip`，开发者模式加载。）

### 2) 安装 CLI

```bash
npm install -g @jackwener/opencli
```

### 3) 健康检查

```bash
opencli doctor
opencli daemon status
```

### 4) 试运行

```bash
opencli list
opencli hackernews top --limit 5
opencli bilibili hot --limit 5
```

---

## 3 分钟演示流程（复制即用）

```bash
# Step 1: 安装（已安装可跳过）
npm install -g @jackwener/opencli

# Step 2: 健康检查
opencli doctor

# Step 3: 查看可用能力
opencli list search --site github

# Step 4: 运行公开数据命令（无需登录）
opencli hackernews top --limit 5

# Step 5: 输出 JSON，便于程序消费
opencli hackernews top --limit 5 -f json

# Step 6: 浏览器原语（Agent 常用）
opencli browser open https://example.com --session research
opencli browser network --static --session research
```

如果要演示「浏览器会话复用」，可加一条（需先在 Chrome/Chromium 登录目标站点）：

```bash
opencli bilibili hot --limit 5
```

---

## 团队常见用法

### A. 统一命令发现入口

将以下信息写入团队的 AI 规则文档（如 `AGENTS.md` 或 `.cursor/rules/*.mdc`）：

- 先执行 `opencli list` 查看可用能力
- 优先使用 `opencli <tool> <command>`，再考虑手动浏览器操作
- 需要任意网页操作时，用 `opencli browser` 原语

这样可以让 Agent 在同一套命令空间下完成任务，减少口径不一致。

### B. 把现有本地工具纳入 Hub

```bash
opencli register mycli
opencli gh pr list --limit 5
opencli docker ps
```

### C. 机器可读输出

```bash
opencli bilibili hot -f json
opencli reddit hot -f csv
opencli list -f json
```

### D. 给 Agent 写新适配器

```bash
opencli adapter init
opencli adapter check github/search
opencli adapter test
```

配合 `opencli-adapter-author` 技能，可以从页面侦察一路生成适配器代码。

---

## 安全与合规注意点

1. **仅在授权场景使用自动化能力**：遵守目标平台 ToS 和团队合规要求
2. **登录状态在本地浏览器**：避免把 Cookie、Token 硬编码进脚本
3. **最小权限原则**：团队账号按角色分级，降低误操作风险
4. **审计留痕**：关键自动化任务记录命令与结果
5. **v2 升级**：先在小范围验证命令语法与输出格式变化

---

## 适用与不适用场景

| 场景 | 适配度 | 说明 |
|------|--------|------|
| 需要把网页操作标准化为命令 | ⭐⭐⭐⭐⭐ | 降低人工重复点击成本 |
| 希望 AI Agent 可自动执行固定流程 | ⭐⭐⭐⭐⭐ | 统一命令接口更稳定 |
| 需要 Agent 操作任意网页（含登录态） | ⭐⭐⭐⭐⭐ | `opencli browser` 原语 |
| 团队有大量现有 CLI 工具待统一 | ⭐⭐⭐⭐ | 便于发现和复用 |
| 强监管、禁止浏览器自动化环境 | ⭐⭐ | 需先评估合规与风控 |

---

## 参考资料

- 项目主页：<https://github.com/jackwener/OpenCLI>
- 官方 README：<https://github.com/jackwener/OpenCLI/blob/main/README.md>
- npm：<https://www.npmjs.com/package/@jackwener/opencli>
- 中文文档：<https://github.com/jackwener/OpenCLI/blob/main/README.zh-CN.md>

---

## 历史沿革

- **2026-11**：约 30.9k ⭐，v2.0.2；定位升级为「通用浏览器自动化 CLI + agent-browser 替代」；新增 `opencli browser` 原语、适配器作者技能、JSON 命令契约；Chrome 扩展上架。
- **2026-10-17 / 10-20**：v2.0.0 → v2.0.2，引入破坏性语法与输出变更。
- **2026-04（旧版）**：当时定位是「网站 + Electron + 本地 CLI 的统一 Hub」，命令以 `opencli <site> <action>` 为主；星标数未在文中记录。
- **2026-03**：项目进入课程 M7 / M11，作为「网站转 CLI」工具介绍。

---

*← 返回 [M11 开发提效工具](./README.md) | [课程总览](../README.md)*
