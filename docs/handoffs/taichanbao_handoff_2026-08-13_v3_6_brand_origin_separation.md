# 台產報 Handoff — V3.6 Brand-Origin Separation

日期：2026-08-13

## 專案名稱
台產報 / Taichanbao

## Repository
`qookey109-pixel/Taichanbao`

## 目前狀態

```text
Version: V3.6 Brand-Origin Separation
Real research candidates: 104
MIT active exact models: 100
Deep editorial cases: 4
Deep editorial candidates: 1 (KD-884HP0, blocked)
Enrichment queue: 20
Researched: 15
Verified tasks: 21
Not-found tasks: 33
Blocked tasks: 6
Pending tasks: 20
Taiwan-brand confirmed: 7
Non-Taiwan-brand confirmed: 3
Current-sale/supply confirmed: 9
Exact official product pages: 2
Formal published: 0
```

## 本次已完成

- V3.5 final production 已 success。
- P2 第一批 4 records 完成：KD-703HP1、Panasonic NR-C507XVS、NR-D507XVS、NR-C617XVS。
- 新增 `data/enrichment.results.v3.json`；Results Manifest 升為 3 batches / 15 records。
- Queue 升為 V3.6，15/20 records completed。
- Panasonic 官方歷史證實品牌源自 1918 日本大阪，三筆 Panasonic brand result 均為 `non_taiwan_brand`。
- 三個 Panasonic exact models 同時保留有效 MIT 臺灣製造證據與官方登錄銷售通路。
- CHIMEI KD-703HP1：台灣品牌身分 verified、官方 current catalog verified、exact official page verified；官方規格明列製造產地台灣；image rights blocked。
- `scripts/build_public_catalog.py` 分開統計 Taiwan / non-Taiwan brand outcomes。
- 新增 `assets/brand-origin-v3-6.js` / `.css`，前台呈現品牌身分與 MIT exact-model 製造證據的雙軸結果。
- `scripts/validate_enrichment_v3_4.py` 加入 Panasonic separation regression：raw Registry 品牌欄仍 unverified、manufacturing evidence 仍 active，只有受控 enrichment 可標 `non_taiwan_brand`。
- `scripts/validate_site.py`、CI、Pages、README、PROJECT_STATUS、build-info 全部升級 V3.6。
- 新增研究紀錄 `docs/research/2026-08-13_panasonic_brand_origin_separation.md`。

## 核心 Panasonic regression

Panasonic brand origin：
- `https://news.panasonic.com/global/press/en180307-2`
- `https://www.panasonic.com/global/consumer/history.html`

MIT exact models：
- NR-C507XVS: `https://keid.nat.gov.tw/mittw/products/prod_more?id=287469`
- NR-D507XVS: `https://keid.nat.gov.tw/mittw/products/prod_more?id=287468`
- NR-C617XVS: `https://keid.nat.gov.tw/mittw/products/prod_more?id=287465`

Correct representation:

```text
brand_origin_status              non_taiwan_brand
manufacturing_evidence_status    mit_certified_active
record_scope                     exact_model
publication_status               unpublished
```

## CHIMEI KD-703HP1

- official exact page: `https://www.chimei.com.tw/dish-dryer/ultraviolet%20%20rays/kd-703hp1`
- current product line: `https://www.chimei.com.tw/dish-dryer/ultraviolet%20%20rays`
- MIT exact model in Registry

Correct representation:

```text
brand_origin_status              taiwan_brand_confirmed
manufacturing_evidence_status    mit_certified_active
current_sale_confirmed           true
exact_official_product_page      verified
image_rights                     blocked
publication_status               unpublished
```

## V3.5 Deep Candidate 保留

KD-884HP0 仍是 blocked deep candidate；圖片權利與 editorial review 未完成，不得 promotion 或 published。

## 重要治理

- 台灣品牌 ≠ 台灣製造。
- 非台灣品牌可以有臺灣製造 exact models。
- 台灣品牌不可把單一型號製造證據外推到全品牌。
- MIT active ≠ live stock。
- sales channels ≠ live inventory。
- exact official page 必須品牌／公司官方精確型號頁。
- 官方圖片可見 ≠ 可重用。
- Deep candidate ≠ deep case ≠ formal publication。
- Formal Publication Gate 不降低；published 仍為 0。

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
data/deep_case.candidates.json

assets/brand-origin-v3-6.js
assets/brand-origin-v3-6.css
assets/enrichment-v3-4.js
assets/deep-candidates-v3-5.js

scripts/build_public_catalog.py
scripts/validate_enrichment_v3_4.py
scripts/validate_deep_candidates_v3_5.py
scripts/validate_site.py

.github/workflows/validate.yml
.github/workflows/pages.yml

docs/research/2026-08-13_panasonic_brand_origin_separation.md
```

## 尚未完成

- V3.6 final production 尚需用 `docs/deployment/pages-production-result.json` 驗收。
- Queue 剩餘 5 P2 records / 20 tasks：YYMe yellow、NINO1881 blue、YYMe pink、Anti Arctic、伯諾。
- KD-884HP0 image rights / editorial review 未解決。

## 明確下一步

1. 驗收 V3.6 final production。
2. 完成最後 5 P2，使 Queue 20/20 complete。
3. 對 20 筆做 promotion audit：Deep Candidate / research-only / non-Taiwan-brand-but-Taiwan-made。
4. Formal published 維持 0，除非完整通過既有 Gate。

## 新對話接續指令

繼續台產報 `qookey109-pixel/Taichanbao`。以 GitHub main 的 `PROJECT_STATUS.md`、`README.md` 與 `docs/handoffs/taichanbao_handoff_2026-08-13_v3_6_brand_origin_separation.md` 為基準。不要重做 V3.6。先驗收最新 Pages production result；成功後完成剩餘 5 筆 P2。Panasonic 三筆已驗證為非台灣品牌但具有有效 MIT 臺灣製造 exact-model 證據，不得改標成台灣品牌。KD-884HP0 仍為 blocked deep candidate。published 維持 0。
