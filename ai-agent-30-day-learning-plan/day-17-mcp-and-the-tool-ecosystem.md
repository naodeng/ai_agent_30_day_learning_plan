# 第 17 天：MCP 与工具生态

## 今日目标

能说清 MCP 的 tools、resources、prompts 与接入价值，画出 MCP 架构。

## 学习安排

| 时间 | 模块 | 做什么 |
|---|---|---|
| 0-10 分钟 | 核心概念 | 通读当天术语表，圈出 3 个你最想在工作里用上的概念。 |
| 10-25 分钟 | 阅读输入 | 精读当天章节重点，只抓问题、思路、结论。 |
| 25-45 分钟 | 实践任务 | 动手完成输出模板，必须产出一份可复用产物。 |
| 45-55 分钟 | 追问与反思 | 回答追问练习，标记卡住的概念。 |
| 55-60 分钟 | 复盘与作业 | 整理自检清单，定下明天要复习的一点。 |

## 核心概念

| 术语 | 中文解释 | 应用场景 |
|---|---|---|
| MCP | Model Context Protocol：连接模型应用与工具、数据源的开放协议，统一接入标准 | 一个 Agent 通过 MCP 同时接入 GitHub、数据库、监控系统 |
| MCP server | 实现 MCP 协议的服务端，负责暴露工具、资源并访问外部系统 | 一个包装了公司监控 API 的 MCP server |
| tool | MCP server 暴露的可调用操作，有名称、描述与参数 schema | GitHub server 里的 create_issue |
| resource | MCP server 暴露的只读数据源，按 URI 访问，如文件、配置、文档 | 读取 nginx.conf、CI 配置文件 |
| prompt | MCP server 提供的可复用指令模板，封装特定场景的提示 | 「分析构建失败原因」模板 |
| protocol | 客户端与服务端之间的消息协议，定义初始化、能力协商与调用流程 | Agent client 与 MCP server 的握手与调用 |
| tool discovery | 客户端连接后获取服务端暴露的工具列表与描述的过程 | 启动时拉取全部 MCP server 的工具清单 |
| caching | 对工具列表、资源等相对稳定的数据做缓存，减少重复请求 | 工具清单缓存，按版本号失效 |
| API wrapper | 普通封装：只做代码级包装，没有统一协议与发现机制 | 直接在代码里 import 一个 SDK 函数 |
| security risk | 引入外部 server 带来的越权、数据泄露、注入风险 | 未审计的第三方 MCP server 访问生产数据 |

## 阅读重点

- 对应章节：第 4 章中 MCP 协议相关内容（工具生态、协议统一、接入方式）。
- 关注点：
  - MCP 解决「每个系统一套接入方式」的碎片化问题：统一协议、统一发现。
  - tools、resources、prompts 三类能力的区别与各自用途。
  - MCP server 与普通 API wrapper 的本质区别：协议、发现、生命周期管理。
  - 工具列表是上下文中低频变化的部分，需要稳定、可缓存。
- 补充材料：
  - MCP 官方文档 modelcontextprotocol.io（协议架构、术语与规范）。
  - Anthropic MCP 快速入门（连接本地 server 的示例）。
  - 《Agentic Design Patterns》第 10 章「MCP」：https://adp.xindoo.xyz/chapters/Chapter%2010_%20Model%20Context%20Protocol%20(MCP) ，从模式视角看工具生态的协议统一价值。
  - 《Agentic Design Patterns》附录 C「智能体框架概览」：https://adp.xindoo.xyz/chapters/Appendix%20C%20-%20Quick%20overview%20of%20Agentic%20Frameworks ，重点看各框架对 MCP 的原生支持。

## 理解检查

- MCP 想解决的问题是什么？没有它之前，一个 Agent 接 5 个系统要重复做哪些事？
- Tool、Resource、Prompt 三者分别适合什么场景？各举一例。
- MCP Server 和普通 API Wrapper 的差别在哪里？
- 工具列表为什么需要稳定、可缓存？频繁变化会带来什么问题？

## 实践任务

背景：你负责的测试团队想让 Agent 能查代码、查数据、发通知，先画清楚 MCP 架构，再评估哪些系统值得接入。

步骤：

