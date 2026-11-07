# M10-02 · Cloud Agent 工作原理

> 📅 内容基准：2026-11 ｜ ⏱️ 时效性：高 ｜ 🔁 下次复核：2027-02

> 沙箱、执行循环、凭据隔离、状态管理——它是怎么做到"自主干活"的。**2026 年新增的重点是：环境即配置、凭据不进沙箱、网络出口可管控。**

---

## 一句话结论

Cloud Agent 的工程本质没有变：**隔离环境 + ReAct 循环 + Git 交付**。但 2026 年的产品把它做成了"**环境（environment）**"这个一等公民：仓库、依赖、网络、密钥、启动脚本都固化成一个可复用配置，任务只是在这个环境里跑的一次会话。

---

## 整体架构

```
用户（Web / 手机 / 桌面 / CLI / IM）
  │  任务指令 + 环境选择
  ▼
调度层（Orchestrator）
  │  分配沙箱 / 选择镜像 / 注入环境配置
  ▼
隔离执行环境（云 VM / 容器 / 本地隔离 VM）
  ├─ 仓库（clone 或上传 bundle）
  ├─ 依赖与工具（setup script）
  ├─ Shell / 浏览器 / 测试运行器
  ├─ 网络出口（allowlist / 可关闭）
  └─ 凭据代理（token 不进沙箱）
        │
        ▼
  Agent 执行循环：THINK → ACT → OBSERVE → …
        │
        ▼
  验证（测试 / lint / 构建）
        │
        ▼
  交付：分支 / PR / 文件 / 报告
        │
        ▼
  通知 + 人工 review
```

---

## 第一步：构建环境（environment）

2026-11 的主流产品都要求你先定义环境，而不是"每次从零 clone"：

| 产品 | 环境定义 |
|------|----------|
| Claude Code cloud | Cloud environment：网络访问级别、环境变量、setup script |
| Codex Cloud | Environment：仓库、依赖、网络与密钥、可发布的已保存状态 |
| Copilot in the cloud | Cloud sandbox / GitHub Actions / Remote 三种环境 |
| Cowork | 桌面端本地隔离 VM（按会话） |

**为什么要固化环境？**

- 依赖安装是长任务里最容易被浪费的步骤；缓存/快照能显著缩短启动时间。
- 网络与密钥策略集中管理，避免每个任务各写一套。
- 任务失败可以归因到"环境问题"还是"代码问题"。

**典型 setup：**

```bash
git clone <repo> /workspace && cd /workspace
git checkout -b agent/<task-id>
npm ci            # 或 pip install -r requirements.txt
# 可选：缓存、代码生成、数据库迁移
```

---

## 第二步：任务规划

Agent 拿到任务后先理解全局，再动手：

```
任务："把所有 API 错误处理统一改成 ErrorHandler"

1. 搜索代码库，定位所有 try/except / console.error
2. 列出涉及文件与调用链
3. 读取现有 ErrorHandler 实现
4. 制定修改顺序（从底层到上层）
5. 逐文件修改并验证
```

这个规划由 LLM 驱动，不是硬编码。好的 Cloud Agent 会**先给计划、再执行**；你也可以要求它"先输出计划，等我确认"。

---

## 第三步：执行循环（核心）

```
THINK:   "先看 auth.py 的结构"
ACT:     cat src/auth.py
OBSERVE: [文件内容]

THINK:   "第 47 行的 try/except 需要替换"
ACT:     edit_file(...)
OBSERVE: "已修改"

THINK:   "验证语法"
ACT:     python -m py_compile src/auth.py
OBSERVE: "无语法错误"

THINK:   "跑相关测试"
ACT:     pytest tests/test_auth.py -v
OBSERVE: "3 passed"
```

与本地 Agent 的区别只有两点：**执行在隔离环境里**、**你不需要实时盯着**。

---

## 第四步：验证与自我修复

```
改完 → 跑测试 → 失败 → 读 traceback → 修 → 再跑 → 通过 → 提交
```

这是 Cloud Agent 最有价值的部分，也是风险所在：

- ✅ 能自己发现并修复明显错误；
- ⚠️ 可能"改测试让它通过"、跳过失败用例、或降低断言强度。

**对策：** review 时专门看测试文件是否被修改；CI 在干净环境重跑；关键仓库开分支保护。

---

## 第五步：结果交付

```bash
git add -A
git commit -m "refactor: 统一 API 错误处理"
git push origin agent/<task-id>
# 创建 PR / 或在 Web 界面点"创建 PR"
```

你收到的是：**分支 + diff + PR**。部分产品（Copilot、Claude Code、Codex）还能继续监听 PR：

