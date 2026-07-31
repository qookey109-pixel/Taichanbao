# 台產報（Taichanbao）

台產報同時推動兩件事：推薦值得支持的台灣品牌，以及逐項揭露產品實際產地、製程與資料缺口。

## 線上位置

- Repository：`qookey109-pixel/Taichanbao`
- 正式網站：`https://qookey109-pixel.github.io/Taichanbao/`
- V2.5 預覽：`https://qookey109-pixel.github.io/Taichanbao/versions_review/v2.5/`
- Default branch：`main`

## 目前採用版本

- 正式首頁：雜誌型選品誌介面（原 V0.3 視覺基準）
- 預覽版本：`V2.5 Recovery Baseline`
- 正式發布資料：`0`
- 展示資料：皆為介面示範，不得視為正式查證結果

正式首頁保留：

- 橘色跑馬燈
- 左側導覽、中央專題、右側資訊欄
- 「今日台產」封面主題
- 產品專題、品牌索引、本月台產榜
- 搜尋、分類與產品履歷 Drawer
- 手機版底部導覽

V2.5 預覽保留：

- 研究預覽／正式發布雙檢視
- Formal Publication Gate
- 場景篩選、收藏與排序
- 6 筆明確標示為 `demo_only`、`unpublished` 的 JSON 展示資料

## 專案結構

```text
index.html                              正式雜誌型首頁
versions_review/v2.5/index.html         V2.5 Recovery 預覽
assets/styles.css                       V2.5 預覽樣式
assets/app.js                           V2.5 預覽互動與 Gate
data/products.demo.json                 6 筆示範資料
db/                                     SQLite schema 與可攜式資料庫
incoming/                               待匯入 CSV／TSV／XLSX
scripts/import_data.py                   既有資料匯入工具
scripts/validate_data.py                 示範資料驗證
scripts/validate_site.py                 正式首頁與預覽版本驗證
.github/workflows/validate.yml          一般驗證
.github/workflows/pages.yml             GitHub Pages 發布
docs/review/                            本機與匯出比對報告
docs/imports/                           ChatGPT 匯出歷史參考
docs/handoffs/                          專案接續文件
versions_review/                        歷史與預覽版本保存
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

舊 Project 文件曾記錄 20 筆候選與研究資料，但目前仍未取得原始 JSON、來源證據與完整研究文件。因此目前沒有重建或猜測這些正式候選內容。

## 資料治理

- 台灣品牌不等於台灣製造。
- 以單一產品／型號為查證單位。
- 雜誌型首頁的產品目前仍是示範資料。
- `demo_only` 不得進入正式發布。
- `ready_for_editorial_review` 不等於 `published`。
- 前台、排序、收藏或 metadata 不得自行升級產品狀態。
- 未知維持待確認，衝突不得隱藏。
- 未取回證據前，不得補造正式候選。
