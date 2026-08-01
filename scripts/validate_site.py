from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
index = (ROOT / "index.html").read_text(encoding="utf-8")
magazine_js = (ROOT / "assets/magazine.js").read_text(encoding="utf-8")
image_js = (ROOT / "assets/product-image-enhancements.js").read_text(encoding="utf-8")
magazine_css = (ROOT / "assets/magazine.css").read_text(encoding="utf-8")
image_css = (ROOT / "assets/product-images.css").read_text(encoding="utf-8")
preview = (ROOT / "versions_review/v2.5/index.html").read_text(encoding="utf-8")
preview_js = (ROOT / "assets/app.js").read_text(encoding="utf-8")
preview_css = (ROOT / "assets/styles.css").read_text(encoding="utf-8")

for token in [
    "台灣品牌選品誌", "V2.7 OFFICIAL IMAGE PILOT", "今日台產",
    "產品專題", "品牌索引", "本月台產榜", "正式發布 Gate",
    "assets/magazine.css", "assets/product-images.css",
    "assets/magazine.js", "assets/product-image-enhancements.js",
    "6 筆示範＋4 筆官方圖片候選"
]:
    assert token in index, token

for token in ["publicationGate", "localStorage", "products.demo.json", "favoritesOnly"]:
    assert token in magazine_js, token

for token in ["drawer-media", "image_source_url", "permission_pending", "MutationObserver"]:
    assert token in image_js, token

for token in [".story-art.has-image", ".drawer-media", ".drawer-source", ".rights-pending"]:
    assert token in image_css, token

assert ".ticker" in magazine_css
for token in ["V2.5 Recovery Baseline", "研究預覽", "正式發布 Gate", '<base href="../../">']:
    assert token in preview, token
assert "publicationGate" in preview_js
assert ".ticker" in preview_css
print("OK: V2.7 official image pilot; V2.5 preview retained")
