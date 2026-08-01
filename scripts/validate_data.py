from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
rows = json.loads((ROOT / "data/products.demo.json").read_text(encoding="utf-8"))

assert len(rows) == 10, "expected six demo records and four official-source pilots"
assert len({row["id"] for row in rows}) == len(rows), "duplicate id"

required = {
    "id", "brand", "name", "category", "scene", "taiwan_brand",
    "verification_status", "publication_status", "origin_summary",
    "score", "emoji", "tags", "media"
}

demo_count = 0
pilot_count = 0
published_count = 0

for row in rows:
    missing = required - row.keys()
    assert not missing, f"{row.get('id')}: missing {sorted(missing)}"
    assert "<img" not in str(row["emoji"]).lower(), f"{row['id']}: emoji must not contain HTML"
    assert isinstance(row["media"], dict), f"{row['id']}: media must be an object"
    assert isinstance(row["media"].get("gallery"), list), f"{row['id']}: media.gallery must be an array"
    assert isinstance(row["media"].get("evidence"), list), f"{row['id']}: media.evidence must be an array"

    main = row["media"].get("main")
    assert isinstance(main, dict), f"{row['id']}: media.main required"
    assert main.get("kind") in {"image", "placeholder"}, f"{row['id']}: invalid main kind"

    for item in [main, *row["media"]["gallery"], *row["media"]["evidence"]]:
        assert isinstance(item, dict), f"{row['id']}: media item must be an object"
        assert item.get("kind") in {"image", "placeholder"}, f"{row['id']}: invalid media kind"
        assert item.get("alt"), f"{row['id']}: media alt required"
        if item["kind"] == "image":
            assert str(item.get("url", "")).startswith("https://") or str(item.get("url", "")).startswith("assets/"), f"{row['id']}: invalid media URL"
            assert item.get("source_name"), f"{row['id']}: image source_name required"
            assert item.get("rights_status"), f"{row['id']}: image rights_status required"
            assert item.get("checked_at"), f"{row['id']}: image checked_at required"
        else:
            assert item.get("emoji"), f"{row['id']}: placeholder emoji required"

    assert row["publication_status"] == "unpublished"
    published_count += int(row["publication_status"] == "published")

    if row["verification_status"] == "demo_only":
        demo_count += 1
        assert main["kind"] == "placeholder"
    elif row["verification_status"] == "official_source_found":
        pilot_count += 1
        assert main["kind"] == "image"
        for field in ["model", "image_url", "image_source_url", "image_source_name", "image_rights_status"]:
            assert row.get(field), f"{row['id']}: missing {field}"
        assert row["image_rights_status"] == "permission_pending"
    else:
        raise AssertionError(f"{row['id']}: unsupported verification_status")

assert demo_count == 6
assert pilot_count == 4
assert published_count == 0
print(f"OK: demo={demo_count}; official-source pilots={pilot_count}; published={published_count}; complete media model enabled")
