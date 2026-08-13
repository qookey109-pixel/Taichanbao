from pathlib import Path
from datetime import date
import json
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
rows = json.loads((ROOT / "data/products.registry.json").read_text(encoding="utf-8"))

assert isinstance(rows, list), "registry must be an array"
assert len(rows) >= 15, "V3 requires at least 15 registry records"
assert len({row["id"] for row in rows}) == len(rows), "duplicate registry id"

required = {
    "id", "record_origin", "brand", "brand_origin_status", "company", "name",
    "category", "scene", "model", "model_confirmed", "verification_status",
    "publication_status", "manufacturing_evidence_status", "evidence_level",
    "record_scope", "origin_summary", "certification", "source_url",
    "source_name", "source_type", "source_checked_at", "emoji", "tags"
}

today = date(2026, 8, 13)
categories = set()
brands = set()

for row in rows:
    missing = required - row.keys()
    assert not missing, f"{row.get('id')}: missing {sorted(missing)}"
    assert row["record_origin"] == "mit_registry"
    assert row["verification_status"] == "government_registry_verified"
    assert row["publication_status"] == "unpublished"
    assert row["manufacturing_evidence_status"] == "mit_certified_active"
    assert row["evidence_level"] == "A"
    assert row["record_scope"] == "exact_model"
    assert row["model_confirmed"] is True
    assert row["model"].strip(), f"{row['id']}: model required"
    assert row["brand_origin_status"] in {"taiwan_brand_confirmed", "non_taiwan_brand", "unverified"}
    assert row["source_type"] == "government_mit_registry"
    parsed = urlparse(row["source_url"])
    assert parsed.scheme == "https" and parsed.netloc == "keid.nat.gov.tw", f"{row['id']}: source must be official MIT registry"

    cert = row["certification"]
    for field in ["scheme", "certificate_no", "status", "passed_at", "valid_until"]:
        assert cert.get(field), f"{row['id']}: certification.{field} required"
    assert cert["scheme"] == "MIT微笑標章"
    assert cert["status"] == "有效"
    valid_until = date.fromisoformat(cert["valid_until"])
    assert valid_until >= today, f"{row['id']}: certification expired on {valid_until}"
    date.fromisoformat(cert["passed_at"])
    date.fromisoformat(row["source_checked_at"])

    categories.add(row["category"])
    brands.add(row["brand"])

assert len(categories) >= 6, f"expected diversified categories, got {sorted(categories)}"
assert len(brands) >= 10, f"expected diversified brands, got {len(brands)}"
assert any(row["id"] == "mit-tendays-dmit017-5" for row in rows)
assert any(row["id"] == "mit-panasonic-nrc387hvls" for row in rows)
assert any(row["certification"]["valid_until"] == "2029-07-27" for row in rows)

print(
    f"OK: registry={len(rows)}; categories={len(categories)}; brands={len(brands)}; "
    "all records exact-model MIT active and unpublished"
)
