from pathlib import Path
from datetime import date
from urllib.parse import urlparse
from collections import Counter
import json

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "data/registry.manifest.json").read_text(encoding="utf-8"))
assert manifest["version"] == "V3.3 Registry Scale 100"
assert manifest["total_records"] == 100
assert len(manifest["shards"]) == 3

rows = []
for shard in manifest["shards"]:
    path = ROOT / shard["path"]
    data = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(data, list), f"{shard['id']}: shard must be an array"
    assert len(data) == shard["records"], f"{shard['id']}: manifest count mismatch"
    rows.extend(data)

assert len(rows) == 100
ids = [row["id"] for row in rows]
certs = [row["certification"]["certificate_no"] for row in rows]
assert len(set(ids)) == 100, "duplicate registry id across shards"
assert len(set(certs)) == 100, "duplicate MIT certificate across shards"

today = date.today()
required = {
    "id", "record_origin", "brand", "brand_origin_status", "company", "name", "category", "scene",
    "model", "model_confirmed", "verification_status", "publication_status", "manufacturing_evidence_status",
    "evidence_level", "record_scope", "origin_summary", "certification", "source_url", "source_name",
    "source_type", "source_checked_at", "emoji", "tags"
}
for row in rows:
    missing = required - row.keys()
    assert not missing, f"{row.get('id')}: missing {sorted(missing)}"
    assert row["record_origin"] == "mit_registry"
    assert row["verification_status"] == "government_registry_verified"
    assert row["publication_status"] == "unpublished"
    assert row["manufacturing_evidence_status"] == "mit_certified_active"
    assert row["evidence_level"] == "A"
    assert row["record_scope"] == "exact_model"
    assert row["model_confirmed"] is True
    parsed = urlparse(row["source_url"])
    assert parsed.scheme == "https" and parsed.netloc == "keid.nat.gov.tw", f"{row['id']}: non-official source"
    cert = row["certification"]
    assert cert["scheme"] == "MIT微笑標章"
    assert cert["status"] == "有效"
    assert date.fromisoformat(cert["valid_until"]) >= today, f"{row['id']}: expired MIT record"

appliance = json.loads((ROOT / "data/products.registry.appliances.json").read_text(encoding="utf-8"))
assert len(appliance) == 35
assert all(row["category"] == "家電" for row in appliance)
assert len({row["brand"] for row in appliance}) >= 6
source_urls = {row["source_url"] for row in appliance}
assert any("p=2" in url for url in source_urls), "appliance shard must retain page-2 provenance"
assert any("p=4" in url for url in source_urls), "appliance shard must retain page-4 provenance"
assert any("p=5" in url for url in source_urls), "appliance shard must retain page-5 provenance"

lifestyle = json.loads((ROOT / "data/products.registry.lifestyle.json").read_text(encoding="utf-8"))
assert len(lifestyle) == 50
lifestyle_counts = Counter(row["category"] for row in lifestyle)
assert lifestyle_counts == Counter({"寢具": 14, "居家織品": 12, "袋包收納": 12, "居家用品": 12}), lifestyle_counts
assert all(any(f"classid={class_id}" in row["source_url"] for class_id in (5, 6, 9, 20)) for row in lifestyle)

category_counts = Counter(row["category"] for row in rows)
largest_category, largest_count = category_counts.most_common(1)[0]
assert largest_count <= 40, f"category concentration too high: {largest_category}={largest_count}/100"
assert category_counts["家電"] <= 40
assert len(category_counts) >= 8, f"category diversity too low: {len(category_counts)}"

print(
    f"OK: registry scale={len(rows)} across {len(manifest['shards'])} shards; certificates unique=100; "
    f"lifestyle=50; largest_category={largest_category}:{largest_count}; published=0"
)
