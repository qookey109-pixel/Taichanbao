# 台產報 PROJECT STATUS

更新日期：2026-08-01

## Version

`V2.8 Complete Media Architecture`

## 正式網站方向

雜誌型介面是正式產品基準。新資料治理與圖片功能必須融入雜誌版，不改回一般資料庫 Dashboard。

## 已完成

- 保留 V2.7 雜誌首頁、搜尋、分類、場景、排序、收藏與 Formal Publication Gate。
- 建立 `media.main / media.gallery / media.evidence` 完整圖片架構。
- 卡片使用主圖；Drawer 可切換主圖、圖片集與查證照片。
- 顯示圖片來源、來源類型、權利狀態與查閱日期。
- 圖片失敗時提供 emoji fallback。
- 移除以 `emoji` 欄位執行 `<img>` HTML 的資料方式。
- 建立 `docs/MEDIA_MODEL.md` 與 `data/product.media.template.json`。
- 更新資料與網站驗證器。
- 保留 V2.5 Recovery 預覽、SQLite 與既有匯入流程。

## 資料狀態

```text
示範資料：6
官方圖片候選：4
正式發布：0
圖片權利待確認：4
```

## 未完成

- 為產品補充第二張以上的官方圖片。
- 收集包裝、型號、產地與製造商查證照片。
- 取得或確認官方圖片使用授權。
- 將可授權圖片下載為 Repository 本地資產，避免外站擋圖或網址失效。
- 取回原先 20 筆候選與完整研究證據。
- 建立 SQLite 到公開 JSON 的受控發布流程。

## 不可覆蓋

- 使用者選定的雜誌型正式首頁方向。
- V2.3 Formal Publication Gate。
- V2.5 Recovery Baseline 預覽。
- 既有 SQLite 與資料匯入治理成果。
- 圖片顯示不得改變查證或發布狀態。

## 下一步

1. 選一筆產品補齊 `gallery` 與 `evidence`，驗證完整多圖流程。
2. 建立圖片授權追蹤清單。
3. 取得一筆完整可發布的真實產品資料，測試 Formal Publication Gate。
