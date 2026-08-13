from pathlib import Path
from collections import Counter
import json

ROOT = Path(__file__).resolve().parents[1]
base = json.loads((ROOT / "data/products.demo.json").read_text(encoding="utf-8"))
manifest = json.loads((ROOT / "data/registry.manifest.json").read_text(encoding="utf-8"))
overrides = json.loads((ROOT / "data/product.media.overrides.json").read_text(encoding="utf-8"))

assert manifest["version"] == "V3.3 Registry Scale 100"
assert manifest["total_records"] == 100
assert len(manifest["shards"]) == 3

registry = []
for shard in manifest["shards"]:
    registry.extend(json.loads((ROOT / shard["path"]).read_text(encoding="utf-8")))

demos = [row for row in base if row["verification_status"] == "demo_only"]
deep = [row for row in base if row["verification_status"] != "demo_only"]
assert len(demos) == 6
assert len(deep) == 4
assert len(registry) == 100
assert len(deep) + len(registry) == 104, "V3.3 real research catalog must contain 104 records"
assert all(row["publication_status"] == "unpublished" for row in deep + registry)

base_ids = {row["id"] for row in base}
registry_ids = {row["id"] for row in registry}
assert not (base_ids & registry_ids), "registry ids collide with editorial/demo ids"
assert len(registry_ids) == 100
assert len({row["certification"]["certificate_no"] for row in registry}) == 100

deep_ids = {row["id"] for row in deep}
override_ids = {row["id"] for row in overrides}
assert override_ids <= deep_ids
assert deep_ids == {"pilot-tendays-tdt01", "pilot-sampo-sr-c58dv", "pilot-tatung-tac11hnm", "pilot-oright-bio-caffeine"}

categories = Counter(row["category"] for row in registry)
assert categories["家電"] <= 40
assert categories["寢具"] >= 16
assert categories["居家織品"] >= 14
assert categories["袋包收納"] == 12
assert categories["居家用品"] == 12
assert len(categories) >= 8
assert all(row["evidence_level"] == "A" for row in registry)

print(
    f"OK: V3.3 catalog real=104 (deep=4 + MIT=100); demos=6 isolated; "
    f"categories={len(categories)}; published=0"
)
