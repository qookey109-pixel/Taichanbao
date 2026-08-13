from pathlib import Path
from datetime import date
import json

ROOT = Path(__file__).resolve().parents[1]
loader = (ROOT / "assets/catalog-v3.js").read_text(encoding="utf-8")
js = (ROOT / "assets/lifecycle-v3-2.js").read_text(encoding="utf-8")
css = (ROOT / "assets/lifecycle-v3-2.css").read_text(encoding="utf-8")
manifest = json.loads((ROOT / "data/registry.manifest.json").read_text(encoding="utf-8"))

for token in ["lifecycle-v3-2.css", "lifecycle-v3-2.js"]:
    assert token in loader, token

for token in [
    "registry-expiry.json", "catalog.public.json", "registry.manifest.json",
    "lifecycle-section", "lifecycleNext", "life90", "data-life-window",
    "lifecycle-pill", "decorateCatalogCards", "deriveReport"
]:
    assert token in js, token

for token in [
    ".lifecycle-section", ".lifecycle-metrics", ".lifecycle-row",
    ".lifecycle-pill", ".lifecycle-pill.soon", ".lifecycle-pill.urgent"
]:
    assert token in css, token

rows = []
for shard in manifest["shards"]:
    rows.extend(json.loads((ROOT / shard["path"]).read_text(encoding="utf-8")))
assert len(rows) == manifest["total_records"] == 100

today = date.today()
remaining = []
for row in rows:
    valid = date.fromisoformat(row["certification"]["valid_until"])
    remaining.append((valid - today).days)

assert all(days >= 0 for days in remaining), "expired Registry must be blocked before lifecycle render"
within_30 = sum(0 <= days <= 30 for days in remaining)
within_90 = sum(0 <= days <= 90 for days in remaining)
within_180 = sum(0 <= days <= 180 for days in remaining)
within_365 = sum(0 <= days <= 365 for days in remaining)
assert within_90 >= within_30
assert within_180 >= within_90
assert within_365 >= within_180
assert within_90 >= 1, "lifecycle fixture should exercise an upcoming expiry"

print(
    f"OK: lifecycle registry={len(rows)} expired=0; "
    f"within30={within_30} within90={within_90} within180={within_180} within365={within_365}"
)
