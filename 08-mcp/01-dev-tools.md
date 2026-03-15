# ⭐️ M8-01 · 开发工具类 MCP

> 开发者最高频使用的 MCP Server，直接连接代码仓库、容器、CI/CD。

---

## GitHub MCP ⭐ 必装

**功能：** AI 直接操作 GitHub 仓库

```json
{
  "github": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "env": {
      "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token"
    }
  }
}
```

**能做什么：**
- 查看 Issues、PR、commit 记录
- 搜索代码、文件
- 创建 Issue、评论 PR
- 查看仓库结构

**典型用法：**
```
你：帮我看一下 #42 这个 Issue，给出修复方案
AI：[直接读取 Issue 内容，给出完整修复代码]

你：最近 3 次 commit 改了什么，有没有引入新 bug 的风险？
AI：[分析 commit diff，给出风险评估]
```

---

## GitLab MCP

**功能：** 企业版 GitLab 用户专属，支持 OAuth 2.0

```json
{
  "gitlab": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-gitlab"],
    "env": {
      "GITLAB_PERSONAL_ACCESS_TOKEN": "your_token",
      "GITLAB_API_URL": "https://gitlab.your-company.com/api/v4"
    }
  }
}
```

**vs GitHub MCP：**
- 支持自托管 GitLab 实例
- CI/CD Pipeline 检查
- 适合使用 GitLab 的企业团队

---

## Docker MCP

**功能：** AI 直接管理 Docker 容器和镜像

```json
{
  "docker": {
    "command": "npx",
    "args": ["-y", "@docker/mcp-server"]
  }
}
```

**能做什么：**
- 查看运行中的容器状态
- 查看容器日志
- 构建镜像
- 帮你生成 Dockerfile

**典型用法：**
```
你：线上 API 服务崩了，帮我看一下日志
AI：[直接读取容器日志，分析错误原因]

你：帮我写这个 Go 项目的 Dockerfile
AI：[根据项目结构生成优化的多阶段 Dockerfile]
```

---

## Playwright MCP ⭐ 强推

**功能：** AI 控制真实浏览器，调试前端 Bug

```json
{
  "playwright": {
    "command": "npx",
    "args": ["-y", "@executeautomation/playwright-mcp-server"]
  }
}
```

**能做什么：**
- 截图当前页面，AI 直接看到 UI
- 读取 console 报错
- 模拟用户操作（点击、输入、提交）
- 自动生成 E2E 测试用例

**典型用法（Vue/Flutter Web）：**
```
你：我的登录页面样式乱了，帮我看一下
AI：[截图页面，分析 CSS 问题，给出修复方案]

你：帮我测试一下购物车流程是否正常
AI：[模拟操作，发现问题，生成测试报告]
```

---

## Desktop Commander MCP

**功能：** AI 执行本地终端命令

```json
{
  "desktop-commander": {
    "command": "npx",
    "args": ["-y", "@wonderwhy-er/desktop-commander"]
  }
}
```

**能做什么：**
- 执行 shell 命令
- 读写本地文件
- 启动/停止进程

⚠️ **安全提示：** 此 MCP 权限较大，只在可信环境使用

---

## Filesystem MCP ⭐ 必装

**功能：** AI 读写本地文件，是最基础的 MCP

```json
{
  "filesystem": {
    "command": "npx",
    "args": [
      "-y",
      "@modelcontextprotocol/server-filesystem",
      "/Users/你的用户名/Projects"
    ]
  }
}
```

**说明：** 路径参数限制 AI 只能访问指定目录，保证安全。

---

## 下一步

- [⭐️ M8-02 数据库类 MCP](./02-database.md)
- [M8-03 效率工具类 MCP](./03-productivity.md)
