🇨🇳 中文 | [🇬🇧 English](README_EN.md)

# AI Agent 30 天学习计划

面向有一定编程基础的新手的 30 天 AI Agent 学习计划，主线为李博杰《深入理解 AI Agent：设计原理与工程实践》第 1、2、3、4、5、6、7、8、10 章，覆盖执行循环、上下文工程、记忆与 RAG、工具与 MCP、Coding Agent、评估、后训练与多 Agent 协作，最终做出一个可运行、可评估的小型 Agent。

在线站点：<https://ai-agent-30-day-learning-plan.inaodeng.com/>

---

## 30 天课程总览

### 六阶段递进

| 阶段 | 天数 | 重点 |
| --- | --- | --- |
| 基础认知 | Day 01-05 | Agent 定义、LLM 角色、任务拆解、状态与反馈、最小 Agent 设计 |
| 上下文工程 | Day 06-10 | 上下文构成、结构化 Prompt、压缩与摘要、Skills、上下文设计文档 |
| 记忆与 RAG | Day 11-15 | 用户记忆、RAG 链路、检索质量、最小 RAG Demo、记忆 + RAG 设计 |
| 工具与 MCP | Day 16-20 | 工具 schema、MCP 生态、权限分级、Coding Agent、工具型 Agent Demo |
| 评估与进化 | Day 21-25 | 评估入门、指标设计、eval set、后训练概念、反馈闭环 |
| 多 Agent 与项目 | Day 26-30 | 多 Agent 协作、通信与状态、最终项目设计与实现、总结复盘 |

### 每日课程表

