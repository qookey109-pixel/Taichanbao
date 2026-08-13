from pathlib import Path
from datetime import date
from urllib.parse import urlparse
import json

ROOT = Path(__file__).resolve().parents[1]
candidates = json.loads((ROOT / "data/deep_case.candidates.json").read_text(encoding="utf-8"))
registry_manifest = json.loads((ROOT / "data/registry.manifest.json").read_text(encoding="utf-8"))
results_manifest = json.loads((ROOT / "data/enrichment.results.manifest.json").read_text(encoding="utf-8"))
queue = json.loads((ROOT / "data/enrichment.queue.json").read_text(encoding="utf-8"))

registry_rows = []
for shard in registry_manifest["shards"]:
    registry_rows.extend(json.loads((ROOT / shard["path"]).read_text(encoding="utf-8")))
registry = {row["id"]: row for row in registry_rows}

result_rows = []
for batch in results_manifest["batches"]:
    result_rows.extend(json.loads((ROOT / batch["path"]).read_text(encoding="utf-8"))["records"])
results = {row["record_id"]: row for row in result_rows}
queue_map = {row["record_id"]: row for row in queue["items"]}

assert candidates["version"] == "V3.5 Deep Candidate Gate"
assert len(candidates["items"]) == 1
candidate = candidates["items"][0]
assert candidate["candidate_id"] == "deep-candidate-chimei-kd884hp0"
assert candidate["source_record_id"] == "mit-appliance-0200003802030-kd-884hp0"
assert candidate["candidate_stage"] == "deep_editorial_candidate"
assert candidate["candidate_status"] == "blocked_assets"
assert candidate["publication_status"] == "unpublished"
assert len(candidate["blocking_reasons"]) >= 2

source_id = candidate["source_record_id"]
assert source_id in registry
assert source_id in results
assert source_id in queue_map
row = registry[source_id]
result = results[source_id]
queue_item = queue_map[source_id]

assert row["model"] == "KD-884HP0(白)"
assert row["publication_status"] == "unpublished"
assert row["verification_status"] == "government_registry_verified"
assert row["manufacturing_evidence_status"] == "mit_certified_active"
assert row["certification"]["certificate_no"] == "02000038-02030"
assert date.fromisoformat(row["certification"]["valid_until"]) >= date.today()
assert queue_item["status"] == "completed"

findings = result["findings"]
assert findings["brand_identity"]["status"] == "verified"
assert findings["brand_identity"]["result"] == "taiwan_brand_confirmed"
assert findings["current_sale"]["status"] == "verified"
assert findings["official_product_page"]["status"] == "verified"
assert findings["image_rights"]["status"] == "blocked"

expected_gate = {
    "brand_identity": "pass",
    "exact_model_identity": "pass",
    "mit_manufacturing_evidence": "pass",
    "current_sale_or_supply": "pass",
    "exact_official_product_page": "pass",
    "key_conflict_review": "pass_no_conflict_found",
    "image_rights": "blocked",
    "editorial_review": "pending",
    "formal_publication": "blocked",
}
assert candidate["gate"] == expected_gate

hosts = set()
for evidence in candidate["evidence"]:
    url = evidence["source_url"]
    parsed = urlparse(url)
    assert parsed.scheme == "https"
    hosts.add(parsed.netloc)
assert "www.chimei.com.tw" in hosts
assert "keid.nat.gov.tw" in hosts
assert candidate["media"]["status"] == "blocked_permission_required"
assert candidate["media"]["source_page"].startswith("https://www.chimei.com.tw/")
assert candidate["checked_at"] == "2026-08-13"

print(
    "OK: deep candidates=1; KD-884HP0 pre-editorial gates pass=6; "
    "image-rights=blocked; editorial=pending; publication=blocked/unpublished"
)
