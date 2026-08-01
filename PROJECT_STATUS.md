# 台產報 PROJECT STATUS

更新日期：2026-08-01

## Version

`V2.10 SAMPO Multi-Image + External Evidence`

## 正式網站方向

雜誌型介面是正式產品基準。資料治理、圖片、搜尋、收藏與發布 Gate 必須融入雜誌版，不改回一般資料庫 Dashboard。

## 本次完成

- 保留 V2.8 Complete Media Architecture 與 V2.9 TENDAYS 多圖案例。
- 建立 `data/product.media.overrides.json`，可在不覆蓋主產品 JSON 的情況下擴充媒體與證據。
- 選定 SAMPO 聲寶 `SR-C58DV(Y7)` 作為第二個完整多圖案例。
- 新增 3 張聲寶官方產品頁圖片。
- 新增 1 個實體銘牌、製造地與序號照片待補位置。
- 新增官方規格與經濟部能源署節能標章外部證據區。
- 建立 `data/image_rights.sampo.json` 與 `scripts/validate_sampo_media.py`。
- CI 與 GitHub Pages 會驗證 SAMPO override、外部證據與圖片權利追蹤。
- 正式發布維持 0。

## SAMPO 查核判斷

聲寶官方頁可確認：

- 完整型號 `SR-C58DV(Y7)`
- 容積 580L
- 變頻鋼板三門
- 能源效率 1 級
- 國際條碼 `4718060318855`

經濟部能源署節能標章資料可確認：

- 聲寶獲證型號清單包含基礎型號 `SR-C58DV`
- 電冰箱比較資料列出 580L
- 能源因數標示值 26.2

政府資料不提供製造地，因此維持：

```text
verification_status: official_source_found
publication_status: unpublished
製造地: 待確認
```

## 資料狀態

```text
示範資料：6
官方圖片候選：4
多圖案例：2
TENDAYS 圖片：4
SAMPO 圖片：4（主圖 1＋圖片集 3）
SAMPO 查證照片位置：1
SAMPO 外部證據：2
正式發布：0
所有官方圖片權利：permission_pending
```

## 未完成

- 取得 TENDAYS 與 SAMPO 實體型號、製造地與標章照片。
- 取得或確認官方圖片使用授權。
- 將具授權圖片下載為 Repository 本地資產。
- 為大同與 O'right 建立多圖與查證照片。
- 取回原先 20 筆候選與完整研究證據。
- 建立 SQLite 到公開 JSON 的受控發布流程。

## 不可覆蓋

- 使用者選定的雜誌型正式首頁方向。
- V2.3 Formal Publication Gate。
- V2.5 Recovery Baseline 預覽。
- V2.8 Complete Media Architecture。
- V2.9 TENDAYS 多圖案例與圖片權利追蹤。
- 既有 SQLite 與資料匯入治理成果。
- 圖片顯示不得改變查證或發布狀態。
- 官方規格或政府能效資料不得冒充製造地證據。

## 下一步

1. 取得 SAMPO 實體銘牌與製造地照片。
2. 確認 SAMPO 圖片使用授權。
3. 為大同建立第三個完整多圖案例。
4. 完成一筆獨立證據與圖片權利皆清楚的正式發布候選。
