🇨🇳 中文 | [🇬🇧 English](README_EN.md)

# AI Agent 30 天学习计划

面向有一定编程基础的新手的 30 天 AI Agent 学习计划，主线为李博杰《深入理解 AI Agent：设计原理与工程实践》第 1、2、3、4、5、6、7、8、10 章，覆盖执行循环、上下文工程、记忆与 RAG、工具与 MCP、Coding Agent、评估、后训练与多 Agent 协作，最终做出一个可运行、可评估的小型 Agent。

在线站点：<https://ai-agent-30-day-learning-plan.inaodeng.com/>

---

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

## 课程结构

| 阶段 | 天数 | 重点 |
| --- | --- | --- |
| 基础认知 | Day 01-05 | Agent 定义、LLM 角色、任务拆解、状态与反馈、最小 Agent 设计 |
| 上下文工程 | Day 06-10 | 上下文构成、结构化 Prompt、压缩与摘要、Skills、上下文设计文档 |
| 记忆与 RAG | Day 11-15 | 用户记忆、RAG 链路、检索质量、最小 RAG Demo、记忆 + RAG 设计 |
| 工具与 MCP | Day 16-20 | 工具 schema、MCP 生态、权限分级、Coding Agent、工具型 Agent Demo |
| 评估与进化 | Day 21-25 | 评估入门、指标设计、eval set、后训练概念、反馈闭环 |
| 多 Agent 与项目 | Day 26-30 | 多 Agent 协作、通信与状态、最终项目设计与实现、总结复盘 |

## 内容源文件

| 路径 | 说明 |
| --- | --- |
| `ai_agent_30_day_learning_plan.md` | 30 天总目录和学习说明 |
| `ai-agent-30-day-learning-plan/day-*.md` | 每日课程源文件 |
| `scripts/build_site.py` | Markdown 到静态网站的构建脚本 |
| `site/assets/` | 网站样式和前端交互 |
| `.github/workflows/pages.yml` | GitHub Pages 自动部署流程 |
| `AGENTS.md` | 给 coding agents 使用的项目级维护说明 |

## 5 分钟开始

### 1. 克隆项目

```bash
git clone https://github.com/naodeng/ai-agent-30-day-learning-plan.git
cd ai-agent-30-day-learning-plan
```

### 2. 生成网站

```bash
python3 scripts/build_site.py
```

### 3. 本地预览

```bash
python3 -m http.server 8000 --directory _site
```

然后打开 <http://localhost:8000> 查看生成后的站点。

## 更新课程内容

1. 修改 `ai_agent_30_day_learning_plan.md` 或 `ai-agent-30-day-learning-plan/day-*.md`。
2. 运行 `python3 scripts/build_site.py`。
3. 本地预览 `_site/`，确认目录、链接和页面内容正常。
4. 提交到 `main`。
5. GitHub Actions 会自动构建并更新 GitHub Pages。

## 验证命令

```bash
python3 scripts/build_site.py
python3 -m py_compile scripts/build_site.py
```

当前项目构建后应生成 31 个 HTML 页面：1 个首页 + 30 个每日课程页。

## GitHub Pages 设置

在 GitHub 仓库页面进入 `Settings -> Pages`，将 `Build and deployment` 的 `Source` 设置为 `GitHub Actions`。

之后每次 push 到 `main` 都会触发：

1. Checkout 仓库
2. 安装 Python
3. 运行 `scripts/build_site.py`
4. 上传 `_site/` artifact
5. 发布到 GitHub Pages

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
└── LICENSE
```

## 维护原则

- Markdown 是唯一课程内容源。
- `_site/` 是构建产物，不提交到仓库。
- 新增或重命名课程文件时，同步更新总目录表格。
- 修改生成逻辑后，必须重新运行构建和 Python 语法检查。

## 许可证

本项目基于仓库内 [LICENSE](LICENSE) 发布。课程内容和代码可按许可证条款使用、修改和分发。
