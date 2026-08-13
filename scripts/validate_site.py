from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
index = (ROOT / "index.html").read_text(encoding="utf-8")
magazine_js = (ROOT / "assets/magazine.js").read_text(encoding="utf-8")
magazine_css = (ROOT / "assets/magazine.css").read_text(encoding="utf-8")
media_js = (ROOT / "assets/product-image-enhancements.js").read_text(encoding="utf-8")
media_css = (ROOT / "assets/product-images.css").read_text(encoding="utf-8")
catalog_loader = (ROOT / "assets/catalog-v3.js").read_text(encoding="utf-8")
catalog_js = (ROOT / "assets/catalog-v3-1.js").read_text(encoding="utf-8")
catalog_css = (ROOT / "assets/catalog-v3.css").read_text(encoding="utf-8")
lifecycle_js = (ROOT / "assets/lifecycle-v3-2.js").read_text(encoding="utf-8")
lifecycle_css = (ROOT / "assets/lifecycle-v3-2.css").read_text(encoding="utf-8")
scale_js = (ROOT / "assets/scale-v3-3.js").read_text(encoding="utf-8")
public_builder = (ROOT / "scripts/build_public_catalog.py").read_text(encoding="utf-8")
expiry_builder = (ROOT / "scripts/report_registry_expiry.py").read_text(encoding="utf-8")
registry_seed = (ROOT / "data/products.registry.json").read_text(encoding="utf-8")
registry_appliances = (ROOT / "data/products.registry.appliances.json").read_text(encoding="utf-8")
registry_lifestyle = (ROOT / "data/products.registry.lifestyle.json").read_text(encoding="utf-8")
manifest = json.loads((ROOT / "data/registry.manifest.json").read_text(encoding="utf-8"))
overrides = (ROOT / "data/product.media.overrides.json").read_text(encoding="utf-8")
build_info = json.loads((ROOT / "build-info.json").read_text(encoding="utf-8"))
preview = (ROOT / "versions_review/v2.5/index.html").read_text(encoding="utf-8")
preview_js = (ROOT / "assets/app.js").read_text(encoding="utf-8")
preview_css = (ROOT / "assets/styles.css").read_text(encoding="utf-8")

for token in [
    "台灣製證據資料誌", "產品證據資料庫", "assets/catalog-v3.css", "assets/catalog-v3.js",
    "catalogTotal", "mitCertifiedCount", "deepCaseCount", "catalogSourceFilter",
    "catalogEvidenceFilter", "catalogBrandFilter", "正式發布 Gate", "data-view", "data-scroll=\"database\""
]:
    assert token in index, token

for token in ["publicationGate", "localStorage", "taichanbao-favorites", "products.demo.json", "favoritesOnly", "pushState"]:
    assert token in magazine_js, token

for token in ["product.media.overrides.json", "mergeProduct", "external_evidence", "renderExternalEvidence", "renderGallery", "rightsLabel", "safeUrl"]:
    assert token in media_js, token

for token in ["catalog-v3-1.js", "lifecycle-v3-2.js", "lifecycle-v3-2.css", "scale-v3-3.js", "V3.3 Registry Scale 100"]:
    assert token in catalog_loader, token

for token in [
    "V3.3 REGISTRY SCALE 100", "V3.3 Registry Scale 100", "data/catalog.public.json", "validPublicCatalog",
    "registry.manifest.json", "products.demo.json", "product.media.overrides.json",
    "public_catalog", "manifest_fallback", "evidenceLevel", "catalog_source", "catalogGrid",
    "enhanceMediaScopes", "同系列補充圖", "精確型號", "records.length === 104",
    "mit_active_exact_models === 100", "registry_shards === 3"
]:
    assert token in catalog_js, token

for token in [
    "registry-expiry.json", "catalog.public.json", "lifecycle-section", "lifecycleNext",
    "data-life-window", "lifecycle-pill", "expiredCount", "decorateCatalogCards"
]:
    assert token in lifecycle_js, token

