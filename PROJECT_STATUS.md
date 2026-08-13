# 台產報 PROJECT STATUS

更新日期：2026-08-13

## Version

`V3.2 Registry Lifecycle`

## 正式網站方向

台產報維持「雜誌選品＋精確型號證據資料庫」雙層架構。品牌身分、單一產品型號、臺灣製造證據、政府標章、圖片權利、證據有效期限與正式發布狀態必須分開管理。

## V3.2 本次完成

- 保留 V3.1 的 50 筆 MIT 有效精確型號、4 筆深度編輯案例與 6 筆隔離 Demo。
- 新增 `assets/lifecycle-v3-2.js` 與 `assets/lifecycle-v3-2.css`。
- 前台新增「到期管理」導覽與 Registry Lifecycle Dashboard。
- Dashboard 顯示：已過期、30／90／180／365 天內到期、下一筆到期產品與剩餘天數。
- 到期清單可切換 30／90／180／365 天視窗；點擊項目可沿用 Catalog Drawer 查看該精確型號證據履歷。
- Catalog 卡片會對 365 天內到期的 MIT 紀錄加上剩餘天數標籤；90 天內與 30 天內使用不同提醒層級。
- 正式部署優先讀 `data/registry-expiry.json`；若部署產物不存在，前端會從 `catalog.public.json` 或 Registry manifest/shards 自動重算，不造成資料庫白屏。
- Pages build 在 artifact 上傳前執行 `scripts/report_registry_expiry.py --output data/registry-expiry.json`。
- 新增 `scripts/validate_lifecycle_v3_2.py`，驗證 Lifecycle UI、50 筆 Registry 有效期限與即將到期 fixture。
- `scripts/validate_site.py` 升級為 V3.2，鎖定 Dashboard、expiry report、public-catalog-first 與既有 V2.5 preview。
- `build-info.json` 升級為 V3.2，保存 54 real／50 MIT／4 deep／6 demo／0 published，以及 lifecycle 指標。
- CI 與 Pages workflow 加入 V3.2 lifecycle Python／Node 檢查。

## Pages Deployment Recovery／Workflow 修正

2026-08-13 已完成 Pages recovery，正式 production workflow 曾回報：

```text
build_result: success
deploy_result: success
page_url: https://qookey109-pixel.github.io/Taichanbao/
```

V3.2 開發期間另外抓到一個 workflow 問題：production workflow 在 deploy 後把 `pages-production-result.json` commit 回 `main`，該 commit 又會再次觸發 Pages workflow，形成自我觸發循環。現已在 `.github/workflows/pages.yml` 加入：

```yaml
paths-ignore:
  - "docs/deployment/pages-production-result.json"
```

因此 production report commit 不再觸發下一輪 Pages build；workflow 可以正常收斂。一次性 diagnostic workflows 已刪除，診斷結果 JSON 保留。

## V3.2 資料狀態

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
已過期 Registry：0
90 天內到期：1
```

目前最近到期 fixture 為 TENDAYs `DMIT017-5(白)`，有效期限 `2026-10-27`。Dashboard 只表達政府標章證據的生命週期，不代表品牌身分、現售狀態、圖片權利或正式發布狀態跟著改變。

## 公開資料 Pipeline

```text
products.demo.json
        │
        ├─ 4 deep editorial cases
        │
registry.manifest.json
        ├─ products.registry.json (15)
        └─ products.registry.appliances.json (35)
        │
        ├───────────────┐
        ▼               ▼
build_public_catalog   report_registry_expiry
        │               │
        ▼               ▼
catalog.public.json    registry-expiry.json
        │               │
        └───────┬───────┘
                ▼
       assets/catalog-v3-1.js
       assets/lifecycle-v3-2.js
```

兩個 JSON 都是 deploy-time artifact，不作為人工維護 source of truth。研究來源仍是 deep cases／Registry shards。

## 證據治理

- MIT 有效紀錄只套用到該 Registry 所列精確型號，不可外推同品牌其他產品。
- MIT 製造證據不等於品牌國籍證據。
- `evidence_level: A` 不等於正式發布。
- Registry 一律 `publication_status: unpublished`。
- 已過期 MIT 紀錄必須阻擋 Registry 驗證，不可繼續顯示為有效證據。
- 到期提醒只改變維護優先順序，不自動改任何產品查證／發布欄位。
- MIT 標章圖樣不直接複製進網站；只保存文字型證據與官方來源。
- 圖片權利與製造證據分離。
- 搜尋、收藏、圖片、排序、metadata、到期 UI 都不得升級發布狀態。

## 核心檔案

```text
index.html
assets/catalog-v3.js
assets/catalog-v3-1.js
assets/catalog-v3.css
assets/lifecycle-v3-2.js
assets/lifecycle-v3-2.css
assets/magazine.js
assets/product-image-enhancements.js

data/products.demo.json
data/products.registry.json
data/products.registry.appliances.json
data/registry.manifest.json
data/product.media.overrides.json

scripts/build_public_catalog.py
scripts/report_registry_expiry.py
scripts/validate_lifecycle_v3_2.py
scripts/validate_registry.py
scripts/validate_registry_scale.py
scripts/validate_v3_catalog.py
scripts/validate_v3_1_catalog.py
scripts/validate_site.py

.github/workflows/validate.yml
.github/workflows/pages.yml
build-info.json
docs/deployment/pages-production-result.json
```

## 尚未完成

- Registry 50 → 100：下一批優先補餐廚、居家用品、清潔、日用品與其他非家電類，降低家電集中度。
- 逐步替現有 Registry 補台灣品牌身分、現售狀態、官方產品頁與可合法使用圖片，而不是只增加 MIT 筆數。
- 若要接既有 SQLite，需要先定位正式資料庫檔、schema 與 import lineage，再建立 adapter；目前不猜測舊表。
- 取得四個深度案例的圖片授權與實體標示證據。
- 選一筆完整通過圖片權利、實體證據與編輯審核的產品，測試第一筆正式發布。

## 不可覆蓋

- 雜誌型正式首頁方向。
- V2.3 Formal Publication Gate。
- V2.5 Recovery Baseline 預覽。
- V2.8 Complete Media Architecture。
- TENDAYS、SAMPO、大同、O'right 四個深度案例。
- V3.0 Evidence Catalog 資料治理。
- V3.1 Registry shard／manifest 與 public-catalog-first 架構。
- V3.2 Registry Lifecycle／expiry report 架構。
- 臺灣品牌 ≠ 臺灣製造。
- MIT 精確型號證據不得外推同品牌其他產品。

## 下一步

1. Registry 50 → 100：優先增加非家電 MIT 精確型號。
2. 新增資料分類集中度 Gate，避免單一類別占比過高。
3. 逐步替既有 50 筆補品牌身分與現售狀態。
4. 若定位到既有 SQLite 正式 schema，再建立 SQLite adapter，不直接修改既有資料庫。
5. 第一筆正式發布仍必須完整通過現有 Gate。
