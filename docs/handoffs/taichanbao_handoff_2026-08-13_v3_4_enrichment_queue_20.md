# 台產報 Handoff — V3.4 Enrichment Queue 20 / Batch 2

日期：2026-08-13

## 專案名稱
台產報 / Taichanbao

## Repository
`qookey109-pixel/Taichanbao`

## 目前狀態

```text
Version: V3.4 Enrichment Queue 20 — Batch 2
Real research candidates: 104
MIT active exact models: 100
Deep editorial cases: 4
Registry shards: 3
Enrichment queue: 20
Researched queue records: 10
Verified enrichment tasks: 12
Not-found tasks: 23
Blocked tasks: 5
Pending tasks: 40
Enrichment Taiwan-brand confirmed records: 6
Enrichment current-sale/supply confirmed records: 5
Exact-model official product pages confirmed: 1
Formal published: 0
```

## 本輪已完成

- V3.3 Scale 100、V3.2 Lifecycle、分類集中度 Gate、Formal Publication Gate 全部保留。
- 第一批 5 筆：SNUG、MIFIYA、JUMP、ADHOC、格蕾絲。
- 第二批新增完成 5 筆：三環牌 296、奇美 KD-884HP0、奇美 KD-853HM0、YYMe 1157508(紫)、NINO1881 L2425(粉色)。
- `data/enrichment.results.v1.json` 升到 Batch 2，共保存 10 筆 findings。
- `data/enrichment.queue.json` 目前 10 筆 completed、10 筆 queued。
- 累計任務：12 verified／23 not_found／5 blocked／40 pending。
- `scripts/validate_enrichment_v3_4.py` 已鎖定上述 Batch 2 統計與 Queue／Results 一致性。
- `scripts/build_public_catalog.py` 繼續只把人工 verified 的品牌身分與現售結果合併到 deploy-time catalog；raw Registry 不改寫。
- `build-info.json`、`scripts/validate_site.py`、`PROJECT_STATUS.md` 已同步 Batch 2。
- published 維持 0。

## 第二批證據重點

### 三環牌 `296#(1082#)(白)`
- 官方品牌：`https://www.chungtatowel.com.tw/about.aspx`
- 精確型號 MIT：`https://keid.nat.gov.tw/mittw/products/prod_more?id=286230`
- 品牌身分 verified：中大棉織官方說明 1951 年創於雲林虎尾，以三環牌為品牌識別並支持台灣 MIT 品牌。
- current_sale verified：MIT 列自營店面、傳統市場、展售會；不代表即時庫存。
- exact-model brand page not_found。
- 官方圖片無重用授權 → blocked。

### 奇美 `KD-884HP0`
- 官方品牌：`https://www.chimei.com.tw/brand-story`
- 官方精確型號：`https://electronics.chimei.com.tw/dish-dryer/ultraviolet%20%20rays/kd-884hp0`
- 官方產品列表：`https://www.chimei.com.tw/dish-dryer/all`
- 品牌身分 verified：CHIMEI 由台灣奇美集團發展。
- current_sale verified：目前官方烘碗機列表列 KD-884HP0 為 NEW。
- official_product_page verified：精確型號官方頁存在；規格明列製造產地台灣。
- image_rights blocked：官網 All rights reserved。
- 目前是 Queue 中最完整的 exact-model enrichment 案例，但仍 unpublished。

### 奇美 `KD-853HM0(白)`
- 品牌身分 verified。
- current_sale verified：MIT 精確型號頁 `https://keid.nat.gov.tw/mittw/products/prod_more?id=287271` 列新視代科技經銷通路；不代表即時庫存。
- current CHIMEI product list 未找到該型號，所以 exact-model official product page = not_found。
- exact-model official image = not_found。

### YYMe `1157508(紫)`
- MIT listing：`https://keid.nat.gov.tw/mittw/products/?classid=5&p=9`
- exact model active to 2029-07-02。
- brand_identity/current_sale/official_product_page/image_rights 均 not_found。
- 不得從元維棉織廠為台灣申請者推定 YYMe 品牌國籍。

### NINO1881 `L2425(粉色)`
- MIT listing：`https://keid.nat.gov.tw/mittw/products/?classid=5&p=5`
- MIT company：`https://keid.nat.gov.tw/mittw/products/manu_more?id=2398`
- exact model active to 2029-07-21。
- brand_identity/current_sale/official_product_page/image_rights 均 not_found。
- 搜尋到的同名 NINO1881 床墊網站不是足以確認該毛巾品牌身分的同一證據鏈，因此不混用。

## 第一批結果保留

- SNUG：品牌 verified；現售／exact page not_found；圖片 blocked。
- MIFIYA：四項 not_found。
- JUMP：四項 not_found。
- ADHOC：品牌＋sales channel verified；exact page not_found；圖片 blocked。
- 格蕾絲：品牌＋客製供應 verified；exact page not_found；圖片 blocked。

## 治理規則

- Enrichment completed ≠ verified；not_found／blocked 是正式研究結果。
- MIT 製造證據不得推定品牌國籍或現售。
- current_sale 只能套用精確型號；銷售通路紀錄不等於即時庫存。
- exact-model official product page 必須是品牌／公司官方頁。
- KD-884HP0 的台灣產地官方規格不得外推到 KD-853HM0 或其他奇美產品。
- 公開可見圖片不等於可重用；無授權則 blocked/not_found。
- verified enrichment 只經受控 builder 反映到 public catalog；不得自動修改 manufacturing evidence、verification status 或 publication status。
- Formal Publication Gate 不降低；published 維持 0。

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

1. 驗收 Batch 2 最後 production build/deploy。
2. 評估 KD-884HP0 是否升級成新的 deep editorial candidate，但不得直接 published。
3. 完成剩餘 P1 `YYMe 1147508(紫)`。
4. 再研究 P2：KD-703HP1、Panasonic NR-C507XVS／NR-D507XVS／NR-C617XVS、YYMe/NINO1881 同系列、Anti Arctic、伯諾。
5. 任何圖片仍須先解決使用權；Formal Publication Gate 維持 0 published。

## 新對話可直接使用的接續指令

繼續台產報 `qookey109-pixel/Taichanbao`。以 GitHub main、`PROJECT_STATUS.md` 與本 Handoff 為準。V3.4 已完成兩批、共 10 筆 enrichment，不要重查這 10 筆，除非有新的官方證據。先驗收 Batch 2 最新 Pages production result。之後優先評估 KD-884HP0 deep-case candidate、完成 YYMe 1147508(紫)，再進 P2。台灣品牌、MIT 製造、現售、exact official page、圖片權利與正式發布必須分開；published 維持 0。
