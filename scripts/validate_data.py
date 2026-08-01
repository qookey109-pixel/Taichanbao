from pathlib import Path
import json
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
rows = json.loads((ROOT / "data/products.demo.json").read_text(encoding="utf-8"))

assert len(rows) == 10, "expected six demo records and four official-source pilots"
required = {
    "id", "brand", "name", "category", "scene", "taiwan_brand",
    "verification_status", "publication_status", "origin_summary",
    "score", "emoji", "tags"
}
assert len({row["id"] for row in rows}) == len(rows), "duplicate id"

demo_rows = [row for row in rows if row["verification_status"] == "demo_only"]
pilot_rows = [row for row in rows if row["verification_status"] == "official_source_found"]
assert len(demo_rows) == 6
assert len(pilot_rows) == 4
assert all(row["publication_status"] == "unpublished" for row in rows)

for row in rows:
    missing = required - row.keys()
    assert not missing, f"{row.get('id')}: missing {sorted(missing)}"

for row in pilot_rows:
    for field in ["model", "image_url", "image_source_url", "image_source_name", "image_rights_status"]:
        assert row.get(field), f"{row['id']}: missing {field}"
    assert urlparse(row["image_url"]).scheme == "https"
    assert urlparse(row["image_source_url"]).scheme == "https"
    assert row["image_rights_status"] == "permission_pending"

assert {row["brand"] for row in pilot_rows} == {
    "TENDAYS 恬褋仕", "大同 TATUNG", "O'right 歐萊德", "SAMPO 聲寶"
}
print("OK: demo=6; official-source pilots=4; published=0")
