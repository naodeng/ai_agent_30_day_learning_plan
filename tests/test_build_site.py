import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD_SITE_PATH = ROOT / "scripts" / "build_site.py"


spec = importlib.util.spec_from_file_location("build_site", BUILD_SITE_PATH)
build_site = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules["build_site"] = build_site
spec.loader.exec_module(build_site)


class BuildSiteTests(unittest.TestCase):
    def test_html_page_includes_cloudflare_web_analytics_beacon(self):
        page = build_site.html_page("Example", "<main>Body</main>", "")

        self.assertIn("https://static.cloudflareinsights.com/beacon.min.js", page)
        self.assertIn('data-cf-beacon=\'{"token": "84929ec639084f508ef5f25cdbaea7ff"}\'', page)
        self.assertLess(page.index("static.cloudflareinsights.com/beacon.min.js"), page.index("</body>"))
