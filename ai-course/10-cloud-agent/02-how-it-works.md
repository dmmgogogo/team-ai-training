# M10-02 · Cloud Agent 工作原理

> 沙箱、执行循环、状态管理——它是怎么做到自主干活的

---

## 整体架构

```
用户
  │  发出任务指令
  ▼
任务调度层（Orchestrator）
  │  拆解任务 / 分配资源
  ▼
云端沙箱环境（Sandbox VM / Container）
  ├─ 代码仓库（clone 你的 repo）
  ├─ 完整 Shell 环境
  ├─ 依赖安装空间
  └─ 网络访问（受限）
        │
        ▼
   AI Agent 执行循环
   THINK → ACT → OBSERVE → THINK → ...
        │
        ▼
    结果输出
    （PR / 文件变更 / 报告）
        │
        ▼
     通知用户
```

---

## 第一步：沙箱环境的建立

Cloud Agent 启动时，第一件事是**构建一个和你项目完全一致的干净环境**：

```bash
# 伪代码：Cloud Agent 启动流程
git clone https://github.com/your-org/your-repo /workspace
cd /workspace
git checkout -b agent/task-20240315-fix-auth  # 新建独立分支

# 安装依赖（真实执行）
npm install
# 或
pip install -r requirements.txt

# 环境就绪，开始执行任务
```

**为什么要隔离？**
- 避免破坏你的本地环境
- 多个任务可以并行跑互不影响
- 失败了直接丢弃这个环境，没有副作用

---

## 第二步：任务规划

Agent 拿到任务后，不会直接开始改代码，而是先**理解全局**：

```
任务："把所有 API 接口的错误处理统一改成用 ErrorHandler 类"

Agent 的规划过程：
1. 搜索代码库：find . -name "*.py" | xargs grep "except"
2. 列出所有涉及文件（找到 23 个文件）
3. 分析现有的 ErrorHandler 类（在 utils/errors.py）
4. 制定修改顺序（从底层依赖到上层调用）
5. 开始逐文件修改
```

这个规划过程本身也由 LLM 驱动，不是硬编码的。

---

## 第三步：执行循环（核心）

和本地 Agent 相同的 ReAct 循环，但有真实的 Shell 执行权：

```
THINK:   "我需要先了解 auth.py 的结构"
ACT:     cat src/auth.py
OBSERVE: [读取到文件内容]

THINK:   "第 47 行的 try/except 需要改，先修改"
ACT:     edit_file(src/auth.py, line=47, ...)
OBSERVE: "文件已修改"

THINK:   "改完后要验证语法正确"
ACT:     python -m py_compile src/auth.py
OBSERVE: "✅ 无语法错误"

THINK:   "跑一下相关单元测试"
ACT:     pytest tests/test_auth.py -v
OBSERVE: "3 passed, 0 failed"

THINK:   "这个文件改完了，继续下一个..."
```

**关键：它能真正执行命令并看到结果**，而不只是建议你去执行。

---

## 第四步：验证与自我修复

Cloud Agent 的重要能力：**跑测试 → 发现错误 → 自动修复**

```
改完代码
    ↓
跑测试：pytest tests/
    ↓
发现 2 个测试失败
    ↓
分析失败原因（读 traceback）
    ↓
修改代码
    ↓
再跑测试
    ↓
全部通过 ✅
    ↓
提交结果
```

这个循环可以自动重复多次，直到测试通过或达到重试上限。

---

## 第五步：结果交付

任务完成后的标准流程：

```bash
# Agent 自动完成的操作
git add -A
git commit -m "fix: 统一 API 错误处理为 ErrorHandler 类

- 修改 23 个文件
- 保持原有 HTTP 状态码行为不变  
- 所有相关测试通过"

git push origin agent/task-20240315-fix-auth

# 创建 Pull Request
# → 通知你来 review
```

**你收到的是：** 一个完整的 PR，包含所有变更，随时可以 review 并合并。

---

## 状态管理：Agent 如何"记住"做了什么

长任务的难点是**状态持久化**：

```
短期记忆（Context Window）
  → 当前正在处理的文件和上下文
  → 有 Token 限制，超出则总结压缩

工作状态（持久化）
  → 已完成的文件列表写入 .agent-state.json
  → 遇到中断可以从断点继续

Git 本身就是最好的状态记录
  → 每完成一个子任务就 commit
  → 出错可以 git revert 回滚
```

---

## 安全边界

Cloud Agent 不是无限制的，有明确的访问控制：

| 允许 | 不允许（默认） |
|------|--------------|
| 读写仓库代码 | 访问生产数据库 |
| 安装开发依赖 | 访问外部 API（需授权） |
| 跑测试和 lint | 部署到生产环境 |
| 创建 PR/分支 | 直接合并代码 |
| 搜索代码库 | 访问其他仓库 |

**设计原则：** Agent 做，人来 review，最终决策权始终在你手上。

---

## 和本地 Agent 模式的技术对比

| 技术维度 | 本地 Claude Code / Cursor | Cloud Agent |
|----------|--------------------------|-------------|
| 执行环境 | 你的本地 shell | 云端隔离容器 |
| 任务时长 | 取决于上下文窗口 | 可以跑数小时 |
| 并发 | 单任务 | 多任务并行 |
| 断点续跑 | ❌ | ✅ |
| 费用 | API Token 费用 | 平台费 + Token |
| 数据隐私 | 代码留在本地 | 上传到云端 |

---

## 小结

Cloud Agent 的本质是：

```
= 云端隔离环境
+ 真实 Shell 执行权
+ LLM ReAct 循环
+ 异步任务调度
+ Git 作为结果交付载体
```

不神秘，但组合在一起威力很大。

---

## 下一步

- [M10-03 如何使用 Cloud Agent](./03-using-cloud-agent.md) — 实战上手指南
