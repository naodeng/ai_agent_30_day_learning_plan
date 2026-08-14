#!/usr/bin/env python3
"""Build the GitHub Pages site from the Markdown lesson sources."""

from __future__ import annotations

import html
import re
import shutil
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLAN_FILE = ROOT / "ai_agent_30_day_learning_plan.md"
LESSON_DIR = ROOT / "ai-agent-30-day-learning-plan"
ASSET_DIR = ROOT / "site" / "assets"
OUTPUT_DIR = ROOT / "_site"
HOMEPAGE_URL = "https://inaodeng.com"
HOMEPAGE_TITLE = "软件测试同学"
HOMEPAGE_ICON = "https://inaodeng.com/favicon.ico"
LICENSE_URL = "https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hans"
CLOUDFLARE_WEB_ANALYTICS = (
    "<!-- Cloudflare Web Analytics -->"
    "<script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' "
    "data-cf-beacon='{\"token\": \"554915042c8249b8bd1e1af4d53f3514\"}'></script>"
    "<!-- End Cloudflare Web Analytics -->"
)


@dataclass(frozen=True)
class Lesson:
    day: int
    source_stage: str
    topic: str
    chinese_topic: str
    goal: str
    source_path: Path
    slug: str
    phase_key: str
    phase_label: str
    phase_title: str
    accent: str

    @property
    def day_label(self) -> str:
        return f"Day {self.day:02d}"

    @property
    def href(self) -> str:
        return f"days/{self.slug}.html"


PHASES = [
    {
        "key": "Foundation",
        "label": "基础认知",
        "title": "基础认知",
        "id": "foundation",
        "range": "Day 01-05",
        "accent": "#0f766e",
        "days": range(1, 6),
    },
    {
        "key": "Context Engineering",
        "label": "上下文工程",
        "title": "上下文工程",
        "id": "context-engineering",
        "range": "Day 06-10",
        "accent": "#b45309",
        "days": range(6, 11),
    },
    {
        "key": "Memory & RAG",
        "label": "记忆与 RAG",
        "title": "记忆与 RAG",
        "id": "memory-rag",
        "range": "Day 11-15",
        "accent": "#2563eb",
        "days": range(11, 16),
    },
    {
        "key": "Tools & MCP",
        "label": "工具与 MCP",
        "title": "工具与 MCP",
        "id": "tools-mcp",
        "range": "Day 16-20",
        "accent": "#be123c",
        "days": range(16, 21),
    },
    {
        "key": "Evaluation & Evolution",
        "label": "评估与进化",
        "title": "评估与进化",
        "id": "evaluation-evolution",
        "range": "Day 21-25",
        "accent": "#4f46e5",
        "days": range(21, 26),
    },
    {
        "key": "Multi-Agent & Project",
        "label": "多 Agent 与项目",
        "title": "多 Agent 与项目",
        "id": "multi-agent-project",
        "range": "Day 26-30",
        "accent": "#7c2d12",
        "days": range(26, 31),
    },
]


def phase_for_day(day: int) -> dict[str, object]:
    for phase in PHASES:
        if day in phase["days"]:
            return phase
    raise ValueError(f"No phase configured for Day {day:02d}")


def slugify(value: str) -> str:
    value = value.lower()
    value = value.replace("&", "and")
    value = value.replace("qanda", "qanda")
    value = value.replace("q&a", "qanda")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def split_markdown_table_row(line: str) -> list[str]:
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    return cells


def parse_plan() -> list[Lesson]:
    lessons: list[Lesson] = []
    for line in PLAN_FILE.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| Day "):
            continue

        cells = split_markdown_table_row(line)
        if len(cells) != 6:
            continue

        day_text, source_stage, topic, chinese_topic, goal, file_cell = cells
        day_match = re.search(r"Day\s+(\d+)", day_text)
        link_match = re.search(r"\(([^)]+)\)", file_cell)
        if not day_match or not link_match:
            continue

        day = int(day_match.group(1))
        phase = phase_for_day(day)
        lessons.append(
            Lesson(
                day=day,
                source_stage=source_stage,
                topic=topic,
                chinese_topic=chinese_topic,
                goal=goal,
                source_path=ROOT / link_match.group(1),
                slug=slugify(f"day-{day:02d}-{topic}"),
                phase_key=str(phase["key"]),
                phase_label=str(phase["label"]),
                phase_title=str(phase["title"]),
                accent=str(phase["accent"]),
            )
        )

    if len(lessons) != 30:
        raise RuntimeError(f"Expected 30 lessons, found {len(lessons)}")

    missing = [lesson.source_path for lesson in lessons if not lesson.source_path.exists()]
    if missing:
        missing_list = "\n".join(str(path.relative_to(ROOT)) for path in missing)
        raise FileNotFoundError(f"Missing lesson Markdown files:\n{missing_list}")

    return sorted(lessons, key=lambda lesson: lesson.day)


