# 台產報 Handoff — V2.7 Official Image Pilot

日期：2026-08-01

## Repository

`qookey109-pixel/Taichanbao`

## 正式方向

雜誌型介面是正式首頁基準。資料透明化、查證 Gate、圖片、收藏與搜尋功能必須融入雜誌版面，不改回一般資料庫 Dashboard。

## 本次完成

- 正式首頁升級為 `V2.7 Official Image Pilot`。
- 新增 `assets/product-images.css`。
- 新增 `assets/product-image-enhancements.js`。
- 卡片可顯示官方來源圖片；失敗時使用 emoji fallback。
- Drawer 顯示官方大圖、圖片來源、查閱日期及 `permission_pending` 權利狀態。
- 保留既有 TENDAYS、大同與 O'right 官方來源候選。
- 新增 SAMPO 聲寶 `SR-C58DV(Y7)` 官方來源候選。
- 資料總數：6 筆示範＋4 筆官方來源候選。
- 正式發布維持 0。
- 更新驗證 scripts、GitHub Actions、README 與 PROJECT_STATUS。

## 官方圖片候選

1. TENDAYS 健康隨身枕 `TDT01-T017A`
2. 大同晶鋼電鍋 `TAC-11HN-M`
3. O'right Bio 咖啡因強健洗髮精 `4712782261130`
4. SAMPO 聲寶冰箱 `SR-C58DV(Y7)`

全部維持：

```text
verification_status: official_source_found
publication_status: unpublished
image_rights_status: permission_pending
```

## 重要限制

- 官方產品頁或官方獎項頁只代表來源存在，不等於產地獨立查證完成。
- 未取得圖片授權前，不得標示為可自由使用。
- 前台收藏、排序、搜尋與 metadata 不得升級資料狀態。
- 目前沒有任何產品通過正式發布 Gate。

## 下一步

1. 檢查四張外連圖片在 GitHub Pages 的實際顯示狀態。
2. 補充品牌圖片使用條款或取得授權。
3. 選一筆產品進行外部來源與實體標示核對。
4. 通過完整 Gate 後，再建立第一筆正式發布資料。
