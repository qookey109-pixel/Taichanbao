# Panasonic Brand-Origin Separation Research

日期：2026-08-13

## 結論

Panasonic 是**非台灣品牌**，但以下三個精確冰箱型號同時具有有效的臺灣 MIT 微笑標章製造證據：

- `NR-C507XVS`
- `NR-D507XVS`
- `NR-C617XVS`

這是台產報「品牌國籍 ≠ 製造地」規則的正式 regression case。

## 品牌起源

Panasonic 官方資料：

- `https://news.panasonic.com/global/press/en180307-2`
- `https://www.panasonic.com/global/consumer/history.html`

官方歷史記載公司由松下幸之助於 1918 年在日本大阪創立。因此品牌身分：

```text
brand_identity.status = verified
brand_identity.result = non_taiwan_brand
```

台灣松下是台灣在地公司／申請與製造主體的證據，不能改變 Panasonic 的日本品牌起源。

## Exact-model MIT evidence

### NR-C507XVS

MIT：`https://keid.nat.gov.tw/mittw/products/prod_more?id=287469`

- certificate：`02000013-03970`
- valid until：2029-06-15
- 台灣 Panasonic 經銷商、量販、網路購物通路列於官方紀錄

### NR-D507XVS

MIT：`https://keid.nat.gov.tw/mittw/products/prod_more?id=287468`

- certificate：`02000013-03969`
- valid until：2029-06-15
- 官方登錄銷售通路存在

### NR-C617XVS

MIT：`https://keid.nat.gov.tw/mittw/products/prod_more?id=287465`

- certificate：`02000013-03966`
- valid until：2029-06-15
- 官方登錄銷售通路存在

## 正確資料模型

```text
brand_origin_status              non_taiwan_brand
manufacturing_evidence_status    mit_certified_active
record_scope                     exact_model
current_sale_confirmed           true  # supply channels confirmed, not live stock
publication_status               unpublished
```

## 官方 exact-model page

本輪在 Panasonic 官方網域沒有找到三個型號的可索引 exact-model 商品頁，因此：

```text
official_product_page.status = not_found
image_rights.status = not_found
```

不使用第三方零售頁替代品牌官方 exact-model page，也不抓第三方圖片。

## 治理要求

1. 不得將 Panasonic 標示為台灣品牌。
2. 不得因 Panasonic 是日本品牌而否定上述三個型號的 MIT 臺灣製造證據。
3. MIT 證據只套用各自精確型號。
4. 銷售通路紀錄只表示供應通路，不是即時庫存。
5. 這三筆目前仍是 research records，不是正式發布產品。
