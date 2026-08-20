# 第 16 天：工具调用基础

## 今日目标

能为工具写清用途、schema、返回结构与失败处理，理解「工具调用决策」与「工具执行」的区别。

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
| tool | 工具是 Agent 连接外部世界的方式：模型负责决策，代码负责执行 | 让 Agent 查询日志、查询指标、生成报告 |
| tool schema | 描述工具输入输出格式的结构化定义（如 JSON Schema），模型据此生成合法参数 | 声明 query_logs 的参数类型、必填项与取值范围 |
| parameter | 调用工具时传入的具体值，类型、必填、默认值都要在 schema 里写清 | start_time 必须传 ISO 8601 格式的时间串 |
| return value | 工具执行后返回给模型的数据，结构应稳定、可解析、带错误码 | 查询返回 {total, items, error}，而不是一段散文 |
| tool description | 给模型看的自然语言说明，告诉模型何时用、怎么用、边界在哪 | 描述里写明「仅查询当前环境近 7 天日志」 |
| tool selection | 模型根据任务与工具描述决定调用哪个工具的过程 | 「CPU 高」选 query_metrics，不选 generate_markdown_report |
| error handling | 工具失败时如何识别、记录、重试或降级的策略 | 日志服务超时返回错误码，Agent 转用备用查询路径 |
| retry | 对瞬时失败按策略再次调用，通常带退避与次数上限 | 查询超时后等待 1 秒重试 1 次 |
| permission | 工具能否被调用、由谁授权的规则，高风险操作必须显式授权 | 生成报告允许，删除数据拒绝 |
| side effect | 工具执行除返回值外对外部系统产生的影响，写操作要明确声明 | generate_markdown_report 会在草稿目录落盘文件 |

## 阅读重点

- 对应章节：第 4 章「工具」——工具分类、工具描述、工具调用决策与执行、异步工具、主动工具发现。
- 关注点：
  - 工具是 Agent 连接外部世界的方式，模型负责「决策」，执行交给代码。
  - 工具描述属于上下文的一部分，模型靠它判断何时调、调哪个、参数怎么填。
  - 「工具调用决策」与「工具执行」是两件事：模型可能选对工具但传错参数，也可能选错工具。
  - 返回值设计决定后续推理质量：结构化、带错误码、字段稳定。
- 补充材料：
  - Anthropic 官方 tool use 文档（tool schema 与 function calling 的写法）。
  - OpenAI function calling 文档（JSON Schema 参数声明示例）。
  - 《Agentic Design Patterns》第 5 章「工具使用」：https://adp.xindoo.xyz/chapters/Chapter%205_%20Tool%20Use ，从模式视角对照工具描述、调用决策与执行的分工。
  - 《Agentic Design Patterns》附录 B「AI 智能体交互：从 GUI 到真实世界环境」：https://adp.xindoo.xyz/chapters/Appendix%20B%20-%20AI%20Agentic%20Interactions_%20From%20GUI%20to%20Real%20world%20environment ，看工具如何让 Agent 与真实环境交互。

## 理解检查

- 工具描述写得太笼统（只说「查询日志」），模型会在哪些场景用错工具？
- 如果 schema 里把 end_time 标成必填、但用户没给结束时间，调用会发生什么？
- 查询接口返回结构不稳定（有时数组、有时对象），对 Agent 后续分析有什么影响？
- 哪些工具应该在调用前加权限确认？你的判断依据是什么？

## 实践任务

背景：你要为一个「性能排查 Agent」设计 3 个工具，Day 20 的 Demo 会直接复用。工具由代码实现，模型只负责选择与传参，所以定义的质量直接决定调用质量。

步骤：

- 为每个工具写一句话用途，包含触发场景与使用边界。
- 写输入参数 schema：类型、必填、默认值、取值范围。
- 设计返回结构：固定字段 + 错误码，保证可解析。
- 列出失败情况与对应处理方式（重试、报错、降级）。
- 标注权限要求与确认策略。

产出：一份 tools.md，包含 3 个工具的完整定义。

工具清单：

