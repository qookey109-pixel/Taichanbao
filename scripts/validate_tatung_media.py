from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
overrides = json.loads((ROOT / "data/product.media.overrides.json").read_text(encoding="utf-8"))
rights = json.loads((ROOT / "data/image_rights.tatung.json").read_text(encoding="utf-8"))

record = next(row for row in overrides if row["id"] == "pilot-tatung-tac11hnm")
assert record["current_sale_confirmed"] is True
assert record["origin_evidence_status"] == "official_sources_consistent"
assert len(record["media"]["gallery"]) == 4
assert len(record["media"]["evidence"]) == 1
assert len(record["external_evidence"]) == 3

images = [item for item in record["media"]["gallery"] if item["kind"] == "image"]
assert len(images) == 4
assert all(item["rights_status"] == "permission_pending" for item in images)
assert all(item["url"].startswith("https://www.etungo.com.tw/") for item in images)

tracked = {row["asset_url"]: row for row in rights}
assert len(tracked) == 4
for image in images:
    assert image["url"] in tracked
    assert tracked[image["url"]]["rights_status"] == image["rights_status"]
    assert tracked[image["url"]]["source_url"] == image["source_url"]

official = next(row for row in record["external_evidence"] if row["source_type"] == "official_product_page")
assert "產地標示台灣" in official["findings"]
assert "實體銘牌" in official["scope_note"]

award = next(row for row in record["external_evidence"] if row["source_type"] == "official_award_registry")
assert "TAC-11HN-M" in " ".join(award["findings"])

print("OK: Tatung gallery=4; evidence placeholder=1; external evidence=3; rights tracked=4")
