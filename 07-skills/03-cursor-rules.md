# ⭐️ M7-03 · Cursor Rules 社区精选

> 社区整理的高质量 `.cursorrules` 模板，按技术栈分类。直接复制，按项目微调即可。
> 资源网站：[cursor.directory](https://cursor.directory) | [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules)

---

## 如何使用

1. 在项目 `.cursor/rules/` 目录下创建 `.mdc` 文件（如 `project.mdc`）
2. 粘贴对应模板内容（规则正文部分）
3. 按项目实际情况修改（框架版本、命名规范等）
4. 提交到 Git，团队共享

> 旧版 `.cursorrules`（根目录单文件）仍可使用，但新项目推荐用 `.cursor/rules/*.mdc` 格式，支持多文件和条件触发。详见 [M6-01](../06-ai-project-setup/01-cursorrules.md)。

---

## Go 后端精选规则

```markdown
You are an expert in Go, Gin/Beego framework, and RESTful API design.

## Code Style
- Use meaningful variable names in camelCase
- Write concise comments for exported functions
- Follow standard Go project layout: cmd/, internal/, pkg/

## Architecture Rules
- Strict layering: handler → service → repository
- Never call repository directly from handler
- All errors must be propagated upward, never silently dropped
- Use structured logging (zap), never fmt.Println

## API Conventions
- Uniform response: {"code": int, "msg": string, "data": any}
- All user input must be validated before processing
- Use context for request-scoped values (user_id, trace_id)

## Security
- Never log sensitive data (passwords, tokens)
- Always use parameterized queries, never string concatenation for SQL
- JWT validation in middleware, not in business logic

## When Writing Code
- Show complete, runnable code snippets
- Include error handling for every operation
- Suggest tests for complex logic
```

---

## Flutter 精选规则

```markdown
You are an expert Flutter developer using Dart with null safety.

## Architecture
- Feature-first folder structure: lib/features/<feature>/{data,models,providers,pages}
- Use Riverpod for state management (not Provider or GetX)
- Use GoRouter for navigation

## Code Rules
- All log calls through AppLogger, never use print/debugPrint
- Any async operation >300ms must show loading UI with buttons disabled
- Handle all error states (loading / error / empty / data)
- Images must have error placeholder and loading placeholder

## Naming
- Files: snake_case (user_profile.dart)
- Classes: PascalCase
- Private members: _prefixed

## API
- Only call /api/backend/* and /api/common/*
- All network calls through the Dio-based http_client
- Handle 401 → clear token → redirect to login

## When Writing Code
- Always include null safety (? and ! operators correctly)
- For UI code, provide complete Widget implementations
- Mention which packages are needed with version
```

---

## Vue 3 精选规则

```markdown
You are an expert Vue 3 developer with TypeScript and Composition API.

## Rules
- Always use Composition API with <script setup> syntax
- Never use Options API
- Use Pinia for state management (not Vuex)
- Use Vue Router 4 for routing

## Code Style
- Component names: PascalCase
- File names: PascalCase for components, kebab-case for pages
- Use TypeScript, define interfaces for all props and emits
- Extract reusable logic into composables (use*)

## API Calls
- All API calls go through src/api/ directory
- Never call axios directly in components
- Handle loading / error / success states for every async operation

## Performance
- Use v-memo for expensive list items
- Lazy-load routes with defineAsyncComponent
- Use shallowRef for large non-reactive objects

## When Writing Code
- Provide complete SFC (Single File Component) examples
- Include TypeScript types for all props
```

---

## UniApp 精选规则

```markdown
You are an expert UniApp developer targeting WeChat Mini Programs and H5.

## Platform Rules
- Primary target: WeChat Mini Program
- Use conditional compilation for platform differences:
  #ifdef MP-WEIXIN ... #endif
- Never use DOM APIs (not available in mini programs)
- Use uni.xxx APIs instead of web native APIs

## Code Style
- Use Vue 3 Composition API with <script setup>
- Pages in pages/ directory, components in components/
- Global state via Pinia (not globalData)

## Restrictions
- Main package must be < 2MB (use sub-packages for large features)
- Avoid CSS selectors not supported by mini programs (* selector, etc.)
- Images must use relative paths or CDN URLs

## When Writing Code
- Mark which APIs are mini-program specific vs universal
- Provide fallback for H5 when using wx-specific APIs
```

---

## 通用规则（所有项目追加）

```markdown
## AI Collaboration Rules
- If my request is unclear, ask first before writing code
- When modifying existing code, change only what's necessary
- Don't introduce new dependencies without asking me first
- Keep generated code consistent with existing project style
- For security-sensitive code (auth, payments), add a warning comment
```

---

## 快速找规则的网站

| 网站 | 说明 |
|------|------|
| [cursor.directory](https://cursor.directory) | 最大的 cursorrules 集合，按语言/框架分类 |
| [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | GitHub 精选列表，持续更新 |
| [cursor.sh/docs](https://docs.cursor.com/context/rules-for-ai) | 官方文档，最新语法说明 |

---

## 下一步

- [M8 MCP 精选大全](../08-mcp/01-dev-tools.md)
- [⭐️ M6-04 真实案例：全栈项目 AI 配置实战](../06-ai-project-setup/04-real-world-template.md)
