from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
base = json.loads((ROOT / "data/products.demo.json").read_text(encoding="utf-8"))
overrides = json.loads((ROOT / "data/product.media.overrides.json").read_text(encoding="utf-8"))

# V3.1 regression baseline is intentionally pinned to the original two shards.
registry = []
for path in ["data/products.registry.json", "data/products.registry.appliances.json"]:
    registry.extend(json.loads((ROOT / path).read_text(encoding="utf-8")))

demos = [row for row in base if row["verification_status"] == "demo_only"]
deep = [row for row in base if row["verification_status"] != "demo_only"]
assert len(demos) == 6
assert len(deep) == 4
assert len(registry) == 50
assert len(deep) + len(registry) == 54, "V3.1 real research catalog must contain 54 records"
assert all(row["publication_status"] == "unpublished" for row in deep + registry)

base_ids = {row["id"] for row in base}
registry_ids = {row["id"] for row in registry}
assert not (base_ids & registry_ids), "registry ids collide with editorial/demo ids"
assert len(registry_ids) == 50

deep_ids = {row["id"] for row in deep}
override_ids = {row["id"] for row in overrides}
assert override_ids <= deep_ids
assert deep_ids == {"pilot-tendays-tdt01", "pilot-sampo-sr-c58dv", "pilot-tatung-tac11hnm", "pilot-oright-bio-caffeine"}

assert sum(row["category"] == "家電" for row in registry) >= 38, "V3.1 should materially expand appliance coverage"
assert len({row["brand"] for row in registry}) >= 15
assert len({row["category"] for row in registry}) >= 6
assert all(row["evidence_level"] == "A" for row in registry)

print("OK: V3.1 regression real=54 (deep=4 + MIT=50); demos=6 isolated; published=0")
