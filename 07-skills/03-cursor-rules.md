# ⭐️ M7-03 · Cursor 规则与技能社区精选

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 社区里的规则模板依然好用，但 2026 年的玩法变了：Cursor 同时支持 **Rules（`.mdc`）**、**AGENTS.md**、**Skills** 和 **Plugins**，还提供了把动态规则/斜杠命令转成 Skills 的迁移能力。抄模板之前，先想清楚它该以哪种形态存在。

---

## 一、2026-11 的 Cursor 配置全景

| 机制 | 位置 | 适合 |
|------|------|------|
| **Project Rules** | `.cursor/rules/*.mdc` | 按 glob / 描述 / 手动触发的条件规则 |
| **AGENTS.md** | 仓库根目录（可嵌套） | 跨工具的项目事实 |
| **Agent Skills** | `.agents/skills/`、`.cursor/skills/` | 多步骤流程，按需加载 |
| **Plugins** | Customize → Plugins / Cursor Marketplace | 团队分发 |
| **MCP** | `mcp.json` / Customize → MCP | 连接外部工具 |
| **User / Team Rules** | 设置 / 团队后台 | 个人与团队级规则 |

> 普通 `.md` 放在 `.cursor/rules/` 会被忽略（没有 frontmatter）；要纯 Markdown 就用 `AGENTS.md`。内置的 `/migrate-to-skills` 可以把部分动态规则和斜杠命令转成 Agent Skills（来源：[Cursor Rules 文档](https://cursor.com/docs/rules)、[Cursor Agent Skills](https://cursor.com/docs/skills)，2026-11）。

---

## 二、社区入口（2026-11）

| 入口 | 说明 |
|------|------|
| [cursor.directory](https://cursor.directory) | Cursor 官方文档推荐的社区目录（规则 + MCP），可按语言/框架筛选 |
| [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | GitHub 精选列表，已更新为 "Cursor Project Rules" 术语 |
| [Cursor Marketplace](https://cursor.com/marketplace) | 官方插件与 MCP 市场，可一键安装 |
| Cursor 内置 Skills | `/create-rule`、`/create-skill`、`/review` 等，可在 `/` 菜单直接调用 |

> 社区站点偶尔会有访问限制或改版，链接以官方文档指向为准。

---

## 三、如何使用社区模板

1. 在社区找到对应技术栈的模板；
2. 判断形态：
   - 若是"项目事实"（技术栈、命令、目录）→ 合并进 `AGENTS.md`；
   - 若是"按文件生效的规范"→ 放进 `.cursor/rules/*.mdc`；
   - 若是"多步骤流程"→ 写成 `SKILL.md`；
3. 按项目实际情况修改（框架版本、命名规范）；
4. 提交到 Git，团队共享；
5. 用真实任务验证一次。

> 不要把模板原样粘贴：社区模板往往假设了特定版本或目录结构，直接套用会产生"规则和代码对不上"的错觉。

---

## 四、精选规则模板

以下模板可以写成 `.mdc`（带 frontmatter），也可以作为章节放进 `AGENTS.md`。

### Go 后端

```markdown
You are an expert in Go and RESTful API design.

## Code Style
- 变量/函数 camelCase，导出函数写注释
- 遵循标准布局：cmd/、internal/、pkg/

## Architecture
- 严格分层：handler → service → repository
- handler 不得直接调用 repository
- 错误必须向上传递，禁止静默丢弃
- 结构化日志（zap），禁止 fmt.Println

## API
- 统一响应：{"code": int, "msg": string, "data": any}
- 所有输入必须校验
- 请求级数据用 context 传递（user_id、trace_id）

## Security
- 不记录敏感数据（密码、token）
- SQL 必须参数化，禁止字符串拼接
- JWT 校验放中间件，不放业务逻辑
```

### Flutter

```markdown
You are an expert Flutter developer using Dart with null safety.

## Architecture
- feature-first：lib/features/<feature>/{data,models,providers,pages}
- 状态管理 Riverpod，路由 GoRouter

## Code Rules
- 日志统一走 AppLogger，禁止 print/debugPrint
- 异步操作 > 300ms 必须显示 loading 并禁用按钮
- 处理 loading / error / empty / data 四种状态
- 图片必须有加载失败占位

## API
- 只调用 /api/backend/* 与 /api/common/*
- 401 → 清 token → 跳登录
```

### Vue 3

```markdown
You are an expert Vue 3 developer with TypeScript and Composition API.

## Rules
- 使用 <script setup>，禁止 Options API
- 状态管理 Pinia，路由 Vue Router 4
- 组件 PascalCase，页面 kebab-case
- 所有 props / emits 定义 TypeScript 类型

## API
- 所有请求走 src/api/，组件内禁止直接调 axios
- 每个异步操作处理 loading / error / success

## Performance
- 大列表用 v-memo
- 路由懒加载
- 大对象用 shallowRef
```

### UniApp

```markdown
You are an expert UniApp developer targeting WeChat Mini Programs and H5.

## Platform Rules
- 主目标：微信小程序
- 平台差异用条件编译：#ifdef MP-WEIXIN ... #endif
- 禁止 DOM API，使用 uni.xxx
- 主包 < 2MB，大功能用分包

## Code Style
- Vue 3 Composition API + <script setup>
- 全局状态用 Pinia（不用 globalData）
- 避免小程序不支持的 CSS 选择器
```

---

## 五、通用规则（所有项目追加）

```markdown
## AI Collaboration
- 需求不清晰时先提问，不要猜
- 修改只改必要部分，不重构无关代码
- 引入新依赖前先说明
- 生成代码与现有项目风格保持一致
- 安全敏感代码（认证、支付）加风险提示
```

> 这套规则现在更适合放在 `AGENTS.md` 的「协作约定」里，而不是每个 `.mdc` 重复一遍。

---

## 六、怎么挑模板：5 条判断标准

1. **只看与当前版本匹配的模板**：框架大版本不同，规则可能误导。
2. **有具体约束的优先**：写"禁止 X、必须 Y"的比"注意质量"有用。
3. **规则数量控制**：常驻规则越多，遵守率越低。
4. **看是否可验证**：能不能用一条命令/一次 review 检验。
5. **看来源与更新**：优先官方或活跃维护的社区列表。

---

## 七、安全提醒

- 规则文件本身风险低，但**插件和带脚本的 Skill 风险高**：安装前阅读内容。
- 不要从来源不明的仓库复制含 shell 命令的规则（例如要求执行远端脚本）。
- 团队规则进 Git 走 PR，重要变更需 review。

---

## 八、历史沿革

| 时间 | 事件 |
|------|------|
| 2023 | `.cursorrules` 单文件出现，社区模板开始流行 |
| 2024–2025 | `.cursor/rules/*.mdc` 成为官方推荐；cursor.directory、awesome-cursorrules 壮大 |
| 2025-08 | AGENTS.md 开放格式发布，Cursor 支持其作为简化替代 |
| 2026 | Cursor 引入 Agent Skills、Plugins、Subagents；`/migrate-to-skills` 支持把动态规则转成 Skills |
| 2026-11 | 推荐组合：AGENTS.md（事实）+ `.cursor/rules/*.mdc`（条件规则）+ Skills（流程） |

---

## 九、下一步

- [M8 MCP 精选大全](../08-mcp/01-dev-tools.md)
- [⭐️ M6-01 AI 项目配置：从 .cursorrules 到 AGENTS.md](../06-ai-project-setup/01-cursorrules.md)
- [⭐️ M6-04 真实案例：全栈项目 AI 配置实战](../06-ai-project-setup/04-real-world-template.md)
