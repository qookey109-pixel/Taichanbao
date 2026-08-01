# 台產報圖片授權追蹤

版本：V2.9 TENDAYS Multi-Image Pilot  
更新日期：2026-08-01

## 檔案

- `data/products.demo.json`：產品與 `media.main / gallery / evidence`
- `data/image_rights.json`：每一張實際圖片的權利追蹤
- `scripts/validate_media_rights.py`：確認圖片資料與權利表一一對應

## 規則

1. 每個 `kind: image` 項目都必須存在於 `data/image_rights.json`。
2. `kind: placeholder` 不列入授權表。
3. `permission_pending` 必須提供 `action_required`。
4. 外連官方圖片不等於已取得使用授權。
5. 權利狀態未確認，不得下載為正式本地資產或通過 Formal Publication Gate。
6. `media.evidence` 可以先使用 placeholder 建立缺口，但必須明確說明待補內容。
