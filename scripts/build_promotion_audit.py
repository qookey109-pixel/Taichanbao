from pathlib import Path
from datetime import date
import argparse
import json

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_results():
    manifest = load("data/enrichment.results.manifest.json")
    rows = []
    for batch in manifest["batches"]:
        payload = load(batch["path"])
        batch_rows = payload.get("records", [])
        assert len(batch_rows) == int(batch["records"])
        rows.extend(batch_rows)
    assert len(rows) == int(manifest["total_researched_records"])
    return rows


def load_registry():
    manifest = load("data/registry.manifest.json")
    rows = []
    for shard in manifest["shards"]:
        rows.extend(load(shard["path"]))
    return {row["id"]: row for row in rows}


def classify(result, registry_row, registered_candidates):
    f = result["findings"]
    identity = f["brand_identity"]
    sale = f["current_sale"]["status"] == "verified"
    official_page = f["official_product_page"]["status"] == "verified"
    rights = f["image_rights"]["status"]
    brand_result = identity.get("result") if identity.get("status") == "verified" else "unverified"

    if brand_result == "taiwan_brand_confirmed":
        if sale and official_page:
            registered = registry_row["id"] in registered_candidates
            return {
                "bucket": "deep_candidate_assets_blocked" if rights == "blocked" else "deep_candidate_review",
                "promotion_state": "registered_deep_candidate" if registered else "eligible_for_deep_candidate_review",
                "reason": "台灣品牌、現售／供應與 exact-model 官方頁皆已驗證；候選層仍須保留圖片權利與正式發布 Gate。",
            }
        return {
            "bucket": "taiwan_brand_research_only",
            "promotion_state": "hold_research",
            "reason": "台灣品牌身分已確認，但現售或 exact-model 官方頁仍不完整，不升 Deep Candidate。",
        }

    if brand_result == "non_taiwan_brand":
        assert registry_row["manufacturing_evidence_status"] == "mit_certified_active"
        return {
            "bucket": "non_taiwan_brand_taiwan_made",
            "promotion_state": "exclude_from_taiwan_brand_recommendation",
            "reason": "品牌已確認非台灣品牌；保留此 exact model 的 MIT 台灣製造證據，但不列入台灣品牌推薦。",
        }

    return {
        "bucket": "brand_origin_unverified_research_only",
        "promotion_state": "hold_research",
        "reason": "MIT exact-model 製造證據存在，但品牌身分或消費端證據不足，維持 research-only。",
    }


def build():
    results = load_results()
    registry = load_registry()
    candidate_payload = load("data/deep_case.candidates.json")
    registered_candidates = {item["source_record_id"] for item in candidate_payload["items"]}

    items = []
    for result in results:
        rid = result["record_id"]
        row = registry[rid]
        classification = classify(result, row, registered_candidates)
        items.append({
            "record_id": rid,
            "brand": row["brand"],
            "name": row["name"],
            "model": row["model"],
            "category": row["category"],
            "brand_identity_result": result["findings"]["brand_identity"].get("result", "unverified"),
            "manufacturing_evidence_status": row["manufacturing_evidence_status"],
            "publication_status": row["publication_status"],
            **classification,
        })

    buckets = {}
    for item in items:
        buckets[item["bucket"]] = buckets.get(item["bucket"], 0) + 1

    assert len(items) == 20
    assert buckets == {
        "deep_candidate_assets_blocked": 2,
        "taiwan_brand_research_only": 6,
        "non_taiwan_brand_taiwan_made": 3,
        "brand_origin_unverified_research_only": 9,
    }
    assert sum(item["promotion_state"] == "registered_deep_candidate" for item in items) == 2
    assert sum(item["promotion_state"] == "eligible_for_deep_candidate_review" for item in items) == 0
    assert all(item["publication_status"] == "unpublished" for item in items)

    return {
        "version": "V3.8 Candidate Promotion Review",
        "generated_at": date.today().isoformat(),
        "researched_records": len(items),
        "formal_published": 0,
        "registered_deep_candidates": 2,
        "eligible_unregistered_deep_candidates": 0,
        "buckets": buckets,
        "items": items,
        "policy": "Promotion Audit classifies research outcomes only. V3.8 registers both qualifying CHIMEI records as blocked Deep Candidates; it never changes formal publication state automatically.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="data/promotion-audit.json")
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    payload = build()
    if args.check_only:
        print(json.dumps({
            "researched": payload["researched_records"],
            "registered_candidate": payload["registered_deep_candidates"],
            "eligible_unregistered": payload["eligible_unregistered_deep_candidates"],
            **payload["buckets"],
            "published": payload["formal_published"],
        }, ensure_ascii=False, sort_keys=True))
        return
    path = ROOT / args.output
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {path.relative_to(ROOT)} records={payload['researched_records']}")


if __name__ == "__main__":
    main()
