from pathlib import Path
from datetime import date
import argparse
import json

ROOT = Path(__file__).resolve().parents[1]

LEVEL_MAP = {
    "publishable": "A",
    "official_sources_consistent": "B",
    "partial_official_record": "C",
    "official_claim_only": "D",
    "insufficient": "D",
}


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def first_source(row):
    external = row.get("external_evidence") or []
    if external:
        source = external[0]
        return source.get("source_url", ""), source.get("source_name", "")
    return (
        row.get("image_source_url") or row.get("brand_product_url") or "",
        row.get("image_source_name") or "官方來源",
    )


def merge_deep(base, override):
    override = override or {}
    merged = {**base, **override}
    base_media = base.get("media") or {}
    over_media = override.get("media") or {}
    merged["media"] = {
        **base_media,
        **over_media,
        "main": over_media.get("main") or base_media.get("main"),
        "gallery": over_media.get("gallery") if isinstance(over_media.get("gallery"), list) else base_media.get("gallery", []),
        "evidence": over_media.get("evidence") if isinstance(over_media.get("evidence"), list) else base_media.get("evidence", []),
    }
    merged["external_evidence"] = override.get("external_evidence") if isinstance(override.get("external_evidence"), list) else base.get("external_evidence", [])
    status = merged.get("origin_evidence_status", "insufficient")
    source_url, source_name = first_source(merged)
    merged.update({
        "catalog_source": "deep_case",
        "evidence_level": LEVEL_MAP.get(status, "D"),
        "brand_origin_status": "taiwan_brand_confirmed" if merged.get("taiwan_brand") is True else "unverified",
        "record_scope": "exact_model",
        "source_url": source_url,
        "source_name": source_name,
    })
    return merged


def normalize_registry(row):
    return {
        **row,
        "catalog_source": "mit_registry",
        "taiwan_brand": row.get("brand_origin_status") == "taiwan_brand_confirmed",
        "current_sale_confirmed": None,
        "external_evidence": [],
    }


def build():
    base = load("data/products.demo.json")
    overrides = load("data/product.media.overrides.json")
    manifest = load("data/registry.manifest.json")
    override_map = {row["id"]: row for row in overrides}

    deep = [merge_deep(row, override_map.get(row["id"])) for row in base if row["verification_status"] != "demo_only"]
    demos = [row for row in base if row["verification_status"] == "demo_only"]
    registry = []
    for shard in manifest["shards"]:
        registry.extend(normalize_registry(row) for row in load(shard["path"]))

    expected_registry = int(manifest["total_records"])
    records = deep + registry
    ids = [row["id"] for row in records]
    assert len(deep) == 4
    assert len(registry) == expected_registry, f"registry count mismatch {len(registry)}/{expected_registry}"
    assert len(records) == len(deep) + expected_registry
    assert len(set(ids)) == len(ids)
    assert all(row.get("publication_status") == "unpublished" for row in records)
    assert all(row.get("source_url") for row in records), "every public record needs a primary source URL"
    assert all(row.get("source_name") for row in records), "every public record needs a primary source name"

    return {
        "schema_version": 1,
        "catalog_version": manifest["version"],
        "generated_at": date.today().isoformat(),
        "counts": {
            "real_research_candidates": len(records),
            "deep_editorial_cases": len(deep),
            "mit_active_exact_models": len(registry),
            "isolated_demo_records": len(demos),
            "formal_published": sum(row.get("publication_status") == "published" for row in records),
            "registry_shards": len(manifest["shards"]),
        },
        "records": records,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="data/catalog.public.json")
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    catalog = build()
    if args.check_only:
        print(json.dumps(catalog["counts"], ensure_ascii=False, sort_keys=True))
        return
    output = ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {output.relative_to(ROOT)} records={len(catalog['records'])}")


if __name__ == "__main__":
    main()
