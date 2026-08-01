from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
index = (ROOT / "index.html").read_text(encoding="utf-8")
magazine_js = (ROOT / "assets/magazine.js").read_text(encoding="utf-8")
magazine_css = (ROOT / "assets/magazine.css").read_text(encoding="utf-8")
preview = (ROOT / "versions_review/v2.5/index.html").read_text(encoding="utf-8")
preview_js = (ROOT / "assets/app.js").read_text(encoding="utf-8")
preview_css = (ROOT / "assets/styles.css").read_text(encoding="utf-8")

# 正式首頁：V2.6 Magazine Discovery。
for token in [
    "台灣品牌選品誌",
    "V2.6 MAGAZINE DISCOVERY",
    "今日台產",
    "產品專題",
    "品牌索引",
    "本月台產榜",
    "正式發布 Gate",
    "assets/magazine.css",
    "assets/magazine.js",
    "data-view",
    "data-scene",
]:
    assert token in index, token

for token in [
    "publicationGate",
    "localStorage",
    "taichanbao-favorites",
    "products.demo.json",
    "favoritesOnly",
    "pushState",
]:
    assert token in magazine_js, token

for token in [
    ".ticker",
    ".layout",
    ".mobile-nav",
    ".discovery-panel",
    ".favorite-btn",
    ".method-grid",
]:
    assert token in magazine_css, token

# V2.5 Recovery Baseline 仍可從歷史預覽路徑開啟。
for token in [
    "V2.5 Recovery Baseline",
    "研究預覽",
    "正式發布",
    "正式發布 Gate",
    '<base href="../../">',
]:
    assert token in preview, token

for token in ["publicationGate", "localStorage", "favorites"]:
    assert token in preview_js, token

assert ".ticker" in preview_css
assert ".layout" in preview_css
assert ".mobile-nav" in preview_css

print("OK: V2.6 Magazine Discovery is official; V2.5 preview remains available")
