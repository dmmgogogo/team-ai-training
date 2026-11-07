# ⭐️ M6-04 · 真实案例：全栈项目 AI 配置实战

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 理论看完，来看真实项目怎么做的。
> 参考模板：[backend-front-template](https://github.com/dmmgogogo/backend-front-template)（最后更新 2026-03，按本文迁移到 2026-11 标准）
>
> 技术栈：Go 后端 + Flutter App + Vue3 管理后台

---

## 一句话结论

这个模板最初的思路（**模块独立 + 规范跟着模块走 + 技能复用**）在 2026 年依然正确；需要升级的是**文件形态**：

```
2026-03 版（模板现状）              2026-11 标准（本文）
AGENTS.md                          AGENTS.md（根 + 每模块嵌套）
backend/CLAUDE.md                  保留（Claude 专属），通用事实回填 AGENTS.md
.claude/skills/                    .agents/skills/（跨工具）+ .claude/skills/（Claude）
—                                  .claude/rules/（路径规则）
—                                  .mcp.json（团队 MCP）
```

> 模板仓库自 2026-03 后未再更新，直接 fork 会缺少 AGENTS.md 原生支持、skills 互通、MCP 项目配置等 2026 年的做法。建议 fork 后按本文升级。

---

## 一、2026-11 推荐目录结构

```
project-root/
├── AGENTS.md                       # 全局：架构、命令、协作约定
├── CLAUDE.md                       # @AGENTS.md + Claude 专属
├── .mcp.json                       # 团队 MCP（Claude Code）
├── .agents/
│   └── skills/                     # 跨工具技能（Cursor / Codex 等可读）
│       ├── beego-api/SKILL.md
│       ├── mysql/SKILL.md
│       └── redis/SKILL.md
├── .claude/
│   ├── rules/
│   │   ├── backend.md              # 可加 paths: backend/**
│   │   └── frontend.md
│   └── skills/                     # Claude Code 专属技能（可软链到 .agents/skills）
├── backend/
│   ├── AGENTS.md                   # 后端专属事实
│   └── CLAUDE.md                   # 后端 Claude 专属补充
├── frontend/
│   ├── flutter/
│   │   ├── AGENTS.md
│   │   └── CLAUDE.md
│   └── vben-admin/
│       ├── AGENTS.md
│       └── CLAUDE.md
└── docs/
    ├── ARCHITECTURE.md
    ├── API.md
    └── ADR/
```

**核心原则不变**：每个模块携带自己的 AI 规范文件，复制模块时规范跟着走。

---

## 二、根 AGENTS.md 写了什么

```markdown
# AGENTS.md

## 项目概述
全栈基础框架：Go 后端 + Flutter App + Vue3 管理后台。

## 模块
| 模块 | 技术栈 | 启动命令 |
|------|--------|----------|
| backend | Go + Beego | `go run main.go` |
| frontend/flutter | Flutter + Riverpod | `flutter run` |
| frontend/vben-admin | Vue3 + Vite | `pnpm dev` |

## 后端请求链路
HTTP → 中间件 → Controller → Service → Model

## API 命名空间
- 管理端：`/api/admin/*`
- 用户端：`/api/backend/*`
- 公共：`/api/common/*`

## 新增功能标准步骤
Model → DTO → Controller → Route → 测试

## 深入资料
- 架构：`docs/ARCHITECTURE.md`
- 接口：`docs/API.md`
- 各模块细节：见对应目录的 AGENTS.md
```

> 关键：**根 AGENTS.md 写整体，模块 AGENTS.md 写细节，CLAUDE.md 只补 Claude 专属。**

---

## 三、各模块 AGENTS.md / CLAUDE.md 重点

### backend

```markdown
# backend/AGENTS.md

## 分层
controller → service → model，禁止跨层

## 约定
- 统一返回：{"code": 200, "msg": "...", "data": {}}
- 错误码定义在 `internal/pkg/errcode/`
- 用户端与管理端使用不同的 BaseController
- `c.Error(code)` 调用后会自动 StopRun，不需要 return
- 数据库操作必须通过 model 层，禁止在 controller 里写 SQL
```

```markdown
# backend/CLAUDE.md

@AGENTS.md

## Claude 专属
- 改 `internal/` 前先读 `docs/API.md` 对应章节
- 新增接口必须同步更新 `docs/API.md`
```

### frontend/flutter

```markdown
# frontend/flutter/AGENTS.md

## 结构
feature-first：`lib/features/<feature>/{data,models,providers,pages}`

## 约定
- 所有日志走 `AppLogger`，禁止 `print`
- 操作 > 300ms 必须显示 loading 并禁用按钮
- 图片必须有加载失败占位
- 只调用 `/api/backend/*` 和 `/api/common/*`
- 401 → 清 token → 跳登录
```

### frontend/vben-admin

```markdown
# frontend/vben-admin/AGENTS.md

## 约定
- 只调用 `/api/admin/*`
- 权限控制用 `v-auth` 指令做按钮级控制
- API base url 从 `.env` 读，禁止硬编码
- 新增页面的同时更新路由与权限配置
```

---

## 四、Skills 的设计与复用

Skills 存放**可复用的技术能力**，独立于具体业务：

```
.agents/skills/
├── beego-api/    # 如何用 Beego 写 API（框架层知识）
├── mysql/        # MySQL 查询、事务、索引优化
└── redis/        # 缓存、分布式锁、消息队列
```

`SKILL.md` 示例：

```markdown
---
name: beego-api
description: 用 Beego 框架编写 REST API，包括 Controller、DTO、路由与错误码约定。新增或修改后端接口时使用。
---

# Beego API 规范

## 步骤
1. 在 `internal/model/` 定义数据结构
2. 在 `internal/dto/` 定义请求/响应 DTO
3. 在 `internal/controller/` 实现 handler（只做参数校验与调用 service）
4. 在 `internal/service/` 实现业务逻辑
5. 在 `internal/router/` 注册路由
6. 更新 `docs/API.md`

## 约定
- 统一返回格式见 `backend/AGENTS.md`
- 错误用 errcode 常量，不写裸字符串
```

**用法**：

```
你：参考 @.agents/skills/beego-api 帮我写一个用户查询接口
AI：[按 Beego 规范生成，不会用 Gin 的写法]
```

**与 AGENTS.md 的区别**：

- `AGENTS.md` = 这个项目的**事实**（每次都要知道）；
- `skills/` = 可复用的**流程**（需要时才加载）。

把 skills 复制到任意项目即可复用，不绑定业务。

---

## 五、`CLAUDE.md` 与 `AGENTS.md` 的分工（2026 版）

| 对比项 | `AGENTS.md` | `CLAUDE.md` |
|--------|-------------|-------------|
| 适用工具 | Codex、Cursor、Copilot、Claude Code 等 | Claude Code |
| 多文件 | ✅ 每个模块一个，就近优先 | ✅ 每个目录一个，层级合并 |
| 跟模块移动 | ✅ | ✅ |
| 推荐场景 | 所有团队 | 以 Claude Code 为主，或有 Claude 专属约定 |

**最佳实践**：根目录写 `AGENTS.md`；`CLAUDE.md` 用 `@AGENTS.md` 导入，只补 Claude 专属内容。这样一份事实只维护一次。

---

## 六、复用这个模板的方法

```bash
git clone https://github.com/dmmgogogo/backend-front-template my-new-project
cd my-new-project

# 按需删除不需要的模块
rm -rf frontend/flutter      # 不需要 App
rm -rf frontend/vben-admin   # 不需要管理后台

# 更新 AGENTS.md 与各模块 AGENTS.md 里的项目特定信息
```

### 升级 checklist（从 2026-03 模板迁到 2026-11 标准）

- [ ] 在根目录创建 `AGENTS.md`，把 `CLAUDE.md` 里的通用事实搬过去
- [ ] 每个模块加 `AGENTS.md`，原 `CLAUDE.md` 改为 `@AGENTS.md` + 专属补充
- [ ] 通用技能迁到 `.agents/skills/`，Claude 专属技能放 `.claude/skills/`
- [ ] 把"按文件类型生效"的规范拆到 `.claude/rules/`（带 `paths`）
- [ ] 添加 `.mcp.json`（GitHub/数据库等团队工具），密钥走环境变量
- [ ] 用 `/init` 或手工生成一次，跑 `/doctor prompt-audit` 检查冲突
- [ ] 让 Cursor 和 Claude Code 各跑一个真实任务，确认规则生效
- [ ] 删除重复/过时的旧规则文件

---

## 七、这个案例值得抄的 5 个点

1. **模块级规范文件**：换模块就换规范，不用在大文件里找。
2. **技能与业务分离**：skills 可跨项目复用。
3. **根 + 模块两层结构**：根写整体，模块写细节。
4. **明确"新增功能标准步骤"**：AI 每次按同一路径走，输出稳定。
5. **把"不要动的地方"写清楚**：减少误改。

## 八、2026 年还需要补的 3 个点

1. **MCP 项目配置**：把团队常用工具（GitHub、数据库、监控）写进 `.mcp.json`。
2. **Skills 标准化**：统一 `SKILL.md` 格式，标注 owner 与触发词。
3. **规则治理**：定期审查冲突与过时规则，避免"规则越写越多、AI 越来越懵"。

---

## 历史沿革

- **2026-03**：初版全栈项目模板（`.cursorrules` + `AI-CONTEXT.md` + MCP 配置）。
- **2026-04**：全站统一为 `.cursor/rules/*.mdc`，模板同步。
- **2026-11**：本页改为"参考模板 + 迁移 checklist"，指向 AGENTS.md / CLAUDE.md / Skills / MCP 的新写法；原模板仓库最后更新于 2026-03，未声称已升级。

---

## 九、下一步

- 直接 fork：[backend-front-template](https://github.com/dmmgogogo/backend-front-template)
- [⭐️ M6-01 AI 项目配置：从 .cursorrules 到 AGENTS.md](./01-cursorrules.md)
- [⭐️ M6-02 给 AI 喂上下文：项目文档规范](./02-ai-context.md)
- [M6-03 MCP 项目集成](./03-mcp-integration.md)
