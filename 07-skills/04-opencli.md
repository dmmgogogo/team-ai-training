# ⭐️ M7-04 · OpenCLI：将网站和工具统一为 CLI

> 最后更新：2026年4月（基于 OpenCLI 官方 README）。  
> OpenCLI 把网站、Electron 应用和本地 CLI 工具统一成一个可被 AI 发现的命令入口，适合做团队自动化与 Agent 工作流。

---

## 什么是 OpenCLI

**OpenCLI** 是由 [jackwener](https://github.com/jackwener) 维护的开源项目，定位是 **Universal CLI Hub + AI Native Runtime**。

它的核心价值不是“单一网站爬取”，而是把分散能力统一成标准命令接口：

- Website -> CLI（网站能力命令化）
- Electron App -> CLI（桌面应用命令化）
- Local CLI -> Hub（统一收口现有本地工具）

**GitHub**: <https://github.com/jackwener/opencli>  
**npm**: <https://www.npmjs.com/package/@jackwener/opencli>

---

## 2026 年 4 月版关键信息

- 支持 **79+ adapters**（持续增长）
- 可直接复用 Chrome/Chromium 登录态
- 面向 AI Agent，支持在 `AGENT.md` / `.cursor/rules/*.mdc` 中配置发现入口
- 前置要求：**Node.js >= 20**（或 Bun >= 1.0）

---

## 快速上手（官方推荐路径）

## 1) 安装浏览器桥接扩展

1. 到 GitHub Releases 下载 `opencli-extension.zip`
2. 解压后打开 `chrome://extensions`
3. 开启开发者模式并加载已解压扩展

## 2) 安装 CLI

```bash
npm install -g @jackwener/opencli
```

## 3) 检查状态

```bash
opencli doctor
opencli daemon status
```

## 4) 跑第一个命令

```bash
opencli list
opencli hackernews top --limit 5
opencli hackernews top --limit 5 -f json
```

---

## 与 AI Agent 的集成方式

推荐在团队规则中加入这条约定：

1. 先执行 `opencli list` 探测可用能力
2. 优先使用 `opencli <tool> <command>`，减少手工网页操作

示例（可写入 `AGENT.md`）：

```md
Tool discovery:
- run `opencli list` before deciding browser/manual steps
- prefer `opencli <tool> <command>` for reproducible operations
```

---

## 三类典型命令

### 1) 公共数据（无需登录）

```bash
opencli hackernews top --limit 10 -f json
```

### 2) 浏览器登录态复用（需已登录）

```bash
opencli bilibili hot --limit 5
```

### 3) 统一调用本地工具（CLI Hub）

```bash
opencli gh pr list --limit 5
opencli docker ps
```

---

## 团队接入建议（精简版）

1. **先选 1-2 个高频场景试点**（如热点抓取、周报聚合）
2. **统一输出格式**：优先 `-f json`，便于后处理
3. **写入团队规则**：让 Agent 固定先走 `opencli list`
4. **合规先行**：仅在授权平台和合规范围内使用自动化

---

## 风险与注意事项

- 仅在授权场景中使用，遵守目标平台 ToS
- 浏览器登录态在本机，避免把 Cookie/Token 硬编码进脚本
- 关键自动化流程要留痕（命令、结果、时间）

---

## 相关资料

- 项目主页：<https://github.com/jackwener/opencli>
- 官方 README：<https://github.com/jackwener/opencli/blob/main/README.md>
- M11 实战文档：[`M11-02 OpenCLI：CLI Hub`](../11-dev-tools/02-opencli-cli-hub.md)

---

*← 返回 [M7 Skills 精选](./README.md) | [课程总览](../README.md)*
