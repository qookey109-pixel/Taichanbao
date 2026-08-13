from pathlib import Path
from datetime import date
import argparse
import json

ROOT = Path(__file__).resolve().parents[1]


def load_manifest():
    return json.loads((ROOT / "data/registry.manifest.json").read_text(encoding="utf-8"))


def build_report():
    manifest = load_manifest()
    rows = []
    for shard in manifest["shards"]:
        rows.extend(json.loads((ROOT / shard["path"]).read_text(encoding="utf-8")))

    expected = int(manifest["total_records"])
    assert len(rows) == expected, f"expiry report registry count mismatch {len(rows)}/{expected}"

    today = date.today()
    windows = {30: [], 90: [], 180: [], 365: []}
    expired = []
    for row in rows:
        valid = date.fromisoformat(row["certification"]["valid_until"])
        days = (valid - today).days
        item = {
            "id": row["id"],
            "brand": row["brand"],
            "name": row.get("name", ""),
            "model": row["model"],
            "category": row.get("category", ""),
            "certificate_no": row["certification"]["certificate_no"],
            "valid_until": valid.isoformat(),
            "days_remaining": days,
        }
        if days < 0:
            expired.append(item)
        for window in windows:
            if 0 <= days <= window:
                windows[window].append(item)

    for items in windows.values():
        items.sort(key=lambda item: (item["days_remaining"], item["brand"], item["model"]))
    expired.sort(key=lambda item: item["days_remaining"])

    return {
        "generated_at": today.isoformat(),
        "registry_version": manifest["version"],
        "registry_records": len(rows),
        "expired_count": len(expired),
        "expired": expired,
        "expiring_within_30_days": windows[30],
        "expiring_within_90_days": windows[90],
        "expiring_within_180_days": windows[180],
        "expiring_within_365_days": windows[365],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="")
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    report = build_report()
    expected = int(load_manifest()["total_records"])
    assert report["registry_records"] == expected
    assert report["expired_count"] == 0, "expired MIT Registry record detected"
    payload = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.check_only:
        print(f"OK: registry={report['registry_records']} expired=0; within90={len(report['expiring_within_90_days'])}")
        return
    if args.output:
        path = ROOT / args.output
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(payload, encoding="utf-8")
        print(f"WROTE {path.relative_to(ROOT)}")
        return
    print(payload, end="")


if __name__ == "__main__":
    main()
