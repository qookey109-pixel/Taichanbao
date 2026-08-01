# 台產報（Taichanbao）V2.9 TENDAYS Multi-Image Pilot

台產報以雜誌選品為正式前台，推薦台灣品牌，同時逐項揭露單一產品的產地、製程、圖片來源、權利狀態與資料缺口。

## 線上位置

- Repository：`qookey109-pixel/Taichanbao`
- 正式網站：`https://qookey109-pixel.github.io/Taichanbao/`
- V2.5 預覽：`https://qookey109-pixel.github.io/Taichanbao/versions_review/v2.5/`
- Default branch：`main`

## 目前狀態

- 完整圖片架構：`media.main / media.gallery / media.evidence`
- 示範資料：6
- 官方圖片候選：4
- 實際圖片資產：7
- 正式發布：0
- 所有官方圖片權利目前均為 `permission_pending`

## V2.9 本次完成

以 TENDAYS 健康隨身枕 `TDT01-T017A` 驗證完整多圖流程：

- 主圖：1
- 官方圖片集：3
- 查證照片位置：1 個 placeholder
- 圖片權利追蹤：已寫入 `data/image_rights.json`
- MIT／產品頁查核紀錄：`docs/research/2026-08-01_tendays_media_and_mit_check.md`

官方產品頁可確認型號、有現貨及品牌的 MIT／在地製造宣稱；經濟部 MIT 公開業者頁可確認恬褋仕有獲證產品，但本次尚未定位到完全相符的 `TDT01-T017A` 型號，因此仍維持：

```text
verification_status: official_source_found
origin_evidence_status: official_claim_only
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
data/product.media.template.json
data/image_rights.json
docs/MEDIA_MODEL.md
docs/IMAGE_RIGHTS_TRACKING.md
scripts/validate_data.py
scripts/validate_media_rights.py
scripts/validate_site.py
```

## 驗證

```bash
python scripts/validate_data.py
python scripts/validate_media_rights.py
python scripts/validate_site.py
node --check assets/magazine.js
node --check assets/product-image-enhancements.js
node --check assets/app.js
```

## 資料治理

- 台灣品牌不等於台灣製造。
- 以單一產品／型號為查證單位。
- 官方產品頁宣稱不等於獨立產地證據。
- `demo_only` 與 `official_source_found` 不得進入正式發布。
- 收藏、排序、圖片或 metadata 不得自行升級資料狀態。
- `permission_pending` 不代表圖片已取得使用授權。
- 每一張實際圖片都必須存在於 `data/image_rights.json`。
- 未知維持待確認，衝突不得隱藏。
