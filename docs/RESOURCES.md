# 官方文档、公开数据与 2026 行业/招聘资料

> 2026-10-25 更新。先学官方文档；行业案例的厂商成效指标属于自述；面经作者的 OC/Offer 也属于自述，不能推导录用概率。

## 业务场景与公开模拟数据

- [Sierra τ-bench / τ-Knowledge 源码和 banking_knowledge 数据](https://github.com/sierra-research/tau2-bench)
- [τ-Knowledge 介绍](https://taubench.com/blog/tau-knowledge.html)
- [腾讯云：医疗器械售后 Agent 生产化复盘（2026-08）](https://adp.tencent.com/zh/blog/adp-fde-medical-device-after-sales-agent)：现行知识、复杂实体、权限、引用、Bad Case、人工运营。
- [IDC：企业 Agent 的 ROI 与长期组织价值（2026-09）](https://www.idc.com/resource-center/blog/%E4%BC%81%E4%B8%9A-agent-%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E8%A7%82%E5%AF%9F%EF%BC%9A%E7%AE%97%E5%A5%BD%E5%BD%93%E4%B8%8Broi%EF%BC%8C%E5%B8%83%E5%B1%80%E7%BB%84%E7%BB%87%E9%95%BF%E6%9C%9F%E8%BD%AC/)：可量化的企业流程选择。
- [4TU ResearchData/BPI 流程日志](https://data.4tu.nl/)：仅后续过程挖掘扩展，不当作银行完整数据库。

## 后端、数据、向量检索

- [FastAPI 官方中文教程](https://fastapi.tiangolo.com/zh/tutorial/)
- [SQLAlchemy 2.0](https://docs.sqlalchemy.org/en/20/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/docs/)
- [pgvector](https://github.com/pgvector/pgvector)
- [pytest](https://docs.pytest.org/)
- [Zammad 官方 Ticket API](https://docs.zammad.org/en/latest/api/ticket/)：W6–W8 真实第三方工单适配目标。

## Agent Harness / MCP / 训练

- [LangChain Agents](https://docs.langchain.com/oss/python/langchain/agents)（基础 Agent Loop）
- [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)（需要时做状态图/Checkpoint）
- [LangChain Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview)（参考 Harness 思路，不是必选依赖）
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP 规范](https://modelcontextprotocol.io/specification/)
- [Hugging Face TRL](https://huggingface.co/docs/trl/index) / [PEFT](https://huggingface.co/docs/peft/index)
- [Docker Compose](https://docs.docker.com/compose/), [React](https://react.dev/learn), [Vite](https://vite.dev/guide/)

## 2026 求职交叉验证

- [中小企业 AI 应用开发/MCP/后端历史招聘样本](https://www.shixiseng.com/intern/inn_geukrvqd1q2q)
- [平安科技 AI 工程/算法岗位样本](https://campus.pingan.com/positionDetail?positionId=b56d37a5667c33c284f62ec197443518)
- [腾讯后端实习面经 + 作者报告百度 OC](https://m.nowcoder.com/discuss/842801019334455296)
- [2026 春招 RAG/Agent + 后端项目求职复盘](https://m.nowcoder.com/discuss/869231276035760128)
- [携程 AI 应用一面（自述 OC）](https://www.nowcoder.com/feed/main/detail/2b1c35eace4a4bb3bd88ee669f163793)
- [字节 AI 平台岗位一面（自述失败，含算法手撕）](https://api-cdn.nowcoder.com/feed/main/detail/fa50ef5521f84cb788f911cd31e5a98a)

## 引用与真实性

- 记录阅读日期、URL、岗位日期以及可能的失效状态。
- 不从单条样本外推市场录用概率。
- 面经、厂商案例、官方 SDK 文档与自己实测结果分开标注。
- 在报告中区分“设计目标”“模拟实验已验证”“第三方公开宣称”。
