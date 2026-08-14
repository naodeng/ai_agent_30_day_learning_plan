[🇨🇳 中文](README.md) | 🇬🇧 English

# AI Agent 30-Day Learning Plan

A 30-day AI Agent learning plan for beginners with a programming background, built around 李博杰《深入理解 AI Agent：设计原理与工程实践》 chapters 1, 2, 3, 4, 5, 6, 7, 8, and 10. It covers execution loops, context engineering, memory and RAG, tools and MCP, coding agents, evaluation, post-training, and multi-agent collaboration, ending with a small runnable and evaluable Agent.

Website: <https://ai-agent-30-day-learning-plan.inaodeng.com/>

---

## 30-Day Course Overview

### Six Phases

| Phase | Days | Focus |
| --- | --- | --- |
| Foundation | Day 01-05 | What an Agent is, the LLM's role, task decomposition, state and feedback, minimal Agent design |
| Context Engineering | Day 06-10 | Context composition, structured prompts, compression and summarization, Skills, context design document |
| Memory & RAG | Day 11-15 | User memory, the RAG pipeline, retrieval quality, a minimal RAG demo, memory + RAG design |
| Tools & MCP | Day 16-20 | Tool schemas, the MCP ecosystem, permission tiers, coding agents, a tool-based Agent demo |
| Evaluation & Evolution | Day 21-25 | Evaluation basics, metric design, eval sets, post-training concepts, feedback loops |
| Multi-Agent & Project | Day 26-30 | Multi-agent collaboration, communication and state, final project design and implementation, retrospective |

### Daily Lessons

| Day | Phase | Topic | Goal | Duration |
| --- | --- | --- | --- | --- |
| Day 01 | Foundation | Understanding What an AI Agent Is | Explain the difference between an Agent and a Chatbot, and draw the observe-think-act-feedback loop | 60 min |
| Day 02 | Foundation | The Role of the LLM Inside an Agent | Distinguish model capability from system engineering; explain the LLM's decision, reasoning, and generation roles | 60 min |
| Day 03 | Foundation | Task Decomposition and Planning | Break vague tasks into executable steps; understand planning granularity and dynamic adjustment | 60 min |
| Day 04 | Foundation | Agent State and Feedback | Model an Agent as a multi-turn state machine; explain state, history, and tool feedback | 60 min |
| Day 05 | Foundation | Weekly Review 1: Minimal Agent Design | Independently produce a one-page "Daily Report Agent v0.1" design doc | 60 min |
| Day 06 | Context Engineering | Context Engineering Basics | Distinguish system instruction, user message, tool description, memory, and retrieved content | 60 min |
| Day 07 | Context Engineering | Structured Prompt Design | Rewrite vague instructions into structured prompts with role, goal, steps, constraints, and output format | 60 min |
| Day 08 | Context Engineering | Context Compression and Summarization | Design summarization, trimming, and layered-memory strategies to control context growth in long tasks | 60 min |
| Day 09 | Context Engineering | Agent Skills and Reusable Context | Package repeated workflows into reusable Skills with clear use cases and failure handling | 60 min |
| Day 10 | Context Engineering | Weekly Review 2: Context Design Document | Produce a "Test Report Agent Context Design v0.1" document | 60 min |
| Day 11 | Memory & RAG | User Memory Basics | Distinguish short-term context from long-term memory; define memory boundaries and privacy constraints | 60 min |
| Day 12 | Memory & RAG | RAG Basics | Explain the full pipeline: chunking, embedding, retrieval, reranking, generation, citation | 60 min |
| Day 13 | Memory & RAG | Retrieval Quality and Knowledge Organization | Design metadata and structured indexes for a knowledge base; understand vector retrieval limits | 60 min |
| Day 14 | Memory & RAG | Building a Minimal RAG Demo | Build a minimal RAG Q&A demo with local document loading, chunking, retrieval, and citations | 60 min |
| Day 15 | Memory & RAG | Weekly Review 3: Memory + RAG Design | Produce a "Knowledge Base Q&A Agent Design v0.1" and clarify memory vs. knowledge boundaries | 60 min |
| Day 16 | Tools & MCP | Tool Calling Basics | Write clear tool schemas, return structures, and failure handling; separate call decisions from execution | 60 min |
| Day 17 | Tools & MCP | MCP and the Tool Ecosystem | Explain MCP tools, resources, prompts, and the value of adoption | 60 min |
| Day 18 | Tools & MCP | Tool Safety and Permission Boundaries | Design tool permissions by read-only, low-risk write, and high-risk write tiers | 60 min |
| Day 19 | Tools & MCP | Coding Agent Basics | Design a complete Coding Agent flow for fixing failing test scripts | 60 min |
| Day 20 | Tools & MCP | Weekly Review 4: Tool-Based Agent Demo | Build an Agent demo that calls 2-3 tools to analyze Nginx CPU usage | 60 min |
| Day 21 | Evaluation & Evolution | Agent Evaluation Basics | Design task sets and scoring rubrics; explain how human and automated evaluation combine | 60 min |
| Day 22 | Evaluation & Evolution | Designing Eval Metrics | Turn "feels good" into primary metrics and guardrail metrics | 60 min |
| Day 23 | Evaluation & Evolution | Building a Small Eval Set | Build an eval set covering failure cases, with must_not_do rules and scoring rubrics | 60 min |
| Day 24 | Evaluation & Evolution | Model Post-Training Concepts | Distinguish pretraining, SFT, and RL; know when NOT to rush into training | 60 min |
| Day 25 | Evaluation & Evolution | Continuous Improvement and Feedback Loops | Design trajectory logging and feedback pipelines so the Agent keeps improving | 60 min |
| Day 26 | Multi-Agent & Project | Multi-Agent Collaboration Basics | Design Planner/Research/Writer/Reviewer role separation and context boundaries | 60 min |
| Day 27 | Multi-Agent & Project | Multi-Agent Communication and State | Design inter-agent message formats, intermediate artifacts, and conflict handling | 60 min |
| Day 28 | Multi-Agent & Project | Final Project Design | Define the MVP scope and success criteria for a technical problem analysis Agent | 60 min |
| Day 29 | Multi-Agent & Project | Final Project Implementation and Eval | Complete a demoable version and run success/failure cases through the eval set | 60 min |
| Day 30 | Multi-Agent & Project | Summary, Retrospective, and Next Steps | Produce a 30-day retrospective and a next-stage learning direction | 60 min |

