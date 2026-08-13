from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
queue = json.loads((ROOT / "data/enrichment.queue.json").read_text(encoding="utf-8"))
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
for item in queue["items"]:
    rid = item["record_id"]
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
verified_tasks = sum(state == "verified" for item in queue["items"] for state in item["tasks"].values())
print(f"OK: enrichment queue=20; P1={p1}; categories={len({registry[item['record_id']]['category'] for item in queue['items']})}; verified_tasks={verified_tasks}; publication unchanged")
