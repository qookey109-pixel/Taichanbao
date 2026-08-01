# 台產報 PROJECT STATUS

更新日期：2026-08-01

## Version

`V2.7 Official Image Pilot`

## 正式網站方向

使用者明確選擇雜誌型版本作為正式首頁。後續功能必須融入雜誌選品介面，不應改回一般資料庫 Dashboard。

## 已完成

- 保留三欄雜誌首頁、橘色跑馬燈、封面專題、產品專題、品牌索引、本月台產榜與手機版。
- 保留搜尋、場景、收藏、五種排序與正式發布 Gate。
- 正式首頁讀取 `data/products.demo.json`。
- 建立研究預覽／正式發布雙檢視與 `?view=published` 網址狀態。
- 加入官方圖片與來源顯示支援。
- 產品卡片可顯示官方主圖，載入失敗時退回 emoji。
- 產品 Drawer 顯示官方大圖、來源連結、查閱日期與圖片權利狀態。
- 保留 TENDAYS、大同、O'right 三筆既有官方來源候選。
- 新增 SAMPO 聲寶 `SR-C58DV(Y7)` 官方來源圖片候選。
- 保留 V2.5 Recovery Baseline 於 `versions_review/v2.5/`。
- 保留既有 SQLite schema、資料庫與 `scripts/import_data.py` 匯入流程。
- 更新資料驗證、網站驗證與 GitHub Pages 部署流程。

## 正式資料狀態

```text
介面示範資料：6
官方來源圖片候選：4
正式發布：0
demo_only：6
official_source_found：4
unpublished：10
圖片權利 permission_pending：4
```

## 官方來源圖片候選

- TENDAYS 健康隨身枕 `TDT01-T017A`
- 大同晶鋼電鍋 `TAC-11HN-M`
- O'right Bio 咖啡因強健洗髮精 `4712782261130`
- SAMPO 聲寶冰箱 `SR-C58DV(Y7)`

這四筆只能出現在研究預覽。官方頁面可作為名稱、型號、圖片或品牌宣稱的來源，但不等於產地已完成獨立查證，亦不代表圖片已取得使用授權。

## 未完成

- 取回原先 20 筆候選 JSON、來源、研究文件與完整查證紀錄。
- 取得或確認官方產品圖片的使用授權。
- 以實體標示、政府資料或其他獨立來源核對官方產地宣稱。
- 重新核對 AREX 09、TENDAYS、花伴小方巾、HITACHI NTB、聲寶 SR-C58DV。
- 建立正式 intake 表單或後端。
- 把 SQLite 正式資料與前台公開 JSON 建立受控發布流程。
- 將介面示範產品替換成具完整證據與圖片權利資料的正式產品。

## 不可重做或覆蓋

- 使用者選定的雜誌型正式首頁方向。
- 候選 01–05 既有查證成果；原檔取回前不得重新猜測。
- V0.3／V1.2 雜誌介面基準。
- V0.4 候選資料基礎。
- V0.5 研究預覽。
- V2.3 Formal Publication Gate。
- V2.5 Recovery Baseline 預覽。
- TENDAYS、大同與 O'right 既有官方來源候選。
- 既有 SQLite 與資料匯入治理成果。

## 重要決策

- 台灣品牌不等於台灣製造。
- 以單一產品／型號為查證單位。
- `demo_only` 與 `official_source_found` 均不得進入正式發布。
- `ready_for_editorial_review` 不等於 `published`。
- 正式資料不得由前台、排序、收藏或 metadata 自動升級。
- 官方來源、獨立證據與圖片權利狀態必須分開記錄。
- 圖片權利未確認時保持 `permission_pending`。
- 未知維持待確認，衝突不得隱藏。
- 雜誌視覺是正式產品基準；新功能應以漸進方式整合。

## 下一步

1. 驗證四個官方圖片網址在 GitHub Pages 是否可正常外連顯示。
2. 逐一補充圖片使用條款或取得品牌授權。
3. 先選一筆產品完成外部證據、實體標示與圖片權利的全流程查證。
4. 通過 Gate 後再建立第一筆正式發布資料。
