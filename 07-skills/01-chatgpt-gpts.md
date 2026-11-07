# ⭐️ M7-01 · ChatGPT 技能生态（2026：GPT Store 退场，Plugins / Skills 接棒）

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 重要变化：**自定义 GPT 正在退役**。OpenAI 正在把工作流迁移到 **Plugins + Skills**。本文保留 GPT Store 的精选清单作为历史档案，同时给出 2026-11 的正确入口与迁移方法。

---

## 一句话结论

| 你想做的事 | 2025 的做法 | 2026-11 的做法 |
|-----------|-------------|----------------|
| 找现成助手 | GPT Store 搜 GPT | [ChatGPT 插件目录](https://chatgpt.com/plugins) 搜 Plugin / Skill |
| 做自己的助手 | 创建自定义 GPT | 用 Plugin Creator 创建 Plugin（可含 Skill + App） |
| 团队共享 | 发布 GPT / 分享链接 | 工作区共享 Plugin / Skill；管理员控制 |
| 写多步流程 | GPT Instructions | **Skill**（可复用、可上传、可扫描） |

> **截至 2026-11：个人账号（Free/Go/Plus/Pro）已不能新建或发布 GPT；受影响的企业工作区新建入口已于 2026-10-26 关闭；标准退役日期为 2026-12-11。**（来源：[OpenAI 帮助中心 · GPTs in ChatGPT](https://help.openai.com/en/articles/8554407-gpts-in-chatgpt)，访问于 2026-11）

---

## 一、现状快照（2026-11）

### GPT 退役时间线

| 时间 | 事件 |
|------|------|
| 2026-10-26 | 受影响的 Enterprise 工作区**停止新建 GPT**（FedRAMP 工作区除外） |
| 2026-11 | 个人账号（Free/Go/Plus/Pro）不能新建/发布 GPT；已有 GPT 仍可使用与编辑 |
| 2026-12-11 | **标准退役日期**（未迁移的 GPT 到期） |
| 2027-02-11 | FedRAMP 工作区与获批延期的工作区退役日期 |

> 迁移后，原 GPT 变为**只读**。具体日期与迁移步骤以 [OpenAI 的退役 FAQ](https://help.openai.com/en/articles/20001519) 为准。

### 现在用什么

| 能力 | 载体 | 入口 |
|------|------|------|
| 流程说明 / 可复用指令 | **Skill** | 侧边栏 **Plugins** → **Skills** 标签页 |
| 连接外部服务 | **Connected app** | 插件安装时的授权流程 |
| 打包分发 | **Plugin** | [插件目录](https://chatgpt.com/plugins) |
| 开发/自定义 | Plugin Creator | 安装后 `@plugin-creator` 对话创建 |

### 可用性（注意）

- Skills 主要面向 **Business / Enterprise / Healthcare / Edu** 工作区，受管理员设置与角色权限控制；
- 部分插件标注 **Desktop only**，只能在桌面端使用；
- 插件可包含 Skills、Apps，也可以只含 Skills（不需要连接外部服务）。

---

## 二、迁移：从 GPT 到 Plugin + Skill

### 步骤

1. **盘点**你在用的 GPT：哪些是"提示词 + 知识文件"，哪些是"调 API"。
2. **拆分**：
   - 流程/指令 → 写成 **Skill**（`SKILL.md` 结构，见 [M5-04b](../05-practical/04-skills.md)）；
   - 外部 API/Action → 做成 **App / MCP**，在插件中连接；
   - 知识文件 → 放进 Skill 的 `references/` 或插件资源。
3. **创建**：安装 Plugin Creator，然后 `@plugin-creator` 描述需求：

   ```text
   @plugin-creator 创建一个 Project Updates 插件：
   从 Slack 和 Linear 收集进展，按附带的模板生成周报。
   模板作为 skill 的参考文件。
   ```

4. **测试**：让插件实际跑一次任务，检查它是否正确使用 skill 与 app。
5. **共享**：工作区管理员可设置安装策略（Available / Installed），成员也可按链接或工作区目录共享。
6. **留意旧 GPT**：迁移完成前它仍可用；迁移后原 GPT 只读。

### 迁移时最容易踩的坑

| 坑 | 说明 |
|----|------|
| GPT 的 Actions 不会自动变成 App | 需要重新配置连接与授权 |
| 知识文件不会自动迁移 | 需要放进 Skill 的 references 或插件资源 |
| 管理权限是两套 | 插件可用性 与 app 授权 分别控制 |
| 个人账号不能发布 | 需要工作区与相应角色权限 |

来源：[Plugins in ChatGPT](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt)、[Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)（2026-11）。

---

## 三、2026 年值得关注的入口

| 入口 | 链接 | 用途 |
|------|------|------|
| 插件目录 | [chatgpt.com/plugins](https://chatgpt.com/plugins) | 浏览 Public / Your workspace / Personal / Installed |
| Skills 标签页 | 插件目录 → Skills | 查已安装、自己创建、共享给你的 skill |
| Skills 编辑器 | [chatgpt.com/skills/editor](https://chatgpt.com/skills/editor) | 直接编辑 skill |
| Plugin Creator | 插件目录安装 | 对话式创建插件 |
| OpenAI Verified | 插件详情页徽章 | 官方审核过的插件 |

### 选插件的判断标准

1. **有没有 OpenAI Verified 徽章**（不代表可以跳过安全审查）。
2. **看它包含哪些 App、需要什么授权**。
3. **看是否 Desktop only**，是否影响团队使用。
4. **看更新频率与提供方**。
5. **敏感场景先小范围试用**。

---

## 四、历史档案：GPT Store 时代（2023–2026）

> 以下清单是 GPT Store 时期（约 2023–2025）开发向的常见 GPT。**它们可能已迁移、改名或不可用**，仅作历史参考——今天请到[插件目录](https://chatgpt.com/plugins)找对应能力。

### 编程开发类

| GPT 名称 | 当时的核心功能 | 今天对应的能力 |
|---------|---------------|----------------|
| Grimoire | 代码向导，生成项目骨架 | 编码类 Plugin / Codex |
| Code Copilot | 补全、重构、debug | Codex / 编码插件 |
| Diagrams: Show Me | 生成流程图、ER 图 | 图表类 Plugin |
| API Docs | 读懂 API 文档并生成示例 | 文档类 Skill + 联网 |
| SQL Expert | 自然语言转 SQL | 数据库 MCP + Skill |
| RegEx Generator | 生成正则 | 通用模型能力已覆盖 |

### Debug & 代码审查类

| GPT 名称 | 当时的核心功能 |
|---------|---------------|
| Bug Finder | 找 bug 并给修复方案 |
| Code Review | 安全/性能/可维护性审查 |
| Security Code Review | 注入、XSS、权限等安全审计 |

### 文档 & 效率类

| GPT 名称 | 当时的核心功能 |
|---------|---------------|
| Tech Doc Generator | 代码 → API 文档 / README |
| Git Commit Helper | diff → commit message |
| Unit Test Generator | 函数 → 单元测试 |
| Changelog Generator | commit → changelog |

### 架构 & 设计类

| GPT 名称 | 当时的核心功能 |
|---------|---------------|
| System Design GPT | 需求 → 系统方案 |
| Database Designer | 业务 → 表结构 |
| API Designer | REST / GraphQL 设计 |

> 这些 GPT 的"能力"大多已经被三样东西替代：**更强的通用模型**、**编码 agent（Codex / Claude Code / Cursor）**、**可复用的 Skill**。

---

## 五、给团队的建议

1. **停止新建 GPT**：新建工作流一律走 Plugin + Skill。
2. **趁早迁移**：12-11 前完成，别等到只读。
3. **把"机构知识"沉淀成 Skill**：Code Review、周报、发版检查这类流程，做成 `SKILL.md` 进仓库。
4. **区分"流程"与"连接"**：流程用 Skill，外部系统用 App/MCP。
5. **治理**：谁能装插件、谁能创建带 MCP 的插件，是管理员要提前定的策略。

---

## 六、历史沿革

| 时间 | 事件 |
|------|------|
| 2023-03 | ChatGPT Plugins 发布，首次让模型调用外部服务 |
| 2023-11 | OpenAI 推出 GPTs 与 GPT Store，自定义助手爆发 |
| 2024–2025 | GPT Store 成为最大的"提示词应用市场"；质量参差 |
| 2026 | OpenAI 宣布退役自定义 GPT，转向 Plugins + Skills |
| 2026-09 | Anthropic 上线 Claude Marketplace（同类竞品动作） |
| 2026-10-26 | 受影响企业工作区停止新建 GPT |
| 2026-12-11 | 标准退役日期 |

---

## 七、下一步

- [⭐️ M7-02 Claude 项目工作区：Projects → Skills / Plugins](./02-claude-projects.md)
- [⭐️ M7-03 Cursor 规则与技能社区精选](./03-cursor-rules.md)
- [⭐️ M5-04b Skills：技能扩展](../05-practical/04-skills.md)
