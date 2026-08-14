# Day 13 - Retrieval Quality and Knowledge Organization

## 今日目标

能为知识库设计 metadata 与结构化索引，理解向量检索的局限。

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
| metadata | 元数据：描述文档属性（项目、环境、日期、版本等）的字段，用于过滤、排序与追溯 | 检索时限定"只查 order-service 生产环境" |
| structured index | 结构化索引：按字段组织文档目录，支持精确过滤与聚合 | 按文档类型统计知识库分布 |
| knowledge graph | 知识图谱：用实体与关系组织知识，支持多跳关联查询 | "WAF 与 Nginx 的关系"这类跨文档问题 |
| vector search limitation | 向量检索的局限：语义相近不等于事实正确，对数值、符号、权限不敏感 | "P95 超过 200ms"被检索成"P95 相关" |
| metadata filtering | 元数据过滤：先按字段筛掉不相关文档，再做向量检索 | 只检索 2026 年 8 月、生产环境的文档 |
| hybrid search | 混合检索：关键词检索与向量检索结合，互补字面与语义 | "Nginx 503"关键词命中加"服务不可用"语义命中 |
| staleness | 知识过期：知识库内容与真实系统不一致，导致回答过时 | 版本升级后旧排查步骤还在知识库 |
| precision and recall | 精确率与召回率：检索质量的两面，精确率衡量相关性，召回率衡量是否遗漏 | 评估检索对"CPU 升高"相关文档的覆盖 |
| document versioning | 文档版本：文档标注版本号，回答时引用正确版本 | 部署步骤引用 v3.0 而不是 v2.1 |
| index update | 索引更新：文档增删改后同步更新索引与向量 | 文档删除后向量库同步清理对应条目 |

## 阅读重点

- 对应章节：第 3 章中结构化索引、知识图谱、检索质量相关内容
- 关注点：只用向量检索的局限：语义相似但事实不同、数值与符号不敏感、无法表达权限
- 关注点：metadata 过滤如何缩小检索范围、提升精确率
- 关注点：知识图谱的适用场景：实体关系与多跳问题，什么时候才值得引入
- 关注点：知识库的过期问题：staleness 怎么发现、怎么处理
- 补充材料：向量数据库官方文档中关于 metadata filtering 的用法
- 补充材料：检索评估相关材料：recall@k、precision@k 的定义与口径
- 补充材料：《Agentic Design Patterns》第 14 章「知识检索（RAG）」：https://adp.xindoo.xyz/chapters/Chapter%2014_%20Knowledge%20Retrieval%20(RAG) ，重点看混合检索、元数据过滤与检索质量评估的实践。

## 理解检查

- 只用向量检索有什么局限？举一个"语义相近但答案错误"的例子。
- 元数据过滤能解决什么问题？它不能解决什么问题？
- 什么时候需要知识图谱？普通 metadata 加向量检索不够时的信号是什么？
- 如何发现知识库过期？你会在流程里加什么检查点？

## 实践任务

背景：你的团队有 50 篇测试文档（用例模板、排障手册、环境说明、缺陷规范），直接做向量检索时经常把测试环境文档混进生产环境问题的答案。今天给这些文档设计 metadata。

- 为 8 个字段做设计：项目名、环境、日期、文档类型、负责人、版本、关键系统、风险等级
- 每个字段确定：类型（string / enum / date / array）、取值示例、用途（过滤 / 排序 / 追溯 / 风险提示）、是否必填
- 用下方模板输出 schema 表，并给 2 条真实文档的 metadata 示例
- 写一条你工作中会用的 metadata 过滤条件，说明想达到的效果

## 输出模板

