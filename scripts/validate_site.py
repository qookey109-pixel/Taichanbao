from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def text(path):
    return (ROOT / path).read_text(encoding="utf-8")

def data(path):
    return json.loads(text(path))

index = text("index.html")
magazine_js = text("assets/magazine.js")
magazine_css = text("assets/magazine.css")
media_js = text("assets/product-image-enhancements.js")
media_css = text("assets/product-images.css")
catalog_loader = text("assets/catalog-v3.js")
catalog_js = text("assets/catalog-v3-1.js")
catalog_css = text("assets/catalog-v3.css")
lifecycle_js = text("assets/lifecycle-v3-2.js")
lifecycle_css = text("assets/lifecycle-v3-2.css")
scale_js = text("assets/scale-v3-3.js")
enrichment_js = text("assets/enrichment-v3-4.js")
enrichment_css = text("assets/enrichment-v3-4.css")
deep_js = text("assets/deep-candidates-v3-5.js")
deep_css = text("assets/deep-candidates-v3-5.css")
public_builder = text("scripts/build_public_catalog.py")
expiry_builder = text("scripts/report_registry_expiry.py")
registry_seed = text("data/products.registry.json")
registry_appliances = text("data/products.registry.appliances.json")
registry_lifestyle = text("data/products.registry.lifestyle.json")
registry_manifest = data("data/registry.manifest.json")
enrichment_queue = data("data/enrichment.queue.json")
enrichment_results_manifest = data("data/enrichment.results.manifest.json")
deep_candidates = data("data/deep_case.candidates.json")
overrides = text("data/product.media.overrides.json")
build_info = data("build-info.json")
preview = text("versions_review/v2.5/index.html")
preview_js = text("assets/app.js")
preview_css = text("assets/styles.css")

# Formal magazine shell and frozen publication behavior remain present.
for token in ["台灣製證據資料誌", "產品證據資料庫", "assets/catalog-v3.css", "assets/catalog-v3.js", "catalogTotal", "mitCertifiedCount", "deepCaseCount", "catalogSourceFilter", "catalogEvidenceFilter", "catalogBrandFilter", "正式發布 Gate", "data-view", 'data-scroll="database"']:
    assert token in index, token
for token in ["publicationGate", "localStorage", "taichanbao-favorites", "products.demo.json", "favoritesOnly", "pushState"]:
    assert token in magazine_js, token
for token in ["product.media.overrides.json", "mergeProduct", "external_evidence", "renderExternalEvidence", "renderGallery", "rightsLabel", "safeUrl"]:
    assert token in media_js, token

# Progressive frontend layers are all loaded in order, with V3.5 as the final version marker.
for token in ["catalog-v3-1.js", "lifecycle-v3-2.js", "lifecycle-v3-2.css", "scale-v3-3.js", "enrichment-v3-4.js", "enrichment-v3-4.css", "deep-candidates-v3-5.js", "deep-candidates-v3-5.css", "V3.5 Deep Candidate Gate"]:
    assert token in catalog_loader, token
for token in ["V3.3 REGISTRY SCALE 100", "V3.3 Registry Scale 100", "data/catalog.public.json", "validPublicCatalog", "registry.manifest.json", "products.demo.json", "product.media.overrides.json", "public_catalog", "manifest_fallback", "evidenceLevel", "catalog_source", "catalogGrid", "enhanceMediaScopes", "同系列補充圖", "精確型號", "records.length === 104", "mit_active_exact_models === 100", "registry_shards === 3"]:
    assert token in catalog_js, token
for token in ["registry-expiry.json", "catalog.public.json", "lifecycle-section", "lifecycleNext", "data-life-window", "lifecycle-pill", "expiredCount", "decorateCatalogCards"]:
    assert token in lifecycle_js, token
for token in ["V3.3 REGISTRY SCALE 100", "v33BalanceNote", "最大分類", "上限 40%", "registry.manifest.json"]:
    assert token in scale_js, token

# Enrichment is now manifest-driven and P1-complete.
for token in ["enrichment.queue.json", "enrichment.results.manifest.json", "loadResults", "V3.5 · ENRICHMENT P1 COMPLETE", "brand_identity", "current_sale", "official_product_page", "image_rights", "已研究紀錄", "state-not_found", "state-blocked", "data-catalog-id"]:
    assert token in enrichment_js, token
for token in [".enrichment-section", ".enrichment-metrics", ".enrichment-row", ".enrichment-task", ".enrichment-row.researched", ".state-not_found", ".state-blocked"]:
    assert token in enrichment_css, token
assert enrichment_queue["version"] == "V3.5 Enrichment Queue 20"
assert len(enrichment_queue["items"]) == 20
assert sum(item["status"] == "completed" for item in enrichment_queue["items"]) == 11
assert all(item["status"] == "completed" for item in enrichment_queue["items"] if item["priority"] == "P1")
assert enrichment_results_manifest["version"] == "V3.5 Enrichment Results Manifest"
assert enrichment_results_manifest["total_researched_records"] == 11
assert len(enrichment_results_manifest["batches"]) == 2
assert sum(batch["records"] for batch in enrichment_results_manifest["batches"]) == 11

