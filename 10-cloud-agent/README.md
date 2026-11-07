# M10 · AI Cloud Agent

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 云端/远程 AI Agent：持续运行、主动推送、自动执行。
> **2026-11 版图已经和 2026-03 初版完全不同**：Claude Cowork / Duet、Codex Cloud、Copilot in the cloud、Antigravity 相继登场，Google Jules 宣布关停。旧产品描述保留在文末「历史沿革」。

---

## 模块概述

本模块回答四个问题：

1. **Cloud Agent 是什么**，和本地 IDE / 聊天工具有什么本质区别；
2. **2026-11 有哪些产品形态**，各自怎么触发、在哪执行、权限与计费如何；
3. **怎么用好**：任务描述、边界控制、PR review；
4. **怎么自建**：Claude Code / Codex / OpenClaw / CI 的组合。

**适合人群**：所有人（自建部分面向开发同学）

---

## 2026-11 版图速览

| 产品 | 一句话形态 |
|------|-----------|
| **Claude Code（cloud sessions）** | 在 Anthropic 云 VM 里跑 Claude Code，浏览器/手机/终端都能起任务，可 teleport 回本地 |
| **Claude Code（Remote Control）** | 代码仍在你机器上跑，但可以从手机/浏览器远程操控 |
| **Claude Cowork** | 面向知识工作的桌面/云端 Agent：本地隔离 VM、定时任务、连接器 |
| **Claude Duet** | 主动型个人 Agent（research preview，美国 Pro/Max/Ultra 候补） |
| **OpenAI Codex Cloud** | ChatGPT 里的云端编码任务：环境、任务、PR，一套流程 |
| **GitHub Copilot in the cloud** | GitHub 原生云 Agent：cloud sandbox / Actions / 远程环境三种执行位置 |
| **Google Antigravity** | Google 的 agent-first 开发平台；承接 Jules 的远程后台任务能力 |
| **Devin** | 商业化 AI 软件工程师，2026 年转向个人订阅 + 团队席位 |
| **Cursor Cloud Agents** | IDE 内的云端 Agent 入口（与 Cursor 深度整合） |
| **OpenClaw（自托管）** | 自己的 Gateway + 云端会话，渠道与数据完全自控 |

---

## 本模块文件

| 编号 | 文件 | 内容概述 |
|------|------|----------|
| [M10-01 ⭐️](./01-what-is-cloud-agent.md) | **什么是 AI Cloud Agent** | 概念、2026-11 版图、形态分类与选型 |
| [M10-02 ⭐️](./02-how-it-works.md) | **Cloud Agent 工作原理** | 沙箱、执行循环、凭据隔离、结果交付 |
| [M10-03 ⭐️](./03-using-cloud-agent.md) | **如何使用（实战）** | 各产品上手路径、任务模板、避坑 |
| [M10-04](./04-build-your-own.md) | **自建 Cloud Agent 工作流** | Claude Code / Codex / OpenClaw / CI 组合 |

---

## 历史沿革

- **2026-11**：版图重写：Claude Code cloud / Remote Control、Cowork、Duet、Codex Cloud、Copilot in the cloud、Antigravity、Devin 各自成形；Jules 关停。
- **2026-10**：Claude Duet research preview（10-21）；Google 宣布 Jules 关停并并入 Antigravity（10-29）。
- **2026-04**：Claude Cowork GA（04-09）。
- **2026-03（课程初版）**：模块建立，以 Cursor Background Agent、Devin、GitHub Copilot Workspace、Claude Code CLI、OpenAI Codex 为主线；这些产品的形态与定价后来均发生重大变化。

---

*← 返回 [课程总览](../README.md)*
