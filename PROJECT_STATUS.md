# 台產報 PROJECT STATUS

更新日期：2026-08-01

## Version

`V2.11 Tatung Multi-Image + Taiwan Origin Evidence`

## 正式網站方向

雜誌型介面是正式產品基準。資料治理、圖片、搜尋、收藏與發布 Gate 必須融入雜誌版，不改回一般資料庫 Dashboard。

## 本次完成

- 保留 V2.8 Complete Media Architecture、V2.9 TENDAYS 與 V2.10 SAMPO 多圖案例。
- 選定大同晶鋼電鍋 `TAC-11HN-M` 作為第三個完整多圖案例。
- 新增大同 e同購官方商城 4 張圖片。
- 新增 1 個實體銘牌、型號、製造地與序號照片待補位置。
- 新增大同官方產品頁、官方商城與台灣精品三組外部證據。
- 大同官方產品頁直接標示台灣製造與產地台灣。
- 官方商城確認目前仍有銷售。
- 建立 `data/image_rights.tatung.json` 與 `scripts/validate_tatung_media.py`。
- 修正 SAMPO 驗證器，使多筆 override 可並存。
- CI 與 GitHub Pages 會同時驗證 SAMPO 與大同多圖資料。
- 正式發布維持 0。

## 大同查核判斷

大同官方產品頁可確認：

- 型號 `TAC-11HN-M`
- 11 人份
- SUS316L 不鏽鋼
- 電功率 700W
- 保溫電功率 40W
- 台灣製造
- 產地台灣

大同 e同購官方商城可確認同一型號仍在銷售；台灣精品官方頁可交叉確認型號、公司與 SUS316L 材質。

目前維持：

```text
verification_status: official_source_found
origin_evidence_status: official_sources_consistent
publication_status: unpublished
```

原因是仍缺實體銘牌照片、圖片使用權確認與完整編輯審核。

## 資料狀態

```text
示範資料：6
官方圖片候選：4
多圖案例：3
TENDAYS 圖片：4
SAMPO 圖片：4
大同圖片：5（主圖 1＋圖片集 4）
大同查證照片位置：1
大同外部證據：3
正式發布：0
所有官方圖片權利：permission_pending
```

## 未完成

- 取得 TENDAYS、SAMPO 與大同的實體型號、製造地或標章照片。
- 取得或確認所有官方圖片使用授權。
- 將具授權圖片下載為 Repository 本地資產。
- 為 O'right 建立第四個完整多圖案例。
- 取回原先 20 筆候選與完整研究證據。
- 建立 SQLite 到公開 JSON 的受控發布流程。

## 不可覆蓋

- 使用者選定的雜誌型正式首頁方向。
- V2.3 Formal Publication Gate。
- V2.5 Recovery Baseline 預覽。
- V2.8 Complete Media Architecture。
- V2.9 TENDAYS、V2.10 SAMPO 與 V2.11 大同多圖案例。
- 既有 SQLite 與資料匯入治理成果。
- 圖片顯示不得改變查證或發布狀態。
- 官方產地標示不得在缺乏編輯審核時直接升級為正式發布。

## 下一步

1. 取得大同 TAC-11HN-M 實體銘牌與製造地照片。
2. 確認大同商城與台灣精品圖片使用授權。
3. 為 O'right 建立第四個完整多圖案例。
4. 選一筆圖片權利與實體證據皆清楚的產品，測試第一筆正式發布。
