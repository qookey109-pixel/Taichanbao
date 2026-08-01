# 台產報（Taichanbao）V2.7 Official Image Pilot

台產報以「雜誌選品」作為正式前台，同時推動兩件事：推薦值得支持的台灣品牌，以及逐項揭露單一產品的實際產地、製程與資料缺口。

## 線上位置

- Repository：`qookey109-pixel/Taichanbao`
- Pages：`https://qookey109-pixel.github.io/Taichanbao/`
- V2.5 功能預覽：`https://qookey109-pixel.github.io/Taichanbao/versions_review/v2.5/`
- Default branch：`main`

## 目前狀態

- 正式首頁：`V2.7 Official Image Pilot`
- 正式發布：`0`
- 介面示範資料：`6` 筆
- 官方來源圖片候選：`4` 筆
- 所有資料仍為 `unpublished`
- 本機資料庫：`db/taiwan_industry_report.sqlite`
- CSV／TSV／XLSX 匯入工具：`scripts/import_data.py`

## 官方圖片候選

目前保留四筆研究預覽候選：

- TENDAYS 健康隨身枕 `TDT01-T017A`
- 大同晶鋼電鍋 `TAC-11HN-M`
- O'right Bio 咖啡因強健洗髮精 `4712782261130`
- SAMPO 聲寶冰箱 `SR-C58DV(Y7)`

每筆候選均保留：

- 型號
- 官方產品頁或官方獎項頁
- 圖片網址與圖片來源名稱
- 查閱日期
- `image_rights_status: permission_pending`
- `publication_status: unpublished`

官方頁面能證明圖片、名稱、型號或品牌宣稱存在，但不等於產品產地已完成獨立查證，也不代表圖片已取得使用授權。

## V2.7 功能

- 保留三欄雜誌首頁、跑馬燈、封面專題、產品專題、品牌索引與右側資訊欄。
- 搜尋品牌、產品、分類、場景與標籤。
- 居家、辦公、送禮、外出四種場景。
- 五種排序與 `localStorage` 收藏。
- 研究預覽／正式發布雙檢視。
- Formal Publication Gate；示範與官方來源候選都不會自動進入正式發布。
- 產品卡片顯示官方圖片；載入失敗時退回 emoji。
- Drawer 顯示大圖、官方來源、查閱日期與圖片權利狀態。
- V2.5 Recovery Baseline 保留在 `versions_review/v2.5/`。

## 專案結構

```text
index.html                              V2.7 雜誌型正式首頁
assets/magazine.css                     雜誌首頁主樣式
assets/magazine.js                      搜尋、篩選、收藏、排序與 Gate
assets/product-images.css               官方圖片與來源區塊樣式
assets/product-image-enhancements.js    Drawer 官方圖片與來源增強
data/products.demo.json                 6 筆示範＋4 筆官方來源候選
db/                                     SQLite schema 與可攜式資料庫
incoming/                               待匯入 CSV／TSV／XLSX
scripts/import_data.py                   既有資料匯入工具
scripts/validate_data.py                 資料狀態與來源欄位驗證
scripts/validate_site.py                 V2.7 與 V2.5 結構驗證
.github/workflows/validate.yml          一般驗證
.github/workflows/pages.yml             GitHub Pages 發布
versions_review/v2.5/                   V2.5 Recovery 預覽
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
- `demo_only` 與 `official_source_found` 不得進入正式發布。
- `ready_for_editorial_review` 不等於 `published`。
- 前台、排序、收藏或 metadata 不得自行升級產品狀態。
- 官方宣稱必須與外部證據、實體標示或其他來源分開記錄。
- 圖片權利未確認時必須保持 `permission_pending`。
- 未知維持待確認，衝突不得隱藏。
