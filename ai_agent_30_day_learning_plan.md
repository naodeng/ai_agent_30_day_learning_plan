# AI Agent 新手 30 天学习计划

## 适用对象

你有一定的编程/技术基础（会写脚本、用过 LLM），想系统理解 AI Agent 的概念与工程实践，并在 30 天里从「看懂概念」走到「做出一个可运行、可评估的小型 Agent Demo」。

学习主线是李博杰《深入理解 AI Agent：设计原理与工程实践》第 1、2、3、4、5、6、7、8、10 章，覆盖执行循环、上下文工程、记忆与 RAG、工具与 MCP、Coding Agent、评估、后训练与多 Agent 协作。每天 60 分钟起步，时间充足可延长到 120 分钟；每 5 天做一次小复盘，每 10 天形成一个可运行成果。

## 30 天目标

- 能用自己的话解释 Agent 是什么，说清 Agent 与普通 Chatbot 的区别，画出「观察 → 思考 → 行动 → 反馈」执行循环。
- 能设计 system prompt、任务上下文、压缩与摘要策略，封装可复用 Skill，输出上下文设计文档。
- 能说清记忆、知识库与 RAG 的完整链路，并搭建一个最小 RAG 问答 Demo。
- 能为 Agent 设计工具 schema、权限分级，理解 MCP 协议与 Coding Agent 工作流，做出工具型 Agent Demo。
- 能建立小型 eval set，设计主指标与护栏指标，理解后训练与持续进化的边界。
- 能判断何时需要多 Agent，设计协作与通信机制，并完成一个综合 Agent 项目。
- 30 天后能完成最小闭环：设计上下文、接工具、查知识库、记录轨迹、用 eval 判断好坏，做出一个可解释、可控、可改进的小型 Agent。

## 每天固定 60 分钟结构

| 时间 | 内容 | 目标 |
|---|---|---|
| 0-10 分钟 | 核心概念与术语 | 先掌握当天主题的关键概念，建立最小认知框架 |
| 10-25 分钟 | 阅读/章节输入 | 精读对应章节重点，只抓问题、思路、结论 |
| 25-45 分钟 | 实践任务 | 动手完成输出模板，必须产出一份可复用产物 |
| 45-55 分钟 | 追问与反思 | 回答追问练习，标记卡住的概念 |
| 55-60 分钟 | 复盘与作业 | 整理自检清单，定下明天要复习的一点 |

如果当天时间充足，可以再花 30-60 分钟完成「进阶扩展」或打磨 Demo。

## Day 6-30 规划重点

Day 6-10 进入上下文工程：system prompt 结构化设计、压缩与摘要、Skills 封装，第 10 天形成《上下文设计文档》。

Day 11-15 进入记忆与 RAG：用户记忆边界、RAG 完整链路、检索质量与知识组织，第 14 天做出最小 RAG Demo。

Day 16-20 进入工具与 MCP：工具 schema、权限分级、MCP 生态与 Coding Agent，第 20 天做出工具型 Agent Demo。

Day 21-25 进入评估与进化：任务集与评分标准、主指标/护栏指标、eval set、后训练概念与反馈闭环。

Day 26-30 进入多 Agent 与最终项目：协作模式、通信与状态，最后完成综合 Agent 项目与复盘报告。

## 每日文件

