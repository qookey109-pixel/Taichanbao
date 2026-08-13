from pathlib import Path
from collections import Counter
import json

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "data/registry.manifest.json").read_text(encoding="utf-8"))
rows = []
for shard in manifest["shards"]:
    rows.extend(json.loads((ROOT / shard["path"]).read_text(encoding="utf-8")))

assert len(rows) == manifest["total_records"] == 100
counts = Counter(row["category"] for row in rows)
category, count = counts.most_common(1)[0]
share = count / len(rows)

assert share <= 0.40, f"largest category exceeds 40%: {category}={count}/{len(rows)} ({share:.1%})"
assert counts["家電"] <= 40, f"appliance concentration too high: {counts['家電']}/100"
assert len(counts) >= 8, f"need at least 8 categories, got {len(counts)}"
assert sum(counts[name] for name in ("寢具", "居家織品", "袋包收納", "居家用品")) >= 50

print(f"OK: category balance categories={len(counts)} largest={category}:{count} ({share:.1%}); appliances={counts['家電']}/100")