- CI 失败 → 自动修；
- reviewer 评论 → 自动响应（有歧义时会先问你）；
- 合并冲突 → 目前多数产品不能自动处理，需要手动 rebase。

---

## 状态管理：长任务怎么"记住"

| 层 | 作用 | 限制 |
|----|------|------|
| 上下文窗口 | 当前任务的工作记忆 | 会压缩/截断 |
| 环境状态 | 依赖、缓存、文件系统 | 环境过期/回收后丢失 |
| 会话历史 | 对话与工具调用记录 | 跨设备可继续（部分产品） |
| Git | 最可靠的状态记录 | 需要 agent 主动 commit |

**实践建议：** 让 agent 每完成一个子任务就 commit；长任务拆成多个小任务；把计划写进仓库文件（如 `docs/plan.md`），这样 teleport/重启后还能接着干。

---

## 安全边界（2026 年重点）

| 边界 | 做法 |
|------|------|
| **隔离** | 每会话独立 VM/容器；本地 Agent 用隔离 VM 或沙箱 |
| **凭据** | Git 凭据与签名密钥留在沙箱外，由代理按请求注入；网络密钥同理 |
| **网络** | 默认 allowlist，可关闭；高风险环境限制出口域名 |
| **权限** | 会话级权限模式；写操作需审批；组织策略可禁用云会话 |
| **审计** | 会话日志、工具调用记录、用量报表 |
| **人工闸门** | 合并前必须 review；生产部署不交给 Agent |

> 一个容易忽略的点：即使"关闭网络"，Agent 仍可能与模型 API 通信，**数据仍可能离开沙箱**。合规判断要看完整链路，而不是只看"有没有外网"。

---

## 两种执行模式的技术对比

| 技术维度 | 托管云沙箱 | 本地执行 + 远程控制 |
|----------|-----------|---------------------|
| 执行位置 | 厂商云 VM | 你的机器 |
| 代码位置 | 上传/克隆到云端 | 留在本地 |
| 机器要求 | 无（关电脑也能跑） | 机器要开机、进程要常驻 |
| 断点续跑 | 会话可恢复（环境过期会回收） | 依赖本地进程 |
| 并发 | 多会话并行 | 受本机资源限制 |
| 数据隐私 | 取决于厂商与配置 | 最高 |
| 计费 | 套餐用量 / 席位 / token | 主要是我方算力 + API |

---

## 并行：从"一个 Agent"到"一组 Agent"

2026 年的产品普遍支持并行，但机制不同：

| 机制 | 代表 | 隔离方式 |
|------|------|----------|
| 多会话并行 | Claude Code cloud、Codex Cloud | 每会话独立环境 |
| Agent view（研究预览） | Claude Code | 后台会话 + 可选 worktree |
| Agent Teams（实验，默认关闭） | Claude Code | 共享任务列表 + 互相消息，**不自动隔离 worktree**，需按文件划分 |
| 动态工作流 | Claude Code | 脚本编排大量 subagent，交叉验证 |
| Projects（公测） | Claude Code | 一个项目下多条线程，云端或 Remote Control |

**教训：** 并行不是免费的——token 成倍、冲突概率上升、review 成本上升。先串行跑通，再并行。

---

## 小结

```
Cloud Agent
= 可复用环境（仓库 + 依赖 + 网络 + 密钥）
+ 隔离执行 + ReAct 循环
+ 验证与自我修复
+ Git 交付（PR）
+ 人工 review 闸门
```

不神秘，但每一层都需要工程化。**"能跑"和"能放心合并"之间，差的是环境、权限与 review 流程。**

---

## 历史沿革

- **2026-11**：环境（environment）成为标准抽象；凭据代理、网络密钥、自托管环境成为企业选项；并行机制从"多会话"扩展到 agent teams / workflows / projects。
- **2026-07-28**：MCP 规范无状态化，云端 Agent 接 MCP 的方式随之调整（不再依赖会话握手）。
- **2026-03（课程初版）**：当时的架构描述以"Cursor Background Agent / Devin"为样本，强调"clone repo → ReAct → PR"，没有环境配置、凭据代理、网络 allowlist 这些概念。旧描述保留在 [M10-01 历史沿革](./01-what-is-cloud-agent.md#历史沿革)，作为"Cloud Agent 1.0"的认知快照。

---

## 下一步

- [M10-03 如何使用 Cloud Agent](./03-using-cloud-agent.md) — 实战上手指南
- [M10-04 自建 Cloud Agent 工作流](./04-build-your-own.md) — 自己搭一套