def parse_inline(text: str) -> str:
    escaped = html.escape(text, quote=False)
    return re.sub(r"`([^`]+)`", lambda m: f"<code>{m.group(1)}</code>", escaped)


def render_table(lines: list[str]) -> str:
    rows = [split_markdown_table_row(line) for line in lines]
    header = rows[0]
    body = rows[2:]
    header_html = "".join(f"<th>{parse_inline(cell)}</th>" for cell in header)
    body_html = []
    for row in body:
        cells = "".join(f"<td>{parse_inline(cell)}</td>" for cell in row)
        body_html.append(f"<tr>{cells}</tr>")
    return (
        '<div class="table-wrap"><table><thead><tr>'
        + header_html
        + "</tr></thead><tbody>"
        + "".join(body_html)
        + "</tbody></table></div>"
    )


def render_list(lines: list[str], checklist: bool) -> str:
    if checklist:
        items = []
        for line in lines:
            checked = "checked" if line.startswith("- [x] ") or line.startswith("- [X] ") else ""
            text = re.sub(r"^- \[[ xX]\]\s+", "", line)
            items.append(
                '<li class="check"><label><input type="checkbox" '
                + checked
                + f"> <span>{parse_inline(text)}</span></label></li>"
            )
        return '<ul class="checklist">' + "".join(items) + "</ul>"

    items = [f"<li>{parse_inline(re.sub(r'^-\s+', '', line))}</li>" for line in lines]
    return "<ul>" + "".join(items) + "</ul>"


def markdown_to_html(markdown_text: str) -> str:
    lines = markdown_text.splitlines()
    blocks: list[str] = []
    paragraph: list[str] = []
    i = 0

    def flush_paragraph() -> None:
        if paragraph:
            text = " ".join(part.strip() for part in paragraph).strip()
            if text:
                blocks.append(f"<p>{parse_inline(text)}</p>")
            paragraph.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            flush_paragraph()
            i += 1
            continue

        if stripped.startswith("```"):
            flush_paragraph()
            code_lines: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            blocks.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
            i += 1
            continue

        if stripped.startswith("#"):
            flush_paragraph()
            level = len(stripped) - len(stripped.lstrip("#"))
            text = stripped[level:].strip()
            blocks.append(f"<h{level}>{parse_inline(text)}</h{level}>")
            i += 1
            continue

        if stripped.startswith("|"):
            flush_paragraph()
            table_lines: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            if len(table_lines) >= 3:
                blocks.append(render_table(table_lines))
            continue

        if stripped.startswith("- [") or stripped.startswith("- "):
            flush_paragraph()
            list_lines: list[str] = []
            checklist = stripped.startswith("- [")
            while i < len(lines):
                current = lines[i].strip()
                if checklist and current.startswith("- ["):
                    list_lines.append(current)
                    i += 1
                    continue
                if not checklist and current.startswith("- ") and not current.startswith("- ["):
                    list_lines.append(current)
                    i += 1
                    continue
                break
            blocks.append(render_list(list_lines, checklist))
            continue

        paragraph.append(line)
        i += 1

    flush_paragraph()
    return "\n".join(blocks)


def html_page(title: str, body: str, asset_prefix: str) -> str:
    return (
        '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f"<title>{html.escape(title)}</title>"
        '<meta name="theme-color" content="#0f766e">'
        f'<link rel="icon" type="image/svg+xml" href="{asset_prefix}assets/site-icon.svg">'
        f'<link rel="alternate icon" type="image/png" sizes="32x32" href="{asset_prefix}assets/favicon-32.png">'
        f'<link rel="apple-touch-icon" sizes="180x180" href="{asset_prefix}assets/apple-touch-icon.png">'
        f'<link rel="stylesheet" href="{asset_prefix}assets/style.css"></head><body>'
        + body
        + render_footer()
        + f'<script src="{asset_prefix}assets/app.js"></script>'
        + CLOUDFLARE_WEB_ANALYTICS
        + "</body></html>"
    )


