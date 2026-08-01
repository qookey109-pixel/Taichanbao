# 台產報（Taichanbao）V2.8 Complete Media Architecture

台產報以雜誌選品為正式前台，推薦台灣品牌，同時逐項揭露單一產品的產地、製程、證據與資料缺口。

## 線上位置

- Repository：`qookey109-pixel/Taichanbao`
- 正式網站：`https://qookey109-pixel.github.io/Taichanbao/`
- V2.5 預覽：`https://qookey109-pixel.github.io/Taichanbao/versions_review/v2.5/`
- Default branch：`main`

## 目前狀態

- 正式首頁：`V2.8 Complete Media Architecture`
- 示範資料：6
- 官方圖片候選：4
- 正式發布：0
- 所有官方候選圖片權利目前均為 `permission_pending`

## V2.8 主要功能

- 保留三欄雜誌首頁、封面專題、產品專題、品牌索引與右側資訊欄。
- 搜尋、分類、場景、五種排序、收藏與正式發布 Gate。
- 完整圖片資料模型：
  - `media.main`
  - `media.gallery`
  - `media.evidence`
- 卡片顯示主圖，Drawer 支援圖片縮圖切換。
- 每張圖片保存來源、用途、權利狀態與查閱日期。
- 圖片載入失敗時顯示 emoji fallback。
- JSON 不再執行內嵌 `<img>` HTML，降低資料型 XSS 風險。
- 圖片顯示與產品查證／發布狀態完全分離。

## 核心檔案

```text
index.html
assets/magazine.css
assets/magazine.js
assets/product-images.css
assets/product-image-enhancements.js
data/products.demo.json
data/product.media.template.json
docs/MEDIA_MODEL.md
scripts/validate_data.py
scripts/validate_site.py
```

## 驗證

```bash
python scripts/validate_data.py
python scripts/validate_site.py
node --check assets/magazine.js
node --check assets/product-image-enhancements.js
node --check assets/app.js
```

## 資料治理

- 台灣品牌不等於台灣製造。
- 以單一產品／型號為查證單位。
- `demo_only` 不得進入正式發布。
- `ready_for_editorial_review` 不等於 `published`。
- 收藏、排序、圖片或 metadata 不得自行升級資料狀態。
- `permission_pending` 不代表圖片已取得使用授權。
- 未知維持待確認，衝突不得隱藏。
