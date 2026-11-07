# 变更日志 · CHANGELOG

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高（持续追加） ｜ 🔁 每次更新时追加

> 本文件按时间倒序记录课程的结构与内容变化。详细讨论见对应 commit / PR。
> 版本快照 tag：`snapshot-2026-04`（M11 完成版）、`snapshot-2026-07`（GitBook 同步版）、`snapshot-2026-pre-reorg`（自动巡检时期末版）、`snapshot-2026-11`（历史重整版）。

---

## 2026-11-07 · 历史重整版（v3）

**主题：从"追最新"改为"记录演进 + 可持续维护"。**

新增结构：

- 新增 **M0 · AI 演进史**（`00-history/`），作为课程第一部分：
  - M0-01 AI 大事记（2017–2026）
  - M0-02 六次范式转移：我们如何与 AI 协作
  - M0-03 模型家谱：各模型家族的版本演进
  - M0-04 年度回顾：当年的判断与后来的现实（2023–2026）
- M4 新增 **上下文工程**、**评测与质量闭环** 两篇（新的工程思维）。

内容更新：

- M2 恢复"当前快照（2026-11）+ 历史沿革"写法：
  - 国际：Claude 5.5 家族（Opus 5.5 / Sonnet 5.5 / Haiku 5.5）与 Fable 5.1 / Mythos 5.1、GPT-6 家族（Astra / Sol / Terra / Luna，含 GPT-6.1 Sol）、Gemini 4 Argon / Carbon、Grok 4.7、Meta Muse。
  - 国内：DeepSeek V4 系列（V4 Pro / V4.1-Flash）、Qwen3.8 Max、Kimi K3.1 Pro、GLM-5.3、MiniMax M3、MiMo-V2.6、Step 5 Preview、豆包 / 混元。
  - 价格统一为"带读取日期的快照 + 官方入口 + 缓存/批量折扣说明"。
- M3 / M11：更新 Cursor 3（2026-04）、SpaceX 收购（2026-06）、Claude Code Agent Teams、Codex、Copilot、Antigravity 2.0、Windsurf → Devin Desktop、Gemini CLI 企业化、Aider / Continue 维护状态；M11 星标与版本改为"截至 2026-11"并附 GitHub 链接。
- M5 / M6 / M7 / M8 / M9 / M10：同步 Skills / Plugins 与 GPT Store 退役、MCP 2026-07-28 规范、OpenClaw 2.0（v2026.10.10）、Claude Cowork / Duet、Cloud Agent 版图（含 Jules 关停）等新形态；旧内容降级为「历史沿革」保留。
- M1 / M4：补充 Thinking / effort、MoE 激活参数、1M 上下文与缓存、Agentic RAG、子 Agent、MCP 治理；新增 M4-05 上下文工程、M4-06 评测与质量闭环。
- 全站：统一文件头部"内容基准 / 时效性 / 下次复核"元信息；修复旧文件头损坏文本（如 `P26年4月`）。

维护机制：

- 新增 `MAINTAINING.md`（三层内容模型、更新节奏、历史保留、来源规范、责任分工）。
- 新增 `CHANGELOG.md`（本文件）。
- 用 `scripts/check_docs.py` + `.github/workflows/docs-health.yml` **每周体检**，替换旧的"每 3 天自动改写日期"机制（该机制会造成文档"看起来新、内容旧"）。
- 新增 git tag：`snapshot-2026-04`、`snapshot-2026-07`、`snapshot-2026-pre-reorg`、`snapshot-2026-11`。
- 修正 M5-04 / M5-04b 编号不一致、M11 编号与目录链接、部分模块 README 链接。

---

## 2026-07-04 · GitBook 同步

- 通过 GitBook 编辑器更新内容并同步回仓库。

---

## 2026-04-24 · M11 编号与文章补充

- 规范化 M11 文件编号，修复相关导航链接。
- 新增《Claude Code 省 Token 指南》（宝玉 / dotey 文章整理）。

---

## 2026-04-17 · 深度更新 + 自动巡检（v2）

- M2 / M3 / references 等改为"稳态维护"：删除高波动跑分、价格、市场份额，保留定位与选型方法。
- 首页增加"最近更新"摘要。
- 新增 `scripts/refresh_docs.py` 与 `.github/workflows/docs-auto-refresh.yml`，每 3 天自动更新日期标签。
- ⚠️ 后续复盘：该机制只会刷新日期、不更新内容，已被 2026-11 版取代。

---

## 2026-04-07 · M11 补充（v1 最后一版）

- 新增 Superpowers、gstack 两篇开发提效工具介绍。
- README 首页更新最近更新摘要。

---

## 2026-04-05 · OpenCLI 实战

- 新增 OpenCLI 三分钟演示流程与项目资料。
- M11 / M7 增加 OpenCLI 索引链接。

---

## 2026-03-30 · 全站纠错

- 统一 Cursor Rules 写法为 `.cursor/rules/*.mdc`。
- 修复功能描述与错别字（三批修复）。
- 首页增加"最近更新时间 + 变更摘要"。

---

## 2026-03-20 · OpenCLI 介绍

- 新增 M7-04《OpenCLI：将网站转换为 CLI 工具》。

---

## 2026-03-17 · M11 模块

- 新增 M11 开发提效工具模块，迁移 `rtk` 文章。
- 新增 M5-12 rtk Token 节省实战、M6-01 通用规则模板。

---

## 2026-03-16 · 模块补齐

- 新增 M10 AI Cloud Agent 模块。
- 为 M1–M10 补齐模块 README，修复目录 404。
- `.cursorrules` 迁移为 `.cursor/rules/*.mdc` 新体系。

---

## 2026-03-15 · M6–M9

- 新增 M6 AI 项目配置规范、M7 Skills 精选、M8 MCP 精选、M9 OpenClaw。
- 补充 M5-09/10/11（安全隐私、代码审查、成本管理）。

---

## 2026-03-14 · 课程建立

- 初始课程体系：M1–M5，共 14 个文件。
- 拆分 Tools / Skills，补充模型版本时间线与来源链接，新增 `references.md`。
- 纳入 MiniMax M1 / M2 / M2.5 等 2026-03 发布内容。
