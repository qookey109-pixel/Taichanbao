from pathlib import Path
from datetime import date, timedelta
import json

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "data/registry.manifest.json").read_text(encoding="utf-8"))
rows = []
for shard in manifest["shards"]:
    rows.extend(json.loads((ROOT / shard["path"]).read_text(encoding="utf-8")))

today = date.today()
windows = {30: [], 90: [], 180: [], 365: []}
for row in rows:
    valid = date.fromisoformat(row["certification"]["valid_until"])
    days = (valid - today).days
    for window in windows:
        if 0 <= days <= window:
            windows[window].append({"id": row["id"], "brand": row["brand"], "model": row["model"], "certificate_no": row["certification"]["certificate_no"], "valid_until": valid.isoformat(), "days_remaining": days})

report = {
    "generated_at": today.isoformat(),
    "registry_records": len(rows),
    "expired": sum(date.fromisoformat(row["certification"]["valid_until"]) < today for row in rows),
    "expiring_within_30_days": windows[30],
    "expiring_within_90_days": windows[90],
    "expiring_within_180_days": windows[180],
    "expiring_within_365_days": windows[365]
}
print(json.dumps(report, ensure_ascii=False, indent=2))
