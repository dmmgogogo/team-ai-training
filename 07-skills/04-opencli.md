# ⭐️ M7-04 · OpenCLI：将网站转换为 CLI 工具

> OpenCLI 是一个强大的工具，可以将任意网站转换为命令行工具，支持 AI 辅助的 API 发现和适配器生成。无需存储凭证，直接复用浏览器登录状态。

---

## 什么是 OpenCLI

**OpenCLI** 是由 [jackwener](https://github.com/jackwener) 开发的开源项目，通过 AI 和浏览器自动化技术，将网站转换为命令行工具。它支持 19+ 个主流网站，提供 80+ 个命令，让开发者可以在终端中直接操作网站功能。

**GitHub**: [https://github.com/jackwener/opencli](https://github.com/jackwener/opencli)  
**npm 包**: `@jackwener/opencli` (2.6K+ 周下载量)

---

## 核心特性

### 1. 多网站支持

支持 19+ 个主流网站，包括：
- **社交媒体**: Twitter/X、Reddit、Bilibili、小红书
- **知识社区**: 知乎、YouTube
- **开发平台**: GitHub、GitLab
- 更多网站持续增加中...

### 2. 零风险凭证管理

- **复用浏览器登录状态**：通过 Chrome Extension 复用已登录的浏览器会话
- **无需存储凭证**：不保存任何密码或 token，安全性极高
- **自动发现配置**：`opencli setup` 自动发现所需 token

### 3. AI 驱动的功能

- **`explore` 命令**：自动发现网站的 API 接口
- **`synthesize` 命令**：自动生成适配器代码
- **`cascade` 命令**：检测网站的认证策略

### 4. 自愈式配置

- **`opencli doctor`**：诊断 10+ 种工具配置问题
- **`opencli doctor --fix`**：一键修复常见配置问题
- **动态加载**：支持声明式 `.yaml` 或自定义 `.ts` 适配器

---

## 安装与配置

### 前置要求

- Node.js >= 18.0.0
- Chrome 浏览器（已登录目标网站）

### 安装方式

**方式一：npm 全局安装**
```bash
npm install -g @jackwener/opencli
```

**方式二：从源码安装**
```bash
git clone https://github.com/jackwener/opencli.git
cd opencli
npm install
npm link
```

### 初始化配置

```bash
# 自动发现并配置所需 token
opencli setup

# 诊断配置问题
opencli doctor

# 一键修复配置
opencli doctor --fix
```

---

## 使用示例

### 基础命令

```bash
# 查看所有可用命令
opencli --help

# 查看支持的网站列表
opencli list

# 使用特定网站的命令
opencli bilibili <command>
opencli twitter <command>
opencli zhihu <command>
```

### 实际场景

**1. Bilibili 操作**
```bash
# 搜索视频
opencli bilibili search "AI 大模型"

# 获取视频信息
opencli bilibili video <video_id>

# 查看用户信息
opencli bilibili user <user_id>
```

**2. Twitter/X 操作**
```bash
# 发布推文
opencli twitter post "Hello from CLI!"

# 查看时间线
opencli twitter timeline

# 搜索推文
opencli twitter search "AI"
```

**3. 知乎操作**
```bash
# 搜索问题
opencli zhihu search "如何学习 AI"

# 获取回答
opencli zhihu answer <answer_id>
```

---

## AI 辅助功能

### 自动发现 API

```bash
# 探索网站的 API 接口
opencli explore <website_url>

# 示例：探索 Bilibili 的 API
opencli explore https://www.bilibili.com
```

### 生成适配器

```bash
# 基于发现的 API 生成适配器
opencli synthesize <website_name>

# 生成后会自动注册到 clis/ 目录
```

### 检测认证策略

```bash
# 检测网站的认证方式
opencli cascade <website_url>
```

---

## 自定义适配器

### 方式一：YAML 声明式配置

在 `clis/` 目录创建 `.yaml` 文件：

```yaml
name: my-site
description: 我的网站 CLI
baseUrl: https://api.example.com
commands:
  - name: search
    description: 搜索内容
    method: GET
    path: /search
    params:
      - name: q
        type: string
        required: true
```

### 方式二：TypeScript 自定义适配器

在 `clis/` 目录创建 `.ts` 文件：

```typescript
import { CLI } from '@jackwener/opencli';

export default {
  name: 'my-site',
  commands: {
    search: async (args) => {
      // 自定义实现
      return await fetch(`https://api.example.com/search?q=${args.q}`);
    }
  }
} as CLI;
```

适配器会自动注册，无需手动配置。

---

## 最佳实践

### 1. 安全使用

- ✅ 使用浏览器已登录的会话，避免在 CLI 中存储凭证
- ✅ 定期运行 `opencli doctor` 检查配置安全
- ✅ 不要在脚本中硬编码敏感信息

### 2. 批量操作

```bash
# 结合 shell 脚本批量处理
for video_id in $(cat video_ids.txt); do
  opencli bilibili video $video_id >> results.json
done
```

### 3. 集成到工作流

```bash
# 在 CI/CD 中使用
opencli github issue create \
  --title "自动创建 Issue" \
  --body "$(cat issue_template.md)"
```

### 4. 自定义命令别名

在 `~/.bashrc` 或 `~/.zshrc` 中添加：

```bash
alias bili="opencli bilibili"
alias tw="opencli twitter"
alias zh="opencli zhihu"
```

---

## 常见问题

### Q: 如何添加新网站支持？

A: 有两种方式：
1. 使用 `opencli explore` 自动发现 API
2. 在 `clis/` 目录手动创建适配器文件

### Q: 支持哪些认证方式？

A: 支持 Cookie、Token、OAuth 等多种方式，通过浏览器扩展自动处理。

### Q: 如何调试命令？

A: 使用 `--verbose` 或 `--debug` 参数查看详细日志：

```bash
opencli bilibili search "test" --verbose
```

### Q: 配置丢失怎么办？

A: 运行 `opencli setup` 重新配置，或使用 `opencli doctor --fix` 自动修复。

---

## 相关资源

- **GitHub 仓库**: [https://github.com/jackwener/opencli](https://github.com/jackwener/opencli)
- **npm 包**: [@jackwener/opencli](https://www.npmjs.com/package/@jackwener/opencli)
- **OpenCLI 规范**: [https://opencli.org/](https://opencli.org/)（参考规范文档）

---

## 适用场景

| 场景 | 说明 |
|------|------|
| **批量内容管理** | 批量发布、编辑、删除内容 |
| **数据采集** | 自动化采集网站数据 |
| **工作流集成** | 集成到 CI/CD 或自动化脚本 |
| **API 探索** | 快速了解网站的 API 结构 |
| **开发测试** | 快速测试网站功能 |

---

*← 返回 [M7 Skills 精选](./README.md) | [课程总览](../README.md)*
