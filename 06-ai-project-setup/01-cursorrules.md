# ⭐️ M6-01 · .cursorrules 配置指南

> `.cursorrules` 是放在项目根目录的文件，Cursor 每次生成代码前都会读它。写好这个文件，AI 就知道你的项目是什么、规范是什么，不用每次重复说。

---

## 为什么要配 .cursorrules？

没有 .cursorrules 时，AI 每次都在"猜"你的项目：
- 不知道你用 Vue 2 还是 Vue 3
- 不知道你的 UniApp 是编译到小程序还是 H5
- 不知道你的 Flutter 用哪个状态管理
- 不知道团队的命名规范

**有了 .cursorrules，AI 一进项目就了解全貌，输出直接符合规范。**

---

## Vue 项目 .cursorrules 模板

```markdown
# 项目说明
这是一个 Vue 3 项目，使用 Composition API（不用 Options API）。
状态管理使用 Pinia，路由使用 Vue Router 4。
UI 组件库：Element Plus。
请求封装在 src/api/ 目录，统一使用 axios。

# 代码规范
- 组件文件名使用 PascalCase，如 UserProfile.vue
- 变量和函数使用 camelCase
- 常量使用 UPPER_SNAKE_CASE
- 接口类型定义放在 src/types/ 目录

# 重要约定
- 所有异步操作必须有错误处理
- 禁止在组件内直接调用 API，必须通过 src/api/ 封装
- 新增页面需同时更新路由配置

# 回答风格
- 直接给代码，不需要解释基础概念
- 代码示例使用 TypeScript
- 如果有多种实现方式，优先推荐最简洁的
```

---

## UniApp 项目 .cursorrules 模板

```markdown
# 项目说明
这是一个 UniApp 项目，主要编译目标：微信小程序 + H5。
使用 Vue 3 + setup 语法糖。
UI 组件库：uni-ui。
网络请求统一封装，使用 uni.request 而非 axios（小程序不支持）。

# 平台差异处理
- 涉及平台差异的代码必须用条件编译：
  #ifdef MP-WEIXIN ... #endif
- 不要使用 DOM 操作，小程序不支持
- 图片、文件路径处理需考虑小程序和 H5 的差异

# 代码规范
- 页面文件放在 pages/ 目录，组件放在 components/
- 全局状态使用 Pinia
- 避免使用小程序不支持的 CSS 选择器（如 * 通配符）

# 回答风格
- 涉及 API 时，优先使用 uni.xxx 而不是 web 原生 API
- 给出代码时标注哪些是小程序专有、哪些是通用的
```

---

## Flutter 项目 .cursorrules 模板

```markdown
# 项目说明
这是一个 Flutter 项目，目标平台：iOS + Android。
Dart 版本：3.x，使用 null safety。
状态管理：Riverpod（不用 Provider 或 GetX）。
网络请求：Dio。
路由：GoRouter。

# 代码规范
- Widget 文件名使用 snake_case，如 user_profile.dart
- 类名使用 PascalCase
- 私有变量和方法以下划线开头，如 _userName
- 每个页面对应独立文件，放在 lib/pages/ 目录
- 复用组件放在 lib/widgets/ 目录

# 重要约定
- 禁止在 UI 层直接写业务逻辑
- 异步操作使用 async/await，不用 .then() 链式调用
- 所有颜色、字体大小定义在 lib/theme/ 中，不要写魔法数字

# 回答风格
- 直接给完整可运行的代码
- 如果涉及第三方包，注明包名和版本
- 遇到平台差异问题，同时给出 iOS 和 Android 的处理方式
```

---

## Golang 后端项目 .cursorrules 模板

```markdown
# 项目说明
这是一个 Golang 后端项目，Go 版本 1.21+。
Web 框架：Gin。
ORM：GORM，数据库 MySQL。
配置管理：Viper。
日志：Zap。

# 项目结构
cmd/          # 程序入口
internal/
├── handler/  # HTTP 处理器（接收请求、参数校验、调用 service）
├── service/  # 业务逻辑层
├── repo/     # 数据库操作层
└── model/    # 数据结构定义
pkg/          # 可复用的公共库

# 代码规范
- 严格遵循分层架构：handler → service → repo，禁止跨层调用
- 错误处理：所有错误必须向上传递，不要在中间层直接 log 后丢弃
- 接口统一返回格式：{"code": 0, "msg": "ok", "data": {...}}
- 数据库操作禁止在 handler 层直接写，必须通过 repo 封装
- 所有对外接口必须有入参校验（使用 binding tag）

# 重要约定
- 新增接口需同时更新路由注册（router.go）
- 数据库字段变更需要写对应的 migration 文件
- 禁止在代码里硬编码配置（IP、密码、密钥），统一走配置文件

# 回答风格
- 直接给完整可运行的代码
- 遇到并发场景，主动提示是否需要加锁
- 错误信息用英文，日志信息可以用中文
```

---

## 通用补充规则（所有项目都加）

在每个模板末尾加上这段，效果很好：

```markdown
# AI 协作约定
- 我的问题如果不清晰，先问我再动手
- 修改已有代码时，只改必要部分，不要重构无关代码
- 不要自作主张引入新的依赖包，引入前先告诉我
- 给出的代码必须和项目现有风格保持一致
```

---

## 如何在团队中共享 .cursorrules

1. 把 `.cursorrules` 提交到 Git 仓库（不要加入 .gitignore）
2. 团队所有人 clone 后自动生效
3. 项目规范变更时，同步更新这个文件
4. 建议在 README 里说明"本项目已配置 .cursorrules，请使用 Cursor 开发"

---

## 下一步

- [⭐️ M6-02 给 AI 喂上下文：项目文档规范](./02-ai-context.md)
- [M6-03 MCP 项目集成](./03-mcp-integration.md)
