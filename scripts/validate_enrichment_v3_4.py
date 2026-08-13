from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
queue = json.loads((ROOT / "data/enrichment.queue.json").read_text(encoding="utf-8"))
results = json.loads((ROOT / "data/enrichment.results.v1.json").read_text(encoding="utf-8"))
manifest = json.loads((ROOT / "data/registry.manifest.json").read_text(encoding="utf-8"))

rows = []
for shard in manifest["shards"]:
    rows.extend(json.loads((ROOT / shard["path"]).read_text(encoding="utf-8")))
registry = {row["id"]: row for row in rows}

assert queue["version"] == "V3.4 Enrichment Queue 20"
assert len(queue["items"]) == 20
assert len({item["record_id"] for item in queue["items"]}) == 20
assert set(queue["task_types"]) == {"brand_identity", "current_sale", "official_product_page", "image_rights"}

allowed_task_states = {"pending", "in_progress", "verified", "not_found", "blocked", "not_applicable"}
allowed_queue_states = {"queued", "in_progress", "completed", "blocked"}
queue_map = {}
for item in queue["items"]:
    rid = item["record_id"]
    queue_map[rid] = item
    assert rid in registry, f"queue record missing from Registry: {rid}"
    assert item["priority"] in {"P1", "P2", "P3"}
    assert item["status"] in allowed_queue_states
    assert set(item["tasks"]) == set(queue["task_types"])
    assert all(state in allowed_task_states for state in item["tasks"].values())
    row = registry[rid]
    assert row["publication_status"] == "unpublished", f"queue must not include published Registry: {rid}"
    assert row["verification_status"] == "government_registry_verified"
    assert row["record_scope"] == "exact_model"

p1 = sum(item["priority"] == "P1" for item in queue["items"])
assert p1 >= 8
assert len({registry[item["record_id"]]["category"] for item in queue["items"]}) >= 4

assert results["version"] == "V3.4 Enrichment Results Batch 2"
assert results["updated_at"] == "2026-08-13"
assert len(results["records"]) == 10
assert len({row["record_id"] for row in results["records"]}) == 10

result_states = []
for result in results["records"]:
    rid = result["record_id"]
    assert rid in queue_map, f"result record not in enrichment queue: {rid}"
    item = queue_map[rid]
    assert item["status"] == "completed", f"researched record must be completed: {rid}"
    assert result["checked_at"] == "2026-08-13"
    findings = result["findings"]
    assert set(findings) == set(queue["task_types"])
    for task_type, finding in findings.items():
        state = finding["status"]
        result_states.append(state)
        assert state in allowed_task_states - {"pending", "in_progress"}
        assert item["tasks"][task_type] == state, f"queue/result state mismatch: {rid}/{task_type}"
        assert finding.get("result")
        assert finding.get("summary")
        assert isinstance(finding.get("sources", []), list)
        for source in finding.get("sources", []):
            assert source.get("name")
            assert source.get("type")
            assert source.get("url", "").startswith("https://")
    assert registry[rid]["publication_status"] == "unpublished"

verified_tasks = sum(state == "verified" for item in queue["items"] for state in item["tasks"].values())
pending_tasks = sum(state == "pending" for item in queue["items"] for state in item["tasks"].values())
completed_records = sum(item["status"] == "completed" for item in queue["items"])
assert completed_records == 10
assert verified_tasks == 12
assert pending_tasks == 40
assert result_states.count("verified") == 12
assert result_states.count("not_found") == 23
assert result_states.count("blocked") == 5

confirmed_brand_records = 0
confirmed_sale_records = 0
exact_official_page_records = 0
for result in results["records"]:
    findings = result["findings"]
    if findings["brand_identity"]["status"] == "verified" and findings["brand_identity"]["result"] == "taiwan_brand_confirmed":
        confirmed_brand_records += 1
    if findings["current_sale"]["status"] == "verified":
        confirmed_sale_records += 1
    if findings["official_product_page"]["status"] == "verified":
        exact_official_page_records += 1
assert confirmed_brand_records == 6
assert confirmed_sale_records == 5
assert exact_official_page_records == 1

print(
    "OK: enrichment queue=20; researched=10; verified_tasks=12; "
    "not_found=23; blocked=5; pending=40; Taiwan-brand=6; sale=5; exact-page=1; publication unchanged"
)
