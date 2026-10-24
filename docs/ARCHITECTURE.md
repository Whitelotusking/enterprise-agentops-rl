# 系统架构与技术设计总纲（设计稿）

> 当前仅为架构规划，不代表已实现。每个实现细节以对应阶段的 ADR 与测试为准。

## 1. 技术架构

- API 层：FastAPI、Pydantic、JWT/OIDC（按阶段逐步引入），统一结构化错误。
- 数据层：PostgreSQL + pgvector；关系数据和 RAG 索引统一存储，迁移用 Alembic。
- RAG 层：导入、切分、版本化、全文检索、向量检索、RRF、Rerank 与证据引用。
- Agent 层：LangGraph，有限状态机/工具调用节点/持久化 Checkpoint/人工审批节点。
- MCP 层：业务工具暴露为 schema 明确的服务；工具执行在后端再次校验身份和租户。
- 业务层：模拟账户、交易、工单、审批与状态迁移；所有“真实金融操作”禁止接入。
- 观测评测层：任务 trace、检索结果、工具调用、错误类型、延迟与使用量。
- Web 层：聊天与任务执行、文档、Trace、Benchmark 四页。
- 训练层：单独的离线/模拟环境，SFT / 条件允许的 GRPO 实验，不直接对线上生产数据更新模型。

## 2. 拟定核心数据实体

| 实体 | 主要字段（初稿） | 目的 |
|---|---|---|
| Tenant | id, name, status | 租户边界 |
| User / Role | id, tenant_id, role | 用户与授权 |
| Document | id, tenant_id, source, version, effective_at | 企业文档版本 |
| DocumentChunk | id, tenant_id, document_id, text, embedding | 文档切片与向量索引 |
| Task | id, tenant_id, user_id, state, status | Agent 业务任务 |
| ToolCall | id, tenant_id, task_id, tool_name, request_hash, status | 轨迹与调用审计 |
| Approval | id, tenant_id, task_id, action_hash, status | 敏感写操作审批 |
| BusinessCase | id, tenant_id, status, external_ref | 模拟工单实体 |
| EvalRun | id, dataset_revision, config_revision, metrics | 实验元数据 |

数据模型将以 W2 迁移定义为准。不要为了“高难度”提前引入 Kafka、Kubernetes、多数据库和微服务。

## 3. RAG 设计

1. 文档导入：归档来源、版本、数据哈希，避免重复导入。
2. 切分：以标题/段落结构为主，记录父文档位置与有效期。
3. 检索：全文检索与 pgvector 查询分开实现，保留原始分数，融合用 RRF。
4. 重排：Cross-Encoder Reranker 为可选实验模块，可关闭形成对照。
5. 过滤：租户、文档权限、有效期、类别均在后端执行；不仅靠 Prompt 过滤。
6. 输出：返回证据、版本、片段 ID，不编造引用。

## 4. Agent 状态与工具

主状态字段建议包含 `task_id`, `tenant_id`, `user_id`, `plan`, `evidence`, `pending_action`, `tool_history`, `checkpoint_version`, `final_result`。各节点职责独立，可运行模拟测试。

- 只读工具允许在授权后执行；写入工具必须重新鉴权，并应用幂等键。
- 敏感写操作触发 Human-in-the-loop 审批，审批绑定 `task_id + action_hash`，避免审批一个动作却执行另一动作。
- 工具超时不表示写操作失败；必须查询业务系统确认状态后再重试。
- 检索命中的外部文本属于不可信输入，不能覆盖系统权限与工具调用规则。
- Agent 的 Checkpoint 不能替代数据库事务与业务补偿机制。

## 5. 企业级安全与可靠性

- **租户隔离**：API 鉴权、业务查询、检索查询、MCP 工具和数据库 RLS 多层校验。
- **最小权限**：Agent 只访问明确声明的工具；禁止自由 SQL 和任意 Shell。
- **幂等与重试**：写入用请求幂等键、唯一约束和明确状态转移；重试处理“成功但响应丢失”。
- **审批**：风险操作在后端暂停，只有经过授权的用户能继续。
- **审计**：记录请求、工具名称、结果状态、耗时及被脱敏的参数，不记录密钥和未授权 PII。
- **数据集安全**：原始基准答案/数据库目标状态仅评测器可读，模型工具端不可读。

## 6. 可观察性与性能

- 每次任务关联 trace_id、task_id，统计节点耗时、检索耗时、工具错误、端到端延迟。
- P50/P95、吞吐、失败率只报告固定硬件、模型、并发条件下的实际测量值。
- 对失败按“检索、规划、参数、权限、业务校验、工具网络、超时、验证失败”归因。

## 7. 原则性取舍

- **首版单体+独立 MCP 服务**：方便自学和排错，避免无证据地拆微服务。
- **首版 PostgreSQL 统一存储**：降低运维成本，方便验证检索和事务。
- **优先验证再优化**：先建任务 Verifier，再训练 RL；先建立检索测试集，再调 RRF。
- **不接真实金融接口**：系统演示仅使用模拟交易与工单。
