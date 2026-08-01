from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
products = json.loads((ROOT / "data/products.demo.json").read_text(encoding="utf-8"))
ledger = json.loads((ROOT / "data/image_rights.json").read_text(encoding="utf-8"))

expected = {}
for product in products:
    media = product["media"]
    groups = [
        ("main", [media["main"]]),
        ("gallery", media["gallery"]),
        ("evidence", media["evidence"]),
    ]
    for role, items in groups:
        for index, item in enumerate(items):
            if item.get("kind") != "image":
                continue
            asset_id = f"{product['id']}:{role}:{index}"
            expected[asset_id] = {
                "product_id": product["id"],
                "media_role": role,
                "media_index": index,
                "asset_url": item["url"],
                "source_url": item.get("source_url", ""),
                "rights_status": item.get("rights_status", "unknown"),
                "checked_at": item.get("checked_at", ""),
            }

assert isinstance(ledger, list), "image rights ledger must be an array"
assert len({row["asset_id"] for row in ledger}) == len(ledger), "duplicate asset_id in image rights ledger"
actual = {row["asset_id"]: row for row in ledger}

assert set(actual) == set(expected), (
    f"ledger mismatch: missing={sorted(set(expected)-set(actual))}; "
    f"extra={sorted(set(actual)-set(expected))}"
)

allowed = {
    "permission_pending", "permission_granted", "owned",
    "public_domain", "creative_commons", "unknown"
}

for asset_id, expected_row in expected.items():
    row = actual[asset_id]
    for field, value in expected_row.items():
        assert row.get(field) == value, f"{asset_id}: {field} mismatch"
    assert row["rights_status"] in allowed, f"{asset_id}: unsupported rights status"
    assert row.get("source_name"), f"{asset_id}: source_name required"
    if row["rights_status"] == "permission_pending":
        assert row.get("action_required"), f"{asset_id}: pending rights need action_required"

pending = sum(row["rights_status"] == "permission_pending" for row in ledger)
assert pending == 7, f"expected seven permission-pending images, got {pending}"
print(f"OK: image rights ledger covers {len(ledger)} image assets; permission_pending={pending}")