def render_footer() -> str:
    return (
        '<footer class="site-footer">'
        '<p class="footer-slogan">先人机协作，再追求全自动。</p>'
        '<p class="footer-credit">'
        f'<a href="{HOMEPAGE_URL}" target="_blank" rel="noopener noreferrer">'
        "© 2026 软件测试同学 X naodeng</a>"
        '<span class="footer-sep">|</span>'
        f'<a href="{LICENSE_URL}" target="_blank" rel="noopener noreferrer">'
        "遵循 CC BY-NC-SA 4.0 许可协议</a>"
        "</p>"
        '<p class="footer-powered">由 Cloudflare &amp; Github &amp; AI 驱动</p>'
        "</footer>"
    )


def render_header(subtitle: str, home_prefix: str = "") -> str:
    return (
        '<header class="topbar"><nav class="nav">'
        f'<a class="brand" href="{home_prefix}index.html">'
        f'<img class="brand-icon" src="{home_prefix}assets/site-icon.svg" alt="" width="36" height="36"> '
        '<span class="brand-text"><span class="brand-title">AI Agent 30-Day Learning Plan</span>'
        f"<small>{html.escape(subtitle)}</small></span></a>"
        '<div class="nav-actions">'
        f'<a class="btn site-link" href="{HOMEPAGE_URL}" target="_blank" rel="noopener noreferrer">'
        f'<img class="site-icon" src="{HOMEPAGE_ICON}" alt="" width="12" height="12" loading="lazy"> '
        f"{html.escape(HOMEPAGE_TITLE)}</a>"
        '<button class="btn" onclick="window.print()">Print</button></div>'
        "</nav></header>"
    )


def render_index(lessons: list[Lesson]) -> str:
    cards_by_phase: dict[str, list[Lesson]] = {str(phase["key"]): [] for phase in PHASES}
    for lesson in lessons:
        cards_by_phase[lesson.phase_key].append(lesson)

    filter_buttons = [
        '<button class="filter active" data-filter="all"><span class="dot" style="background:#17201d"></span>全部</button>'
    ]
    toc_links = []
    phase_sections = []

    for phase in PHASES:
        key = str(phase["key"])
        label = str(phase["label"])
        title = str(phase["title"])
        phase_id = str(phase["id"])
        accent = str(phase["accent"])
        filter_buttons.append(
            f'<button class="filter" data-filter="{html.escape(key)}">'
            f'<span class="dot" style="background:{accent}"></span>{html.escape(label)}</button>'
        )
        toc_links.append(
            f'<a href="#{phase_id}"><span class="dot" style="background:{accent}"></span>{html.escape(title)}</a>'
        )
        cards = []
        for lesson in cards_by_phase[key]:
            cards.append(
                f'<a class="day-card" data-phase="{html.escape(lesson.phase_key)}" '
                f'href="{html.escape(lesson.href)}" style="--accent:{lesson.accent}">\n'
                f'  <div class="card-top"><span class="day-num" style="color:{lesson.accent}">'
                f"{lesson.day_label}</span><span class=\"badge\" style=\"color:{lesson.accent}\">"
                f"{html.escape(lesson.phase_label)}</span></div>\n"
                f"  <h3>{html.escape(lesson.topic)}</h3>\n"
                f"  <p>{html.escape(lesson.goal)}</p>\n"
                "</a>"
            )
        phase_sections.append(
            f'<section class="phase-band" id="{phase_id}"><div class="phase-head">'
            f"<h2>{html.escape(title)}</h2><span class=\"pill\">{html.escape(str(phase['range']))}</span>"
            f'</div><div class="cards">{"".join(cards)}</div></section>'
        )

    body = (
        render_header("context · tools · RAG · eval")
        + '<section class="hero"><div><div class="kicker">60 minutes a day · hands-on agent track</div>'
        + "<h1>Understanding AI Agents</h1>"
        + "<p class=\"lead\">从 Agent 执行循环与上下文工程出发，覆盖记忆与 RAG、工具与 MCP、Coding Agent、评估、后训练与多 Agent 协作，30 天做出一个可解释、可控、可改进的小型 Agent。</p>"
        + '<div class="study-strip"><div class="study-step"><b>0-10</b><span>概念</span></div>'
        + '<div class="study-step"><b>10-25</b><span>阅读</span></div>'
        + '<div class="study-step"><b>25-45</b><span>实践</span></div>'
        + '<div class="study-step"><b>45-55</b><span>追问</span></div>'
        + '<div class="study-step"><b>55-60</b><span>复盘</span></div></div></div>'
        + '<aside class="hero-right"><div class="hero-side-copy">'
        + '<div class="kicker">loop · context · tools · eval</div>'
        + '<h2>for AI Agent Builders</h2>'
        + '<p>每天 60 分钟，把概念读进去、把 Demo 做出来，用 eval 判断每一次改动是否真的变好。</p>'
        + '</div><div class="hero-panel"><div class="metrics">'
        + '<div class="metric"><b>30</b><span>daily lessons</span></div>'
        + '<div class="metric"><b>6</b><span>phased stages</span></div>'
        + '<div class="metric"><b>RAG</b><span>memory + retrieval track</span></div>'
        + '<div class="metric"><b>Eval</b><span>measure what improves</span></div>'
        + "</div></div></aside></section>"
        + '<main class="layout"><aside class="sidebar">'
        + '<input id="search" class="search" placeholder="Search agent, context, RAG, MCP, eval...">'
        + '<div class="section-title">阶段筛选</div><div class="filters">'
        + "".join(filter_buttons)
        + '</div><div class="section-title">目录区</div><div class="toc">'
        + "".join(toc_links)
        + '</div></aside><section class="content">'
        + '<div class="empty">没有匹配的课程，换个关键词试试。</div>'
        + "".join(phase_sections)
        + "</section></main>"
    )
    return html_page("AI Agent - 30 Day Learning Plan", body, "")


