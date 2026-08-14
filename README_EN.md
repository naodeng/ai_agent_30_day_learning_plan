[🇨🇳 中文](README.md) | 🇬🇧 English

# AI Agent 30-Day Learning Plan

A 30-day AI Agent learning plan for beginners with a programming background, built around 李博杰《深入理解 AI Agent：设计原理与工程实践》 chapters 1, 2, 3, 4, 5, 6, 7, 8, and 10. It covers execution loops, context engineering, memory and RAG, tools and MCP, coding agents, evaluation, post-training, and multi-agent collaboration, ending with a small runnable and evaluable Agent.

Website: <https://ai-agent-30-day-learning-plan.inaodeng.com/>

---

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

## Course Structure

| Phase | Days | Focus |
| --- | --- | --- |
| Foundation | Day 01-05 | What an Agent is, the LLM's role, task decomposition, state and feedback, minimal Agent design |
| Context Engineering | Day 06-10 | Context composition, structured prompts, compression and summarization, Skills, context design document |
| Memory & RAG | Day 11-15 | User memory, the RAG pipeline, retrieval quality, a minimal RAG demo, memory + RAG design |
| Tools & MCP | Day 16-20 | Tool schemas, the MCP ecosystem, permission tiers, coding agents, a tool-based Agent demo |
| Evaluation & Evolution | Day 21-25 | Evaluation basics, metric design, eval sets, post-training concepts, feedback loops |
| Multi-Agent & Project | Day 26-30 | Multi-agent collaboration, communication and state, final project design and implementation, retrospective |

## Companion Reference: Agentic Design Patterns

Each day's 阅读重点 - 补充材料 section includes pointers to the Chinese translation of Google's "Agentic Design Patterns" (21 chapters + 7 appendices). The main course index includes a pattern-to-day mapping table for reverse lookup.

- Online reading: https://adp.xindoo.xyz/
- Source repository: https://github.com/naodeng/agentic-design-patterns

## Source Files

| Path | Purpose |
| --- | --- |
| `ai_agent_30_day_learning_plan.md` | Main 30-day course index and learning guide |
| `ai-agent-30-day-learning-plan/day-*.md` | Daily lesson source files |
| `scripts/build_site.py` | Markdown-to-static-site build script |
| `site/assets/` | Website styling and client-side behavior |
| `.github/workflows/pages.yml` | GitHub Pages deployment workflow |
| `AGENTS.md` | Project-level maintenance instructions for coding agents |

## 5-Minute Start

### 1. Clone the repository

```bash
git clone https://github.com/naodeng/ai-agent-30-day-learning-plan.git
cd ai-agent-30-day-learning-plan
```

### 2. Build the site

```bash
python3 scripts/build_site.py
```

### 3. Preview locally

```bash
python3 -m http.server 8000 --directory _site
```

Then open <http://localhost:8000> to view the generated site.

## Updating Course Content

1. Edit `ai_agent_30_day_learning_plan.md` or `ai-agent-30-day-learning-plan/day-*.md`.
2. Run `python3 scripts/build_site.py`.
3. Preview `_site/` locally and verify the index, links, and page content.
4. Push the change to `main`.
5. GitHub Actions will rebuild and update GitHub Pages automatically.

## Verification Commands

```bash
python3 scripts/build_site.py
python3 -m py_compile scripts/build_site.py
```

The current project should generate 31 HTML pages: 1 index page and 30 daily lesson pages.

## GitHub Pages Setup

In the GitHub repository, open `Settings -> Pages` and set `Build and deployment` source to `GitHub Actions`.

After that, every push to `main` triggers:

1. Checkout
2. Python setup
3. `scripts/build_site.py`
4. `_site/` artifact upload
5. GitHub Pages deployment

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
└── LICENSE
```

## Maintenance Rules

- Markdown is the single source of truth for course content.
- `_site/` is generated output and should not be committed.
- When adding or renaming lesson files, update the main index table at the same time.
- After changing generation logic, rerun the site build and Python compile check.

## License

This project is released under the repository [LICENSE](LICENSE). Course content and code may be used, modified, and distributed according to the license terms.
