# 台產報（Taichanbao）V2.6 Magazine Discovery

台產報以「雜誌選品」作為正式前台，並同時推動兩件事：推薦值得支持的台灣品牌，以及逐項揭露單一產品的實際產地、製程與資料缺口。

## 線上位置

- Repository：`qookey109-pixel/Taichanbao`
- Pages：`https://qookey109-pixel.github.io/Taichanbao/`
- V2.5 功能預覽：`https://qookey109-pixel.github.io/Taichanbao/versions_review/v2.5/`
- Default branch：`main`

## 目前狀態

- 正式首頁：`V2.6 Magazine Discovery`
- 正式發布：`0`
- 展示資料：`6` 筆，全部為 `demo_only`、`unpublished`
- 本機資料庫：`db/taiwan_industry_report.sqlite`
- CSV／TSV／XLSX 匯入工具：`scripts/import_data.py`

## V2.6 功能

- 保留三欄雜誌首頁、跑馬燈、封面專題、產品專題、品牌索引與右側資訊欄。
- 搜尋品牌、產品、分類、場景與標籤。
- 食品飲品、生活用品、清潔用品與台灣品牌分類。
- 居家、辦公、送禮、外出四種使用場景。
- 台灣參與分數、產品名稱、品牌、分類與收藏優先五種排序。
- 使用 `localStorage` 保存收藏。
- 研究預覽／正式發布雙檢視與 `?view=published` 深層連結。
- Formal Publication Gate；示範資料不會進入正式發布。
- 產品 Drawer、資料 intake 說明、手機底部導覽與響應式版面。
- V2.5 Recovery Baseline 保留在 `versions_review/v2.5/`。

## 專案結構

```text
index.html                         V2.6 雜誌型正式首頁
assets/magazine.css                V2.6 正式首頁樣式
assets/magazine.js                 搜尋、篩選、收藏、排序與 Gate
assets/styles.css                  V2.5 預覽樣式
assets/app.js                      V2.5 預覽互動
data/products.demo.json            6 筆明確標示的示範資料
db/                                SQLite schema 與可攜式資料庫
incoming/                          待匯入 CSV／TSV／XLSX
scripts/import_data.py              既有資料匯入工具
scripts/validate_data.py            示範資料驗證
scripts/validate_site.py            V2.6 與 V2.5 結構驗證
docs/review/                       本機與匯出比對報告
docs/imports/                      ChatGPT 匯出歷史參考
docs/handoffs/                     專案接續文件
versions_review/                   歷史原型與 V2.5 預覽
```

## 驗證

```bash
python scripts/validate_data.py
python scripts/validate_site.py
node --check assets/magazine.js
node --check assets/app.js
```

## 匯入外部資料

將 `.csv`、`.tsv` 或 `.xlsx` 放入 `incoming/`，再執行：

```bash
python3 scripts/import_data.py
```

重複匯入相同檔案版本會略過；需要強制匯入時使用：

```bash
python3 scripts/import_data.py --force
```

## 尚未恢復

舊 Project 文件曾記錄 20 筆候選與研究資料，但目前仍未取得原始 JSON、來源證據與完整研究文件。因此 V2.6 沒有重建或猜測這些正式候選內容。

## 資料治理

- 台灣品牌不等於台灣製造。
- 以單一產品／型號為查證單位。
- `demo_only` 不得進入正式發布。
- `ready_for_editorial_review` 不等於 `published`。
- 前台、排序、收藏或 metadata 不得自行升級產品狀態。
- 未知維持待確認，衝突不得隱藏。
- 未取回證據前，不得補造正式候選。
