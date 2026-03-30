# ⭐️ M6-04 · 真实案例：全栈项目 AI 配置实战

> 理论看完，来看真实项目怎么做的。
> 模板仓库：[backend-front-template](https://github.com/dmmgogogo/backend-front-template)
>
> 技术栈：Go (Beego) 后端 + Flutter App + Vue3 (Vben Admin) 管理后台

---

## 这个模板的 AI 配置思路

### 核心设计：模块独立 + 技能复用

```
project-root/
├── AGENTS.md                    # 整体项目说明（给 WARP/Codex 读）
├── .claude/                     # 通用 AI 技能库
│   ├── README.md                # Agent vs Skills 使用指南
│   ├── SKILL.md                 # 技能索引
│   └── skills/                  # 可复用技能（beego-api/mysql/redis）
│
├── backend/
│   └── CLAUDE.md                # 后端专属 AI 规范（跟着后端模块走）
│
├── frontend/flutter/
│   └── CLAUDE.md                # Flutter 专属 AI 规范
│
└── frontend/vben-admin/
    └── CLAUDE.md                # Vben Admin 专属 AI 规范
```

**核心原则：每个模块携带自己的 AI 规范文件，复制模块时规范跟着走。**

---

## 不同 AI 工具读不同文件

| AI 工具 | 读取的文件 | 说明 |
|---------|-----------|------|
| **Claude Code（命令行）** | `CLAUDE.md` | 自动向上查找，读最近的 CLAUDE.md |
| **Cursor** | `.cursor/rules/*.mdc` | 项目 `.cursor/rules/` 目录，推荐新格式（旧 `.cursorrules` 仍兼容） |
| **WARP / Codex** | `AGENTS.md` | 项目整体说明 |
| **ChatGPT / Claude（网页）** | 手动 `@` 引用 | 需要在对话中主动引用 |

**这个模板同时配置了 `AGENTS.md` 和各模块 `CLAUDE.md`，覆盖多种 AI 工具。**

---

## AGENTS.md 写了什么

根目录的 `AGENTS.md` 告诉 AI：

1. **项目整体架构** — 三个模块（backend / flutter / vben-admin），各自独立
2. **每个模块的启动命令** — AI 能直接帮你运行和调试
3. **Request 流程** — HTTP → 中间件 → Controller → Service 的完整链路
4. **API 命名空间** — 管理端 `/api/admin/*`，用户端 `/api/backend/*`
5. **新增功能的标准步骤** — Model → DTO → Controller → Route，AI 每次都会按这个走
6. **指向各模块 CLAUDE.md** — 告诉 AI 去哪里找更详细的规范

> 关键：**AGENTS.md 写整体，CLAUDE.md 写细节。**

---

## 各模块 CLAUDE.md 写了什么

### backend/CLAUDE.md 重点
- 分层架构约定（controller → service → model，禁止跨层）
- 统一返回格式 `{"code": 200, "msg": "...", "data": {}}`
- 错误码定义位置
- 两套 BaseController 的区别（用户端 vs 管理端）
- `c.Error(code)` 调用后会自动 StopRun，不需要 return

### frontend/flutter/CLAUDE.md 重点
- feature-first 目录结构
- 所有日志必须走 `AppLogger`，禁止直接 `print`
- 操作 >300ms 必须显示 loading，并 disable 按钮
- 只调用 `/api/backend/*` 和 `/api/common/*`

### frontend/vben-admin/CLAUDE.md 重点
- 只调用 `/api/admin/*`
- 权限控制：`v-auth` 指令做按钮级控制
- API base url 从 `.env` 读，不硬编码

---

## .claude/skills/ 的设计

`.claude/skills/` 存放**可复用的 AI 技能**，独立于具体业务：

```
.claude/skills/
├── beego-api/    # 如何用 Beego 写 API（框架层知识）
├── mysql/        # MySQL 查询、事务、索引优化技巧
└── redis/        # Redis 缓存、分布式锁、消息队列
```

**用法：**
```
你：参考 @.claude/skills/beego-api 帮我写一个用户查询接口
AI：[按照 Beego 规范生成，不会用 Gin 或其他框架的写法]
```

**与 CLAUDE.md 的区别：**
- `CLAUDE.md` = 这个项目的规范（业务上下文）
- `.claude/skills/` = 通用技术技能（框架/工具用法）

可以把 skills 复制到任意项目使用，不绑定业务。

---

## 复用这个模板的方法

### 新建项目时
```bash
git clone https://github.com/dmmgogogo/backend-front-template my-new-project
cd my-new-project

# 按需删除不需要的模块
rm -rf frontend/flutter    # 不需要 App
# 或
rm -rf frontend/vben-admin # 不需要管理后台

# 更新 AGENTS.md 和各模块 CLAUDE.md 里的项目特定信息
```

### 需要定制的地方
- `AGENTS.md` → 更新项目名称、模块说明
- `backend/CLAUDE.md` → 更新错误码、业务模块列表
- `frontend/flutter/CLAUDE.md` → 更新 App 特有的规范
- `.claude/skills/` → 按需新增技能文件

---

## 对比：.cursorrules vs CLAUDE.md

| 对比项 | `.cursor/rules/*.mdc`（新） / `.cursorrules`（旧兼容） | `CLAUDE.md` |
|--------|------------------------------------------------------|-------------|
| **适用工具** | Cursor | Claude Code (CLI) |
| **支持多文件** | `.mdc` 支持多文件按功能拆分；`.cursorrules` 只有一个 | 每个目录一个，自动层级读取 |
| **跟模块移动** | ❌ 在根目录 | ✅ 随模块走 |
| **推荐场景** | Cursor 为主的团队 | Claude Code 为主的团队 |

**最佳实践：两个都配。** 同一个项目同时有 `.cursor/rules/`（或 `.cursorrules`）和 `CLAUDE.md`，覆盖不同工具。

---

## 下一步

- 直接 fork：[backend-front-template](https://github.com/dmmgogogo/backend-front-template)
- [⭐️ M6-01 .cursorrules 配置指南](./01-cursorrules.md)
- [⭐️ M6-02 给 AI 喂上下文：项目文档规范](./02-ai-context.md)
