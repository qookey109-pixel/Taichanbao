# 台產報 Handoff — V2.11.1 O'right Scope-Safe Multi-Image Extension

日期：2026-08-01

## Repository

`qookey109-pixel/Taichanbao`

## 正式方向

雜誌型介面是正式首頁基準。圖片、證據、搜尋、收藏與 Formal Publication Gate 必須融入雜誌版，不改回一般資料庫 Dashboard。

## 本次完成

- 建立第 4 個多圖案例：O'right Bio 咖啡因強健洗髮精 `4712782261130`。
- 精確型號主圖沿用台灣精品官方產品圖。
- 新增 3 張 O'right 官方同系列補充圖。
- 同系列圖片均加入 `relation_scope`，並在 caption 明示不得冒充精確型號或製造地證據。
- 新增 1 個實體條碼、製造商與製造地照片 placeholder。
- 新增兩組外部證據：
  - 台灣精品精確型號紀錄
  - O'right 官方購物網同系列現售頁
- 建立 `data/image_rights.oright.json`。
- 建立 `scripts/validate_oright_media.py`。
- CI 與 Pages Gate 已加入 O'right 範圍驗證。
- 更新 README、PROJECT_STATUS 與研究紀錄。
- 正式發布維持 0。

## O'right 資料判斷

```text
verification_status: official_source_found
origin_evidence_status: partial_official_record
current_sale_confirmed: false
related_series_current_sale_confirmed: true
publication_status: unpublished
```

台灣精品頁可確認精確型號、公司及台灣在地咖啡敘述；O'right 現售頁只支持同系列仍在銷售及品牌原料／認證宣稱。兩者不得混用。

## 現行狀態

```text
示範資料：6
官方圖片候選：4
多圖案例：4
TENDAYS 圖片：4
SAMPO 圖片：4
大同圖片：5
O'right 圖片：4（精確型號主圖 1＋同系列補充圖 3）
正式發布：0
```

## 重要檔案

```text
data/product.media.overrides.json
data/image_rights.oright.json
scripts/validate_oright_media.py
docs/research/2026-08-01_oright_bio_caffeine_media_scope_check.md
README.md
PROJECT_STATUS.md
```

## 不可覆蓋

- 使用者選定的雜誌型正式首頁。
- V2.3 Formal Publication Gate。
- V2.5 Recovery Baseline 預覽。
- V2.8 Complete Media Architecture。
- TENDAYS、SAMPO、大同與 O'right 多圖案例。
- 圖片呈現不得改變查證或發布狀態。
- 同系列圖片不得冒充精確型號圖片。
- 台灣原料不得被表述為成品台灣製造。

## 下一步

1. 在前台縮圖與來源區加入「精確型號／同系列補充」可見標籤。
2. 取得 O'right 4712782261130 實體包裝、條碼與製造地照片。
3. 核對 USDA Biobased 認證適用範圍。
4. 確認四個品牌的圖片使用權。
5. 選一筆圖片權利與實體證據清楚的候選，測試第一筆正式發布。
