# 台產報 PROJECT STATUS

更新日期：2026-08-13

## Version

`V3.1 Registry Scale 50`

## 正式網站方向

台產報維持「雜誌選品＋精確型號證據資料庫」雙層架構。品牌身分、單一產品型號、臺灣製造證據、政府標章、圖片權利與正式發布狀態必須分開管理。

## V3.1 本次完成

- MIT Registry 從 15 筆擴充到 **50 筆有效精確型號**。
- 真實研究候選從 19 筆提升到 **54 筆**：50 MIT Registry＋4 深度編輯案例。
- 新增 35 筆家電型號，來源為經濟部產業發展署 MIT 微笑標章家電查詢第 2、4、5 頁。
- 新增產品包括 Panasonic 冰箱／冷氣、奇美烘碗機、東元捕蚊燈、ALASKA 通風扇、ESUN 空氣淨化機與冰點冷氣等。
- 新增 `data/products.registry.appliances.json` 作為第二個 Registry shard。
- 新增 `data/registry.manifest.json`，前端不再假設 Registry 只能存在單一 JSON。
- 新增 `assets/catalog-v3-1.js`，正式站優先讀 deploy-time `data/catalog.public.json`；不存在或不符 V3.1 完整性條件時，才回退 manifest＋shards。
- `assets/catalog-v3.js` 改為穩定入口 loader，既有首頁引用不必破壞性修改。
- 新增 `scripts/validate_registry_scale.py`：跨 shard 檢查 50 筆 ID、標章編號、官方來源與有效期限唯一性。
- 新增 `scripts/validate_v3_1_catalog.py`：強制 6 Demo、4 deep cases、50 MIT Registry、54 real research candidates、published=0。
- 新增 `scripts/report_registry_expiry.py`：可輸出並驗證 30／90／180／365 天內到期清單；CI 會阻擋已過期 Registry。
- 新增 `scripts/build_public_catalog.py`：可從 4 筆 deep cases＋Registry manifest/shards deterministic 重建單一公開 catalog；支援 `--check-only` 與輸出 `data/catalog.public.json`。
- public catalog 保留每筆主要來源 URL／來源名稱，避免 build 後證據鏈退化。
- CI 已加入 public catalog deterministic check 與 Registry expiry check。
- Pages workflow 已在 artifact 上傳前自動產生 `data/catalog.public.json`。
- `scripts/validate_site.py` 已鎖定 public-catalog-first＋manifest fallback 行為。
- `validate_registry.py` 仍驗證原始 15 筆 seed；V3.1 scale validator 驗證完整 50 筆，保留分層回歸測試。
- GitHub Actions 與 Pages workflow 已加入 V3.1 sharded Registry 與新 JavaScript 驗證。
- `build-info.json` 已更新為 V3.1：54 real／50 MIT／4 deep／6 demo／0 published／2 shards。
- Formal Publication Gate 未降低，正式發布仍維持 0。

## V3.1 資料狀態

```text
真實研究候選：54
├─ 深度多圖案例：4
│  ├─ TENDAYS
│  ├─ SAMPO
│  ├─ 大同
│  └─ O'right
└─ MIT 有效精確型號：50
   ├─ Seed shard：15
   └─ Appliance shard：35

隔離示範資料：6
正式發布：0
Registry shards：2
```

## 本批 35 筆家電資料範圍

官方來源：經濟部產業發展署臺灣製產品 MIT 微笑標章網站。

主要來源頁：

- `?classid=10&p=2`：Panasonic 冰箱、奇美家電／烘碗機、Panasonic 窗型變頻冷氣。
- `?classid=10&p=4`：Panasonic 室內機、東元捕蚊燈、ALASKA 通風扇、ESUN 空氣淨化機。
- `?classid=10&p=5`：冰點分離式冷氣室內／室外機。

每筆保存：精確型號、申請公司、品牌欄位、標章編號、通過日期、有效期限、官方來源與最後查閱日期。

