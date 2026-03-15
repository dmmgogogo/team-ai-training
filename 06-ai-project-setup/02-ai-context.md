# ⭐️ M6-02 · 给 AI 喂上下文：项目文档规范

> AI 对你项目的了解程度，直接决定它输出的质量。这篇讲怎么用文档让 AI 第一次进项目就能快速上手，不乱写、不走弯路。

---

## AI 读项目的方式

当你在 Cursor 里问问题，AI 会读：

```
1. .cursorrules       ← 项目规范（上一篇讲的）
2. 你引用的文件       ← @文件名 直接引用
3. 你的问题上下文     ← 对话历史
4. 自动索引的代码     ← Cursor 自动扫描项目
```

**问题：** 自动扫描的代码量有限，复杂项目 AI 经常"找不到"关键信息。

**解法：** 主动写一个给 AI 看的文档，放在项目里，需要时 `@` 引用。

---

## 推荐创建：AI-CONTEXT.md

在项目根目录创建 `AI-CONTEXT.md`，专门给 AI 看。内容模板：

```markdown
# 项目 AI 上下文文档

## 项目概述
[一句话说清楚这个项目是什么，做什么的]

## 技术栈
- 前端：Vue 3 + TypeScript + Element Plus
- 状态管理：Pinia
- 构建：Vite
- 接口：RESTful API，基地址 /api/v1

## 目录结构
src/
├── api/          # 所有接口封装（按模块分文件）
├── components/   # 公共组件
├── pages/        # 页面
├── stores/       # Pinia store
├── types/        # TypeScript 类型定义
└── utils/        # 工具函数

## 核心业务模块
- 用户模块：登录/注册/权限，见 src/pages/auth/
- 订单模块：下单/支付/查询，见 src/pages/order/
- [按实际项目补充]

## 重要约定
- 新增接口必须在 src/api/ 下创建对应文件
- 所有表单提交前必须做前端校验
- 错误码统一处理逻辑在 src/utils/errorHandler.ts

## 不要碰的地方
- src/legacy/ 是旧代码，不要修改
- 不要改 vite.config.ts，有特殊配置
```

**使用方式：**
```
你：@AI-CONTEXT.md 帮我在订单模块新增一个退款申请页面
AI：[基于完整上下文，直接给出符合项目规范的代码]
```

---

## Flutter / UniApp 项目的 AI-CONTEXT.md 补充

### Flutter 额外要写的

```markdown
## Flutter 特别说明
- 最低支持版本：iOS 13 / Android 6.0
- 所有网络图片必须处理加载失败的占位图
- 页面间传参使用 GoRouter 的 extra 参数
- 本地存储使用 SharedPreferences（不用 Hive）

## 常用 Widget 位置
- 自定义按钮：lib/widgets/custom_button.dart
- 加载动画：lib/widgets/loading_overlay.dart
- 统一错误提示：lib/utils/toast_util.dart
```

### UniApp 额外要写的

```markdown
## UniApp 特别说明
- 主要目标平台：微信小程序
- 分包配置在 pages.json，主包 < 2MB
- 全局数据通过 Pinia 管理，不用 globalData
- 小程序审核敏感词列表在 docs/sensitive-words.txt

## 常用工具位置
- 请求封装：utils/request.js
- 权限检查：utils/permission.js
- 图片上传：utils/upload.js
```

---

## README.md 要让 AI 能看懂

很多项目的 README 只写给人看，AI 读了一头雾水。加一个"AI 快速上手"章节：

```markdown
## AI 开发快速上手

本项目已配置 AI 协作文档：
- `.cursorrules` — 代码规范，Cursor 自动读取
- `AI-CONTEXT.md` — 项目架构说明，问复杂问题时用 @AI-CONTEXT.md 引用

常用 AI 操作：
- 新增功能：`@AI-CONTEXT.md 帮我实现 [功能描述]`
- 定位代码：`@AI-CONTEXT.md 我要修改 [模块名]，相关文件在哪`
- 代码审查：`@[文件名] 帮我 review 这段代码，注意项目规范`
```

---

## 使用 Claude Projects 管理项目上下文

如果用 Claude（非 Cursor）开发：

1. 新建一个 **Claude Project**，命名为项目名
2. 上传以下文件到知识库：
   - `AI-CONTEXT.md`
   - 核心模块的类型定义文件
   - 接口文档（如有）
3. 在 Project 指令中写：
   ```
   你是这个项目的开发助手。
   每次回答前先查阅上传的项目文档，确保代码符合项目规范。
   不确定的地方先问我，不要猜。
   ```

**效果：** 该 Project 下的所有对话都自动带上项目上下文，不用每次重新解释。

---

## 下一步

- [M6-03 MCP 项目集成](./03-mcp-integration.md)
- [⭐️ M6-01 .cursorrules 配置指南](./01-cursorrules.md)