### Daily 60-Minute Routine

| Time | Section | Goal |
| --- | --- | --- |
| 0-10 min | Core concepts and terms | Master the day's key concepts and build a minimal mental model |
| 10-25 min | Reading input | Read the relevant chapter closely; capture problems, ideas, and conclusions only |
| 25-45 min | Hands-on task | Complete the output template; produce one reusable artifact |
| 45-55 min | Follow-up and reflection | Answer the follow-up questions; mark concepts that are still unclear |
| 55-60 min | Review and homework | Go through the self-check list; pick one point to review tomorrow |

With extra time, spend 30-60 more minutes on the "advanced extension" section or polish the demo.

### 30-Day Goals

- Explain in your own words what an Agent is and how it differs from a plain Chatbot; draw the observe → think → act → feedback loop.
- Design system prompts, task context, compression and summarization strategies, package reusable Skills, and produce a context design document.
- Explain the full memory, knowledge base, and RAG pipeline, and build a minimal RAG Q&A demo.
- Design tool schemas and permission tiers for an Agent, understand MCP and Coding Agent workflows, and build a tool-based Agent demo.
- Build a small eval set, design primary and guardrail metrics, and understand the boundaries of post-training and continuous evolution.
- Judge when multiple agents are needed, design collaboration and communication mechanisms, and complete a comprehensive Agent project.
- After 30 days, close the minimal loop: design context, connect tools, query knowledge bases, log trajectories, judge quality with evals, and ship a small Agent that is explainable, controllable, and improvable.

### Deliverables After 30 Days

- One Agent architecture diagram and one context design document.
- One minimal RAG Q&A demo.
- One Agent demo that calls 2-3 tools to automate a task.
- One eval set with 20 cases and an evaluation report.
- One comprehensive Agent MVP project (technical problem analysis Agent).
- One 30-day retrospective and a next-stage learning roadmap.

## Why This Project

| Capability | Description |
| --- | --- |
| 30-day progression | Moves from Agent fundamentals and context engineering to RAG, tools, evaluation, and multi-agent systems |
| Concepts plus hands-on work | A fixed 60-minute routine per day: core concepts, chapter reading, hands-on task, follow-up questions, review |
| Testing/QA-first scenarios | Every example is grounded in test reports, defect analysis, Nginx troubleshooting, and log/metric queries |
| Deliverable-driven | A small review every 5 days, a runnable result every 10 days, and a complete Agent project by day 30 |
| Markdown source files | Course content is maintained as Markdown for readable diffs and easy editing |
| GitHub Pages publishing | Pushes to `main` trigger GitHub Actions to build and deploy the static site |

This project is designed for engineers, SDETs, and quality engineers who want to understand AI Agents systematically and build demos, moving from "using Agents" to "building Agents".

## What You Get

- One complete 30-day learning plan
- 30 daily lesson Markdown files
- A fixed 60-minute daily learning routine
- Practice materials covering concepts, reading, hands-on work, follow-up questions, and self-checks
- A static website that can be generated locally and deployed to GitHub Pages

## Companion Reference: Agentic Design Patterns

Each day's 阅读重点 - 补充材料 section includes pointers to the Chinese translation of Google's "Agentic Design Patterns" (21 chapters + 7 appendices). The main course index includes a pattern-to-day mapping table for reverse lookup.

- Online reading: https://adp.xindoo.xyz/
- Source repository: https://github.com/naodeng/agentic-design-patterns

## Quick Start

Clone and build the local site:

```bash
git clone https://github.com/naodeng/ai-agent-30-day-learning-plan.git
cd ai-agent-30-day-learning-plan
python3 scripts/build_site.py
python3 -m http.server 8000 --directory _site
```

Then open <http://localhost:8000> to view the site.

For detailed build, verification, GitHub Pages deployment, and custom domain instructions, see the deployment guide: [DEPLOY_EN.md](DEPLOY_EN.md) ([中文](DEPLOY.md)).

## Repository Structure

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

## Maintenance Rules

- Markdown is the single source of truth for course content.
- The daily lesson table in the README must stay in sync with the course index `ai_agent_30_day_learning_plan.md`.
- Deployment-related content belongs in `DEPLOY.md` / `DEPLOY_EN.md` only, not duplicated in the README.
- The Chinese and English versions of README and DEPLOY are mirrored documents; change them in pairs.
- `_site/` is generated output and should not be committed.
- After changing generation logic, rerun the site build and Python compile check.

## License

This project is released under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) (Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International), consistent with the website footer. Both course content and code may be used, modified, and distributed under those terms; the full text is in the repository [LICENSE](LICENSE).
