from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
rows = json.loads((ROOT / "data/products.demo.json").read_text(encoding="utf-8"))

assert len(rows) == 9, "expected six demo records and three official-source pilots"
required = {
    "id", "brand", "name", "category", "scene", "taiwan_brand",
    "verification_status", "publication_status", "origin_summary",
    "score", "emoji", "tags"
}
assert len({row["id"] for row in rows}) == len(rows), "duplicate id"

demo_count = 0
pilot_count = 0
for row in rows:
    missing = required - row.keys()
    assert not missing, f"{row.get('id')}: missing {sorted(missing)}"
    assert row["publication_status"] == "unpublished"
    if row["verification_status"] == "demo_only":
        demo_count += 1
    elif row["verification_status"] == "official_source_found":
        pilot_count += 1
        for field in ["model", "image_url", "image_source_url", "image_source_name", "image_rights_status"]:
            assert row.get(field), f"{row['id']}: missing {field}"
        assert row["image_url"].startswith("https://")
        assert row["image_source_url"].startswith("https://")
        assert row["image_rights_status"] == "permission_pending"
    else:
        raise AssertionError(f"{row['id']}: unsupported verification_status")

assert demo_count == 6
assert pilot_count == 3
print(f"OK: demo={demo_count}; official-source pilots={pilot_count}; published=0")
