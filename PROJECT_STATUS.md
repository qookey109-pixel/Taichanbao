# 台產報 PROJECT STATUS

更新日期：2026-08-01

## Version

`V2.11.1 O'right Scope-Safe Multi-Image Extension`

## 正式網站方向

雜誌型介面是正式產品基準。資料治理、圖片、搜尋、收藏與發布 Gate 必須融入雜誌版，不改回一般資料庫 Dashboard。

## 本次完成

- 保留 V2.8 Complete Media Architecture、V2.9 TENDAYS、V2.10 SAMPO 與 V2.11 大同案例。
- 建立 O'right Bio 咖啡因強健洗髮精 `4712782261130` 第四個多圖案例。
- 精確型號主圖繼續使用台灣精品官方產品圖。
- 新增 3 張 O'right 官方同系列補充圖。
- 每張同系列圖片均加入 `relation_scope`，禁止冒充精確型號圖片。
- 新增 1 個實體條碼、製造商與製造地照片待補位置。
- 新增台灣精品精確型號證據與 O'right 同系列現售頁證據。
- 建立 `data/image_rights.oright.json` 與 `scripts/validate_oright_media.py`。
- CI 與 GitHub Pages 會驗證精確型號／同系列圖片的證據邊界。
- 正式發布維持 0。

## O'right 查核判斷

台灣精品官方紀錄可確認：

- 產品名稱 `Bio 咖啡因強健洗髮精`
- 產品型號 `4712782261130`
- 歐萊德國際股份有限公司
- 採用台灣在地來源咖啡
- 全家 Let's Café 咖啡渣循環再生設計敘述

O'right 官方購物網可確認咖啡因洗髮精同系列目前仍有販售頁，並記載台灣原生咖啡與 USDA Biobased 品牌宣稱；但該頁未顯示 `4712782261130`，因此不能用來確認精確型號仍在銷售，也不能證明成品製造地。

目前維持：

```text
verification_status: official_source_found
origin_evidence_status: partial_official_record
current_sale_confirmed: false
related_series_current_sale_confirmed: true
publication_status: unpublished
```

## 資料狀態

```text
示範資料：6
官方圖片候選：4
多圖案例：4
TENDAYS 圖片：4
SAMPO 圖片：4
大同圖片：5
O'right 圖片：4（精確型號主圖 1＋同系列補充圖 3）
O'right 查證照片位置：1
O'right 外部證據：2
正式發布：0
所有官方圖片權利：permission_pending
```

## 未完成

- 取得 O'right `4712782261130` 實體條碼、製造商與製造地照片。
- 確認 O'right 同系列圖片與台灣精品主圖的使用授權。
- 核對 USDA Biobased 認證實際適用的產品／型號範圍。
- 取得 TENDAYS、SAMPO 與大同的實體標示照片。
- 將具授權圖片下載為 Repository 本地資產。
- 取回原先 20 筆候選與完整研究證據。
- 建立 SQLite 到公開 JSON 的受控發布流程。

## 不可覆蓋

- 使用者選定的雜誌型正式首頁方向。
- V2.3 Formal Publication Gate。
- V2.5 Recovery Baseline 預覽。
- V2.8 Complete Media Architecture。
- V2.9 TENDAYS、V2.10 SAMPO、V2.11 大同與本次 O'right 案例。
- 既有 SQLite 與資料匯入治理成果。
- 圖片顯示不得改變查證或發布狀態。
- 同系列圖片不得冒充精確型號圖片。
- 台灣原料不得被表述為成品台灣製造。

## 下一步

1. 建立前台可見的「精確型號／同系列補充」圖片標籤。
2. 取得 O'right `4712782261130` 實體包裝與製造地照片。
3. 確認四個品牌圖片使用授權。
4. 選一筆圖片權利與實體證據皆清楚的產品，測試第一筆正式發布。
