from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
base = json.loads((ROOT / "data/products.demo.json").read_text(encoding="utf-8"))
registry = json.loads((ROOT / "data/products.registry.json").read_text(encoding="utf-8"))
overrides = json.loads((ROOT / "data/product.media.overrides.json").read_text(encoding="utf-8"))

demos = [row for row in base if row["verification_status"] == "demo_only"]
deep = [row for row in base if row["verification_status"] != "demo_only"]

assert len(demos) == 6, f"expected 6 isolated demo records, got {len(demos)}"
assert len(deep) == 4, f"expected 4 deep editorial cases, got {len(deep)}"
assert len(registry) == 15, f"expected 15 MIT registry records, got {len(registry)}"
assert len(deep) + len(registry) == 19, "V3 real research catalog must contain 19 records"

base_ids = {row["id"] for row in base}
registry_ids = {row["id"] for row in registry}
assert not (base_ids & registry_ids), "registry ids must not collide with editorial/demo ids"

deep_ids = {row["id"] for row in deep}
override_ids = {row["id"] for row in overrides}
assert override_ids <= deep_ids, f"override points outside deep cases: {sorted(override_ids - deep_ids)}"
assert {"pilot-tendays-tdt01", "pilot-sampo-sr-c58dv", "pilot-tatung-tac11hnm", "pilot-oright-bio-caffeine"} == deep_ids

level_map = {
    "publishable": "A",
    "official_sources_consistent": "B",
    "partial_official_record": "C",
    "official_claim_only": "D",
    "insufficient": "D",
}

merged_levels = []
for row in deep:
    override = next((item for item in overrides if item["id"] == row["id"]), {})
    status = override.get("origin_evidence_status", row.get("origin_evidence_status", "insufficient"))
    merged_levels.append(level_map.get(status, "D"))

assert "B" in merged_levels, "Tatung should exercise B-level official-source consistency"
assert "C" in merged_levels, "O'right should exercise C-level partial official evidence"
assert "D" in merged_levels, "TENDAYS/SAMPO should exercise D-level incomplete evidence"
assert all(row["evidence_level"] == "A" for row in registry)
assert all(row["publication_status"] == "unpublished" for row in registry + deep)

print(
    "OK: V3 catalog real=19 (deep=4 + MIT=15); demos=6 isolated; "
    f"deep evidence levels={sorted(merged_levels)}; published=0"
)
