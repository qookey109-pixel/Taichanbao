# 台產報 PROJECT STATUS

更新日期：2026-08-13

## Version

`V3.4 Enrichment Queue 20 — Batch 2`

## 正式網站方向

台產報維持「雜誌選品＋精確型號證據資料庫」雙層架構。台灣品牌身分、精確型號、臺灣製造證據、政府標章、現售狀態、官方產品頁、圖片權利、證據有效期限與正式發布狀態分開管理。

## V3.4 目前完成

- V3.3 Scale 100 完整保留：100 筆 MIT 有效精確型號＋4 筆深度案例＝104 筆真實研究候選。
- Enrichment Queue 固定 20 筆、每筆 4 任務，共 80 個任務；目前已完成兩批、共 **10 筆 P1** 外部查核。
- 第一批：SNUG、MIFIYA、JUMP、ADHOC、格蕾絲。
- 第二批：三環牌 296、奇美 KD-884HP0、奇美 KD-853HM0、YYMe 1157508(紫)、NINO1881 L2425(粉色)。
- `data/enrichment.results.v1.json` 已升到 `V3.4 Enrichment Results Batch 2`，保存 10 筆逐項 findings、來源 URL、查核日期與證據範圍。
- 累計結果：**12 verified、23 not_found、5 blocked、40 pending**。
- 台灣品牌身分已確認的 enrichment records：6 筆（SNUG、ADHOC、格蕾絲、三環牌，以及兩筆奇美）。
- 現售／供應通路已確認：5 筆；這個欄位只表示有官方／政府登錄銷售證據，不等於即時庫存。
- 精確型號品牌官方產品頁已確認：目前 **1 筆，奇美 KD-884HP0**。
- `scripts/validate_enrichment_v3_4.py` 已鎖定 10 researched／12 verified／23 not_found／5 blocked／40 pending。
- `scripts/build_public_catalog.py` 會把人工 verified 的品牌身分與 current-sale 結果受控合併到 deploy-time `catalog.public.json`；原始 MIT Registry 不被改寫。
- `assets/enrichment-v3-4.js` / `.css` 繼續分開呈現 verified／not_found／blocked／pending，並顯示已研究紀錄與查核日期。
- `scripts/validate_site.py`、`build-info.json` 已同步第二批統計。
- `verification_status`、`manufacturing_evidence_status`、`publication_status` 均未因 enrichment 自動升級。

## 目前資料狀態

```text
真實研究候選：104
├─ 深度多圖案例：4
└─ MIT 有效精確型號：100

Enrichment Queue：20
├─ 已研究紀錄：10
├─ 已驗證任務：12
├─ 查無官方證據：23
├─ 權利阻擋：5
└─ 待處理任務：40

Enrichment 台灣品牌已確認：6 records
Enrichment 現售／供應通路已確認：5 records
精確型號品牌官方頁已確認：1 record
隔離 Demo：6
正式發布：0
Registry shards：3
已過期 Registry：0
```

## 第二批 5 筆結果

### 三環牌 `296#(1082#)(白)`
- 品牌身分：verified → 中大棉織官方說明 1951 年創立於雲林虎尾，以三環牌為品牌識別，並稱為台灣 MIT 品牌。
- 現售／供應：verified → MIT 精確型號頁列自營店面、傳統市場、展售會；不宣稱即時庫存。
- 精確型號品牌官方頁：not_found；官方站只有一般產品／品牌介紹。
- 圖片權利：blocked；官方圖片沒有找到第三方重用授權。

### 奇美 `KD-884HP0`
- 品牌身分：verified → CHIMEI 奇美品牌由台灣奇美集團發展。
- 現售：verified → 奇美家電目前烘碗機列表仍列 KD-884HP0 為 NEW。
- 精確型號品牌官方頁：verified → 官方頁完整列型號、規格，並明列「製造產地：台灣」。
- 圖片權利：blocked → 奇美官網 All rights reserved，未取得重用授權。
- 目前為 Enrichment Queue 中最完整的 exact-model 官方頁案例；但仍未通過 Formal Publication Gate。

