from pathlib import Path
from urllib.parse import urlparse
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data/products.registry.json"

REQUIRED = {
    "id", "record_origin", "brand", "brand_origin_status", "company", "name",
    "category", "scene", "model", "model_confirmed", "verification_status",
    "publication_status", "manufacturing_evidence_status", "evidence_level",
    "record_scope", "origin_summary", "certification", "source_url",
    "source_name", "source_type", "source_checked_at", "emoji", "tags"
}


def validate(row):
    missing = REQUIRED - row.keys()
    if missing:
        raise ValueError(f"{row.get('id')}: missing {sorted(missing)}")
    if row["record_origin"] != "mit_registry":
        raise ValueError(f"{row['id']}: record_origin must be mit_registry")
    if row["verification_status"] != "government_registry_verified":
        raise ValueError(f"{row['id']}: verification_status must be government_registry_verified")
    if row["publication_status"] != "unpublished":
        raise ValueError(f"{row['id']}: batch imports can never publish records")
    if row["manufacturing_evidence_status"] != "mit_certified_active":
        raise ValueError(f"{row['id']}: manufacturing_evidence_status must be mit_certified_active")
    if row["evidence_level"] != "A" or row["record_scope"] != "exact_model":
        raise ValueError(f"{row['id']}: MIT imports must be A-level exact-model records")
    if row["model_confirmed"] is not True or not str(row["model"]).strip():
        raise ValueError(f"{row['id']}: exact model is required")
    if row["brand_origin_status"] not in {"taiwan_brand_confirmed", "non_taiwan_brand", "unverified"}:
        raise ValueError(f"{row['id']}: unsupported brand_origin_status")
    url = urlparse(row["source_url"])
    if url.scheme != "https" or url.netloc != "keid.nat.gov.tw":
        raise ValueError(f"{row['id']}: source_url must use official keid.nat.gov.tw HTTPS source")
    cert = row["certification"]
    for field in ["scheme", "certificate_no", "status", "passed_at", "valid_until"]:
        if not cert.get(field):
            raise ValueError(f"{row['id']}: certification.{field} required")
    if cert["scheme"] != "MIT微笑標章" or cert["status"] != "有效":
        raise ValueError(f"{row['id']}: only active MIT certification records can enter this registry")


def main():
    parser = argparse.ArgumentParser(description="Safely merge a normalized MIT registry batch into Taichanbao V3")
    parser.add_argument("batch", type=Path, help="JSON array of normalized MIT records")
    parser.add_argument("--write", action="store_true", help="write merged data/products.registry.json")
    args = parser.parse_args()

    existing = json.loads(REGISTRY.read_text(encoding="utf-8"))
    incoming = json.loads(args.batch.read_text(encoding="utf-8"))
    if not isinstance(incoming, list) or not incoming:
        raise SystemExit("batch must be a non-empty JSON array")

    seen_in_batch = set()
    for row in incoming:
        validate(row)
        if row["id"] in seen_in_batch:
            raise SystemExit(f"duplicate incoming id: {row['id']}")
        seen_in_batch.add(row["id"])

    merged = {row["id"]: row for row in existing}
    certificate_owner = {row["certification"]["certificate_no"]: row["id"] for row in existing}
    added = updated = 0

    for row in incoming:
        cert = row["certification"]["certificate_no"]
        owner = certificate_owner.get(cert)
        if owner and owner != row["id"]:
            raise SystemExit(f"certificate {cert} already belongs to {owner}; refusing collision")
        if row["id"] in merged:
            updated += 1
        else:
            added += 1
        merged[row["id"]] = row
        certificate_owner[cert] = row["id"]

    result = sorted(merged.values(), key=lambda row: (row["category"], row["brand"], row["name"], row["model"]))
    output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"

    print(f"batch valid: incoming={len(incoming)} added={added} updated={updated} total={len(result)}")
    if not args.write:
        print("dry-run only; pass --write to update data/products.registry.json")
        return

    REGISTRY.write_text(output, encoding="utf-8")
    print(f"wrote {REGISTRY.relative_to(ROOT)}")
    print("next: run python scripts/validate_registry.py && python scripts/validate_v3_catalog.py")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
