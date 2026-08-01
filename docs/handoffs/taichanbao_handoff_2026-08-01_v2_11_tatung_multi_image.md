# 台產報 Handoff — V2.11 Tatung Multi-Image + Taiwan Origin Evidence

日期：2026-08-01

## Repository

`qookey109-pixel/Taichanbao`

## 正式方向

雜誌型介面是正式首頁基準。圖片、證據、搜尋、收藏與 Formal Publication Gate 必須融入雜誌版，不改回一般資料庫 Dashboard。

## 本次完成

- 建立第三個完整多圖案例：大同晶鋼電鍋 `TAC-11HN-M`。
- 沿用台灣精品官方主圖。
- 新增大同 e同購官方商城 4 張圖片。
- 新增 1 個實體銘牌、型號、製造地與序號照片 placeholder。
- 新增三組外部證據：
  - 大同官方產品頁
  - 大同 e同購官方商城
  - 台灣精品官方產品頁
- 官方產品頁直接標示「台灣製造」及「產地：台灣」。
- 官方商城確認同一型號仍在銷售。
- 台灣精品頁交叉確認型號、公司與 SUS316L 材質。
- 建立 `data/image_rights.tatung.json`。
- 建立 `scripts/validate_tatung_media.py`。
- 修正 `scripts/validate_sampo_media.py`，支援多筆 override。
- 更新 CI、Pages Gate、README、PROJECT_STATUS 與網站版本標示。
- 正式發布維持 0。

## 現行狀態

```text
Version: V2.11 Tatung Multi-Image + Taiwan Origin Evidence
示範資料: 6
官方圖片候選: 4
完整多圖案例: 3
TENDAYS 圖片: 4
SAMPO 圖片: 4
大同圖片: 5（主圖 1＋圖片集 4）
正式發布: 0
```

## 大同資料判斷

```text
verification_status: official_source_found
origin_evidence_status: official_sources_consistent
current_sale_confirmed: true
publication_status: unpublished
```

尚未正式發布的原因：

- 缺少實體銘牌、序號與製造地照片。
- 官方商城與台灣精品圖片權利仍為 `permission_pending`。
- 尚未完成正式編輯審核。

## 重要檔案

```text
data/product.media.overrides.json
data/image_rights.tatung.json
scripts/validate_tatung_media.py
docs/research/2026-08-01_tatung_tac11hnm_media_and_origin_check.md
README.md
PROJECT_STATUS.md
```

## 不可覆蓋

- 使用者選定的雜誌型正式首頁。
- V2.3 Formal Publication Gate。
- V2.5 Recovery Baseline 預覽。
- V2.8 Complete Media Architecture。
- V2.9 TENDAYS、V2.10 SAMPO 與 V2.11 大同多圖案例。
- 圖片呈現不得改變查證或發布狀態。
- 官方產地標示不得在缺乏圖片權利與編輯審核時直接升級成正式發布。

## 下一步

1. 取得大同 TAC-11HN-M 實體銘牌、序號與製造地照片。
2. 確認大同商城及台灣精品圖片的使用權。
3. 為 O'right 建立第四個完整多圖案例。
4. 選一筆圖片權利與實體證據皆清楚的產品，測試第一筆正式發布。
