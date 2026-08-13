# CHIMEI KD-884HP0 Deep Candidate Research

日期：2026-08-13

## 結論

`KD-884HP0` 達到台產報 V3.5 的 Deep Candidate 前置條件，但**尚未成為正式 deep editorial case，更未正式發布**。

目前狀態：

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
publication_status               unpublished
```

## 品牌身分

奇美家電官方品牌故事：
`https://www.chimei.com.tw/brand-story`

官方內容說明：
- 奇美集團創始於 1960 年。
- 2006 年新增 B2C `CHIMEI 奇美品牌` 事業。
- 奇美集團創辦與主要品牌發展脈絡在台灣。
- 官方頁亦提到 CHIMEI 曾獲台灣百大品牌等品牌紀錄。

因此 `brand_identity` 可標為 `taiwan_brand_confirmed`。

## 精確型號官方頁

奇美家電官方：
`https://www.chimei.com.tw/dish-dryer/ultraviolet%20%20rays/kd-884hp0`

官方頁直接列：
- 型號：`KD-884HP0`
- 容量：88L
- 製造產地：`台灣`
- 紫外線／高溫烘乾等產品規格

這是 exact-model 官方證據，只適用 KD-884HP0。

## MIT 精確型號

經濟部產業發展署 MIT 微笑標章：
`https://keid.nat.gov.tw/mittw/products/prod_more?id=287272`

官方紀錄：
- 標章編號：`02000038-02030`
- 型號：`KD-884HP0(白)`
- 品牌：奇美
- 通過日期：2026-06-01
- 有效日期：2029-06-01
- 狀態：有效
- 銷售通路：列有經銷商資訊

MIT 證據只能套用精確型號，不外推到 KD-853HM0、KD-703HP1 或其他奇美產品。

## 現售／供應

奇美家電官方烘碗機產品線與 exact-model 頁可用，加上 MIT 精確型號銷售通路紀錄，可支持 `current_sale_or_supply: pass`。

此結論不等於任何單一門市「即時有庫存」。

## 圖片權利

官方 exact-model 頁可看到多張產品圖片，但奇美家電網站頁尾為 `All rights reserved`，目前沒有找到允許第三方下載／重製至台產報的授權。

因此：

```text
image_rights: blocked
media.status: blocked_permission_required
```

台產報目前只保存來源頁，不把官方圖片下載進 repository。

## 為何沒有直接發布

Deep Candidate 只是中間層。這筆目前至少還缺：

1. 圖片重用授權或合法替代素材。
2. 台產報 deep editorial review。
3. 正式 Publication Gate 最終人工審核。

任何一項未完成，都不得把 candidate 改成 published。
