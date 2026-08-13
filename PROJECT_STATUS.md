# 台產報 PROJECT STATUS

更新日期：2026-08-13

## Version

`V3.6 Brand-Origin Separation`

## 正式網站方向

台產報維持「雜誌選品＋精確型號證據資料庫」架構。V3.6 正式把**品牌國籍**與**精確型號製造證據**拆成兩條獨立證據鏈：非台灣品牌可以有台灣製造型號，台灣品牌也不能把單一型號的產地外推到全品牌。

## V3.6 本次完成

- V3.3 Scale 100、V3.2 Lifecycle、V3.5 Deep Candidate Gate 全部保留。
- Enrichment Results Manifest 升級為 3 batches／15 researched records。
- P1 11/11 完成；P2 第一批 4 records 完成：CHIMEI `KD-703HP1`、Panasonic `NR-C507XVS`、`NR-D507XVS`、`NR-C617XVS`。
- Enrichment 累計：21 verified、33 not_found、6 blocked、20 pending。
- 台灣品牌已確認：7 records；非台灣品牌已確認：3 records；現售／供應已確認：9；exact official product page：2。
- 新增 `data/enrichment.results.v3.json`。
- `data/enrichment.results.manifest.json` 升級為 `V3.6 Enrichment Results Manifest`。
- `data/enrichment.queue.json` 升級為 `V3.6 Brand-Origin Separation`，目前 15/20 records completed。
- `scripts/build_public_catalog.py` 現在分開統計 `enrichment_taiwan_brand_confirmed` 與 `enrichment_non_taiwan_brand_confirmed`。
- 新增 `assets/brand-origin-v3-6.js` / `.css`，前台顯示「品牌身分 × MIT exact-model 製造證據」雙軸結果。
- `scripts/validate_enrichment_v3_4.py` 加入 Panasonic brand-origin regression：raw Registry 必須保持 `brand_origin_status: unverified`、MIT 製造證據維持 active，而 enrichment 才能將品牌身分標成 `non_taiwan_brand`。
- `scripts/validate_site.py`、CI、Pages、README、`build-info.json` 均已升級 V3.6。

## Panasonic Brand-Origin Separation

Panasonic 官方歷史資料確認品牌／公司源自 **1918 年日本大阪**，所以以下三個型號的品牌身分均為：

```text
brand_origin_status: non_taiwan_brand
```

同時，三個精確型號都有有效 MIT 微笑標章臺灣製造證據：

```text
NR-C507XVS  MIT 02000013-03970  valid to 2029-06-15
NR-D507XVS  MIT 02000013-03969  valid to 2029-06-15
NR-C617XVS  MIT 02000013-03966  valid to 2029-06-15
```

這三筆亦有 MIT 官方登錄的 Panasonic 台灣經銷／量販／網路購物通路，但不得解讀為即時庫存。

因此前台正確呈現是：

> **非台灣品牌已確認｜此精確型號 MIT 台灣製造證據有效**

不得因台灣松下是申請／製造公司而把 Panasonic 改成台灣品牌。

## CHIMEI KD-703HP1 對照案例

- brand_identity：verified → `taiwan_brand_confirmed`
- current_sale：verified → 奇美官方目前烘碗機列表列 `KD-703HP1` 為 HOT。
- official_product_page：verified → exact-model 官方頁存在。
- 官方規格明列 `製造產地：台灣`。
- image_rights：blocked → 官方網站未授予第三方圖片重用權。

因此 KD-703HP1 可呈現：

> **台灣品牌已確認｜此精確型號台灣製造證據有效**

但其產地證據不得外推到其他奇美商品。

## 目前資料狀態

```text
真實研究候選：104
MIT exact models：100
Deep editorial cases：4
Deep candidates：1（KD-884HP0，blocked_assets）
Formal published：0

Enrichment Queue：20
├─ researched：15
├─ verified tasks：21
├─ not_found：33
├─ blocked：6
└─ pending：20

Taiwan-brand confirmed：7
Non-Taiwan-brand confirmed：3
Current-sale/supply confirmed：9
Exact official product pages：2
```

## V3.5 Deep Candidate 保留

`KD-884HP0` 仍只是 Deep Candidate：

```text
brand / exact model / MIT / supply / official page / conflict review  PASS
image_rights                                                        BLOCKED
editorial_review                                                     PENDING
formal_publication                                                   BLOCKED
```

不可直接加入正式 deep cases 或 published。

## 證據治理

- 台灣品牌 ≠ 台灣製造。
- 非台灣品牌可以有特定台灣製造型號。
- 台灣品牌不能把單一型號的臺灣產地外推至其他型號。
- MIT 製造證據不得推定品牌國籍。
- 有效 MIT ≠ 即時現售；官方登錄銷售通路 ≠ 即時庫存。
- 同系列頁 ≠ exact-model 官方頁。
- 官方圖片公開可見 ≠ 已取得重用授權。
- Deep candidate ≠ deep editorial case ≠ formal publication。
- Enrichment／Brand-Origin View／Lifecycle／圖片／搜尋／metadata 都不能自動升級 publication。
- Formal Publication Gate 維持，published = 0。

## 核心檔案

```text
data/enrichment.queue.json
data/enrichment.results.manifest.json
data/enrichment.results.v1.json
data/enrichment.results.v2.json
data/enrichment.results.v3.json
data/deep_case.candidates.json

assets/enrichment-v3-4.js
assets/deep-candidates-v3-5.js
assets/brand-origin-v3-6.js
assets/brand-origin-v3-6.css

scripts/build_public_catalog.py
scripts/validate_enrichment_v3_4.py
scripts/validate_deep_candidates_v3_5.py
scripts/validate_site.py

.github/workflows/validate.yml
.github/workflows/pages.yml
build-info.json
```

## 尚未完成

- 驗收 V3.6 最終 production build/deploy。
- Queue 剩餘 5 P2 records／20 tasks：YYMe 1157508(黃)、NINO1881 L2425(藍)、YYMe 1157508(粉)、Anti Arctic R-9-K、伯諾 LT9CMW8879。
- KD-884HP0 圖片重用權與 editorial review 仍未完成。
- 後續仍可補餐廚／清潔用品 Registry 廣度，但目前優先完成 Enrichment Queue。

## 下一步

1. 驗收 V3.6 production。
2. 完成最後 5 筆 P2，使 Enrichment Queue 20/20 complete。
3. 對完成的 20 筆做 promotion audit：哪些可進 Deep Candidate、哪些應保持 research-only、哪些屬非台灣品牌但台灣製型號。
4. Formal published 維持 0，除非完整通過既有 Publication Gate。
