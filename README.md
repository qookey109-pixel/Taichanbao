# 台產報（Taichanbao）V2.11.1 O'right Scope-Safe Multi-Image Extension

台產報以雜誌選品為正式前台，推薦台灣品牌，同時逐項揭露單一產品的產地、製程、圖片來源、權利狀態、外部證據與資料缺口。

## 線上位置

- Repository：`qookey109-pixel/Taichanbao`
- 正式網站：`https://qookey109-pixel.github.io/Taichanbao/`
- V2.5 預覽：`https://qookey109-pixel.github.io/Taichanbao/versions_review/v2.5/`
- Default branch：`main`

## 目前狀態

- 完整圖片架構：`media.main / media.gallery / media.evidence`
- 示範資料：6
- 官方圖片候選：4
- 多圖案例：TENDAYS、SAMPO、大同、O'right
- 正式發布：0
- 所有官方圖片權利目前均為 `permission_pending`

## O'right 第四個多圖案例

以 Bio 咖啡因強健洗髮精 `4712782261130` 建立範圍安全的多圖案例：

- 精確型號主圖：沿用台灣精品官方產品圖
- 同系列官方補充圖：3 張
- 查證照片位置：1 個實體條碼、製造商與製造地 placeholder
- 精確型號證據：台灣精品官方紀錄
- 同系列現售證據：O'right 官方購物網咖啡因洗髮精頁
- 圖片權利追蹤：`data/image_rights.oright.json`
- 範圍驗證：`scripts/validate_oright_media.py`

台灣精品頁可確認產品名稱、型號 `4712782261130`、公司與台灣在地咖啡原料敘述。O'right 現售頁可確認咖啡因洗髮精系列仍在銷售、採用台灣原生咖啡及品牌的 USDA Biobased 宣稱，但頁面未顯示 `4712782261130`，因此不得視為得獎型號現售、精確型號照片或製造地證據。

目前維持：

```text
verification_status: official_source_found
origin_evidence_status: partial_official_record
current_sale_confirmed: false
related_series_current_sale_confirmed: true
publication_status: unpublished
```

## 核心檔案

```text
index.html
assets/magazine.css
assets/magazine.js
assets/product-images.css
assets/product-image-enhancements.js
data/products.demo.json
data/product.media.overrides.json
data/image_rights.json
data/image_rights.sampo.json
data/image_rights.tatung.json
data/image_rights.oright.json
docs/MEDIA_MODEL.md
docs/IMAGE_RIGHTS_TRACKING.md
scripts/validate_data.py
scripts/validate_media_rights.py
scripts/validate_sampo_media.py
scripts/validate_tatung_media.py
scripts/validate_oright_media.py
scripts/validate_site.py
```

## 驗證

```bash
python scripts/validate_data.py
python scripts/validate_media_rights.py
python scripts/validate_sampo_media.py
python scripts/validate_tatung_media.py
python scripts/validate_oright_media.py
python scripts/validate_site.py
node --check assets/magazine.js
node --check assets/product-image-enhancements.js
node --check assets/app.js
```

## 資料治理

- 台灣品牌不等於台灣製造。
- 以單一產品／型號為查證單位。
- 精確型號圖片與同系列圖片必須分開記錄。
- 同系列現售頁不得自動證明得獎型號仍在銷售。
- 台灣原料不等於成品在台灣製造。
- 官方產品頁、官方商城與獎項頁的證據範圍必須分開記錄。
- `demo_only` 與 `official_source_found` 不得進入正式發布。
- 收藏、排序、圖片或 metadata 不得自行升級資料狀態。
- `permission_pending` 不代表圖片已取得使用授權。
- 未知維持待確認，衝突不得隱藏。
