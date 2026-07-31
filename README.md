# 台產報（Taichanbao）V2.5 Recovery Baseline

台產報同時推動兩件事：推薦值得支持的台灣品牌，以及逐項揭露產品實際產地、製程與資料缺口。

## 線上位置

- Repository：`qookey109-pixel/Taichanbao`
- Pages：`https://qookey109-pixel.github.io/Taichanbao/`
- Default branch：`main`

## 目前狀態

- 網站版本：`V2.5 Recovery Baseline`
- 正式發布：`0`
- 展示資料：`6` 筆，全部為 `demo_only`、`unpublished`
- 本機資料庫：`db/taiwan_industry_report.sqlite`
- CSV／TSV／XLSX 匯入工具：`scripts/import_data.py`

## 已恢復與整合

- V1.2 雜誌型三欄與跑馬燈概念
- V2.3 研究預覽／正式發布雙檢視
- V2.3 Formal Publication Gate
- V2.4 四種場景、收藏、五種排序與三種 intake 說明
- 響應式桌機與手機介面
- JSON 示範資料
- SQLite 與既有資料匯入流程
- 資料與網站驗證器
- GitHub Actions 驗證流程

## 專案結構

```text
index.html                         V2.5 網站入口
assets/styles.css                  網站樣式
assets/app.js                      搜尋、篩選、收藏、Gate 與 Discovery
data/products.demo.json            6 筆明確標示的示範資料
db/                                SQLite schema 與可攜式資料庫
incoming/                          待匯入 CSV／TSV／XLSX
scripts/import_data.py              既有資料匯入工具
scripts/validate_data.py            示範資料驗證
scripts/validate_site.py            網站結構驗證
docs/review/                       本機與匯出比對報告
docs/imports/                      ChatGPT 匯出歷史參考
docs/handoffs/                     專案接續文件
versions_review/                   歷史原型保存
```

## 驗證

```bash
python scripts/validate_data.py
python scripts/validate_site.py
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

舊 Project 文件曾記錄 20 筆候選與研究資料，但目前仍未取得原始 JSON、來源證據與完整研究文件。因此 V2.5 沒有重建或猜測這些正式候選內容。

## 資料治理

- 台灣品牌不等於台灣製造。
- 以單一產品／型號為查證單位。
- `demo_only` 不得進入正式發布。
- `ready_for_editorial_review` 不等於 `published`。
- 前台、排序、收藏或 metadata 不得自行升級產品狀態。
- 未知維持待確認，衝突不得隱藏。
- 未取回證據前，不得補造正式候選。
