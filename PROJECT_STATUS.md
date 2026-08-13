# 台產報 PROJECT STATUS

更新日期：2026-08-13

## Version

`V3.5 Deep Candidate Gate`

## 正式網站方向

台產報維持「雜誌選品＋精確型號證據資料庫」雙層架構，並新增「Deep Candidate」中間層。台灣品牌身分、精確型號、臺灣製造證據、政府標章、現售狀態、官方產品頁、圖片權利、證據有效期限、深度專題候選與正式發布狀態全部分開管理。

## V3.5 本次完成

- V3.3 Scale 100、V3.2 Lifecycle、V3.4 Enrichment 架構全部保留。
- Enrichment P1 **11 / 11 全部完成**。
- 最後 P1 `YYMe 1147508(紫)` 已查核：MIT 精確型號有效至 2029-07-02，但品牌國籍、現售、exact-model 品牌官方頁、官方圖片權利均 `not_found`；不從台灣申請廠商或 MIT 製造證據反推品牌國籍。
- Enrichment 累計：11 researched、12 verified、27 not_found、5 blocked、36 pending；剩餘全部為 P2。
- 新增 `data/enrichment.results.manifest.json`，Enrichment Results 改為可分批累積：
  - `data/enrichment.results.v1.json`：前兩批 10 records。
  - `data/enrichment.results.v2.json`：第三批 1 record。
- `scripts/build_public_catalog.py` 改為依 Results Manifest 合併所有 enrichment batches，並保存人工 verified 的品牌身分、current sale、exact official page URL 與 enrichment findings；raw Registry 不改寫。
- 新增 `data/deep_case.candidates.json`。
- 第一個 Deep Candidate：**CHIMEI 奇美 KD-884HP0**。
- KD-884HP0 Deep Candidate 前置 Gate：品牌身分、精確型號、MIT 製造證據、現售／供應、exact official product page、重大衝突初查全部 PASS。
- KD-884HP0 官方精確型號頁明列 `製造產地：台灣`；MIT 標章 `02000038-02030` 有效至 2029-06-01。證據只適用此型號。
- KD-884HP0 仍被 `image_rights: blocked` 與 `editorial_review: pending` 阻擋，因此 `formal_publication: blocked`、`publication_status: unpublished`。
- 新增 `assets/deep-candidates-v3-5.js` / `.css`，前台直接顯示 Candidate Gate 與阻擋原因。
- 新增 `scripts/validate_deep_candidates_v3_5.py`，從 Registry＋Enrichment Results 交叉驗證 candidate，不允許跳過圖片權利或人工編輯審核。
- `assets/catalog-v3.js` 已載入 V3.5 Deep Candidate Layer；V3.5 是目前前台最終版本標記。
- `scripts/validate_enrichment_v3_4.py` 已升級為 Manifest 驗證並鎖定 P1 完成。
- `scripts/validate_site.py`、GitHub Actions、Pages workflow、README、`build-info.json` 均已升級到 V3.5。

## 目前資料狀態

```text
真實研究候選：104
├─ 既有深度編輯案例：4
└─ MIT 有效精確型號：100

Deep editorial candidates：1
└─ CHIMEI KD-884HP0 → blocked_assets

Enrichment Queue：20
├─ P1：11 / 11 完成
├─ 已研究紀錄：11
├─ verified：12
├─ not_found：27
├─ blocked：5
└─ P2 pending tasks：36

台灣品牌已確認 enrichment records：6
現售／供應已確認：5
exact official product page 已確認：1
正式發布：0
Registry shards：3
已過期 Registry：0
```

## KD-884HP0 Deep Candidate Gate

```text
brand_identity                  PASS
exact_model_identity             PASS
mit_manufacturing_evidence       PASS
current_sale_or_supply           PASS
exact_official_product_page      PASS
key_conflict_review              PASS · no conflict found
image_rights                     BLOCKED
editorial_review                 PENDING
formal_publication               BLOCKED
```

重要：官方 exact-model 頁的「製造產地：台灣」不得外推到 KD-853HM0、KD-703HP1 或其他奇美商品。

## Enrichment Results Pipeline

```text
data/enrichment.results.manifest.json
├─ enrichment.results.v1.json (10)
└─ enrichment.results.v2.json (1)
          │
          ▼
scripts/build_public_catalog.py
          │
          ▼
data/catalog.public.json  # deploy-time artifact
```

`completed` 只表示該輪研究結束；`not_found` / `blocked` 都是正式結果，不代表尚未處理。

## 證據治理

- 台灣品牌 ≠ 台灣製造。
- MIT 製造證據不得推定品牌國籍或現售。
- 有效 MIT 標章 ≠ 即時在售。
- 銷售通路紀錄 ≠ 即時庫存。
- 同系列頁 ≠ exact-model 官方頁。
- 官方圖片公開可見 ≠ 已取得重用授權。
- Deep candidate ≠ deep editorial case ≠ formal publication。
- Candidate Gate、Enrichment、圖片、搜尋、Lifecycle、metadata 均不能自動升級 publication。
- Formal Publication Gate 不降低，正式發布維持 0。

## 核心檔案

```text
data/enrichment.queue.json
data/enrichment.results.manifest.json
data/enrichment.results.v1.json
data/enrichment.results.v2.json
data/deep_case.candidates.json

assets/enrichment-v3-4.js
assets/enrichment-v3-4.css
assets/deep-candidates-v3-5.js
assets/deep-candidates-v3-5.css

scripts/build_public_catalog.py
scripts/validate_enrichment_v3_4.py
scripts/validate_deep_candidates_v3_5.py
scripts/validate_site.py

.github/workflows/validate.yml
.github/workflows/pages.yml
build-info.json
```

## 尚未完成

- 驗收 V3.5 最後 production build／deploy。
- Deep Candidate KD-884HP0 的圖片重用授權／可合法替代素材仍未解決。
- KD-884HP0 尚未完成 deep editorial review，因此不能加入正式 deep cases，更不能 published。
- P2 尚有 9 records／36 tasks：KD-703HP1、Panasonic 三個冰箱型號、YYMe 同系列、NINO1881 同系列、Anti Arctic、伯諾。
- 補餐廚／清潔用品 Registry 廣度仍可在後續進行。

## 下一步

1. 驗收 V3.5 production。
2. 進 P2 enrichment，優先 `KD-703HP1` 與三個 Panasonic 冰箱；Panasonic 品牌國籍必須獨立查證，不因台灣 MIT 製造紀錄視為台灣品牌。
3. 另開圖片授權／替代素材工作流處理 KD-884HP0，未解決前保持 blocked candidate。
4. Formal published 維持 0。
