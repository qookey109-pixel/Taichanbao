from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
overrides = json.loads((ROOT / "data/product.media.overrides.json").read_text(encoding="utf-8"))
rights = json.loads((ROOT / "data/image_rights.sampo.json").read_text(encoding="utf-8"))

record = next(row for row in overrides if row["id"] == "pilot-sampo-sr-c58dv")
assert len(record["media"]["gallery"]) == 3
assert len(record["media"]["evidence"]) == 1
assert len(record["external_evidence"]) == 2

images = [item for item in record["media"]["gallery"] if item["kind"] == "image"]
assert len(images) == 3
assert all(item["rights_status"] == "permission_pending" for item in images)
assert all(item["url"].startswith("https://www.sampo.com.tw/") for item in images)

tracked = {row["asset_url"]: row for row in rights}
assert len(tracked) == 3
for image in images:
    assert image["url"] in tracked
    assert tracked[image["url"]]["rights_status"] == image["rights_status"]
    assert tracked[image["url"]]["source_url"] == image["source_url"]

government = next(row for row in record["external_evidence"] if row["source_type"] == "government_energy_label_registry")
assert "SR-C58DV" in " ".join(government["findings"])
assert "不支持製造地" in government["scope_note"]

print("OK: SAMPO gallery=3; evidence placeholder=1; external evidence=2; rights tracked=3")
