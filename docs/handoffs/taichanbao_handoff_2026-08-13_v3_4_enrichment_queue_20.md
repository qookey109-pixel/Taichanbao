# 台產報 Handoff — V3.4 Enrichment Queue 20 / Batch 1

日期：2026-08-13

## 專案名稱
台產報 / Taichanbao

## Repository
`qookey109-pixel/Taichanbao`

## 目前狀態

```text
Version: V3.4 Enrichment Queue 20
Real research candidates: 104
MIT active exact models: 100
Deep editorial cases: 4
Registry shards: 3
Enrichment queue: 20
Researched queue records: 5
Verified enrichment tasks: 5
Not-found tasks: 12
Blocked tasks: 3
Pending tasks: 60
Enrichment Taiwan brands confirmed: 3
Enrichment current-sale/supply confirmed: 2
Formal published: 0
```

## 本輪已完成

- 不重做 V3.3 Scale 100。
- 實際完成第一批 5 筆 P1 enrichment：SNUG、MIFIYA、JUMP、ADHOC、格蕾絲。
- 新增 `data/enrichment.results.v1.json`，保存 finding、摘要、來源與查核日期。
- `data/enrichment.queue.json` 第一批 5 筆改為 completed；任務結果與 Results 檔一致。
- 第一批任務結果：5 verified、12 not_found、3 blocked。
- SNUG、ADHOC、格蕾絲：品牌身分 verified → `taiwan_brand_confirmed`。
- ADHOC GENTLE 102(金)：MIT 精確型號頁列自營銷售通路，因此 current_sale verified，但不宣稱即時庫存。
- 格蕾絲 1161-3(米)：MIT 精確型號頁列客製化供應通路，因此 current_sale verified，但不當成一般零售現貨。
- MIFIYA MIFIYA01(白)、JUMP 168(藍)：MIT 製造證據有效，但品牌國籍／官方現售／精確型號品牌頁仍 not_found。
- SNUG／ADHOC／格蕾絲圖片權利為 blocked；官方頁未授予重用權。
- Workbench 現在分開顯示 verified／not_found／blocked／pending，並顯示已研究紀錄與每筆本輪摘要。
- `scripts/validate_enrichment_v3_4.py` 鎖定 Queue／Results 一致性與第一批統計。
- `scripts/build_public_catalog.py` 讀取 enrichment results，只把人工 verified 的品牌身分與現售資訊合併到 deploy-time public catalog。
- 原始 MIT Registry、製造證據狀態、verification status、publication status 不被改寫。
- `build-info.json`、`scripts/validate_site.py`、`PROJECT_STATUS.md` 已同步。

## 第一批證據重點

### SNUG S9900000015(紫藕)
- 官方品牌頁：`https://shop.snug.com.tw/about`
- MIT 業者：`https://keid.nat.gov.tw/mittw/products/manu_more?id=1734`
- 品牌身分 verified。
- 精確型號現售與官方商品頁未找到。
- 官方站 Copyright © 2026 sNug，圖片重用 blocked。

### MIFIYA MIFIYA01(白)
- MIT 業者：`https://keid.nat.gov.tw/mittw/products/manu_more?id=3122`
- 製造證據有效；品牌國籍不得由公司所在地推定。
- 品牌身分／現售／品牌官方精確型號頁均 not_found。

### JUMP 168(藍)
- MIT 業者同上。
- 製造證據有效；品牌身分、現售、官方精確型號頁仍 not_found。

### ADHOC GENTLE 102(金)
- 官方品牌：`https://www.adhoceyewear.com/about_view.php?kind1=1&lang=tw&pid=1`
- 精確型號 MIT：`https://keid.nat.gov.tw/mittw/products/prod_more?id=280668`
- 品牌身分 verified。
- 自營銷售通路 verified；不保證即時庫存。
- 精確型號品牌官方商品頁 not_found。
- 官方站 All Rights Reserved，圖片權利 blocked。

### 格蕾絲 1161-3(米)
- 官方品牌：`https://www.gracetowel.net/`
- 官方商城：`https://www.gracetowel.com.tw/`
- 精確型號 MIT：`https://keid.nat.gov.tw/mittw/products/prod_more?id=287833`
- 品牌身分 verified。
- 客製化供應通路 verified；不是零售現貨聲明。
- 精確型號品牌官方商品頁 not_found。
- 圖片權利 blocked。

## 治理規則

- Enrichment completed ≠ verified；not_found／blocked 是正式研究結果。
- MIT 製造證據不得推定品牌國籍或現售。
- current_sale 只能套用精確型號，且銷售通路紀錄不等於即時庫存。
- 同系列頁不能冒充 exact-model official product page。
- 官方圖片公開可見不等於可重用。
- verified enrichment 可經受控 builder 反映到 public catalog，但不得自動修改 manufacturing evidence 或 publication status。
- Formal Publication Gate 不降低；正式發布仍為 0。

## 重要檔案

```text
PROJECT_STATUS.md
build-info.json
data/enrichment.queue.json
data/enrichment.results.v1.json
assets/enrichment-v3-4.js
assets/enrichment-v3-4.css
scripts/validate_enrichment_v3_4.py
scripts/build_public_catalog.py
scripts/validate_site.py
.github/workflows/validate.yml
.github/workflows/pages.yml
```

## 明確下一步

1. 驗收這一批最後 production build/deploy。
2. 再完成下一批 5 筆 P1：優先三環牌 296、奇美 KD-884HP0、奇美 KD-853HM0、YYMe 1157508／1147508 或 NINO1881 L2425。
3. 對 SNUG／ADHOC／格蕾絲繼續追精確型號品牌商品頁與圖片授權。
4. 不因 verified 數量目標而降低證據標準。
5. Formal Publication Gate 維持 0 published。

## 新對話可直接使用的接續指令

繼續台產報 `qookey109-pixel/Taichanbao`。以 GitHub main、`PROJECT_STATUS.md` 與本 Handoff 為準。V3.4 第一批 5 筆 P1 enrichment 已完成，不要重查 SNUG/MIFIYA/JUMP/ADHOC/格蕾絲，除非有新的官方證據。先驗收最新 Pages production result，再做下一批 5 筆 P1。任何 MIT、品牌、現售、官方頁、圖片權利證據都必須限制到實際涵蓋範圍；Formal Publication Gate 不降低，published 維持 0。