| Day | 阶段 | 主题 | 中文主题 | 能力目标 | 文件 |
|---|---|---|---|---|---|
| Day 01 | Foundation | Understanding What an AI Agent Is | 理解 AI Agent 是什么 | 能说清 Agent 与 Chatbot 的区别，画出观察-思考-行动-反馈执行循环 | [day-01-understanding-what-an-ai-agent-is.md](ai-agent-30-day-learning-plan/day-01-understanding-what-an-ai-agent-is.md) |
| Day 02 | Foundation | The Role of the LLM Inside an Agent | LLM 在 Agent 中的角色 | 能区分模型能力与系统工程能力，说清 LLM 的决策、推理与生成职责 | [day-02-the-role-of-the-llm-in-agents.md](ai-agent-30-day-learning-plan/day-02-the-role-of-the-llm-in-agents.md) |
| Day 03 | Foundation | Task Decomposition and Planning | 任务拆解与规划 | 能把模糊任务拆成可执行步骤，理解 planning 的粒度与动态调整 | [day-03-task-decomposition-and-planning.md](ai-agent-30-day-learning-plan/day-03-task-decomposition-and-planning.md) |
| Day 04 | Foundation | Agent State and Feedback | Agent 的状态与反馈 | 能把 Agent 理解为多轮状态机，说清状态、历史与工具反馈 | [day-04-agent-state-and-feedback.md](ai-agent-30-day-learning-plan/day-04-agent-state-and-feedback.md) |
| Day 05 | Foundation | Weekly Review 1: Minimal Agent Design | 阶段复盘 1：最小 Agent 设计 | 能独立完成一页《日报生成 Agent v0.1》设计说明 | [day-05-weekly-review-1-minimal-agent-design.md](ai-agent-30-day-learning-plan/day-05-weekly-review-1-minimal-agent-design.md) |
| Day 06 | Context Engineering | Context Engineering Basics | 上下文工程入门 | 能区分 system instruction、user message、tool description、memory 与检索内容 | [day-06-context-engineering-basics.md](ai-agent-30-day-learning-plan/day-06-context-engineering-basics.md) |
| Day 07 | Context Engineering | Structured Prompt Design | Prompt 结构化设计 | 能把模糊指令改写成角色、目标、步骤、约束、输出格式齐全的结构化 Prompt | [day-07-structured-prompt-design.md](ai-agent-30-day-learning-plan/day-07-structured-prompt-design.md) |
| Day 08 | Context Engineering | Context Compression and Summarization | 上下文压缩与摘要 | 能设计摘要、裁剪与分层记忆策略，控制长任务上下文膨胀 | [day-08-context-compression-and-summarization.md](ai-agent-30-day-learning-plan/day-08-context-compression-and-summarization.md) |
| Day 09 | Context Engineering | Agent Skills and Reusable Context | Agent Skills 与可复用上下文 | 能把重复工作流封装成可复用 Skill，写清适用场景与失败处理 | [day-09-agent-skills-and-reusable-context.md](ai-agent-30-day-learning-plan/day-09-agent-skills-and-reusable-context.md) |
| Day 10 | Context Engineering | Weekly Review 2: Context Design Document | 阶段复盘 2：上下文设计文档 | 能输出《测试报告 Agent 上下文设计 v0.1》 | [day-10-weekly-review-2-context-design-document.md](ai-agent-30-day-learning-plan/day-10-weekly-review-2-context-design-document.md) |
| Day 11 | Memory & RAG | User Memory Basics | 用户记忆入门 | 能区分短期上下文与长期记忆，划定记忆边界与隐私约束 | [day-11-user-memory-basics.md](ai-agent-30-day-learning-plan/day-11-user-memory-basics.md) |
| Day 12 | Memory & RAG | RAG Basics | RAG 基础 | 能说清洗切分、embedding、检索、重排、生成、引用完整链路 | [day-12-rag-basics.md](ai-agent-30-day-learning-plan/day-12-rag-basics.md) |
| Day 13 | Memory & RAG | Retrieval Quality and Knowledge Organization | 检索质量与知识组织 | 能为知识库设计 metadata 与结构化索引，理解向量检索局限 | [day-13-retrieval-quality-and-knowledge-organization.md](ai-agent-30-day-learning-plan/day-13-retrieval-quality-and-knowledge-organization.md) |
| Day 14 | Memory & RAG | Building a Minimal RAG Demo | 搭建最小 RAG Demo | 能实现本地文档加载、切分、检索、带引用的最小 RAG 问答 Demo | [day-14-building-a-minimal-rag-demo.md](ai-agent-30-day-learning-plan/day-14-building-a-minimal-rag-demo.md) |
| Day 15 | Memory & RAG | Weekly Review 3: Memory + RAG Design | 阶段复盘 3：记忆 + RAG 设计 | 能输出《知识库问答 Agent 设计 v0.1》，理清记忆与知识边界 | [day-15-weekly-review-3-memory-and-rag-design.md](ai-agent-30-day-learning-plan/day-15-weekly-review-3-memory-and-rag-design.md) |
| Day 16 | Tools & MCP | Tool Calling Basics | 工具调用基础 | 能为工具写清 schema、返回结构与失败处理，区分调用决策与执行 | [day-16-tool-calling-basics.md](ai-agent-30-day-learning-plan/day-16-tool-calling-basics.md) |
| Day 17 | Tools & MCP | MCP and the Tool Ecosystem | MCP 与工具生态 | 能说清 MCP 的 tools、resources、prompts 与接入价值 | [day-17-mcp-and-the-tool-ecosystem.md](ai-agent-30-day-learning-plan/day-17-mcp-and-the-tool-ecosystem.md) |
| Day 18 | Tools & MCP | Tool Safety and Permission Boundaries | 工具安全与权限边界 | 能按只读、低风险写入、高风险写入分级设计工具权限 | [day-18-tool-safety-and-permission-boundaries.md](ai-agent-30-day-learning-plan/day-18-tool-safety-and-permission-boundaries.md) |
| Day 19 | Tools & MCP | Coding Agent Basics | Coding Agent 入门 | 能设计修复测试脚本失败的 Coding Agent 完整流程 | [day-19-coding-agent-basics.md](ai-agent-30-day-learning-plan/day-19-coding-agent-basics.md) |
| Day 20 | Tools & MCP | Weekly Review 4: Tool-Based Agent Demo | 阶段复盘 4：工具型 Agent Demo | 能做出调用 2-3 个工具完成 Nginx CPU 分析的 Agent Demo | [day-20-weekly-review-4-tool-based-agent-demo.md](ai-agent-30-day-learning-plan/day-20-weekly-review-4-tool-based-agent-demo.md) |
| Day 21 | Evaluation & Evolution | Agent Evaluation Basics | Agent 评估入门 | 能设计任务集与评分标准，说清人工与自动评估如何结合 | [day-21-agent-evaluation-basics.md](ai-agent-30-day-learning-plan/day-21-agent-evaluation-basics.md) |
| Day 22 | Evaluation & Evolution | Designing Eval Metrics | 设计评估指标 | 能把「感觉好用」转化为主指标与护栏指标 | [day-22-designing-eval-metrics.md](ai-agent-30-day-learning-plan/day-22-designing-eval-metrics.md) |
| Day 23 | Evaluation & Evolution | Building a Small Eval Set | 构建小型 Eval Set | 能建立覆盖失败场景、带 must_not_do 与评分标准的评估集 | [day-23-building-a-small-eval-set.md](ai-agent-30-day-learning-plan/day-23-building-a-small-eval-set.md) |
| Day 24 | Evaluation & Evolution | Model Post-Training Concepts | 模型后训练概念 | 能区分预训练、SFT、RL，知道何时不该急着训练模型 | [day-24-model-post-training-concepts.md](ai-agent-30-day-learning-plan/day-24-model-post-training-concepts.md) |
| Day 25 | Evaluation & Evolution | Continuous Improvement and Feedback Loops | 持续进化与反馈闭环 | 能设计轨迹日志与反馈沉淀流程，让 Agent 越用越好 | [day-25-continuous-improvement-and-feedback-loops.md](ai-agent-30-day-learning-plan/day-25-continuous-improvement-and-feedback-loops.md) |
| Day 26 | Multi-Agent & Project | Multi-Agent Collaboration Basics | 多 Agent 协作基础 | 能设计 Planner/Research/Writer/Reviewer 角色分工与上下文边界 | [day-26-multi-agent-collaboration-basics.md](ai-agent-30-day-learning-plan/day-26-multi-agent-collaboration-basics.md) |
| Day 27 | Multi-Agent & Project | Multi-Agent Communication and State | 多 Agent 通信与状态 | 能设计 Agent 间消息格式、中间产物与冲突处理 | [day-27-multi-agent-communication-and-state.md](ai-agent-30-day-learning-plan/day-27-multi-agent-communication-and-state.md) |
| Day 28 | Multi-Agent & Project | Final Project Design | 最终项目设计 | 能定义技术问题分析 Agent 的 MVP 范围与成功标准 | [day-28-final-project-design.md](ai-agent-30-day-learning-plan/day-28-final-project-design.md) |
| Day 29 | Multi-Agent & Project | Final Project Implementation and Eval | 最终项目实现与评估 | 能完成可演示版本，并用评估集跑出成功与失败案例 | [day-29-final-project-implementation-and-eval.md](ai-agent-30-day-learning-plan/day-29-final-project-implementation-and-eval.md) |
| Day 30 | Multi-Agent & Project | Summary, Retrospective, and Next Steps | 总结、复盘与下一阶段路线 | 能输出 30 天学习复盘与下一阶段学习方向 | [day-30-summary-retrospective-and-next-steps.md](ai-agent-30-day-learning-plan/day-30-summary-retrospective-and-next-steps.md) |

