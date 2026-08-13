# Enrichment 20/20 Promotion Audit

日期：2026-08-13

## 目的

第一輪 20 筆 Enrichment Queue 已全部研究完成。研究完成不代表 20 筆都適合推薦，因此 V3.7 在 Enrichment 後再加入 Promotion Audit，將產品依證據完整度與品牌身分分流。

## 最終研究結果

```text
researched records: 20 / 20
verified tasks: 22
not_found tasks: 51
blocked tasks: 7
pending tasks: 0
formal published: 0
```

品牌身分：

```text
Taiwan-brand confirmed: 8
Non-Taiwan-brand confirmed: 3
Brand-origin unresolved: 9
```

## Promotion Audit buckets

### 1. Deep Candidate 條件已達，但資產／編輯 Gate 阻擋：2

- CHIMEI `KD-884HP0`
  - 已登錄 `deep_case.candidates.json`
  - image rights blocked
  - editorial review pending
  - formal publication blocked

- CHIMEI `KD-703HP1`
  - brand identity verified
  - current official catalog verified
  - exact-model official page verified
  - official specification lists Taiwan manufacturing origin
  - image rights blocked
  - Promotion Audit 僅標記 `eligible_for_deep_candidate_review`，沒有自動登錄 candidate

### 2. 台灣品牌 research-only：6

品牌身分已確認，但 current-sale、exact-model 官方頁或其他消費端證據仍不完整，因此維持 research-only。

### 3. 非台灣品牌，但有台灣製 exact-model：3

Panasonic：
- `NR-C507XVS`
- `NR-D507XVS`
- `NR-C617XVS`

Panasonic 品牌起源已確認為日本；三個精確型號仍各自保留有效 MIT 臺灣製造證據。

Promotion state：
`exclude_from_taiwan_brand_recommendation`

這不代表否定其臺灣製造證據，只代表不列入「台灣品牌推薦」。

### 4. 品牌身分待確認 research-only：9

這些產品具有 MIT exact-model 製造證據，但品牌國籍或消費端證據不足。不得由台灣申請公司／製造商直接推定品牌是台灣品牌。

## Anti-Arctic 最終 P2 結果

上比實業官方 Shine Beam 網站由上比實業有限公司營運，並將 Anti-Arctic 明列為品牌分類；MIT 資料亦以同一公司申請 Anti Arctic 品牌商品，因此品牌身分可確認為台灣品牌。

但 `R-9-K(紅)` exact-model：
- current_sale: not_found
- official_product_page: not_found
- image_rights: blocked

同品牌其他商品仍在官方商城，不可外推 R-9-K 仍現售。

## Promotion Audit 治理

Promotion Audit 只做分類與下一步規劃，不執行 promotion：

- 不修改 raw Registry。
- 不修改 manufacturing evidence。
- 不自動新增 Deep Candidate。
- 不修改 Formal Publication Gate。
- 不把 research completed 當成 published。

正式發布仍為 0。
