from pathlib import Path
from datetime import date
from urllib.parse import urlparse
import json

ROOT = Path(__file__).resolve().parents[1]
candidates = json.loads((ROOT / "data/deep_case.candidates.json").read_text(encoding="utf-8"))
rights = json.loads((ROOT / "data/media-rights.requests.json").read_text(encoding="utf-8"))
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
rights_map = {row["record_id"]: row for row in rights["requests"]}

assert candidates["version"] == "V3.8 Candidate Promotion Review"
assert len(candidates["items"]) == 2
assert rights["version"] == "V3.8 Media Rights Requests"
assert len(rights["requests"]) == 2

expected = {
    "mit-appliance-0200003802030-kd-884hp0": {
        "candidate_id": "deep-candidate-chimei-kd884hp0",
        "model": "KD-884HP0(白)",
        "certificate_no": "02000038-02030",
        "mit_url_id": "287272",
    },
    "mit-appliance-0200003802031-kd-703hp1": {
        "candidate_id": "deep-candidate-chimei-kd703hp1",
        "model": "KD-703HP1",
        "certificate_no": "02000038-02031",
        "mit_url_id": "287273",
    },
}

assert {item["source_record_id"] for item in candidates["items"]} == set(expected)
assert set(rights_map) == set(expected)

expected_gate = {
    "brand_identity": "pass",
    "exact_model_identity": "pass",
    "mit_manufacturing_evidence": "pass",
    "current_sale_or_supply": "pass",
    "exact_official_product_page": "pass",
    "key_conflict_review": "pass_no_conflict_found",
    "candidate_editorial_review": "pass",
    "image_rights": "blocked",
    "publication_editorial_review": "pending",
    "formal_publication": "blocked",
}

for candidate in candidates["items"]:
    source_id = candidate["source_record_id"]
    spec = expected[source_id]
    assert candidate["candidate_id"] == spec["candidate_id"]
    assert candidate["candidate_stage"] == "deep_editorial_candidate"
    assert candidate["candidate_status"] == "blocked_assets"
    assert candidate["publication_status"] == "unpublished"
    assert candidate["gate"] == expected_gate
    assert len(candidate["blocking_reasons"]) >= 2
    assert source_id in registry and source_id in results and source_id in queue_map

    row = registry[source_id]
    result = results[source_id]
    queue_item = queue_map[source_id]
    assert row["model"] == spec["model"]
    assert row["publication_status"] == "unpublished"
    assert row["verification_status"] == "government_registry_verified"
    assert row["manufacturing_evidence_status"] == "mit_certified_active"
    assert row["certification"]["certificate_no"] == spec["certificate_no"]
    assert date.fromisoformat(row["certification"]["valid_until"]) >= date.today()
    assert queue_item["status"] == "completed"

    findings = result["findings"]
    assert findings["brand_identity"]["status"] == "verified"
    assert findings["brand_identity"]["result"] == "taiwan_brand_confirmed"
    assert findings["current_sale"]["status"] == "verified"
    assert findings["official_product_page"]["status"] == "verified"
    assert findings["image_rights"]["status"] == "blocked"

    hosts = set()
    mit_evidence_found = False
    rights_evidence_found = False
    for evidence in candidate["evidence"]:
        url = evidence["source_url"]
        parsed = urlparse(url)
        assert parsed.scheme == "https"
        hosts.add(parsed.netloc)
        if evidence["type"] == "government_mit_registry":
            mit_evidence_found = spec["mit_url_id"] in url
        if evidence["type"] == "image_rights_terms":
            rights_evidence_found = url == "https://www.chimei.com.tw/conditions"
    assert any(host.endswith("chimei.com.tw") for host in hosts)
    assert "keid.nat.gov.tw" in hosts
    assert mit_evidence_found
    assert rights_evidence_found

    media = candidate["media"]
    assert media["status"] == "blocked_permission_required"
    assert media["rights_source"] == "https://www.chimei.com.tw/conditions"
    assert media["rights_contact"] == "lcd@mail.chimei.com.tw"
    assert candidate["checked_at"] == "2026-08-13"

    request = rights_map[source_id]
    assert request["rights_status"] == "permission_required"
    assert request["request_status"] == "ready_to_contact"
    assert request["request_sent"] is False
    assert request["contact_email"] == "lcd@mail.chimei.com.tw"
    assert request["terms_source"] == "https://www.chimei.com.tw/conditions"
    assert request["publication_effect"] == "blocked_until_permission_or_licensed_alternative"

print(
    "OK: V3.8 deep candidates=2; candidate-editorial=PASS; image-rights=BLOCKED; "
    "rights requests ready_to_contact=2 unsent=2; publication-editorial=PENDING; published=0"
)