```text
# 测试文档库 Metadata Schema

## 字段定义
| 字段 | 类型 | 取值示例 | 用途 | 是否必填 |
|---|---|---|---|---|
| [project] | [string] | [order-service] | [过滤/分组] | [是] |
| [environment] | [enum] | [dev / staging / prod] | [过滤，避免跨环境误导] | [是] |
| [date] | [date] | [2026-08-14] | [排序与过期检查] | [是] |
| [doc_type] | [enum] | [manual / template / guideline] | [过滤] | [是] |
| [owner] | [string] | [张三] | [追溯与通知] | [否] |
| [version] | [string] | [v2.1] | [版本选择] | [是] |
| [key_system] | [array] | [nginx, mysql] | [跨系统检索] | [否] |
| [risk_level] | [enum] | [low / medium / high] | [回答前风险提示] | [否] |

## 两条示例记录
| 文档 | project | environment | date | doc_type | version | key_system | risk_level |
|---|---|---|---|---|---|---|---|
| [文档名] | [项目] | [环境] | [日期] | [类型] | [版本] | [系统] | [等级] |

## metadata 过滤示例
- 条件：[environment=prod AND project=order-service AND doc_type=manual]
- 期望效果：[只检索生产环境手册，排除测试环境文档]
```

## 示范输出

```text
# 测试文档库 Metadata Schema

## 字段定义
| 字段 | 类型 | 取值示例 | 用途 | 是否必填 |
|---|---|---|---|---|
| project | string | order-service | 过滤、分组 | 是 |
| environment | enum | dev / staging / prod | 过滤，避免跨环境误导 | 是 |
| date | date | 2026-08-14 | 排序与过期检查 | 是 |
| doc_type | enum | manual / template / guideline | 过滤 | 是 |
| owner | string | 李四 | 追溯与通知 | 否 |
| version | string | v2.1 | 版本选择 | 是 |
| key_system | array | nginx, mysql | 跨系统检索 | 否 |
| risk_level | enum | low / medium / high | 回答前风险提示 | 否 |

## 两条示例记录
| 文档 | project | environment | date | doc_type | version | key_system | risk_level |
|---|---|---|---|---|---|---|---|
| nginx-cpu-spike.md | order-service | prod | 2026-08-10 | manual | v2.1 | nginx, waf | high |
| load-test-template.md | order-service | staging | 2026-07-28 | template | v1.3 | nginx, jmeter | medium |

## metadata 过滤示例
- 条件：environment=prod AND project=order-service AND doc_type=manual
- 期望效果：用户问"Nginx CPU 升高"时只检索生产环境手册，不会把 staging 压测记录混进来
```

## 追问练习

- 检索结果相关但不准确怎么办？重排、过滤、生成端约束各能解决哪一部分？
- 如何发现知识库过期？可以设计哪些信号与检查（版本对比、最后更新时间、用户反馈）？
- 什么时候值得引入知识图谱？与 metadata 加向量检索相比，成本在哪里？
- 权限怎么进检索？不同用户应看到不同 metadata 范围的文档，检索端要做什么？

## 常见误区

- 以为 metadata 越多越好：字段膨胀会让录入和维护成本飙升，只保留真正用于过滤与追溯的字段。
- 以为向量检索结果一定相关：语义相近不等于事实正确，也表达不了"这是生产还是测试环境"。
- 文档进了向量库就不用维护：知识库会过期，没有更新机制的知识库会持续给出过时答案。
- 只用向量检索不用关键词：专有名词（order-service、P95）字面匹配更可靠，混合检索更稳。

## 进阶扩展

- 混合检索与 rerank：BM25 与向量检索并行召回，再用重排模型精排，是生产级检索的标配。
- 索引更新流水线：文档发布或删除时自动触发清洗、切分、向量化与 metadata 校验。
- 检索质量评估：用 recall@k、precision@k 与人工抽查评估检索，驱动 metadata 与切分策略调优。

## 今日作业

- 完成 metadata schema 表（8 个字段）与 2 条真实文档示例。
- 写一条你工作中会用到的 metadata 过滤条件，说明想达到的效果。
- 列出一个知识库过期的场景，设计一个能发现它的检查点。
- 明天用这个 schema 给 Day 14 的 Demo 数据打标签。

## 自检清单

- [ ] 我能说清向量检索的至少 3 个局限。
- [ ] 我能解释 metadata 过滤解决了什么问题、解决不了什么。
- [ ] 我能说出什么时候才值得引入知识图谱。
- [ ] 我的 schema 表有 8 个字段，每个都有类型与用途。
- [ ] 我知道明天要复习哪一点。