# Deep candidate Gate is visible and explicitly blocked from publication.
for token in ["data/deep_case.candidates.json", "V3.5 · DEEP CANDIDATE GATE", "證據夠強", "formal_publication", "image_rights", "candidate_status", "data-catalog-id"]:
    assert token in deep_js, token
for token in [".deep-candidate-section", ".deep-gates", ".deep-gate.pass", ".deep-gate.blocked", ".deep-gate.pending", ".deep-blockers"]:
    assert token in deep_css, token
assert deep_candidates["version"] == "V3.5 Deep Candidate Gate"
assert len(deep_candidates["items"]) == 1
candidate = deep_candidates["items"][0]
assert candidate["source_record_id"] == "mit-appliance-0200003802030-kd-884hp0"
assert candidate["candidate_status"] == "blocked_assets"
assert candidate["gate"]["image_rights"] == "blocked"
assert candidate["gate"]["editorial_review"] == "pending"
assert candidate["gate"]["formal_publication"] == "blocked"
assert candidate["publication_status"] == "unpublished"

# Builders retain research-source lineage and only produce deploy-time artifacts.
for token in ["data/catalog.public.json", "catalog_version", 'manifest["version"]', "registry.manifest.json", "enrichment.results.manifest.json", "load_enrichment_results", "apply_enrichment", "official_product_page_url", "enrichment_researched_records", "real_research_candidates", "every public record needs a primary source URL"]:
    assert token in public_builder, token
for token in ["expiring_within_30_days", "expiring_within_90_days", "expiring_within_180_days", "expiring_within_365_days", "expired_count", "--output", 'manifest["total_records"]']:
    assert token in expiry_builder, token

# Registry scale/category evidence remains intact.
for token in [".catalog-hero", ".catalog-metrics", ".catalog-grid", ".catalog-card", ".evidence-badge", ".catalog-controls", ".media-scope-pill"]:
    assert token in catalog_css, token
for token in ["mit-snug-s9900000015", "mit-adhoc-gentle102", "mit-tendays-dmit017-5", "mit-panasonic-nrc387hvls", "government_mit_registry", "MIT微笑標章"]:
    assert token in registry_seed, token
for token in ["NR-C507XVS", "KD-884HP0", "XYFYK106", "E-SUN LM515E2F-CK", "BEC120SGU2", "V3.1家電擴充"]:
    assert token in registry_appliances, token
for token in ["01500039-04089", "01900057-02519", "02800516-00175", "01600539-00134", "袋包收納", "居家用品"]:
    assert token in registry_lifestyle, token
assert registry_manifest["version"] == "V3.3 Registry Scale 100"
assert registry_manifest["total_records"] == 100
assert len(registry_manifest["shards"]) == 3
assert registry_manifest["shards"][2]["records"] == 50
for token in ["pilot-sampo-sr-c58dv", "pilot-tatung-tac11hnm", "pilot-oright-bio-caffeine", "permission_pending"]:
    assert token in overrides, token

# Deployment fingerprint must match V3.5 source state.
assert build_info["version"] == "V3.5 Deep Candidate Gate"
assert build_info["data_snapshot"] == "2026-08-13"
assert build_info["real_research_candidates"] == 104
assert build_info["deep_editorial_cases"] == 4
assert build_info["deep_editorial_candidates"] == 1
assert build_info["deep_candidates_blocked"] == 1
assert build_info["mit_active_exact_models"] == 100
assert build_info["registry_shards"] == 3
assert build_info["isolated_demo_records"] == 6
assert build_info["formal_published"] == 0
assert build_info["registry_lifecycle_dashboard"] is True
assert build_info["category_concentration_gate"] is True
assert build_info["enrichment_queue"] == 20
assert build_info["enrichment_p1_complete"] is True
assert build_info["enrichment_researched_records"] == 11
assert build_info["enrichment_verified_tasks"] == 12
assert build_info["enrichment_not_found_tasks"] == 27
assert build_info["enrichment_blocked_tasks"] == 5
assert build_info["enrichment_pending_tasks"] == 36
assert build_info["enrichment_taiwan_brand_confirmed"] == 6
assert build_info["enrichment_current_sale_confirmed"] == 5
assert build_info["enrichment_exact_official_product_page_confirmed"] == 1
assert build_info["enrichment_result_batches"] == 2
assert build_info["deployment_source"] == "GitHub Actions"

# Media and historical preview stay available.
for token in [".media-gallery", ".media-thumbnails", ".media-thumb", ".media-inventory", ".drawer-media-frame", ".media-rights"]:
    assert token in media_css, token
for token in ["V2.5 Recovery Baseline", "研究預覽", "正式發布", "正式發布 Gate", '<base href="../../">']:
    assert token in preview, token
for token in ["publicationGate", "localStorage", "favorites"]:
    assert token in preview_js, token
assert ".ticker" in magazine_css and ".layout" in magazine_css and ".mobile-nav" in magazine_css
assert ".ticker" in preview_css and ".layout" in preview_css and ".mobile-nav" in preview_css

print("OK: V3.5 Deep Candidate Gate enabled; Registry=100 P1=11/11 researched deep-candidate=1 blocked published=0; V3.3 scale, lifecycle and V2.5 preview retained")
