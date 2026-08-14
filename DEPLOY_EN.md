[🇨🇳 中文](DEPLOY.md) | 🇬🇧 English

# Website Build and Deployment Guide

For the learning plan content, see [README_EN.md](README_EN.md). This guide covers only local builds, verification, and GitHub Pages deployment, for anyone who needs to build the site locally or adjust the deployment flow.

## Local Build and Preview

Prerequisites:

- Python 3.12 (the build script uses only the standard library; no dependency installation)
- git

Steps:

```bash
git clone https://github.com/naodeng/ai-agent-30-day-learning-plan.git
cd ai-agent-30-day-learning-plan
python3 scripts/build_site.py
python3 -m http.server 8000 --directory _site
```

Then open <http://localhost:8000> to preview the site.

A successful build generates 31 HTML pages under `_site/`: 1 index page and 30 daily lesson pages.

Note: `_site/` is generated output, ignored by `.gitignore`, and should not be committed; GitHub Actions regenerates it on every deployment.

## Verification Commands

Build and syntax check:

```bash
python3 scripts/build_site.py
python3 -m py_compile scripts/build_site.py
```

HTML link and list-marker verification (expected output: `html_count=31`, `missing_links=0`, `list_marker_leaks=0`):

```bash
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

Unit test:

```bash
python3 -m unittest tests/test_build_site.py
```

## Content Update and Publishing Flow

1. Edit `ai_agent_30_day_learning_plan.md` or `ai-agent-30-day-learning-plan/day-*.md`.
2. Run `python3 scripts/build_site.py`.
3. Preview `_site/` locally and verify the index, links, and page content.
4. Commit and push to `main`.
5. GitHub Actions builds and publishes to GitHub Pages automatically.

## GitHub Pages Deployment Setup

In the GitHub repository, open `Settings -> Pages`:

- Set `Build and deployment` source to `GitHub Actions`.

Site URL: <https://ai-agent-30-day-learning-plan.inaodeng.com/>

## Automated Deployment Flow

Deployment is handled by `.github/workflows/pages.yml`:

- Triggers: push to `main`, or manual `workflow_dispatch`.
- Required permissions: `contents: read`, `pages: write`, `id-token: write`.
- build job: `actions/checkout@v4` → `actions/setup-python@v5` (Python 3.12) → `python scripts/build_site.py` → `actions/upload-pages-artifact@v3` (uploads `_site/`).
- deploy job: runs in the `github-pages` environment and publishes the artifact with `actions/deploy-pages@v4`.
- The build script writes a `.nojekyll` file so GitHub Pages does not re-process the static files with Jekyll.

## Custom Domain

The site currently uses the custom domain `ai-agent-30-day-learning-plan.inaodeng.com`:

- DNS side: point the subdomain `ai-agent-30-day-learning-plan` to the GitHub Pages address; see the GitHub documentation for exact steps.
- Pages side: enter the domain under `Settings -> Pages -> Custom domain` and enable HTTPS.

To change the domain, update the DNS and Pages settings only; the build and deployment flow needs no changes.

Reference: <https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site>

## FAQ

- Styles missing after build? Preview via `python3 -m http.server` from the `_site/` directory; do not double-click the HTML files directly.
- Site unreachable or 404 after deployment? Confirm the Pages source is GitHub Actions and that the latest Actions run succeeded.
- To redeploy manually: open the Actions tab, select the `deploy` workflow, and click `Run workflow`.

## Related Documents

- Main course index: `ai_agent_30_day_learning_plan.md`
- Project README: [README_EN.md](README_EN.md)
- Maintenance conventions: `AGENTS.md`
