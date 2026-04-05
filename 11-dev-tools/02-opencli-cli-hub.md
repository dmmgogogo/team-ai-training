# M11-02 · OpenCLI：把网站和本地工具统一成 CLI Hub

> OpenCLI 是一个面向 AI 工作流的通用 CLI 运行时。它可以把网站、Electron 应用、本地命令行工具统一成标准化命令接口，便于团队在终端和 AI Agent 中复用。

GitHub: [jackwener/opencli](https://github.com/jackwener/opencli)  
npm: [`@jackwener/opencli`](https://www.npmjs.com/package/@jackwener/opencli)

---

## 这是什么？为什么放在 M11

M11 关注的是「开发提效工具」。OpenCLI 的核心价值是：

1. **统一入口**：把分散的网站操作和本地工具调用收敛到一个命令入口 `opencli ...`
2. **AI 友好**：可以让 AI Agent 通过固定命令发现并执行能力，减少“手工点网页”的重复劳动
3. **可脚本化**：命令可直接接到 Shell 脚本、自动化流程、CI 任务中

一句话：OpenCLI 不是单点工具，而是一个面向团队自动化的 **CLI Hub**。

---

## 核心能力（团队视角）

- **Website -> CLI**：将网站能力包装成命令行命令
- **Electron App -> CLI**：将桌面应用能力暴露为 CLI
- **Local CLI Hub**：注册并透传本地 CLI（如 `gh`、`docker`）统一被 AI 发现
- **浏览器会话复用**：复用 Chrome/Chromium 已登录状态，避免在脚本中保存账号密码
- **AI Skills 集成**：可配合 Cursor/Claude Code 的技能体系，让 Agent 自动调用

---

## 快速上手（官方推荐路径）

## 1) 安装浏览器桥接扩展

1. 打开 OpenCLI GitHub Releases，下载 `opencli-extension.zip`
2. 解压后进入 `chrome://extensions`
3. 开启开发者模式，点击「加载已解压的扩展程序」

## 2) 安装 CLI

```bash
npm install -g @jackwener/opencli
```

## 3) 健康检查

```bash
opencli doctor
opencli daemon status
```

## 4) 试运行

```bash
opencli list
opencli hackernews top --limit 5
opencli bilibili hot --limit 5
```

---

## 3 分钟演示流程（复制即用）

下面这组命令适合团队培训现场演示：先验证环境，再跑一个公开数据命令，最后输出机器可读结果。

```bash
# Step 1: 安装（已安装可跳过）
npm install -g @jackwener/opencli

# Step 2: 健康检查
opencli doctor

# Step 3: 查看可用能力
opencli list

# Step 4: 运行公开数据命令（无需登录）
opencli hackernews top --limit 5

# Step 5: 输出 JSON，便于程序消费
opencli hackernews top --limit 5 -f json
```

如果要演示“浏览器会话复用”，可加一条（需先在 Chrome/Chromium 登录目标站点）：

```bash
opencli bilibili hot --limit 5
```

---

## 团队常见用法

## A. 统一命令发现入口

将以下信息写入团队的 AI 规则文档（如 `AGENT.md` 或 `.cursor/rules/*.mdc`）：

- 先执行 `opencli list` 查看可用能力
- 优先使用 `opencli <tool> <command>`，再考虑手动浏览器操作

这样可以让 Agent 在同一套命令空间下完成任务，减少口径不一致。

## B. 把现有本地工具纳入 Hub

```bash
opencli register mycli
opencli gh pr list --limit 5
opencli docker ps
```

当团队工具越来越多时，这个方式有利于沉淀“统一可发现能力目录”。

## C. 机器可读输出

```bash
opencli bilibili hot -f json
opencli reddit hot -f csv
```

`json/csv/md/yaml` 输出格式便于后续程序处理和报表生成。

---

## 安全与合规注意点

1. **仅在授权场景使用自动化能力**：遵守目标平台 ToS 和团队合规要求
2. **登录状态在本地浏览器**：避免把 Cookie、Token 硬编码进脚本
3. **最小权限原则**：团队账号按角色分级，降低误操作风险
4. **审计留痕**：关键自动化任务建议记录命令与结果，便于排查

---

## 适用与不适用场景

| 场景 | 适配度 | 说明 |
|------|--------|------|
| 需要把网页操作标准化为命令 | ⭐⭐⭐⭐⭐ | 降低人工重复点击成本 |
| 希望 AI Agent 可自动执行固定流程 | ⭐⭐⭐⭐⭐ | 统一命令接口更稳定 |
| 团队有大量现有 CLI 工具待统一 | ⭐⭐⭐⭐ | 便于发现和复用 |
| 强监管、禁止浏览器自动化环境 | ⭐⭐ | 需先评估合规与风控 |

---

## 参考资料

- 项目主页：<https://github.com/jackwener/opencli>
- 官方 README：<https://github.com/jackwener/opencli/blob/main/README.md>
- npm：<https://www.npmjs.com/package/@jackwener/opencli>

---

*← 返回 [M11 开发提效工具](./README.md) | [课程总览](../README.md)*