## 模式对照表（《Agentic Design Patterns》）

每天的「阅读重点 - 补充材料」里都有《Agentic Design Patterns》（Google 智能体设计模式，中文翻译版）的对照阅读条目。下表按模式反查对应 Day，在线阅读：https://adp.xindoo.xyz/ ，原书仓库：https://github.com/naodeng/agentic-design-patterns

| 模式 | 中文名 | 对应 Day | 阅读链接 |
|---|---|---|---|
| 第 1 章 Prompt Chaining | 提示链 | Day 07、Day 09 | https://adp.xindoo.xyz/chapters/Chapter%201_%20Prompt%20Chaining |
| 第 2 章 Routing | 路由 | Day 06 | https://adp.xindoo.xyz/chapters/Chapter%202_%20Routing |
| 第 3 章 Parallelization | 并行化 | Day 03 | https://adp.xindoo.xyz/chapters/Chapter%203_%20Parallelization |
| 第 4 章 Reflection | 反思 | Day 04、Day 25 | https://adp.xindoo.xyz/chapters/Chapter%204_%20Reflection |
| 第 5 章 Tool Use | 工具使用 | Day 16 | https://adp.xindoo.xyz/chapters/Chapter%205_%20Tool%20Use |
| 第 6 章 Planning | 规划 | Day 03 | https://adp.xindoo.xyz/chapters/Chapter%206_%20Planning |
| 第 7 章 Multi-Agent Collaboration | 多智能体协作 | Day 26 | https://adp.xindoo.xyz/chapters/Chapter%207_%20Multi-Agent%20Collaboration |
| 第 8 章 Memory Management | 记忆管理 | Day 06、Day 11、Day 15 | https://adp.xindoo.xyz/chapters/Chapter%208_%20Memory%20Management |
| 第 9 章 Learning and Adaptation | 学习与适应 | Day 24、Day 25 | https://adp.xindoo.xyz/chapters/Chapter%209_%20Learning%20and%20Adaptation |
| 第 10 章 Model Context Protocol (MCP) | MCP | Day 17 | https://adp.xindoo.xyz/chapters/Chapter%2010_%20Model%20Context%20Protocol%20(MCP) |
| 第 11 章 Goal Setting and Monitoring | 目标设定与监控 | Day 05、Day 22、Day 28 | https://adp.xindoo.xyz/chapters/Chapter%2011_%20Goal%20Setting%20and%20Monitoring |
| 第 12 章 Exception Handling and Recovery | 异常处理与恢复 | Day 20 | https://adp.xindoo.xyz/chapters/Chapter%2012_%20Exception%20Handling%20and%20Recovery |
| 第 13 章 Human-in-the-Loop | 人机协同 | Day 18、Day 29 | https://adp.xindoo.xyz/chapters/Chapter%2013_%20Human-in-the-Loop |
| 第 14 章 Knowledge Retrieval (RAG) | 知识检索（RAG） | Day 12-15 | https://adp.xindoo.xyz/chapters/Chapter%2014_%20Knowledge%20Retrieval%20(RAG) |
| 第 15 章 Inter-Agent Communication (A2A) | 智能体间通信 | Day 27 | https://adp.xindoo.xyz/chapters/Chapter%2015_%20Inter-Agent%20Communication%20(A2A) |
| 第 16 章 Resource-Aware Optimization | 资源感知优化 | Day 08、Day 10 | https://adp.xindoo.xyz/chapters/Chapter%2016_%20Resource-Aware%20Optimization |
| 第 17 章 Reasoning Techniques | 推理技术 | Day 02 | https://adp.xindoo.xyz/chapters/Chapter%2017_%20Reasoning%20Techniques |
| 第 18 章 Guardrails/Safety | 护栏与安全 | Day 18 | https://adp.xindoo.xyz/chapters/Chapter%2018_%20Guardrails_Safety%20Patterns |
| 第 19 章 Evaluation and Monitoring | 评估与监控 | Day 21-23、Day 29 | https://adp.xindoo.xyz/chapters/Chapter%2019_%20Evaluation%20and%20Monitoring |
| 第 20 章 Prioritization | 优先级排序 | Day 28 | https://adp.xindoo.xyz/chapters/Chapter%2020_%20Prioritization |
| 第 21 章 Exploration and Discovery | 探索与发现 | Day 30 | https://adp.xindoo.xyz/chapters/Chapter%2021_%20Exploration%20and%20Discovery |
| 引言 | 全书模式地图 | Day 01 | https://adp.xindoo.xyz/chapters/Agentic%20Design%20Patterns |
| 结语 | 全书回顾 | Day 30 | https://adp.xindoo.xyz/chapters/Conclusion |
| 附录 A | 高级提示技术 | Day 07 | https://adp.xindoo.xyz/chapters/Appendix%20A_%20Advanced%20Prompting%20Techniques |
| 附录 B | AI 智能体交互（GUI 到真实环境） | Day 16 | https://adp.xindoo.xyz/chapters/Appendix%20B%20-%20AI%20Agentic%20Interactions_%20From%20GUI%20to%20Real%20world%20environment |
| 附录 C | 智能体框架概览 | Day 01、Day 17 | https://adp.xindoo.xyz/chapters/Appendix%20C%20-%20Quick%20overview%20of%20Agentic%20Frameworks |
| 附录 D | 使用 AgentSpace 构建智能体 | Day 30 | https://adp.xindoo.xyz/chapters/Appendix%20D%20-%20Building%20an%20Agent%20with%20AgentSpace%20(on-line%20only) |
| 附录 E | CLI 上的 AI 智能体 | Day 19 | https://adp.xindoo.xyz/chapters/Appendix%20E%20-%20AI%20Agents%20on%20the%20CLI |
| 附录 F | 推理引擎幕后 | Day 02 | https://adp.xindoo.xyz/chapters/Appendix%20F%20%20-%20Under%20the%20Hood_%20An%20Inside%20Look%20at%20the%20Agents'%20Reasoning%20Engines |
| 附录 G | 编码智能体 | Day 19 | https://adp.xindoo.xyz/chapters/Appendix%20G%20-%20%20Coding%20agents |

