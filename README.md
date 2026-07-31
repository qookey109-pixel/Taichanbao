# 台產報（Taichanbao）

目前專案包含可直接開啟的 V0.3 示範首頁，以及可攜式 SQLite 本機資料庫。首頁中的產品資料仍是介面示範，**不是正式查證或發布資料**。

## 快速開啟

- 首頁：直接以瀏覽器開啟 `index.html`。
- 本機資料庫：`db/taiwan_industry_report.sqlite`。
- 歷史版本與匯出紀錄：見 `versions_review/` 與 `docs/`。

## 專案結構

```text
index.html                         V0.3 示範首頁（目前可預覽版本）
db/                                SQLite schema 與資料庫
incoming/                          待匯入 CSV／TSV／XLSX
scripts/                           資料匯入工具
docs/review/                       比對、建議更新與衝突報告
docs/imports/chatgpt-export-2026-07-29/
                                   Web GPT 匯出決策與來源紀錄
versions_review/v0.1/              V0.1 原型保存
```

## 資料庫

## 匯入資料

1. 將 `.csv`、`.tsv` 或 `.xlsx` 檔案放入 `incoming/`。
2. 在終端機執行：

   ```bash
   cd /Users/qoo/Desktop/台產報
   python3 scripts/import_data.py
   ```

資料會各自匯入對應資料表；原始檔案名稱、工作表名稱、匯入時間與筆數會記錄在 `import_log`。重複匯入相同檔案版本會略過，若要強制重新匯入可執行：

```bash
python3 scripts/import_data.py --force
```

## 檢視資料

macOS 可用內建指令列工具：

```bash
sqlite3 db/taiwan_industry_report.sqlite ".tables"
sqlite3 db/taiwan_industry_report.sqlite "SELECT * FROM import_log;"
```

`.xlsx` 匯入需要 `openpyxl`。若尚未安裝，工具會提示安裝方式；CSV 和 TSV 不需要額外套件。

## 版本與資料治理

- `index.html` 為 V0.3 介面示範。它保留「示範資料」標示，不能當作正式產品資料來源。
- V0.1 保存在 `versions_review/`；根目錄 `index.html` 即為目前採用的 V0.3 示範首頁。不要以歷史檔覆蓋未來正式版本。
- `docs/imports/` 是外部匯出參考資料，不是完整 Repository，也不包含 V2.3／V2.4 的完整程式、資料或驗證器。
- 未來要導入正式候選資料前，應先依 `docs/review/` 的衝突與更新計畫完成來源、狀態與驗證確認。
