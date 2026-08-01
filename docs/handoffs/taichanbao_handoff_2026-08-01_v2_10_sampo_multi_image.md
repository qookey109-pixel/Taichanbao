# 台產報 Handoff — V2.10 SAMPO Multi-Image + External Evidence

日期：2026-08-01

## 本次完成

- 建立 `data/product.media.overrides.json`，讓圖片資料可在不改動主產品 JSON 的情況下擴充。
- SAMPO `SR-C58DV(Y7)` 新增 3 張官方產品頁圖片。
- 新增 1 個實體銘牌、製造地與序號照片待補位置。
- 新增官方規格與經濟部能源署節能標章外部證據區。
- 建立 `data/image_rights.sampo.json` 與 `scripts/validate_sampo_media.py`。
- 重寫圖片增強程式，支援主資料與 override 合併、外部證據顯示。
- 正式發布仍為 0。

## 重要判斷

- 聲寶官方頁確認 `SR-C58DV(Y7)`、580L、1級能效與國際條碼。
- 經濟部能源署資料可找到基礎型號 `SR-C58DV`、580L 與能源因數 26.2。
- 政府資料不提供製造地，因此不能標示為台灣製。
- 新增三張圖片全部是 `permission_pending`。

## 下一步

1. 取得 SAMPO 實體銘牌與製造地照片。
2. 確認 SAMPO 圖片使用授權。
3. 為大同建立第三個多圖案例。
4. 逐步把 override 合併回正式資料發布流程。
