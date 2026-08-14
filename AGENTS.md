# AGENTS.md

This file gives coding agents the project-specific context needed to maintain this repository.

## Project Overview

- This repository contains a 30-day AI Agent learning plan for beginners with a programming background.
- The source of truth is Markdown:
  - Main course index: `ai_agent_30_day_learning_plan.md`
  - Daily lessons: `ai-agent-30-day-learning-plan/day-*.md`
- The published website is generated from the Markdown sources by `scripts/build_site.py`.
- GitHub Pages is deployed through `.github/workflows/pages.yml` after pushes to `main`.
- The course follows 李博杰《深入理解 AI Agent：设计原理与工程实践》 chapters 1, 2, 3, 4, 5, 6, 7, 8, and 10.

## Source and Generated Files

- Edit Markdown source files for course content changes.
- Edit `site/assets/style.css` and `site/assets/app.js` for website presentation or client-side behavior.
- Edit `scripts/build_site.py` only when the Markdown-to-HTML generation behavior must change.
- Do not edit `_site/`; it is generated output and is ignored by Git.

## Build and Preview Commands

- Build the site:

  ```bash
  python3 scripts/build_site.py
  ```

- Preview locally:

  ```bash
  python3 -m http.server 8000 --directory _site
  ```

- Compile-check the generator:

  ```bash
  python3 -m py_compile scripts/build_site.py
  ```

## Verification Before Finishing

Run these checks after changes that affect content, generation, assets, or publishing:

```bash
python3 scripts/build_site.py
python3 -m py_compile scripts/build_site.py
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        link = data.get("href") or data.get("src")
        if link:
            self.links.append(link)

root = Path("_site")
missing = []
for path in root.rglob("*.html"):
    parser = LinkParser()
    parser.feed(path.read_text(encoding="utf-8"))
    for link in parser.links:
        if link.startswith(("http:", "https:", "#")):
            continue
        target = (path.parent / link.split("#", 1)[0]).resolve()
        if not target.exists():
            missing.append((str(path), link))

html_files = list(root.rglob("*.html"))
list_marker_leaks = [
    str(path)
    for path in html_files
    if "<li>-" in path.read_text(encoding="utf-8")
]
print(f"html_count={len(html_files)}")
print(f"missing_links={len(missing)}")
print(f"list_marker_leaks={len(list_marker_leaks)}")
if missing:
    raise SystemExit(missing[:10])
if list_marker_leaks:
    raise SystemExit(list_marker_leaks[:10])
PY
```

Expected result for the current project: `html_count=31`, `missing_links=0`, and `list_marker_leaks=0`.

## Markdown Content Guidelines

- Keep the main index table in `ai_agent_30_day_learning_plan.md` at exactly 30 lesson rows unless intentionally changing the course length.
- The index table has 6 columns: Day, 阶段 (phase key), 主题 (English topic), 中文主题, 能力目标, 文件 (relative link to the lesson file).
- Phase keys must match the `PHASES` list in `scripts/build_site.py`: `Foundation`, `Context Engineering`, `Memory & RAG`, `Tools & MCP`, `Evaluation & Evolution`, `Multi-Agent & Project`.
- When adding or renaming a daily lesson, update both the main index row and the corresponding file in `ai-agent-30-day-learning-plan/`.
- Preserve the daily lesson structure unless the change applies across the whole course:
  - `今日目标`
  - `学习安排`
  - `核心概念`
  - `阅读重点`
  - `理解检查`
  - `实践任务`
  - `输出模板`
  - `示范输出`
  - `追问练习`
  - `常见误区`
  - `进阶扩展`
  - `今日作业`
  - `自检清单`
- Keep examples practical for testing/QA work: test reports, defect analysis, Nginx troubleshooting, log and metric queries, RAG knowledge bases, and eval sets.
- Bilingual content is expected. Keep Chinese explanations clear and use English terms where they are the learning target (e.g. context, tool calling, RAG, MCP, eval).
- The 补充材料 block of each daily lesson may contain 《Agentic Design Patterns》 reading pointers. Format per item: `《Agentic Design Patterns》第 N 章「中文名」：URL ，一句模式视角说明` (appendices use `附录 X「中文名」`). URLs are %20-encoded plain text, preferring `adp.xindoo.xyz/chapters/...` over GitHub blob links. No markdown links, bold, or ordered lists.
- The 模式对照表 in `ai_agent_30_day_learning_plan.md` (21 chapters + 引言/结语 + 7 appendices) must stay in sync with the day-file pointers. Its table rows must not start with `| Day ` — the build script only parses lines beginning with `| Day `.
- `README.md` and `README_EN.md` are mirrored documents; change both together. The 30-row daily lesson table in the READMEs must stay in sync with the course index rows in `ai_agent_30_day_learning_plan.md`.
- Deployment, build, verification, and GitHub Pages content belongs in `DEPLOY.md` / `DEPLOY_EN.md` only — do not duplicate it in the READMEs.

## Generator Constraints

- `scripts/build_site.py` intentionally uses only the Python standard library so GitHub Actions does not need dependency installation.
- The Markdown renderer is deliberately small. It supports the syntax currently used by the course:
  - headings
  - paragraphs
  - fenced code blocks
  - pipe tables
  - unordered lists
  - checklist items
  - inline code
- Lesson files must NOT use ordered lists, bold text, links, images, or HTML, because the renderer does not support them.
- If new Markdown syntax is introduced, update the generator and add verification that the generated HTML still renders correctly.
- Keep generated links relative so the site works under a GitHub Pages project path.

## Publishing Notes

- GitHub Pages must use `GitHub Actions` as the Pages source.
- The workflow publishes `_site/` via `actions/upload-pages-artifact` and `actions/deploy-pages`.
- Do not commit `_site/`; GitHub Actions regenerates it on each push to `main`.
- Human-facing deployment documentation lives in `DEPLOY.md` / `DEPLOY_EN.md`. When the workflow or deployment flow changes, update both deployment docs in the same change.

## Git Hygiene

- Preserve user-authored Markdown content and avoid broad rewrites.
- Keep changes small and scoped to content, generator, assets, workflow, or documentation.
- Before staging, check `git status -sb --ignored` and confirm generated directories remain ignored.
- Do not remove or overwrite course files unless the user explicitly asks.
