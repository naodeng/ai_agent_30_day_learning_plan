🇨🇳 中文 | [🇬🇧 English](DEPLOY_EN.md)

# 网站构建与部署文档

学习计划内容见 [README.md](README.md)。本文档只讲本地构建、验证与 GitHub Pages 部署，供需要本地搭建站点或调整部署流程的人查看。

## 本地构建与预览

前置要求：

- Python 3.12（构建脚本只使用标准库，无需安装依赖）
- git

步骤：

```bash
git clone https://github.com/naodeng/ai-agent-30-day-learning-plan.git
cd ai-agent-30-day-learning-plan
python3 scripts/build_site.py
python3 -m http.server 8000 --directory _site
```

然后打开 <http://localhost:8000> 预览站点。

构建成功后应在 `_site/` 生成 31 个 HTML 页面：1 个首页 + 30 个每日课程页。

说明：`_site/` 是构建产物，已在 `.gitignore` 中忽略，不需要提交；GitHub Actions 会在每次部署时重新生成。

## 验证命令

构建与语法检查：

```bash
python3 scripts/build_site.py
python3 -m py_compile scripts/build_site.py
```

HTML 链接与列表标记校验（预期输出 `html_count=31`、`missing_links=0`、`list_marker_leaks=0`）：

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

单元测试：

```bash
python3 -m unittest tests/test_build_site.py
```

## 内容更新与发布流程

1. 修改 `ai_agent_30_day_learning_plan.md` 或 `ai-agent-30-day-learning-plan/day-*.md`。
2. 运行 `python3 scripts/build_site.py`。
3. 本地预览 `_site/`，确认目录、链接和页面内容正常。
4. 提交并推送到 `main`。
5. GitHub Actions 自动构建并发布到 GitHub Pages。

## GitHub Pages 部署设置

在 GitHub 仓库页面进入 `Settings -> Pages`：

- 将 `Build and deployment` 的 `Source` 设置为 `GitHub Actions`。

站点地址：<https://ai-agent-30-day-learning-plan.inaodeng.com/>

## 自动部署流程

部署由 `.github/workflows/pages.yml` 完成：

- 触发条件：push 到 `main`，或手动触发 `workflow_dispatch`。
- 所需权限：`contents: read`、`pages: write`、`id-token: write`。
- build job：`actions/checkout@v4` 检出代码 → `actions/setup-python@v5` 安装 Python 3.12 → 运行 `python scripts/build_site.py` → `actions/upload-pages-artifact@v3` 上传 `_site/` 产物。
- deploy job：在 `github-pages` 环境中运行 `actions/deploy-pages@v4` 发布产物。
- 构建脚本会写入 `.nojekyll`，避免 GitHub Pages 用 Jekyll 二次处理静态文件。

## 自定义域名

当前站点使用自定义域名 `ai-agent-30-day-learning-plan.inaodeng.com`：

- DNS 侧：将子域名 `ai-agent-30-day-learning-plan` 解析到 GitHub Pages 对应的地址，具体配置方式见 GitHub 文档。
- Pages 侧：在仓库 `Settings -> Pages -> Custom domain` 填入域名，并启用 HTTPS。

更换域名时，修改 DNS 与 Pages 设置即可，构建与部署流程无需改动。

参考：<https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site>

## 常见问题

- 构建后页面样式丢失？确认通过 `python3 -m http.server` 从 `_site/` 目录预览，不要直接双击打开 HTML 文件。
- Pages 部署后打不开或 404？确认 Pages Source 是 GitHub Actions，且最新一次 push 的 Actions 运行成功。
- 手动重新部署：在仓库 Actions 页面选中 `deploy` workflow，点击 `Run workflow`。

## 相关文档

- 学习计划主目录：`ai_agent_30_day_learning_plan.md`
- 项目说明：[README.md](README.md)
- 维护约定：`AGENTS.md`
