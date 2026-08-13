# 台產報 Handoff — V3.7 Enrichment Complete 20/20 + Promotion Audit

日期：2026-08-13

## 專案名稱
台產報 / Taichanbao

## Repository
`qookey109-pixel/Taichanbao`

## 目前狀態

```text
Version: V3.7 Enrichment Complete 20/20
Real research candidates: 104
MIT active exact models: 100
Existing deep editorial cases: 4
Registered deep candidates: 1
Enrichment queue: 20 / 20 complete
Verified tasks: 22
Not-found tasks: 51
Blocked tasks: 7
Pending tasks: 0
Taiwan-brand confirmed: 8
Non-Taiwan-brand confirmed: 3
Current-sale/supply confirmed: 9
Exact official product pages: 2
Formal published: 0
```

## 本次已完成

- V3.6 final production 已 success。
- 完成最後 5 P2：YYMe 1157508(黃)、NINO1881 L2425(藍)、YYMe 1157508(粉)、Anti-Arctic R-9-K、伯諾 LT9CMW8879。
- Enrichment Queue 20/20 全部 completed；pending=0。
- 新增 `data/enrichment.results.v4.json`；Results Manifest 升為 4 batches / 20 records。
- 最終 Enrichment 統計：22 verified / 51 not_found / 7 blocked / 0 pending。
- Anti-Arctic 品牌身分 verified → Taiwan brand；但 R-9-K exact-model current-sale/page 仍 not_found，image rights blocked。
- 新增 deterministic Promotion Audit：`scripts/build_promotion_audit.py`。
- 新增 `scripts/validate_promotion_audit_v3_7.py`。
- Promotion buckets：
  - deep-candidate conditions but asset/editorial gated = 2
  - Taiwan-brand research-only = 6
  - non-Taiwan-brand + Taiwan-made exact-model = 3
  - brand-origin unresolved research-only = 9
- `KD-884HP0`：registered blocked Deep Candidate。
- `KD-703HP1`：eligible for Deep Candidate review，但沒有自動 promotion。
- Panasonic 三筆：exclude from Taiwan-brand recommendation，同時保留 MIT exact-model 台灣製造證據。
- 新增 `assets/promotion-audit-v3-7.js` / `.css`，前台顯示 Promotion Audit。
- `assets/catalog-v3.js` 最終版本標記 V3.7，最後載入 Promotion Audit。
- `assets/enrichment-v3-4.js` 已顯示 20/20 complete。
- `build-info.json`、`scripts/validate_site.py`、CI、Pages、README、PROJECT_STATUS 全部升級 V3.7。
- Pages 部署時生成 `data/promotion-audit.json`。
- 新增研究紀錄 `docs/research/2026-08-13_enrichment_20_promotion_audit.md`。

## Promotion Audit 結果

```text
2  Deep Candidate 證據條件已達，但資產／編輯 Gate 阻擋
6  台灣品牌 research-only
3  非台灣品牌 + 台灣製 exact-model
9  品牌身分待確認 research-only
0  formal published
```

### KD-884HP0
- 已登錄 Deep Candidate。
- image rights blocked。
- editorial review pending。
- formal publication blocked。

### KD-703HP1
- Taiwan brand verified。
- exact-model official page verified。
- current official product line verified。
- official spec lists Taiwan manufacturing origin。
- image rights blocked。
- Promotion Audit 只標 `eligible_for_deep_candidate_review`，不自動加入 candidate。

### Panasonic
三筆：
- NR-C507XVS
- NR-D507XVS
- NR-C617XVS

品牌身分：`non_taiwan_brand`
製造證據：`mit_certified_active`
Promotion state：`exclude_from_taiwan_brand_recommendation`

不得因非台灣品牌否定台灣製造 exact-model 證據，也不得因 MIT 台灣製造證據把 Panasonic 改成台灣品牌。

## 重要治理

- 台灣品牌 ≠ 台灣製造。
- Enrichment completed ≠ verified。
- not_found / blocked 是正式研究結果。
- Promotion Audit ≠ promotion。
- Deep Candidate ≠ formal publication。
- MIT exact-model evidence 不得外推其他型號。
- sales channel ≠ live stock。
- exact official page 必須品牌／公司官方 exact-model 頁。
- 官方圖片可見 ≠ 已取得重用授權。
- Formal Publication Gate 不降低，published 維持 0。

## 重要檔案

```text
PROJECT_STATUS.md
README.md
build-info.json

data/enrichment.queue.json
data/enrichment.results.manifest.json
data/enrichment.results.v1.json
data/enrichment.results.v2.json
data/enrichment.results.v3.json
data/enrichment.results.v4.json
data/deep_case.candidates.json

assets/enrichment-v3-4.js
assets/deep-candidates-v3-5.js
assets/brand-origin-v3-6.js
assets/promotion-audit-v3-7.js
assets/promotion-audit-v3-7.css

scripts/build_public_catalog.py
scripts/build_promotion_audit.py
scripts/validate_enrichment_v3_4.py
scripts/validate_deep_candidates_v3_5.py
scripts/validate_promotion_audit_v3_7.py
scripts/validate_site.py

.github/workflows/validate.yml
.github/workflows/pages.yml

docs/research/2026-08-13_enrichment_20_promotion_audit.md
```

## 尚未完成

- V3.7 final production 尚需以 `docs/deployment/pages-production-result.json` 驗收。
- KD-884HP0 / KD-703HP1 圖片重用授權／合法替代素材未解決。
- KD-884HP0 editorial review 未完成。
- KD-703HP1 尚未人工新增為 Deep Candidate。
- Formal published 仍為 0。

## 明確下一步

1. 先驗收 V3.7 final production。
2. 不再擴 Enrichment Queue；先處理 KD-884HP0 / KD-703HP1 image-rights + editorial promotion review。
3. 決定是否把 KD-703HP1 人工加入 `data/deep_case.candidates.json`，但 image rights 必須保持 blocker。
4. 只有完整通過 Formal Publication Gate 才能產生第一筆 published。

## 新對話接續指令

繼續台產報 `qookey109-pixel/Taichanbao`。先讀 GitHub main 的 `PROJECT_STATUS.md`、`README.md` 與 `docs/handoffs/taichanbao_handoff_2026-08-13_v3_7_enrichment_complete_promotion_audit.md`。不要重做 Enrichment；20/20 已全部研究完成。先驗收最新 Pages production result。成功後停止擴 Queue，優先處理 KD-884HP0 / KD-703HP1 的圖片權利與 editorial promotion review。Panasonic 三筆已確定非台灣品牌但具有有效 MIT 台灣製 exact-model 證據，不得改標成台灣品牌。Formal published 維持 0。
