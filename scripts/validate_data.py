from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
rows = json.loads((ROOT / "data/products.demo.json").read_text(encoding="utf-8"))

assert len(rows) == 6, "expected six demo records"
required = {
    "id", "brand", "name", "category", "scene", "taiwan_brand",
    "verification_status", "publication_status", "origin_summary",
    "score", "emoji", "tags"
}
assert len({row["id"] for row in rows}) == len(rows), "duplicate id"

for row in rows:
    missing = required - row.keys()
    assert not missing, f"{row.get('id')}: missing {sorted(missing)}"
    assert row["verification_status"] == "demo_only"
    assert row["publication_status"] == "unpublished"

print(f"OK: {len(rows)} demo records; published=0")
