# 台產報 PROJECT STATUS

更新日期：2026-08-01

## Version

`V2.9 TENDAYS Multi-Image Pilot`

## 正式網站方向

雜誌型介面是正式產品基準。資料治理、圖片、搜尋、收藏與發布 Gate 必須融入雜誌版，不改回一般資料庫 Dashboard。

## 本次完成

- 保留 V2.8 Complete Media Architecture。
- 選定 TENDAYS 健康隨身枕 `TDT01-T017A` 作為第一個完整多圖案例。
- `media.main`：1 張官方主圖。
- `media.gallery`：3 張官方產品頁圖片。
- `media.evidence`：1 個實體型號、MIT 標章與產地標示待補位置。
- 建立 `data/image_rights.json`，追蹤 7 張實際圖片。
- 建立 `scripts/validate_media_rights.py`，圖片與權利表不一致時阻擋 CI／Pages。
- 建立 TENDAYS 圖片與 MIT 查核紀錄。
- 正式發布維持 0。

## TENDAYS 查核判斷

官方產品頁可確認：

- 有現貨
- 型號 `TDT01-T017A`
- 品牌宣稱通過 MIT 微笑標章
- 品牌宣稱在地製造

經濟部 MIT 公開業者頁可確認恬褋仕存在多筆獲證產品，但本次尚未定位到完全相符的 `TDT01-T017A` 型號。

因此維持：

```text
verification_status: official_source_found
origin_evidence_status: official_claim_only
publication_status: unpublished
```

## 資料狀態

```text
示範資料：6
官方圖片候選：4
實際圖片資產：7
TENDAYS 圖片集：3
TENDAYS 查證照片位置：1
正式發布：0
圖片權利 permission_pending：7
```

## 未完成

- 取得 TENDAYS 實體型號、MIT 標章與製造地照片。
- 取得或確認官方圖片使用授權。
- 將具授權的圖片下載為 Repository 本地資產。
- 為大同、O'right、SAMPO 建立多圖與查證照片。
- 取回原先 20 筆候選與完整研究證據。
- 建立 SQLite 到公開 JSON 的受控發布流程。

## 不可覆蓋

- 使用者選定的雜誌型正式首頁方向。
- V2.3 Formal Publication Gate。
- V2.5 Recovery Baseline 預覽。
- V2.8 Complete Media Architecture。
- 既有 SQLite 與資料匯入治理成果。
- 圖片顯示不得改變查證或發布狀態。
- 官方宣稱不得冒充獨立查證結果。

## 下一步

1. 取得 TENDAYS 實體標示照片並填入 `media.evidence`。
2. 聯絡 TENDAYS 確認圖片使用方式。
3. 選大同或 SAMPO 建立第二個完整多圖案例。
4. 完成一筆獨立證據與圖片權利皆清楚的正式發布候選。
