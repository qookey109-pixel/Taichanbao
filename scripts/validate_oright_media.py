from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
overrides = json.loads((ROOT / "data/product.media.overrides.json").read_text(encoding="utf-8"))
rights = json.loads((ROOT / "data/image_rights.oright.json").read_text(encoding="utf-8"))

record = next(row for row in overrides if row["id"] == "pilot-oright-bio-caffeine")
assert len(record["media"]["gallery"]) == 3
assert len(record["media"]["evidence"]) == 1
assert len(record["external_evidence"]) == 2
assert record["current_sale_confirmed"] is False
assert record["related_series_current_sale_confirmed"] is True
assert record["origin_evidence_status"] == "partial_official_record"

images = [item for item in record["media"]["gallery"] if item["kind"] == "image"]
assert len(images) == 3
assert all(item["rights_status"] == "permission_pending" for item in images)
assert all(item["source_type"] == "official_related_series_page" for item in images)
assert all(item.get("relation_scope") for item in images)
assert all("不視為" in item["caption"] or "不構成" in item["caption"] or "需另查" in item["caption"] for item in images)

tracked = {row["asset_url"]: row for row in rights}
assert len(tracked) == 3
for image in images:
    assert image["url"] in tracked
    assert tracked[image["url"]]["rights_status"] == image["rights_status"]
    assert tracked[image["url"]]["source_url"] == image["source_url"]
    assert tracked[image["url"]]["relation_scope"] == image["relation_scope"]

award = next(row for row in record["external_evidence"] if row["source_type"] == "official_award_registry")
related = next(row for row in record["external_evidence"] if row["source_type"] == "official_related_series_page")
assert "4712782261130" in " ".join(award["findings"])
assert "未提供成品製造地" in award["scope_note"]
assert "不能視為得獎型號" in related["scope_note"]
assert "製造地" in related["scope_note"]

print("OK: O'right gallery=3; evidence placeholder=1; exact-model evidence=1; related-series evidence=1; rights tracked=3")
