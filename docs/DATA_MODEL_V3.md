# 台產報 V3 資料模型

更新：2026-08-13

## 目標

V3 的資料模型不再只有「台灣品牌 / 不是台灣品牌」單一旗標，而是把不同問題拆開：

1. 這是哪一個產品與精確型號？
2. 品牌身分是否已確認？
3. 成品製造／產地證據強度到哪裡？
4. 證據來源涵蓋哪個範圍？
5. 圖片來源與使用權狀態如何？
6. 是否已完成台產報正式發布 Gate？

## 資料層

### 1. Demo Layer

`data/products.demo.json` 中 `verification_status = demo_only` 的 6 筆資料。

用途：UI、搜尋、收藏、排序與 fallback 測試。

規則：

- 永遠不得因前台操作變成正式資料。
- V3 Evidence Catalog 不列入真實研究候選。

### 2. Deep Editorial Layer

既有四個真實研究案例：

- TENDAYS `TDT01-T017A`
- SAMPO `SR-C58DV(Y7)`
- 大同 `TAC-11HN-M`
- O'right `4712782261130`

主資料仍在 `data/products.demo.json` 的非 demo 記錄，深度媒體與外部證據由 `data/product.media.overrides.json` 擴充。

### 3. Government Registry Layer

`data/products.registry.json`

第一批為 15 筆經濟部產業發展署 MIT 微笑標章有效產品。

每筆以精確型號為單位，不以品牌為單位。

## 核心欄位

### 識別

- `id`：台產報內部唯一 ID。
- `brand`：品牌顯示名稱；無法可靠確認時填「品牌待確認」。
- `company`：官方來源中的公司／申請者。
- `name`：產品名稱。
- `model`：精確型號／色碼。
- `model_confirmed`：是否由來源確認精確型號。
- `category`：產品分類。
- `scene`：使用場景。

### 品牌身分

`brand_origin_status`：

- `taiwan_brand_confirmed`
- `non_taiwan_brand`
- `unverified`

品牌身分不得由製造地、MIT 標章或申請公司所在地自動推導。

### 製造證據

`manufacturing_evidence_status`：描述目前掌握的製造／產地證據。

Registry 第一批使用：

- `mit_certified_active`

深度案例可使用既有：

- `official_sources_consistent`
- `partial_official_record`
- `official_claim_only`
- `insufficient`
- `publishable`

### 證據等級

- `A`：政府有效標章／可發布級來源。
- `B`：精確型號官方來源一致。
- `C`：精確型號部分官方證據。
- `D`：官方宣稱、資料不足或待交叉查證。

等級只描述證據強度，不是商品品質分數。

### 證據範圍

`record_scope`：

- `exact_model`：只套用到列出的精確型號。

圖片另可用 `relation_scope`：

- `same_product_family_not_exact_model`：同系列補充圖，不可當精確型號證據。

### 政府標章

`certification`：

```json
{
  "scheme": "MIT微笑標章",
  "certificate_no": "...",
  "status": "有效",
  "passed_at": "YYYY-MM-DD",
  "valid_until": "YYYY-MM-DD"
}
```

標章存在只支持來源明確記錄的型號與範圍；不得外推同品牌其他型號。

### 來源

- `source_url`
- `source_name`
- `source_type`
- `source_checked_at`

政府 Registry 的 `source_url` 必須是官方 `keid.nat.gov.tw` HTTPS URL。

### 發布

`publication_status`：

- `unpublished`
- `published`

Registry 匯入或證據等級變高都不得自動設定成 `published`。

## 圖片

媒體結構仍沿用 V2.8：

```text
media.main
media.gallery[]
media.evidence[]
```

每張實際圖片要記錄：

- URL
- alt
- caption
- source URL/name/type
- rights status
- checked date
- relation scope（需要時）

`permission_pending` 不等於已取得授權。

## V3 前台合併規則

V3 Evidence Catalog：

```text
4 筆 Deep Editorial
+ 15 筆 Government Registry
= 19 筆真實研究候選
```

6 筆 `demo_only` 不加入上述 19 筆。

## 驗證器

- `validate_data.py`：既有編輯／demo 資料。
- `validate_registry.py`：MIT Registry 精確型號、有效期限、官方來源與必要欄位。
- `validate_v3_catalog.py`：跨資料集數量、ID、override 範圍、證據等級與正式發布狀態。
- `validate_media_rights.py`：圖片權利台帳。
- 品牌專用 validator：SAMPO／大同／O'right。
- `validate_site.py`：正式首頁與 V3 前端結構。

## 未來擴充原則

Registry 擴充時優先增加不同產品類別，而不是只堆同一品牌或同類商品。下一階段目標至少 50 筆，並建立受控匯入工具與標章到期檢查。