def render_lesson(lesson: Lesson, lessons: list[Lesson]) -> str:
    markdown = lesson.source_path.read_text(encoding="utf-8")
    article_html = markdown_to_html(markdown)
    previous_lesson = lessons[lesson.day - 2] if lesson.day > 1 else None
    next_lesson = lessons[lesson.day] if lesson.day < len(lessons) else None

    previous_link = (
        f'<a href="{html.escape(previous_lesson.slug)}.html">Previous<br>'
        f"<small>{previous_lesson.day_label} · {html.escape(previous_lesson.topic)}</small></a>"
        if previous_lesson
        else "<span></span>"
    )
    next_link = (
        f'<a href="{html.escape(next_lesson.slug)}.html">Next<br>'
        f"<small>{next_lesson.day_label} · {html.escape(next_lesson.topic)}</small></a>"
        if next_lesson
        else "<span></span>"
    )
    day_nav = f'<div class="day-nav">{previous_link}{next_link}</div>'

    header = (
        render_header("Back to 30-day plan", "../").replace(
            '<button class="btn" onclick="window.print()">Print</button>',
            '<a class="btn" href="../index.html">目录</a><button class="btn" onclick="window.print()">Print</button>',
        )
    )
    body = (
        header
        + '<main class="article">'
        + day_nav
        + '<article class="article-shell">'
        + f'<div class="kicker" style="color:{lesson.accent}">{html.escape(lesson.phase_label)}</div>'
        + '<div class="meta-row">'
        + f'<span class="pill">{lesson.day_label}</span>'
        + '<span class="pill">60 minutes</span>'
        + '<span class="pill">AI Agent 动手实践</span>'
        + "</div>"
        + f'<div class="lesson-body">{article_html}</div>'
        + "</article>"
        + day_nav
        + "</main>"
    )
    return html_page(f"{lesson.day_label} - {lesson.topic}", body, "../")


def build() -> None:
    lessons = parse_plan()
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)

    (OUTPUT_DIR / "days").mkdir(parents=True)
    shutil.copytree(ASSET_DIR, OUTPUT_DIR / "assets")
    (OUTPUT_DIR / ".nojekyll").write_text("", encoding="utf-8")
    (OUTPUT_DIR / "index.html").write_text(render_index(lessons), encoding="utf-8")

    for lesson in lessons:
        output_path = OUTPUT_DIR / "days" / f"{lesson.slug}.html"
        output_path.write_text(render_lesson(lesson, lessons), encoding="utf-8")

    print(f"Built {len(lessons)} lesson pages into {OUTPUT_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    build()