| Day | 阶段 | 主题 | 能力目标 | 时长 |
| --- | --- | --- | --- | --- |
| Day 01 | 基础认知 | 理解 AI Agent 是什么 | 能说清 Agent 与 Chatbot 的区别，画出观察-思考-行动-反馈执行循环 | 60 分钟 |
| Day 02 | 基础认知 | LLM 在 Agent 中的角色 | 能区分模型能力与系统工程能力，说清 LLM 的决策、推理与生成职责 | 60 分钟 |
| Day 03 | 基础认知 | 任务拆解与规划 | 能把模糊任务拆成可执行步骤，理解 planning 的粒度与动态调整 | 60 分钟 |
| Day 04 | 基础认知 | Agent 的状态与反馈 | 能把 Agent 理解为多轮状态机，说清状态、历史与工具反馈 | 60 分钟 |
| Day 05 | 基础认知 | 阶段复盘 1：最小 Agent 设计 | 能独立完成一页《日报生成 Agent v0.1》设计说明 | 60 分钟 |
| Day 06 | 上下文工程 | 上下文工程入门 | 能区分 system instruction、user message、tool description、memory 与检索内容 | 60 分钟 |
| Day 07 | 上下文工程 | Prompt 结构化设计 | 能把模糊指令改写成角色、目标、步骤、约束、输出格式齐全的结构化 Prompt | 60 分钟 |
| Day 08 | 上下文工程 | 上下文压缩与摘要 | 能设计摘要、裁剪与分层记忆策略，控制长任务上下文膨胀 | 60 分钟 |
| Day 09 | 上下文工程 | Agent Skills 与可复用上下文 | 能把重复工作流封装成可复用 Skill，写清适用场景与失败处理 | 60 分钟 |
| Day 10 | 上下文工程 | 阶段复盘 2：上下文设计文档 | 能输出《测试报告 Agent 上下文设计 v0.1》 | 60 分钟 |
| Day 11 | 记忆与 RAG | 用户记忆入门 | 能区分短期上下文与长期记忆，划定记忆边界与隐私约束 | 60 分钟 |
| Day 12 | 记忆与 RAG | RAG 基础 | 能说清洗切分、embedding、检索、重排、生成、引用完整链路 | 60 分钟 |
| Day 13 | 记忆与 RAG | 检索质量与知识组织 | 能为知识库设计 metadata 与结构化索引，理解向量检索局限 | 60 分钟 |
| Day 14 | 记忆与 RAG | 搭建最小 RAG Demo | 能实现本地文档加载、切分、检索、带引用的最小 RAG 问答 Demo | 60 分钟 |
| Day 15 | 记忆与 RAG | 阶段复盘 3：记忆 + RAG 设计 | 能输出《知识库问答 Agent 设计 v0.1》，理清记忆与知识边界 | 60 分钟 |
| Day 16 | 工具与 MCP | 工具调用基础 | 能为工具写清 schema、返回结构与失败处理，区分调用决策与执行 | 60 分钟 |
| Day 17 | 工具与 MCP | MCP 与工具生态 | 能说清 MCP 的 tools、resources、prompts 与接入价值 | 60 分钟 |
| Day 18 | 工具与 MCP | 工具安全与权限边界 | 能按只读、低风险写入、高风险写入分级设计工具权限 | 60 分钟 |
| Day 19 | 工具与 MCP | Coding Agent 入门 | 能设计修复测试脚本失败的 Coding Agent 完整流程 | 60 分钟 |
| Day 20 | 工具与 MCP | 阶段复盘 4：工具型 Agent Demo | 能做出调用 2-3 个工具完成 Nginx CPU 分析的 Agent Demo | 60 分钟 |
| Day 21 | 评估与进化 | Agent 评估入门 | 能设计任务集与评分标准，说清人工与自动评估如何结合 | 60 分钟 |
| Day 22 | 评估与进化 | 设计评估指标 | 能把「感觉好用」转化为主指标与护栏指标 | 60 分钟 |
| Day 23 | 评估与进化 | 构建小型 Eval Set | 能建立覆盖失败场景、带 must_not_do 与评分标准的评估集 | 60 分钟 |
| Day 24 | 评估与进化 | 模型后训练概念 | 能区分预训练、SFT、RL，知道何时不该急着训练模型 | 60 分钟 |
| Day 25 | 评估与进化 | 持续进化与反馈闭环 | 能设计轨迹日志与反馈沉淀流程，让 Agent 越用越好 | 60 分钟 |
| Day 26 | 多 Agent 与项目 | 多 Agent 协作基础 | 能设计 Planner/Research/Writer/Reviewer 角色分工与上下文边界 | 60 分钟 |
| Day 27 | 多 Agent 与项目 | 多 Agent 通信与状态 | 能设计 Agent 间消息格式、中间产物与冲突处理 | 60 分钟 |
| Day 28 | 多 Agent 与项目 | 最终项目设计 | 能定义技术问题分析 Agent 的 MVP 范围与成功标准 | 60 分钟 |
| Day 29 | 多 Agent 与项目 | 最终项目实现与评估 | 能完成可演示版本，并用评估集跑出成功与失败案例 | 60 分钟 |
| Day 30 | 多 Agent 与项目 | 总结、复盘与下一阶段路线 | 能输出 30 天学习复盘与下一阶段学习方向 | 60 分钟 |

### 每天 60 分钟学习节奏

| 时间 | 内容 | 目标 |
| --- | --- | --- |
| 0-10 分钟 | 核心概念与术语 | 先掌握当天主题的关键概念，建立最小认知框架 |
| 10-25 分钟 | 阅读/章节输入 | 精读对应章节重点，只抓问题、思路、结论 |
| 25-45 分钟 | 实践任务 | 动手完成输出模板，必须产出一份可复用产物 |
| 45-55 分钟 | 追问与反思 | 回答追问练习，标记卡住的概念 |
| 55-60 分钟 | 复盘与作业 | 整理自检清单，定下明天要复习的一点 |

如果当天时间充足，可以再花 30-60 分钟完成「进阶扩展」或打磨 Demo。

### 30 天目标

- 能用自己的话解释 Agent 是什么，说清 Agent 与普通 Chatbot 的区别，画出「观察 → 思考 → 行动 → 反馈」执行循环。
- 能设计 system prompt、任务上下文、压缩与摘要策略，封装可复用 Skill，输出上下文设计文档。
- 能说清记忆、知识库与 RAG 的完整链路，并搭建一个最小 RAG 问答 Demo。
- 能为 Agent 设计工具 schema、权限分级，理解 MCP 协议与 Coding Agent 工作流，做出工具型 Agent Demo。
- 能建立小型 eval set，设计主指标与护栏指标，理解后训练与持续进化的边界。
- 能判断何时需要多 Agent，设计协作与通信机制，并完成一个综合 Agent 项目。
- 30 天后能完成最小闭环：设计上下文、接工具、查知识库、记录轨迹、用 eval 判断好坏，做出一个可解释、可控、可改进的小型 Agent。