## 建议使用方式

- 每天只学一个文件，不要贪多。60 分钟内必须产出一份当天产物。
- 每 5 天做一次小复盘（Day 5、10、15、20 自带复盘内容），记录「我能解释什么」和「我能做出什么」。
- 把所有模板替换成你真实的工作场景（测试报告、日志分析、缺陷分析等），越具体越有价值。
- 每个 Demo 都要保留运行日志，Agent 调试主要靠轨迹。
- 学框架前先理解底层概念：上下文、工具、状态、评估。
- 不要追求一步到位做「全自动 Agent」，先做人机协作。

## 30 天后的交付物

- 一张 Agent 架构图与一份上下文设计文档。
- 一个最小 RAG 问答 Demo。
- 一个能调用 2-3 个工具完成自动化任务的 Agent Demo。
- 一套 20 条用例的 eval set 与评估结论。
- 一个综合 Agent MVP 项目（技术问题分析 Agent）。
- 一份 30 天学习复盘与下一阶段学习路线。

## 参考资料

- 《深入理解 AI Agent：设计原理与工程实践》主仓库：https://github.com/bojieli/ai-agent-book
- 在线阅读：https://bojieli.github.io/ai-agent-book/
- 第 1 章：AI Agent 入门：https://bojieli.github.io/ai-agent-book/book/chapter1/
- 第 2 章：上下文工程：https://bojieli.github.io/ai-agent-book/book/chapter2/
- 第 3 章：用户记忆和知识库：https://bojieli.github.io/ai-agent-book/book/chapter3/
- 第 4 章：工具：https://bojieli.github.io/ai-agent-book/book/chapter4/
- 第 5 章：Coding Agent 与通用 Agent：https://bojieli.github.io/ai-agent-book/book/chapter5/
- 第 6 章：Agent 的评估：https://bojieli.github.io/ai-agent-book/book/chapter6/
- 第 7 章：模型后训练：https://bojieli.github.io/ai-agent-book/book/chapter7/
- 第 8 章：Agent 的持续进化：https://bojieli.github.io/ai-agent-book/book/chapter8/
- 第 10 章：多 Agent 协作：https://bojieli.github.io/ai-agent-book/book/chapter10/
- 《Agentic Design Patterns》（Google 智能体设计模式，中文翻译）：https://adp.xindoo.xyz/
- 《Agentic Design Patterns》全书引言（21 章 + 7 附录）：https://adp.xindoo.xyz/chapters/Agentic%20Design%20Patterns
- 《Agentic Design Patterns》原书仓库：https://github.com/naodeng/agentic-design-patterns
- OpenAI Agents SDK：https://openai.github.io/openai-agents-python/
- OpenAI Evals：https://github.com/openai/evals
- Model Context Protocol：https://modelcontextprotocol.io/
- LangGraph：https://docs.langchain.com/oss/python/langgraph/overview

## 一句话总结

30 天内不要追求「掌握所有 Agent 框架」，而是要完成一个最小闭环：能设计上下文，能接工具，能查知识库，能记录轨迹，能用 eval 判断好坏，最后能做出一个可解释、可控、可改进的小型 Agent。
