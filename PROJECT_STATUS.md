# 台產報 PROJECT STATUS

更新日期：2026-08-01

## Version

`V2.6 Magazine Discovery`

## 正式網站方向

使用者明確選擇雜誌型版本作為正式首頁。後續功能必須融入雜誌選品介面，不應改回一般資料庫 Dashboard。

## 已完成

- 保留三欄雜誌首頁、橘色跑馬燈、封面專題、產品專題、品牌索引、本月台產榜與手機版。
- 將 V2.5 的搜尋、場景、收藏、五種排序與正式發布 Gate 整合進雜誌型首頁。
- 正式首頁改讀 `data/products.demo.json`，並保留內嵌 fallback。
- 建立研究預覽／正式發布雙檢視與 `?view=published` 網址狀態。
- 收藏使用 `localStorage`；收藏、排序與篩選不得改變資料狀態。
- 建立產品 Drawer 與三類資料 intake 說明。
- 保留 V2.5 Recovery Baseline 於 `versions_review/v2.5/`。
- 保留既有 SQLite schema、資料庫與 `scripts/import_data.py` 匯入流程。
- 更新網站驗證與 GitHub Pages 自動部署。

## 正式資料狀態

```text
示範資料：6
正式發布：0
demo_only：6
unpublished：6
```

## 未完成

- 取回原先 20 筆候選 JSON。
- 取回來源、研究文件與查證紀錄。
- 取回圖片權利資料。
- 重新核對 AREX 09、TENDAYs、花伴小方巾、HITACHI NTB、聲寶 SR-C58DV。
- 建立正式 intake 表單或後端。
- 把 SQLite 正式資料與前台公開 JSON 建立受控發布流程。
- 將示範 emoji／幾何圖替換成具權利資訊的正式產品圖片。

## 不可重做或覆蓋

- 使用者選定的雜誌型正式首頁方向。
- 候選 01–05 既有查證成果；原檔取回前不得重新猜測。
- V0.3／V1.2 雜誌介面基準。
- V0.4 候選資料基礎。
- V0.5 研究預覽。
- V2.3 Formal Publication Gate。
- V2.5 Recovery Baseline 預覽。
- 既有 SQLite 與資料匯入治理成果。

## 重要決策

- 台灣品牌不等於台灣製造。
- 以單一產品／型號為查證單位。
- `demo_only` 不得進入正式發布。
- `ready_for_editorial_review` 不等於 `published`。
- 正式資料不得由前台、排序、收藏或 metadata 自動升級。
- 未知維持待確認，衝突不得隱藏。
- 雜誌視覺是正式產品基準；新功能應以漸進方式整合。

## 下一步

1. 從本機、舊匯出包或其他聊天室取回原始候選與研究檔。
2. 先導入一筆可完整查證的真實產品，驗證正式發布 Gate 全流程。
3. 建立圖片權利與來源欄位，再逐步替換示範視覺。