## 公開 Catalog Pipeline

```text
products.demo.json
        │
        ├─ 4 deep editorial cases
        │
registry.manifest.json
        ├─ products.registry.json (15)
        └─ products.registry.appliances.json (35)
        │
        ▼
scripts/build_public_catalog.py
        │
        ▼
data/catalog.public.json   # deploy-time generated artifact
        │
        ▼
assets/catalog-v3-1.js     # public-first; shards fallback
```

`catalog.public.json` 不提交作為人工維護主檔；Pages build 會從受控來源重新生成，因此可避免公開資料與研究來源逐漸漂移。

目前 build pipeline 直接使用 JSON deep cases／Registry shards。Repository 的既有 SQLite schema 尚未從可搜尋文字檔可靠定位，因此本次沒有假設或硬接未知 SQLite 表。

## 證據治理

- MIT 有效紀錄只證明該 Registry 所列精確型號符合標章資料，不可外推同品牌其他型號。
- MIT 製造證據不等於品牌國籍證據；多數新家電紀錄仍維持 `brand_origin_status: unverified`。
- `government_registry_verified` 與 `evidence_level: A` 不代表可直接正式發布；仍需台產報發布 Gate。
- Registry 一律 `publication_status: unpublished`。
- 標章有效期限若早於驗證執行日，部署驗證必須失敗。
- 官方網站的 MIT 標章圖樣不直接複製進本站；只保存文字型證據欄位與來源。
- 圖片權利仍與製造證據分離。

## 核心檔案

```text
index.html
assets/catalog-v3.js
assets/catalog-v3-1.js
assets/catalog-v3.css
assets/magazine.js
assets/product-image-enhancements.js

data/products.demo.json
data/products.registry.json
data/products.registry.appliances.json
data/registry.manifest.json
data/product.media.overrides.json

scripts/build_public_catalog.py
scripts/validate_registry.py
scripts/validate_registry_scale.py
scripts/validate_v3_catalog.py
scripts/validate_v3_1_catalog.py
scripts/report_registry_expiry.py
scripts/import_registry_batch.py
scripts/validate_site.py
build-info.json
```

## 尚未完成

- 公開 GitHub Pages 尚未確認實際部署到 V3.1；外部爬取快照仍看到舊 VOL.001 頁面。
- 將 Registry 擴到 100 筆時，要優先補餐廚、居家用品、清潔與其他生活類別，避免家電占比繼續過高。
- 若要接既有 SQLite，需要先定位正式資料庫檔、schema 與 import lineage，再建立 adapter；目前不猜測舊表。
- 將到期報表做成可視化管理頁；Pages 直接發布 expiry JSON 的 workflow 更新本次被工具安全層擋下，CI check 已完成。
- 取得四個深度案例的圖片授權與實體標示證據。
- 選一筆完整通過圖片權利、實體證據與編輯審核的產品，測試第一筆正式發布。

## 不可覆蓋

- 雜誌型正式首頁方向。
- V2.3 Formal Publication Gate。
- V2.5 Recovery Baseline 預覽。
- V2.8 Complete Media Architecture。
- TENDAYS、SAMPO、大同、O'right 四個深度案例。
- V3.0 Evidence Catalog 資料治理。
- V3.1 Registry shard／manifest 架構。
- V3.1 public-catalog-first＋research fallback 架構。
- 臺灣品牌 ≠ 臺灣製造。
- MIT 精確型號證據不得外推同品牌其他產品。
- 搜尋、收藏、圖片與 metadata 不得升級查證或發布狀態。

## 下一步

1. 找出 GitHub Pages 為何尚未能確認 V3.1 deployment，完成 deployment recovery。
2. 建立 Registry expiry dashboard／管理頁。
3. 下一批擴充優先補非家電類，將 Registry 推進 100 筆。
4. 若找到既有 SQLite 正式 schema，再建立 SQLite adapter，不直接修改既有資料庫。
5. 第一筆正式發布仍必須通過現有 Gate。