for token in ["V3.3 REGISTRY SCALE 100", "v33BalanceNote", "最大分類", "上限 40%", "registry.manifest.json"]:
    assert token in scale_js, token

for token in [".lifecycle-section", ".lifecycle-metrics", ".lifecycle-row", ".lifecycle-pill", ".lifecycle-pill.soon", ".lifecycle-pill.urgent"]:
    assert token in lifecycle_css, token

for token in [
    "data/catalog.public.json", "catalog_version", "manifest[\"version\"]",
    "registry.manifest.json", "real_research_candidates", "every public record needs a primary source URL"
]:
    assert token in public_builder, token

for token in ["expiring_within_30_days", "expiring_within_90_days", "expiring_within_180_days", "expiring_within_365_days", "expired_count", "--output", "manifest[\"total_records\"]"]:
    assert token in expiry_builder, token

for token in [".catalog-hero", ".catalog-metrics", ".catalog-grid", ".catalog-card", ".evidence-badge", ".catalog-controls", ".media-scope-pill"]:
    assert token in catalog_css, token

for token in ["mit-snug-s9900000015", "mit-adhoc-gentle102", "mit-tendays-dmit017-5", "mit-panasonic-nrc387hvls", "government_mit_registry", "MIT微笑標章"]:
    assert token in registry_seed, token

for token in ["NR-C507XVS", "KD-884HP0", "XYFYK106", "E-SUN LM515E2F-CK", "BEC120SGU2", "V3.1家電擴充"]:
    assert token in registry_appliances, token

for token in ["01500039-04089", "01900057-02519", "02800516-00175", "01600539-00134", "袋包收納", "居家用品"]:
    assert token in registry_lifestyle, token

assert manifest["version"] == "V3.3 Registry Scale 100"
assert manifest["total_records"] == 100
assert len(manifest["shards"]) == 3
assert manifest["shards"][2]["path"] == "data/products.registry.lifestyle.json"
assert manifest["shards"][2]["records"] == 50

for token in ["pilot-sampo-sr-c58dv", "pilot-tatung-tac11hnm", "pilot-oright-bio-caffeine", "permission_pending"]:
    assert token in overrides, token

assert build_info["version"] == "V3.3 Registry Scale 100"
assert build_info["data_snapshot"] == "2026-08-13"
assert build_info["real_research_candidates"] == 104
assert build_info["deep_editorial_cases"] == 4
assert build_info["mit_active_exact_models"] == 100
assert build_info["registry_shards"] == 3
assert build_info["isolated_demo_records"] == 6
assert build_info["formal_published"] == 0
assert build_info["registry_lifecycle_dashboard"] is True
assert build_info["registry_expired"] == 0
assert build_info["registry_expiring_within_90_days"] >= 1
assert build_info["category_concentration_gate"] is True
assert build_info["max_category_share"] == 0.4
assert build_info["lifecycle_report"] == "data/registry-expiry.json"
assert build_info["deployment_source"] == "GitHub Actions"

for token in [".media-gallery", ".media-thumbnails", ".media-thumb", ".media-inventory", ".drawer-media-frame", ".media-rights"]:
    assert token in media_css, token

for token in ["V2.5 Recovery Baseline", "研究預覽", "正式發布", "正式發布 Gate", '<base href="../../">']:
    assert token in preview, token

for token in ["publicationGate", "localStorage", "favorites"]:
    assert token in preview_js, token

assert ".ticker" in magazine_css
assert ".layout" in magazine_css
assert ".mobile-nav" in magazine_css
assert ".ticker" in preview_css
assert ".layout" in preview_css
assert ".mobile-nav" in preview_css

print("OK: V3.3 Scale 100 enabled; real=104 MIT=100 deep=4 demos=6 published=0; lifecycle, category balance and V2.5 preview retained")
