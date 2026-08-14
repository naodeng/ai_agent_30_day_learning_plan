# Day 27 - Multi-Agent Communication and State

## 今日目标

能设计 Agent 间消息格式与中间产物，处理结论冲突与重复工作。

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
| message protocol | 消息协议，Agent 之间传递消息的约定格式与字段集合 | 定义 Research 发给 Writer 的消息长什么样 |
| structured message | 结构化消息，用固定字段传递任务与结果，而不是自由自然语言 | sender、receiver、task、output_schema 字段化传输 |
| intermediate artifact | 中间产物，Agent 之间交接的工作成果，如检索结果、报告草稿、审查意见 | Research 的检索结果落盘后交给 Writer |
| shared state | 共享状态，多个 Agent 共同读写的状态，如任务进度、结论池 | 记录四个 Agent 各自的完成状态与产出位置 |
| conflict resolution | 冲突处理，两个 Agent 结论不一致时的裁决规则与依据 | 数据与知识库说法矛盾时按证据优先级裁决 |
| duplicate work | 重复工作，多个 Agent 重复执行同一检索或同一工具调用 | 两个 Agent 都查了同一段日志导致成本翻倍 |
| shared memory risk | 共享记忆风险，一个 Agent 的错误写入会污染其他 Agent 的后续决策 | Research 写错的指标进入 Writer 的报告 |
| audit | 审计，记录每条消息、工具调用与状态变更，保证过程可回溯 | 出问题后回放是哪一步引入的错误 |
| confidence | 置信度，Agent 对自己产出可信程度的自评，用于触发人工复核 | 检索结果互相矛盾时标记 low confidence |
| human review | 人工复核，需要人确认才能继续或输出的机制 | 高风险结论输出前必须有人确认 |

## 阅读重点

- 对应章节：第 10 章中多 Agent 协作机制、上下文共享与隔离部分。
- 关注点：
  - 结构化消息与自然语言的区别：固定字段为什么更可靠、更易校验。
  - 中间产物如何定义与落盘：检索结果、报告草稿、审查意见各是什么结构。
  - 共享状态与隔离状态的取舍：什么状态必须共享，什么必须隔离。
  - 冲突处理与审计：结论冲突怎么裁决，过程怎么留痕。
- 补充材料：
  - LangGraph 官方文档中关于共享状态（State）与节点间消息传递的部分。
  - OpenAI Agents SDK 文档中关于 Handoff 与 Guardrail 的部分。

## 理解检查

- Agent 之间传自然语言好，还是结构化数据好？各自的风险是什么？
- 如何避免多个 Agent 重复工作？共享状态能起什么作用？
- 如何处理两个 Agent 结论冲突？裁决规则应该以什么为依据？
- 共享记忆会带来什么风险？如何降低污染的影响？

## 实践任务

背景：Day 26 的四 Agent 协作流程只有角色分工，还没有通信约定。今天为它补上消息格式、冲突处理规则和审计日志。

- 第 1 步：用下面的输出模板，为 Planner 到 Research、Research 到 Writer、Writer 到 Reviewer 三条消息各写一份 yaml，字段一个都不能少。
- 第 2 步：写一条冲突处理规则，场景是 Research 的数据结论与知识库文档说法不一致。
- 第 3 步：设计审计日志的字段清单，并写一条 Research 发消息的审计示例。
- 第 4 步：检查你的设计，找出最可能发生重复工作的环节，写一个去重办法。

## 输出模板

```yaml
# 消息格式 v0.1：四 Agent 协作
sender: [来源 Agent 名]
receiver: [目标 Agent 名]
task: [要对方完成的任务描述]
input:
  - [传给对方的中间产物或数据]
constraints:
  - [限制条件，如时间范围、数据源、语言]
output_schema:
  field_1: [类型与含义]
  field_2: [类型与含义]
confidence: [0-1 之间的自评置信度]
needs_human_review: [true/false，触发人工复核]

# 冲突处理规则
rule_id: [编号]
conflict: [冲突双方与冲突内容]
resolution: [裁决规则：以谁为准、依据什么证据]

# 审计日志字段
audit_log:
  message_id: [唯一编号]
  timestamp: [时间]
  sender: [发送方]
  receiver: [接收方]
  status: [succeeded / failed / needs_review]
```

## 示范输出

```yaml
# Research 发给 Writer 的实际消息
sender: research
receiver: writer
task: 基于检索结果生成 Nginx CPU 分析报告草稿
input:
  - metrics 数据：WAF 开启前后 CPU 均值 35% -> 78%
  - access log 摘要：WAF 规则命中集中在 /api 路径
  - 知识库文章：《WAF 规则与 CPU 开销排查》
constraints:
  - 时间范围限定在 10:00-11:00
  - 报告使用 Markdown
  - 无法验证的数据标注待验证
output_schema:
  assumptions: [string 数组，每条假设附证据]
  evidence: [string 数组，指标与日志引用]
  next_steps: [string 数组，验证步骤]
confidence: 0.7
needs_human_review: false

# 冲突处理规则示例
rule_id: CONFLICT-01
conflict: Research 的指标数据与知识库文档说法不一致
resolution: 以真实运行数据为准，知识库说法降级为参考假设并标注来源

# 审计日志示例
audit_log:
  message_id: msg-0001
  timestamp: 2026-08-14T10:05:00+08:00
  sender: research
  receiver: writer
  status: succeeded
```

## 追问练习

- 共享记忆会带来什么风险？如何设计隔离与回滚机制？
- 多 Agent 系统如何做审计？审计需要记录到什么粒度才能定位问题？
- confidence 应该由谁打？如何避免 Agent 过度自信？
- output_schema 校验失败时，应该重试、降级还是转人工？判断依据是什么？

## 常见误区

- 让 Agent 之间直接传自然语言结论：看似灵活，解析、校验和核对成本都很高。
- 中间产物不落盘：Agent 崩溃或重试后信息丢失，只能整条链路重跑。
- 共享一个全局状态：一个 Agent 的错误写入会污染所有下游 Agent 的决策。
- 冲突时让 LLM 自行投票：没有明确的证据优先级规则，投票结果不可复现。

## 进阶扩展

- 消息总线与事件驱动：真实系统用队列解耦 Agent，支持消息重放与背压控制。
- 状态持久化与事务：中间产物写入存储，失败时可回滚并按断点重试。
- 全链路审计：消息、工具调用、状态变更全部入审计日志，支撑问题定位与合规要求。

## 今日作业

- 为 Day 26 的设计补全三条消息的 yaml，字段一个都不能少。
- 写一条冲突处理规则，说明以谁为准、依据什么证据。
- 设计审计日志字段清单，并写一条 Research 发消息的审计示例。
- 找出你的设计里最可能发生重复工作的环节，写一个去重办法。

## 自检清单

- [ ] 我能用固定字段设计一条完整的 Agent 间消息。
- [ ] 我能说清中间产物为什么要落盘、要定 schema。
- [ ] 我能写出结论冲突的裁决规则。
- [ ] 我能指出共享记忆的风险并设计隔离办法。
- [ ] 我能设计审计日志并解释它解决什么问题。
