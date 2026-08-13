from pathlib import Path
import json
import importlib.util

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location("promotion_audit", ROOT / "scripts/build_promotion_audit.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
payload = module.build()

assert payload["version"] == "V3.8 Candidate Promotion Review"
assert payload["researched_records"] == 20
assert payload["formal_published"] == 0
assert payload["registered_deep_candidates"] == 2
assert payload["eligible_unregistered_deep_candidates"] == 0
assert payload["buckets"] == {
    "deep_candidate_assets_blocked": 2,
    "taiwan_brand_research_only": 6,
    "non_taiwan_brand_taiwan_made": 3,
    "brand_origin_unverified_research_only": 9,
}

items = {item["record_id"]: item for item in payload["items"]}
for rid in [
    "mit-appliance-0200003802030-kd-884hp0",
    "mit-appliance-0200003802031-kd-703hp1",
]:
    assert items[rid]["promotion_state"] == "registered_deep_candidate"
    assert items[rid]["bucket"] == "deep_candidate_assets_blocked"
    assert items[rid]["publication_status"] == "unpublished"

for rid in [
    "mit-appliance-0200001303970-nr-c507xvs",
    "mit-appliance-0200001303969-nr-d507xvs",
    "mit-appliance-0200001303966-nr-c617xvs",
]:
    assert items[rid]["bucket"] == "non_taiwan_brand_taiwan_made"
    assert items[rid]["promotion_state"] == "exclude_from_taiwan_brand_recommendation"
    assert items[rid]["manufacturing_evidence_status"] == "mit_certified_active"
    assert items[rid]["publication_status"] == "unpublished"

assert all(item["publication_status"] == "unpublished" for item in payload["items"])
print("OK: V3.8 promotion audit researched=20; registered-deep-candidate=2; assets-blocked=2; Taiwan-research=6; non-Taiwan/Taiwan-made=3; origin-unverified=9; published=0")
