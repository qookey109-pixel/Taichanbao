# 台產報（Taichanbao）V2.11 Tatung Multi-Image + Taiwan Origin Evidence

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
- 多圖案例：TENDAYS、SAMPO、大同
- 正式發布：0
- 所有官方圖片權利目前均為 `permission_pending`

## V2.11 本次完成

以大同晶鋼電鍋 `TAC-11HN-M` 建立第三個完整多圖案例：

- 主圖：沿用台灣精品官方產品圖
- 官方圖片集：新增大同 e同購官方商城 4 張圖片
- 查證照片位置：1 個實體銘牌、型號、製造地與序號 placeholder
- 大同官方產品頁：確認型號、11 人份、SUS316L、700W、40W，並標示台灣製造與產地台灣
- 大同官方商城：確認目前仍有銷售與相同型號規格
- 台灣精品官方頁：交叉確認型號、公司與 SUS316L 材質
- 圖片權利追蹤：`data/image_rights.tatung.json`
- 媒體覆寫資料：`data/product.media.overrides.json`

目前仍維持：

```text
verification_status: official_source_found
origin_evidence_status: official_sources_consistent
publication_status: unpublished
```

官方頁的產地標示具有價值，但仍需實體銘牌、圖片授權與編輯審核，才可考慮正式發布。

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
docs/MEDIA_MODEL.md
docs/IMAGE_RIGHTS_TRACKING.md
scripts/validate_data.py
scripts/validate_media_rights.py
scripts/validate_sampo_media.py
scripts/validate_tatung_media.py
scripts/validate_site.py
```

## 驗證

```bash
python scripts/validate_data.py
python scripts/validate_media_rights.py
python scripts/validate_sampo_media.py
python scripts/validate_tatung_media.py
python scripts/validate_site.py
node --check assets/magazine.js
node --check assets/product-image-enhancements.js
node --check assets/app.js
```

## 資料治理

- 台灣品牌不等於台灣製造。
- 以單一產品／型號為查證單位。
- 官方產品頁、官方商城與獎項頁的證據範圍必須分開記錄。
- 官方產地標示仍需實體標示或其他證據完成編輯核對。
- `demo_only` 與 `official_source_found` 不得進入正式發布。
- 收藏、排序、圖片或 metadata 不得自行升級資料狀態。
- `permission_pending` 不代表圖片已取得使用授權。
- 未知維持待確認，衝突不得隱藏。
