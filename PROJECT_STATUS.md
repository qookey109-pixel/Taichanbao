# 台產報 PROJECT STATUS

更新日期：2026-08-13

## Version

`V3.4 Enrichment Queue 20`

## 正式網站方向

台產報維持「雜誌選品＋精確型號證據資料庫」雙層架構。台灣品牌身分、精確型號、臺灣製造證據、政府標章、現售狀態、官方產品頁、圖片權利、證據有效期限與正式發布狀態分開管理。

## V3.4 目前完成

- V3.3 Scale 100 完整保留：100 筆 MIT 有效精確型號＋4 筆深度案例＝104 筆真實研究候選。
- `data/enrichment.queue.json`：20 筆優先候選、每筆 4 個研究任務，共 80 個任務。
- 已完成第一批 5 筆 P1 外部查核：SNUG、MIFIYA、JUMP、ADHOC、格蕾絲。
- 新增 `data/enrichment.results.v1.json` 保存第一批每一項 finding、摘要、來源 URL、查核日期與結果範圍。
- 第一批結果：5 verified、12 not_found、3 blocked；尚餘 60 pending。
- 5 筆已研究紀錄全部標為 `completed`，但 completed 只表示本輪研究結束，不表示每項都取得正面證據。
- SNUG、ADHOC、格蕾絲取得可引用的台灣品牌身分證據。
- ADHOC GENTLE 102(金) 與格蕾絲 1161-3(米) 取得官方／政府登錄的銷售通路或客製供應證據；不宣稱即時庫存。
- MIFIYA MIFIYA01(白) 與 JUMP 168(藍) 的 MIT 精確型號製造證據仍有效，但本輪未找到足以確認品牌國籍、品牌官方現售頁或精確型號官方商品頁的證據。
- SNUG、ADHOC、格蕾絲官方網站均未提供可重用圖片授權；相關 image-rights 任務為 `blocked`，不得直接下載／重製官方圖片。
- `assets/enrichment-v3-4.js` / `.css` 已能分開顯示 verified、not_found、blocked、pending，並顯示已研究紀錄數與本輪結果摘要。
- `scripts/validate_enrichment_v3_4.py` 已驗證 Queue 與 Results 狀態一致，並鎖定 5 researched／5 verified／12 not_found／3 blocked／60 pending。
- `scripts/build_public_catalog.py` 已讀取 enrichment results：只把人工 verified 的品牌身分與現售狀態合併至 deploy-time `catalog.public.json`；原始 MIT Registry 不被改寫。
- deploy-time Catalog 目前會把 SNUG、ADHOC、格蕾絲標為 `taiwan_brand_confirmed`；ADHOC、格蕾絲帶 `current_sale_confirmed: true`，並保存 enrichment evidence。
- `verification_status`、`manufacturing_evidence_status`、`publication_status` 均未因 enrichment 自動升級。
- `build-info.json` 與 `scripts/validate_site.py` 已同步第一批 enrichment 指標。

## 目前資料狀態

```text
真實研究候選：104
├─ 深度多圖案例：4
└─ MIT 有效精確型號：100

Enrichment Queue：20
├─ 已研究紀錄：5
├─ 已驗證任務：5
├─ 查無官方證據：12
├─ 權利阻擋：3
└─ 待處理任務：60

Enrichment 台灣品牌已確認：3
Enrichment 現售／供應通路已確認：2
隔離 Demo：6
正式發布：0
Registry shards：3
已過期 Registry：0
```

## 第一批 5 筆結果

### SNUG `S9900000015(紫藕)`
- 品牌身分：verified → 台灣品牌已確認。
- 現售：not_found；MIT 有效不等於精確型號仍可下單。
- 精確型號品牌官方頁：not_found。
- 圖片權利：blocked；官方站保留一切權利，未取得重用授權。

### MIFIYA `MIFIYA01(白)`
- 品牌身分：not_found。
- 現售：not_found。
- 精確型號品牌官方頁：not_found。
- 圖片權利：not_found；沒有找到可審核的精確型號官方素材頁。

### JUMP `168(藍)`
- 品牌身分：not_found。
- 現售：not_found。
- 精確型號品牌官方頁：not_found。
- 圖片權利：not_found。

### ADHOC `GENTLE 102(金)`
- 品牌身分：verified → 台灣品牌已確認。
- 現售：verified → MIT 精確型號頁列台北／台中／雲林自營銷售通路；不宣稱即時庫存。
- 精確型號品牌官方頁：not_found。
- 圖片權利：blocked；官方站 All Rights Reserved。

### 格蕾絲 `1161-3(米)`
- 品牌身分：verified → 台灣品牌已確認。
- 現售：verified → MIT 精確型號頁列「客製化商品」供應通路；不是一般零售現貨聲明。
- 精確型號品牌官方頁：not_found。
- 圖片權利：blocked；未取得官方圖片重用授權。

## Enrichment 治理

- `brand_identity` 與 MIT 製造證據分離；製造商在台灣不等於品牌一定是台灣品牌。
- `current_sale` 必須限定精確型號；有效 MIT 標章本身不等於現售。
- `official_product_page` 只接受品牌／公司官方精確型號頁；同系列頁不能冒充。
- `image_rights` 未有明確重用授權時只能 `blocked`／`not_found`，不能因圖片公開可見就存進 repo。
- Enrichment results 可人工合併品牌身分／現售欄位到 public catalog，但不得自動修改製造證據等級或正式發布狀態。
- Formal Publication Gate 維持不變，正式發布仍為 0。

## V3.3 / V3.2 基線保留

- Registry：100 筆／3 shards。
- 真實研究候選：104。
- 分類集中度 Gate：任一分類 <= 40%，家電 <= 40／100，至少 8 個分類。
- Lifecycle Dashboard：已過期／30／90／180／365 天到期；過期 MIT Registry 阻擋驗證。
- public catalog 為 deploy-time artifact，研究來源仍是 Registry shards＋受控 enrichment results。

## 核心檔案

```text
data/enrichment.queue.json
data/enrichment.results.v1.json
assets/enrichment-v3-4.js
assets/enrichment-v3-4.css
scripts/validate_enrichment_v3_4.py
scripts/build_public_catalog.py
scripts/validate_site.py
build-info.json
PROJECT_STATUS.md
```

其餘 V3.3 Registry、V3.2 Lifecycle、V2.8 Media、V2.5 Recovery、V2.3 Formal Publication Gate 均保留，不得重做或降低標準。

## 尚未完成

- 驗收第一批 enrichment 更新後最新 production build／deploy。
- 繼續 P1：三環牌 296、奇美 KD-884HP0、奇美 KD-853HM0、YYMe 1157508、YYMe 1147508、NINO1881 L2425 等。
- 精確型號官方商品頁目前仍是第一批最大缺口。
- 取得可合法使用的產品圖片／授權。
- 補餐廚與清潔用品 Registry 類別。
- 第一筆正式發布仍必須完整通過 Formal Publication Gate。

## 下一步

1. 驗收本輪 production build／deploy。
2. 再處理下一批 5 筆 P1，優先奇美烘碗機、三環牌與 YYMe／NINO1881。
3. 對已確認品牌身分的產品，繼續找精確型號官方商品頁與圖片授權。
4. 不為了提高 verified 數量而把 MIT 有效、同系列頁或第三方零售頁誤當正式證據。
