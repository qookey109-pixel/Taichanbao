from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
queue = json.loads((ROOT / "data/enrichment.queue.json").read_text(encoding="utf-8"))
results_manifest = json.loads((ROOT / "data/enrichment.results.manifest.json").read_text(encoding="utf-8"))
registry_manifest = json.loads((ROOT / "data/registry.manifest.json").read_text(encoding="utf-8"))

rows = []
for shard in registry_manifest["shards"]:
    rows.extend(json.loads((ROOT / shard["path"]).read_text(encoding="utf-8")))
registry = {row["id"]: row for row in rows}

results = []
for batch in results_manifest["batches"]:
    payload = json.loads((ROOT / batch["path"]).read_text(encoding="utf-8"))
    batch_rows = payload.get("records", [])
    assert len(batch_rows) == batch["records"], f"result batch size mismatch: {batch['id']}"
    results.extend(batch_rows)

assert queue["version"] == "V3.6 Brand-Origin Separation"
assert len(queue["items"]) == 20
assert len({item["record_id"] for item in queue["items"]}) == 20
assert set(queue["task_types"]) == {"brand_identity", "current_sale", "official_product_page", "image_rights"}
assert results_manifest["version"] == "V3.6 Enrichment Results Manifest"
assert results_manifest["total_researched_records"] == 15
assert len(results_manifest["batches"]) == 3
assert len(results) == 15
assert len({row["record_id"] for row in results}) == 15

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

p1_items = [item for item in queue["items"] if item["priority"] == "P1"]
p2_items = [item for item in queue["items"] if item["priority"] == "P2"]
assert len(p1_items) == 11
assert len(p2_items) == 9
assert all(item["status"] == "completed" for item in p1_items), "all P1 enrichment records must remain complete"
assert sum(item["status"] == "completed" for item in p2_items) == 4
assert len({registry[item["record_id"]]["category"] for item in queue["items"]}) >= 4

result_states = []
result_map = {}
for result in results:
    rid = result["record_id"]
    result_map[rid] = result
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
assert completed_records == 15
assert verified_tasks == 21
assert pending_tasks == 20
assert result_states.count("verified") == 21
assert result_states.count("not_found") == 33
assert result_states.count("blocked") == 6

confirmed_taiwan_brand_records = 0
confirmed_non_taiwan_brand_records = 0
confirmed_sale_records = 0
exact_official_page_records = 0
for result in results:
    findings = result["findings"]
    identity = findings["brand_identity"]
    if identity["status"] == "verified" and identity["result"] == "taiwan_brand_confirmed":
        confirmed_taiwan_brand_records += 1
    if identity["status"] == "verified" and identity["result"] == "non_taiwan_brand":
        confirmed_non_taiwan_brand_records += 1
    if findings["current_sale"]["status"] == "verified":
        confirmed_sale_records += 1
    if findings["official_product_page"]["status"] == "verified":
        exact_official_page_records += 1

assert confirmed_taiwan_brand_records == 7
assert confirmed_non_taiwan_brand_records == 3
assert confirmed_sale_records == 9
assert exact_official_page_records == 2

# Brand-origin separation regression: Panasonic stays raw-unverified in Registry,
# while enrichment explicitly verifies it as non-Taiwan brand. MIT manufacturing stays active.
panasonic_ids = {
    "mit-appliance-0200001303970-nr-c507xvs",
    "mit-appliance-0200001303969-nr-d507xvs",
    "mit-appliance-0200001303966-nr-c617xvs",
}
for rid in panasonic_ids:
    assert registry[rid]["brand_origin_status"] == "unverified"
    assert registry[rid]["manufacturing_evidence_status"] == "mit_certified_active"
    finding = result_map[rid]["findings"]["brand_identity"]
    assert finding["status"] == "verified"
    assert finding["result"] == "non_taiwan_brand"
    assert result_map[rid]["findings"]["current_sale"]["status"] == "verified"

kd703 = result_map["mit-appliance-0200003802031-kd-703hp1"]["findings"]
assert kd703["brand_identity"]["result"] == "taiwan_brand_confirmed"
assert kd703["current_sale"]["status"] == "verified"
assert kd703["official_product_page"]["status"] == "verified"
assert kd703["image_rights"]["status"] == "blocked"

print(
    "OK: enrichment queue=20; researched=15; verified=21; not_found=33; blocked=6; pending=20; "
    "Taiwan-brand=7; non-Taiwan-brand=3; sale=9; exact-page=2; Panasonic separation PASS; publication unchanged"
)
