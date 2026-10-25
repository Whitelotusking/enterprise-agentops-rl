# 2026 求职能力映射与项目答辩证据

> 本文用于确定项目需要证明哪些能力；不是“模仿某位求职者的项目就能拿 Offer”。候选人面经与 OC 为自述，岗位要求会变化。

## 1. 应聘方向与对应证明

| 岗位类型 | 企业关注点 | 我们必须有的证据 |
|---|---|---|
| 中小型 AI 应用/Agent 开发 | 客户需求理解、快速交付、REST API、企业软件/MCP 集成 | 独立模拟业务系统联调，最好接入 Zammad；清晰业务 PRD、Demo |
| 大厂 Agent/RAG 应用算法 | 检索质量、上下文、工具策略、失败恢复、离线与线上评测 | 固定检索/任务测试集、Recall/Success 消融、Bad Case 归因 |
| 大厂 AI 平台/后端 | 权限、SQL/缓存、并发、SSE、幂等、故障注入、可观测性 | 跨租户/审批/幂等负例、P95/Trace、设计取舍 |
| LLM 后训练/Agentic RL | 轨迹、可验证奖励、SFT/GRPO、测试隔离、错误工具惩罚 | Base vs SFT vs RL 的实际可复现数据；无结果不得伪称优化 |

**主求职成果 Gate 是 L3**（可部署且有量化/可验证实验）；L1 只是 demo，L2 是核心可靠性，L4 为额外研究增量。适当区分“个人模拟项目”与“企业客户真实上线”。

## 2. 2026 年岗位需求来源

- [中小企业 AI 应用开发，MCP 连接传统工业软件，FastAPI/PostgreSQL（历史岗位）](https://www.shixiseng.com/intern/inn_geukrvqd1q2q)：强调 API / 数据库 / 真实系统接入；部分页面已下线。
- [平安科技相关 AI 岗：NL2SQL、RAG、FastMCP、SSE/Trace/评测](https://campus.pingan.com/positionDetail?positionId=b56d37a5667c33c284f62ec197443518)：强调 AI 链路与后端工程交叉。
- [腾讯云医疗器械售后 Agent 生产化案例](https://adp.tencent.com/zh/blog/adp-fde-medical-device-after-sales-agent)：版本/权限/引用/工单/Bad Case；供应商自述成效不可当独立基准。
- [IDC 企业 Agent ROI 实践观察](https://www.idc.com/resource-center/blog/%E4%BC%81%E4%B8%9A-agent-%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E8%A7%82%E5%AF%9F%EF%BC%9A%E7%AE%97%E5%A5%BD%E5%BD%93%E4%B8%8Broi%EF%BC%8C%E5%B8%83%E5%B1%80%E7%BB%84%E7%BB%87%E9%95%BF%E6%9C%9F%E8%BD%AC/)：可量化、规则清晰、可验证流程优先。

这些链接是**需求选型线索**，不是招聘现状或面试录用保证。2026-10-25 归档。

## 3. 可查看的 2026 年个人求职记录

| 自述记录 | 可借鉴问题 | 证据边界 |
|---|---|---|
| [腾讯后端实习二面，作者补充百度 OC](https://m.nowcoder.com/discuss/842801019334455296) | Agent Plan-Verify-Replan、评测、SSE、Web 安全 | 本人自述，不能证明只靠 Agent 项目获得 Offer |
| [2026 春招五周 5+ Offer，简历有 RAG 智能体](https://m.nowcoder.com/discuss/869231276035760128) | 实验量化、项目选择依据、后端基础 | 还有较强背景、实习与另一高并发后端项目 |
| [携程 AI 应用实习一面（自述 OC）](https://www.nowcoder.com/feed/main/detail/2b1c35eace4a4bb3bd88ee669f163793) | Context 压缩、写入授权、并发与数据库索引 | 不能由标题独立验证正式录用 |
| [字节 AI 开发平台一面（作者自述失败）](https://api-cdn.nowcoder.com/feed/main/detail/fa50ef5521f84cb788f911cd31e5a98a) | RAG 切分、回归测试、Harness 选型、手撕算法 | 说明好项目不能代替算法/CS 基础 |

## 4. 面试官深挖问题 → 证据文件

| 可能追问 | 回答必须基于的项目资料 |
|---|---|
| 为什么选择金融客服/工单，而不是通用 Agent？ | PRD 用户角色、真实行业案例、业务状态与可衡量结果 |
| RAG 为什么选 Hybrid/RRF/Rerank？ | 同条件四组 Recall/MRR/nDCG/P95，至少两个失败例 |
| 文档过期或权限串线怎么处理？ | 文档生效区间/ACL 约束、恶意和错误引用测试 |
| MCP 与普通函数有何区别？ | 独立 MCP Server 和外部工单 API 的实际调用记录 |
| 为什么不是所有节点都放 LangGraph？ | Runner/RuntimeAdapter 接口，状态机与确定性业务事务的分层 |
| Agent 工具超时后怎么恢复？ | 响应丢失、写入唯一键、回查状态与重启测试 |
| 怎么证明工单办成了？ | 独立 Verifier、初始/终态快照与失败归因 |
| 如何计算真实业务价值？ | 自动有效办结率、转人工、错误写入、成本与人工/规则对照 |
| GRPO 奖励怎么防刷？ | 正确拒答、禁止工具、惩罚无必要工单；训练/测试隔离 |
| 你实际完成了什么？ | commit、变更 diff、测试和 demo；明确说明未完成部分 |

## 5. 最终求职材料

- 两分钟演示：从客户问题进入前端，到引用、MCP 调用、审批与工单终态；有失败/转人工例子。
- 一页系统设计：边界、数据流、幂等、工具鉴权以及为什么这样取舍。
- 检索四基线和任务评测报告：指标、样本规模、错误分析、成本与复现实验命令。
- 仓库 README、OpenAPI、架构 ADR、CI、测试日志与部署手册。
- AI 应用工程版 / Agent 算法版两套简历描述，**只使用真实已实现的数据**。
- 另外单独准备 Python/SQL、网络/OS、数据结构与算法；项目不能替代笔试手撕。

## 6. 简历叙述的真实性

**完成后可写：** 设计并实现基于公开模拟金融数据的 ServiceOps Agent Harness，集成 FastAPI、可追溯 RAG、MCP 工单适配、服务端审批/幂等与独立终态评测；通过固定任务集开展 X 组消融，在明确环境下得到 Y 指标。

**尚未实现时只能写：** 正在开发/构建，不写上线用户数、商业合同、服务客户数、提升 93%、节约 60% 人力、真实交易、GRPO 收益或尚无复现实验支持的百分比。
