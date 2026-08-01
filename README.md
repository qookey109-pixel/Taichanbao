# 台產報（Taichanbao）V2.10 SAMPO Multi-Image + External Evidence

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
- 多圖案例：TENDAYS、SAMPO
- 正式發布：0
- 所有官方圖片權利目前均為 `permission_pending`

## V2.10 本次完成

以 SAMPO 聲寶冰箱 `SR-C58DV(Y7)` 建立第二個完整多圖案例：

- 主圖：沿用正式產品資料中的 1 張官方主圖
- 官方圖片集：新增 3 張
- 查證照片位置：1 個實體銘牌、製造地與序號 placeholder
- 官方規格證據：型號、580L、1級能效、國際條碼
- 政府外部證據：經濟部能源署節能標章清單中的基礎型號 `SR-C58DV`
- 圖片權利追蹤：`data/image_rights.sampo.json`
- 媒體覆寫資料：`data/product.media.overrides.json`

政府資料支持型號家族、容量與能效，但不提供製造地。因此仍維持：

```text
verification_status: official_source_found
publication_status: unpublished
製造地: 待確認
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
data/product.media.template.json
data/image_rights.json
data/image_rights.sampo.json
docs/MEDIA_MODEL.md
docs/IMAGE_RIGHTS_TRACKING.md
scripts/validate_data.py
scripts/validate_media_rights.py
scripts/validate_sampo_media.py
scripts/validate_site.py
```

## 驗證

```bash
python scripts/validate_data.py
python scripts/validate_media_rights.py
python scripts/validate_sampo_media.py
python scripts/validate_site.py
node --check assets/magazine.js
node --check assets/product-image-enhancements.js
node --check assets/app.js
```

## 資料治理

- 台灣品牌不等於台灣製造。
- 以單一產品／型號為查證單位。
- 官方產品頁宣稱不等於獨立產地證據。
- 官方規格、政府能效資料與製造地證據必須分開記錄。
- `demo_only` 與 `official_source_found` 不得進入正式發布。
- 收藏、排序、圖片或 metadata 不得自行升級資料狀態。
- `permission_pending` 不代表圖片已取得使用授權。
- 未知維持待確認，衝突不得隱藏。