- query_logs(start_time, end_time, keyword)：按时间范围与关键词查询服务日志。
- query_metrics(metric_name, start_time, end_time)：查询指标曲线与聚合值。
- generate_markdown_report(title, sections)：把分析结果组装成 Markdown 报告文件。

## 输出模板

```text
工具名: [query_logs]
一句话用途: [在什么场景下、解决什么问题、不调用它的代价]
输入参数 (JSON Schema):
{
  "type": "object",
  "properties": {
    "start_time": {"type": "string", "format": "date-time", "description": "[开始时间，必填]"},
    "end_time": {"type": "string", "format": "date-time", "description": "[结束时间，必填]"},
    "keyword": {"type": "string", "description": "[过滤关键词，可选]"}
  },
  "required": ["[必填参数列表]"]
}
返回结构:
{
  "total": 0,
  "items": [{"time": "", "level": "", "message": ""}],
  "error": null
}
失败情况: [超时 / 参数非法 / 无权限] -> [重试 / 报错并说明原因 / 提示用户]
权限要求: [只读，无需确认] 或 [写入，需要确认]
```

## 示范输出

```text
工具名: query_logs
一句话用途: 按时间范围和关键词查询服务日志，用于定位报错与异常行为；不调用它，排查就只能靠猜。
输入参数 (JSON Schema):
{
  "type": "object",
  "properties": {
    "start_time": {"type": "string", "format": "date-time", "description": "查询起始时间，ISO 8601，必填"},
    "end_time": {"type": "string", "format": "date-time", "description": "查询结束时间，ISO 8601，必填"},
    "keyword": {"type": "string", "description": "过滤关键词，可选，如 ERROR 或接口名"}
  },
  "required": ["start_time", "end_time"]
}
返回结构:
{
  "total": 2,
  "items": [
    {"time": "2026-08-14T10:12:31", "level": "ERROR", "message": "timeout connecting to upstream"},
    {"time": "2026-08-14T10:15:02", "level": "WARN", "message": "worker_connections limit reached"}
  ],
  "error": null
}
失败情况: 超时 -> 重试 1 次，仍失败则返回错误码并说明；参数非法 -> 返回 400 与原因；无权限 -> 返回 403。
权限要求: 只读，无需人工确认，但查询范围限制在当前环境。
```

## 追问练习

- 工具失败时 Agent 应该怎么处理？「工具本身挂了」和「参数传错了」分别用什么策略？
- 如果把 generate_markdown_report 的返回设计成只返回文件名、不返回内容，对 Agent 下一步有什么影响？
- 工具描述和 schema 里的 description 分别写什么？写重复了会怎样？
- 什么情况下应该由工具内部自动重试，什么情况下应该由模型决定是否重试？

## 常见误区

- 工具调用不只是「会调 API」：关键是何时调、调哪个、参数对不对、结果怎么回填、失败怎么办。
- schema 写得太松：所有参数都设为可选，模型就会乱传，校验成本全落到执行端。
- 返回结构不稳定：字段名一改，Agent 的推理、缓存、eval 全部失效。
- 只写 happy path：不写失败情况，模型遇到错误时不知道下一步该做什么。

## 进阶扩展

- 工具超时与重试：生产环境每个工具要有独立超时上限，超时按退避重试，仍失败要进降级路径。
- 工具调用轨迹审计：每次调用的入参、出参、耗时都要记录，这是 eval 与排障的基础。
- 异步工具：耗时操作（如跑一次全量回归）返回任务 ID，Agent 稍后轮询结果，而不是阻塞等待。

## 今日作业

- 完成 3 个工具的定义，保存为 tools.md。
- 给每个工具补一个失败案例：怎么失败、Agent 应该怎么做。
- 把今天的工具与 Day 17 的 MCP server 对照：哪些定义可以直接复用。
- 明天开始前，用一句话向别人解释「工具调用决策」和「工具执行」的区别。

## 自检清单

- [ ] 我能为一个工具写出用途、参数 schema、返回结构与失败处理。
- [ ] 我能说清「工具调用决策」与「工具执行」的区别。
- [ ] 我能判断哪些工具需要权限确认。
- [ ] 我能设计稳定、可解析的返回结构。
- [ ] 我知道工具失败时至少有一种处理策略。