- 画出架构图：Agent Client -> MCP Server -> Tool / Resource / External System。
- 在图上标注三处关键交互：初始化与能力协商、工具发现、调用与结果返回。
- 特别说明「工具发现」：Agent 通过协议拿到工具清单，调用结果作为新消息回填上下文。
- 列出 6 个工作中可能接入的 MCP server，各写用途、典型能力、主要风险。
- 选 1 个最想先接入的，说明理由与最小接入范围。

产出：一份 mcp_architecture.md，含架构图与接入清单。

## 输出模板

```text
MCP 架构图:
Agent Client
  |  MCP 协议（初始化 / 能力协商 / 工具发现 / 调用与返回）
  v
MCP Server
  |-- Tool    -> [执行操作，如查询日志]
  |-- Resource-> [只读数据，如配置文件]
  |-- Prompt  -> [复用指令模板，如分析构建失败]
  v
External System: [GitHub / Filesystem / Database / Browser / Slack-Teams / Monitoring]

接入清单:
- [server 名]: 用途 [xxx]；典型能力 [tool 示例 / resource 示例]；主要风险 [xxx]
```

## 示范输出

```text
MCP 架构图:
Agent Client
  |  MCP 协议（JSON-RPC: 初始化、工具发现、调用、结果返回）
  v
MCP Server
  |-- Tool    -> query_logs / query_metrics / send_message
  |-- Resource-> 读取 nginx.conf、测试环境配置
  |-- Prompt  -> 「分析构建失败原因」指令模板
  v
External System: 日志平台 / 监控系统 / 代码仓库 / 消息服务

接入清单:
- Monitoring system: 用途 查指标与告警；典型能力 tool: query_metrics；主要风险 内网数据出域，需网关鉴权
- GitHub: 用途 查 issue 与 PR；典型能力 tool: create_issue；主要风险 写入类操作需人工确认
- Database: 用途 查测试数据；典型能力 tool: run_readonly_sql；主要风险 只读账号也可能泄露数据，需脱敏
- Filesystem: 用途 读写测试报告目录；典型能力 tool: read_file / write_file；主要风险 路径越界，需限定根目录
- Slack/Teams: 用途 通知测试结果；典型能力 tool: send_message；主要风险 群消息不可撤回，发送前需确认
- Browser: 用途 巡检页面可用性；典型能力 tool: navigate / screenshot；主要风险 自动化操作可能触发线上副作用
```

## 追问练习

- 企业里接入 MCP 最大的安全风险是什么？你会用什么控制手段？
- 如果两个 MCP server 都暴露了同名工具（如 query_metrics），Agent 该听谁的？客户端应如何路由？
- Resource 和 RAG 里的知识库有什么区别？什么时候直接读 resource，什么时候走检索？
- 工具发现是动态的，但上下文要求稳定，这两者怎么平衡？

## 常见误区

- 把 MCP server 当成普通 API wrapper：协议还带来统一发现、描述与能力协商，不只是封装。
- 以为接入 MCP 就自动安全：server 能做的事就是 Agent 能做的事，权限边界要单独设计。
- 忽略工具列表的缓存与稳定性：每次启动全量发现，成本高且上下文不稳定。
- 什么能力都想做成 tool：频繁读取的数据与固定指令更适合 resource 与 prompt。

## 进阶扩展

- MCP 企业安全：server 注册白名单、凭据托管、审计日志与网络隔离。
- 多 server 路由：同名工具冲突、能力协商与优先级设置。
- 协议演进与兼容：协议版本协商、能力协商，客户端与服务端各自升级时的策略。

## 今日作业

- 完成架构图与 6 个 server 清单，保存为 mcp_architecture.md。
- 为最想接入的 server 写一个最小接入计划（只暴露 3 个能力）。
- 给接入清单里的每个 server 写一句「接入前提」（凭据、网络、审批人）。
- 查 MCP 官方文档，确认工具列表（tools list）的返回结构。
- 明天开始前，用一句话说明 MCP 比普通 API wrapper 多解决了什么。

## 自检清单

- [ ] 我能画出 MCP 架构并说明各层职责。
- [ ] 我能说清 tools、resources、prompts 的区别。
- [ ] 我能列出工作中值得接入的 MCP server。
- [ ] 我能说出 MCP 与普通 API wrapper 的本质区别。
- [ ] 我能识别企业接入 MCP 的主要安全风险。
