# 台產報 Handoff — V2.8 Complete Media Architecture

日期：2026-08-01

## Repository

`qookey109-pixel/Taichanbao`

## 正式方向

雜誌型介面是正式首頁基準。圖片、搜尋、收藏、資料治理與 Formal Publication Gate 必須整合在雜誌版內。

## 本次完成

- 建立 `media.main / media.gallery / media.evidence` 完整圖片資料模型。
- 正式首頁卡片使用 `media.main`。
- 產品 Drawer 支援主圖、圖片集與查證照片縮圖切換。
- 顯示圖片來源、來源類型、查閱日期與權利狀態。
- 圖片載入失敗時顯示 emoji fallback。
- 移除產品資料以 `<img>` HTML 塞入 `emoji` 的做法。
- 保留四筆官方來源圖片候選及其舊欄位，確保向下相容。
- 建立 `docs/MEDIA_MODEL.md`。
- 建立 `data/product.media.template.json`。
- 更新資料驗證與網站結構驗證。
- README 與 PROJECT_STATUS 更新至 V2.8。

## 資料狀態

```text
示範資料：6
官方圖片候選：4
正式發布：0
圖片權利 permission_pending：4
```

## 重要限制

- `media` 只負責圖片呈現與來源治理，不能改變產品查證或發布狀態。
- `permission_pending` 不代表圖片已取得使用授權。
- 官方產品頁可協助確認產品、型號或品牌宣稱，但不等於產地獨立查證完成。
- 查證照片必須放在 `media.evidence`，不可與一般圖片集混用。
- 正式發布仍必須通過 Formal Publication Gate。

## 下一步

1. 選一件產品補入第二張圖片至 `media.gallery`。
2. 補入一張包裝或產地標示照片至 `media.evidence`。
3. 建立圖片授權追蹤清單。
4. 將取得授權的圖片改存 Repository 本地資產。
