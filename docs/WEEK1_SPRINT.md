# Week 1 开发分支记录｜2026-10-26 至 11-01

> 本文只解释 PR #1 的起步代码及首周执行细节。**最新版业务需求与整体路线图以 main 分支的 [PRODUCT_SCOPE.md](https://github.com/Whitelotusking/enterprise-agentops-rl/blob/main/docs/PRODUCT_SCOPE.md) 和 [ROADMAP.md](https://github.com/Whitelotusking/enterprise-agentops-rl/blob/main/docs/ROADMAP.md) 为准。**
>
> 注意：L1 是端到端业务 MVP，L2 首周只是核心安全/恢复原型；L3 可重复实验和真实系统集成才是主要求职交付标准，L4 训练可选。

## 当前 PR #1 包含什么

- FastAPI 最小应用与 `GET /health`。
- 后端依赖配置和最小 pytest 测试。
- PostgreSQL/pgvector Compose 文件和初始 SQL 脚本。
- τ-bench `banking_knowledge` 数据文件清单与预检脚本。
- 本文的首周冲刺记录。

**尚未由本 PR 完成**：实际客户/工单模型、RAG 索引、真实模型 Agent Loop、MCP Server、JWT、租户授权、审批、幂等、业务终态 Verifier 和完整前端。不要把“环境可运行”写成“业务实现完成”。

## 当前开发机环境（2026-10-25）

开发机 PC2 的新独立 WSL2 发行版 `enterprise-ubuntu` 已安装于 `J:\enterprise\wsl`，Linux 项目目录为 `/home/enterprise/projects/enterprise-agentops-rl`。

上一版此文写到“WSL 无法运行”是过时的系统服务身份检测结果：用登录用户进入 WSL 已验证可运行。PC2 的 Ubuntu 包含 Python 3.12、Node 22、Docker/Compose 以及 PostgreSQL 16/Redis 原生服务；pgvector 原生扩展已启用。因 Docker Hub 无法拉取数据库镜像，目前**不应把 Compose 可用误写成数据库容器已运行**。

本地 GitHub 仓库可能是 ZIP 快照导入，缺少 `.git`；**GitHub 上的文档和本地目录不会自动同步**。在本机修改代码之前检查远程分支、Git 同步状态和本地文件。原始 τ-bench 数据应保持只读，切勿提交标准答案。

## 7 天冲刺

| 日期 | 本周实际要做的工作 | 验收 |
|---|---|---|
| 10/26 | FastAPI 一天集中学习；业务 PRD、任务路由与 Pydantic | API 模型/pytest 通过 |
| 10/27 | SQLAlchemy/Alembic、租户/用户/工单表、独立模拟业务 API | 工单真正写入数据库，重启可查询 |
| 10/28 | τ-bench 文档导入、Embedding、Sparse/Dense RAG、版本/权限过滤 | 返回真实 doc ID、版本和引用 |
| 10/29 | 单 Agent Harness、Tool-Calling Loop、查询业务状态 | 真实模型完成只读多步任务 |
| 10/30 | MCP Server、敏感工单写入、人工审批、幂等键 | 不经授权无法写入，重复提交不会双重建单 |
| 10/31 | 基础 JWT/RBAC、2 租户、任务状态/恢复、简单页面/SSE | 跨租户拒绝，恢复状态可追踪 |
| 11/01 | 端到端测试与录屏、失败归因和验收记录 | 明确记录通过项/未完成项，不夸大产出 |

后续 W2–W10 继续补齐外部系统适配（例如 Zammad）、知识治理、完整状态恢复、四组 RAG 消融、40+40 任务评测和运营台。

## 启动与验证（Linux）

```bash
cd ~/projects/enterprise-agentops-rl
source .venv/bin/activate
cd backend
../.venv/bin/python -m pytest -q tests
../.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

从浏览器访问 `http://localhost:8000/docs`。现有 `/health` 测试只验证接口存活，不等于业务系统完成。原生数据库可用 `pg_isready`、`redis-cli ping` 检查。禁止同时启动监听相同端口的原生数据库和 Compose 数据库容器。

## 本周明确不做

真实客户/交易接入、未经审批的敏感写操作、生产级多租户 SaaS、独立的复杂微服务或 Kubernetes、完整 Zammad 上线、SFT/GRPO 训练、伪造压测/准确率/商业 ROI。
