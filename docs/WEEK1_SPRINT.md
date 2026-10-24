# 一周冲刺：L1 + L2 核心能力（2026-10-24 至 2026-10-31）

> 目标是 L1 可演示系统与 L2 安全/恢复原型。并非一周内达到生产级 L2，GRPO 不在本周范围。

## 环境预检（仅代表已连接 PC2）

| 项目 | 检查结果 |
|---|---|
| 主机 | USER-20250627GR / Windows 10 |
| Python | 3.10.4（需单独安装 Python 3.12） |
| uv | 0.9.10（可直接使用） |
| Node.js | 24.11.1（前端可用） |
| GPU | RTX 3060 Laptop 6GB（只用于轻量推理） |
| Git / Docker | PATH 中未找到 |
| WSL | 查询未成功，不能视作可用 |

未在 PC2 安装软件，也未下载完整模型或数据集；如果换开发主机，必须重新检查。

## 主数据与隔离

主数据为 Sierra 的 [τ-bench/τ³-bench](https://github.com/sierra-research/tau2-bench) 仓库中的 `data/tau2/domains/banking_knowledge/`：

- `documents/`：知识检索数据，需要切分、索引、引用溯源。
- `db.json`：模拟业务初始状态，需要适配业务工具访问接口。
- `tasks.json`：任务与测试相关资料；**不得将官方期望答案直接作为 Agent 的上下文或训练输入**。
- `tasks_voice.json`：本周不使用。

注意：这些是 JSON/文档，不是可以直接连接的 PostgreSQL；先做独立导入层，再逐步迁移结构。原始基准另行克隆，勿直接复制到主项目或提交包含答案的生成物。

## 获取公开数据并预检

在装有 Git 的开发机上运行：

```bash
git clone https://github.com/Whitelotusking/enterprise-agentops-rl.git
git clone https://github.com/sierra-research/tau2-bench.git
cd tau2-bench
uv sync --extra knowledge --extra dev
uv run tau2 check-data
cd ../enterprise-agentops-rl
python scripts/inspect_tau_data.py --repo ../tau2-bench
```

官方 Python 要求 >=3.12、<3.14；`uv sync` 使用仓库的版本约束，不需要事先覆盖系统 Python。上面的检查脚本只列出文件大小、SHA256 和文档个数，不导出答案。

## 启动最小 FastAPI（目前仅健康检查）

```bash
cd backend
uv sync --dev
uv run pytest -q
uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

浏览器验证 `http://127.0.0.1:8000/health` 和 `http://127.0.0.1:8000/docs`。当前 `/health` 只检查进程存活，不代表数据库、RAG 或 Agent 已实现。基础健康检查测试已在隔离验证环境通过（2/2）；PC2 尚未实际运行。

## PostgreSQL + pgvector

在**支持 Docker Compose 的机器上**运行。在主仓库根目录复制 `.env.example` 为 `.env`，并修改 `POSTGRES_PASSWORD` 为仅用于本地开发的强密码。

```bash
docker compose --env-file .env -f infra/compose.dev.yml up -d
docker compose --env-file .env -f infra/compose.dev.yml exec postgres \
  psql -U agentops -d agentops -c "SELECT extversion FROM pg_extension WHERE extname='vector';"
```

如果更改了用户名或数据库名，也相应修改检查命令。端口仅绑定 `127.0.0.1`；不直接向公网开放 5432。SQL 初始化脚本只在空数据卷第一次启动时执行。

若 PC2 无法使用 Docker，不要在 Windows 上强行安装不兼容的 WSL：可在已有 Linux 机器部署数据库，使用 SSH 隧道连接。

## 7 天具体安排

| 日期 | 任务 | 验收 |
|---|---|---|
| 10/24（D0） | 识别开发主机/环境/数据位置；准备预备代码 | 能描述本机、数据库和模型分别运行在哪里 |
| 10/25（D1） | Git + Python 3.12 + `uv`，克隆两仓库 | `pytest`、`tau2 check-data` 成功 |
| 10/26（D2） | Postgres/pgvector、用户/租户/文档/任务表 | 迁移成功、数据重启持久化 |
| 10/27（D3） | 数据导入、切分、Embedding、Sparse/Dense RAG | 检索返回真实文档 ID 与来源 |
| 10/28（D4） | 最小 LangGraph 状态机与 3–5 个工具 | 多步骤模拟任务能真实完成 |
| 10/29（D5） | MCP Server、后端权限、审批、幂等 | 两租户越权拒绝、重复写仅一次 |
| 10/30（D6） | 状态恢复 + 简单 Web Demo | 浏览器端可查看任务与执行记录 |
| 10/31（D7） | 自动测试、演示录屏、README | 可复现地启动，真实报告通过/失败项 |

建议每天 3–5 小时，遇到平台部署障碍时先完成 API/数据代码并用测试数据库验证，不要因为容器卡住而停止全部开发。

## L1 / L2 验收门槛

**L1**：至少一个真实模型/推理端、真实文档检索、可观察的多步工具调用和简单 Web 页面。纯规则/mock 模型只算开发测试，不能宣传 L1 已完成。

**L2 核心**：两模拟租户、后端实施身份/数据权限检查、敏感操作显式审批、数据库幂等、状态持久化、结构化错误和自动化测试。不是生产级安全或大规模部署。

**必需的负向测试**：跨租户非法读写、无权限敏感写入、同一幂等键重复提交、工具参数类型错误、服务重启后重复动作。

## 本周不做

SFT、GRPO、复杂多 Agent、Kubernetes、生产级 SSO、压力规模夸大和无法证明的“企业真实上线”。保持每月额外支出在 0–100 元以内，优先使用已有机器和免费开源数据。

## 官方资料

- [τ-bench Getting Started](https://github.com/sierra-research/tau2-bench/blob/main/docs/getting-started.md)
- [FastAPI](https://fastapi.tiangolo.com/tutorial/)
- [MCP Python SDK](https://py.sdk.modelcontextprotocol.io/)
- [pgvector](https://github.com/pgvector/pgvector)