### 奇美 `KD-853HM0(白)`
- 品牌身分：verified。
- 現售／供應：verified → MIT 精確型號頁列新視代科技經銷通路；不宣稱即時庫存。
- 精確型號品牌官方頁：not_found；目前奇美家電烘碗機產品列表未找到此型號。
- 圖片權利：not_found；沒有找到 exact-model 品牌官方素材頁。

### YYMe `1157508(紫)`
- MIT 精確型號製造證據有效至 2029-07-02。
- 品牌身分：not_found；不能從元維棉織廠／MIT 申請資料直接推成台灣品牌。
- 現售：not_found；該精確型號沒有取得官方銷售通路／品牌現售頁證據。
- 精確型號官方頁、圖片權利：not_found。

### NINO1881 `L2425(粉色)`
- MIT 精確型號製造證據有效至 2029-07-21。
- 品牌身分：not_found；寶佳貿易與 MIT 品牌欄不足以單獨證明品牌國籍，且同名床墊網站不拿來混用。
- 現售：not_found；未取得 exact-model 官方銷售證據。
- 精確型號官方頁、圖片權利：not_found。

## Enrichment 治理

- `completed` 只代表本輪研究已結束，不代表四項都 verified。
- `brand_identity` 與 MIT 製造證據分離；製造商／申請者在台灣不等於品牌一定是台灣品牌。
- `current_sale` 必須限定精確型號；政府登錄銷售通路不等於即時庫存。
- `official_product_page` 只接受品牌／公司官方 exact-model 頁；同系列或第三方零售頁不能冒充。
- `image_rights` 沒有明確重用授權時只能 blocked／not_found。
- KD-884HP0 官方頁的「製造產地：台灣」只適用 KD-884HP0，不外推到 KD-853HM0 或其他奇美商品。
- Enrichment verified 可經 builder 反映到 public catalog，但不得自動修改 manufacturing evidence 等級、verification status 或 publication status。
- Formal Publication Gate 維持不變，正式發布仍為 0。

## V3.3 / V3.2 基線保留

- Registry：100 筆／3 shards；真實研究候選 104。
- 分類集中度 Gate：任一分類 <= 40%，家電 <= 40／100，至少 8 個分類。
- Lifecycle Dashboard：已過期／30／90／180／365 天到期；過期 MIT Registry 阻擋驗證。
- public catalog 為 deploy-time artifact，研究 source of truth 仍是 Registry shards＋受控 enrichment results。

## 核心檔案

```text
data/enrichment.queue.json
data/enrichment.results.v1.json
assets/enrichment-v3-4.js
assets/enrichment-v3-4.css
scripts/validate_enrichment_v3_4.py
scripts/build_public_catalog.py
scripts/validate_site.py
build-info.json
PROJECT_STATUS.md
```

其餘 V3.3 Registry、V3.2 Lifecycle、V2.8 Media、V2.5 Recovery、V2.3 Formal Publication Gate 均保留，不得重做或降低標準。

## 尚未完成

- 驗收 Batch 2 更新後最新 production build／deploy。
- Queue 尚餘 10 筆未研究；其中 P1 尚有 YYMe `1147508(紫)`，其他為 P2。
- 取得可合法使用的產品圖片／授權。
- 對 KD-884HP0 評估是否值得升級成新的 deep editorial case，但不得跳過圖片權利與正式發布 Gate。
- 補餐廚與清潔用品 Registry 類別。
- 第一筆正式發布仍必須完整通過 Formal Publication Gate。

## 下一步

1. 驗收最新 production build／deploy。
2. 對 `KD-884HP0` 建立 deep-case 候選評估，而不是直接發布。
3. 完成剩餘 P1 `YYMe 1147508(紫)`，再開始 P2（KD-703HP1、Panasonic 冰箱、YYMe/NINO1881 同系列、Anti Arctic、伯諾）。
4. 不為了提高 verified 數量而把 MIT 有效、同系列頁或第三方零售頁誤當正式證據。
