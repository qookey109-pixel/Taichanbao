from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
index = (ROOT / "index.html").read_text(encoding="utf-8")
magazine_js = (ROOT / "assets/magazine.js").read_text(encoding="utf-8")
magazine_css = (ROOT / "assets/magazine.css").read_text(encoding="utf-8")
media_js = (ROOT / "assets/product-image-enhancements.js").read_text(encoding="utf-8")
media_css = (ROOT / "assets/product-images.css").read_text(encoding="utf-8")
overrides = (ROOT / "data/product.media.overrides.json").read_text(encoding="utf-8")
preview = (ROOT / "versions_review/v2.5/index.html").read_text(encoding="utf-8")
preview_js = (ROOT / "assets/app.js").read_text(encoding="utf-8")
preview_css = (ROOT / "assets/styles.css").read_text(encoding="utf-8")

for token in [
    "台灣品牌選品誌", "今日台產", "產品專題", "品牌索引",
    "正式發布 Gate", "assets/magazine.css", "assets/product-images.css",
    "assets/magazine.js", "assets/product-image-enhancements.js",
    "data-view", "data-scene",
]:
    assert token in index, token

for token in [
    "publicationGate", "localStorage", "taichanbao-favorites",
    "products.demo.json", "favoritesOnly", "pushState",
]:
    assert token in magazine_js, token

for token in [
    "V2.10 SAMPO MULTI-IMAGE + EXTERNAL EVIDENCE",
    "product.media.overrides.json", "mergeProduct", "external_evidence",
    "renderExternalEvidence", "renderGallery", "renderInventory",
    "data-media-product", "rightsLabel", "safeUrl", "cleanEmoji",
]:
    assert token in media_js, token

for token in [
    "pilot-sampo-sr-c58dv", "government_energy_label_registry",
    "SR-C58DV", "不支持製造地", "permission_pending",
]:
    assert token in overrides, token

for token in [
    ".media-gallery", ".media-thumbnails", ".media-thumb",
    ".media-inventory", ".drawer-media-frame", ".media-rights",
]:
    assert token in media_css, token

for token in [
    "V2.5 Recovery Baseline", "研究預覽", "正式發布",
    "正式發布 Gate", '<base href="../../">',
]:
    assert token in preview, token

for token in ["publicationGate", "localStorage", "favorites"]:
    assert token in preview_js, token

assert ".ticker" in magazine_css
assert ".layout" in magazine_css
assert ".mobile-nav" in magazine_css
assert ".ticker" in preview_css
assert ".layout" in preview_css
assert ".mobile-nav" in preview_css

print("OK: V2.10 SAMPO multi-image and external evidence enabled; V2.5 preview retained")
