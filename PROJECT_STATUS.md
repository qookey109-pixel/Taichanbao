# 台產報 PROJECT STATUS

更新日期：2026-08-13

## Version

`V3.7 Enrichment Complete 20/20`

## 正式網站方向

台產報維持「雜誌選品＋精確型號證據資料庫」架構。V3.7 完成第一輪 20 筆優先產品 Enrichment，並新增 Promotion Audit：研究完成不代表推薦或發布；品牌國籍、精確型號製造證據、現售、官方頁、圖片權利、Deep Candidate 與 Formal Publication 全部分開管理。

## V3.7 本次完成

- V3.3 Registry Scale 100、V3.2 Lifecycle、V3.5 Deep Candidate、V3.6 Brand-Origin Separation 全部保留。
- Enrichment Queue **20 / 20 全部研究完成**，pending=0。
- Enrichment Results Manifest 共 4 batches／20 records：`v1=10`、`v2=1`、`v3=4`、`v4=5`。
- 最終任務統計：22 verified、51 not_found、7 blocked、0 pending。
- 品牌身分：8 筆台灣品牌已確認、3 筆非台灣品牌已確認、其餘 9 筆仍待確認。
- 現售／供應證據已確認 9 筆；exact-model 品牌官方產品頁已確認 2 筆（KD-884HP0、KD-703HP1）。
- 最後 5 筆 P2 已完成：YYMe 1157508(黃)、NINO1881 L2425(藍)、YYMe 1157508(粉)、Anti-Arctic R-9-K、伯諾 LT9CMW8879。
- Anti-Arctic 品牌身分 verified → `taiwan_brand_confirmed`；但 R-9-K exact-model 現售與官方商品頁仍 not_found，圖片權利 blocked。
- YYMe 黃／粉、NINO1881 藍、伯諾均保留 MIT exact-model 製造證據，但品牌／現售／exact official page 等缺口不硬猜。
- 新增 `scripts/build_promotion_audit.py` 與 `scripts/validate_promotion_audit_v3_7.py`。
- Promotion Audit 固定將 20 筆分成四類：
  - 2 筆達 Deep Candidate 證據條件但仍被資產／編輯 Gate 阻擋。
  - 6 筆台灣品牌 research-only。
  - 3 筆非台灣品牌但具有台灣製 exact-model 證據。
  - 9 筆品牌身分未確認 research-only。
- `KD-884HP0` 是已登錄 blocked Deep Candidate；`KD-703HP1` 只是 `eligible_for_deep_candidate_review`，**不自動 promotion**。
- 三筆 Panasonic 永久歸於 `non_taiwan_brand_taiwan_made`：不得列入台灣品牌推薦，但保留 MIT exact-model 台灣製造證據。
- 新增 `assets/promotion-audit-v3-7.js` / `.css`，前台呈現 20 筆研究完成後的實際去向。
- Pages build 在部署前生成 `data/promotion-audit.json`；此檔為 deploy-time artifact，不是人工 source of truth。
- `scripts/validate_enrichment_v3_4.py` 已鎖定 20/20 completion 與 Panasonic regression。
- `scripts/validate_site.py`、CI、Pages、README、`build-info.json` 均已升級 V3.7。

## 目前資料狀態

```text
真實研究候選：104
MIT exact models：100
既有 Deep editorial cases：4
已登錄 Deep Candidate：1（KD-884HP0，blocked_assets）
Formal published：0

Enrichment Queue：20 / 20 complete
├─ verified tasks：22
├─ not_found：51
├─ blocked：7
└─ pending：0

Taiwan-brand confirmed：8
Non-Taiwan-brand confirmed：3
Brand-origin unresolved：9
Current-sale/supply confirmed：9
Exact official product pages：2
```

## Promotion Audit

```text
Deep Candidate 條件已達／資產阻擋：2
├─ KD-884HP0 → registered_deep_candidate
└─ KD-703HP1 → eligible_for_deep_candidate_review

台灣品牌 research-only：6
非台灣品牌＋台灣製 exact-model：3
品牌身分待確認 research-only：9
Formal published：0
```

Promotion Audit 只分類下一步，不修改 Registry、Deep Candidate 或 publication status。

## Panasonic Regression 永久保留

```text
Panasonic brand_origin_status = non_taiwan_brand
NR-C507XVS manufacturing_evidence_status = mit_certified_active
NR-D507XVS manufacturing_evidence_status = mit_certified_active
NR-C617XVS manufacturing_evidence_status = mit_certified_active
```

不得因台灣 MIT 製造證據把 Panasonic 改成台灣品牌，也不得因 Panasonic 是日本品牌否定這三個型號的台灣製造證據。

## KD-884HP0 / KD-703HP1

### KD-884HP0
- 已登錄 Deep Candidate。
- 品牌／型號／MIT／供應／exact official page／衝突初查 PASS。
- image rights BLOCKED。
- editorial review PENDING。
- publication BLOCKED / unpublished。

### KD-703HP1
- 台灣品牌已確認。
- 現行官方產品線、exact official page、台灣製造規格已確認。
- image rights BLOCKED。
- Promotion Audit 只標成可進 Deep Candidate 評估；尚未新增為正式 candidate。

## 資料 Pipeline

```text
Registry shards (100)
Enrichment Results Manifest (20)
Deep Candidate source
       │
       ├─ build_public_catalog.py → catalog.public.json
       ├─ report_registry_expiry.py → registry-expiry.json
       └─ build_promotion_audit.py → promotion-audit.json
```

所有三個公開 JSON 都是 deploy-time artifact；研究 source of truth 保留在受控 Registry / Enrichment / Candidate 檔。

## 證據治理

- 台灣品牌 ≠ 台灣製造。
- Enrichment completed ≠ verified。
- not_found / blocked 是正式研究結果。
- MIT exact-model 證據不得外推其他型號。
- 有效 MIT ≠ 即時在售；銷售通路 ≠ 即時庫存。
- 同系列頁 ≠ exact-model 官方頁。
- 官方圖片公開可見 ≠ 已授權重用。
- Promotion Audit ≠ promotion。
- Deep Candidate ≠ deep editorial case ≠ formal publication。
- Formal Publication Gate 不降低；published 維持 0。

## 核心檔案

```text
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
build-info.json
```

## 尚未完成

- 驗收 V3.7 最終 production build／deploy。
- KD-884HP0 / KD-703HP1 的圖片重用授權或合法替代素材仍未完成。
- KD-884HP0 editorial review 尚未完成；KD-703HP1 尚未人工登錄為 Deep Candidate。
- 第一筆 formal published 仍未產生，且不能在 Gate 不完整時硬推。

## 下一步

1. 驗收 V3.7 final production。
2. 不再擴 Enrichment Queue；先處理 KD-884HP0 / KD-703HP1 的圖片權利與 editorial promotion review。
3. 決定 KD-703HP1 是否人工加入 `data/deep_case.candidates.json`，必須保留 image-rights blocker。
4. 只有完整通過既有 Formal Publication Gate 才能出現第一筆 published。