### 30 天后的交付物

- 一张 Agent 架构图与一份上下文设计文档。
- 一个最小 RAG 问答 Demo。
- 一个能调用 2-3 个工具完成自动化任务的 Agent Demo。
- 一套 20 条用例的 eval set 与评估结论。
- 一个综合 Agent MVP 项目（技术问题分析 Agent）。
- 一份 30 天学习复盘与下一阶段学习路线。

## 为什么用这个项目

| 能力 | 说明 |
| --- | --- |
| 30 天渐进训练 | 从 Agent 基础概念、上下文工程到 RAG、工具、评估与多 Agent，按学习主线递进 |
| 概念 + 动手并重 | 每天 60 分钟固定节奏：核心概念、章节精读、实践任务、追问反思、复盘作业 |
| 测试/QA 场景优先 | 所有示例围绕测试报告、缺陷分析、Nginx 排查、日志与指标查询等真实工作场景 |
| 交付物驱动 | 每 5 天一次小复盘，每 10 天形成一个可运行成果，30 天完成综合 Agent 项目 |
| Markdown 源文件 | 课程内容全部由 Markdown 维护，便于阅读、修改和版本管理 |
| GitHub Pages 自动发布 | 提交到 `main` 后由 GitHub Actions 自动生成并部署静态站点 |

这个项目适合想系统理解 AI Agent 并动手做 Demo 的工程师、测试开发、质量工程师，以及所有想从「用 Agent」走向「做 Agent」的同学。

## 你会得到什么

- 1 份完整的 30 天学习总计划
- 30 个每日学习 Markdown 文件
- 每天 60 分钟的固定学习节奏
- 覆盖概念、阅读、实践、追问和自检的练习内容
- 可本地生成和部署到 GitHub Pages 的静态网站

## 配套参考书：Agentic Design Patterns

每天课程的「阅读重点 - 补充材料」都配有 Google《Agentic Design Patterns》（智能体设计模式）中文翻译版的对照阅读条目（21 章 + 7 个附录），总目录附有「模式对照表」，可按天反查每个模式。

- 在线阅读：https://adp.xindoo.xyz/
- 原书仓库：https://github.com/naodeng/agentic-design-patterns

## 快速开始

克隆并生成本地站点：

```bash
git clone https://github.com/naodeng/ai-agent-30-day-learning-plan.git
cd ai-agent-30-day-learning-plan
python3 scripts/build_site.py
python3 -m http.server 8000 --directory _site
```

然后打开 <http://localhost:8000> 查看站点。

构建、验证、GitHub Pages 部署与自定义域名的详细说明见部署文档：[DEPLOY.md](DEPLOY.md)（[English](DEPLOY_EN.md)）。

## 仓库结构

```text
ai_agent_30_day_learning_plan/
├── .github/workflows/pages.yml
├── scripts/
│   └── build_site.py
├── site/
│   └── assets/
│       ├── app.js
│       └── style.css
├── ai-agent-30-day-learning-plan/
│   └── day-*.md
├── ai_agent_30_day_learning_plan.md
├── AGENTS.md
├── README.md
├── README_EN.md
├── DEPLOY.md
├── DEPLOY_EN.md
└── LICENSE
```

## 维护原则

- Markdown 是唯一课程内容源。
- README 的每日课程表必须与总目录 `ai_agent_30_day_learning_plan.md` 保持同步。
- 部署相关内容只写在 `DEPLOY.md` / `DEPLOY_EN.md`，不在 README 中重复。
- README 与 DEPLOY 的中英版本为镜像文档，改动需成对进行。
- `_site/` 是构建产物，不提交到仓库。
- 修改生成逻辑后，必须重新运行构建和 Python 语法检查。

## 许可证

本项目基于仓库内 [LICENSE](LICENSE) 发布。课程内容和代码可按许可证条款使用、修改和分发。
