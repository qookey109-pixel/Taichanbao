# 台產報 PROJECT STATUS

更新日期：2026-08-13

## Version

`V3.3 Registry Scale 100`

## 正式網站方向

台產報維持「雜誌選品＋精確型號證據資料庫」雙層架構。品牌身分、單一產品型號、臺灣製造證據、政府標章、圖片權利、證據有效期限與正式發布狀態必須分開管理。

## V3.3 本次完成

- MIT Registry 從 **50 → 100 筆有效精確型號**。
- 真實研究候選從 54 → **104 筆**：100 MIT Registry＋4 深度編輯案例。
- 新增 `data/products.registry.lifestyle.json`，共 50 筆非家電生活型 Registry。
- Lifestyle shard 組成：寢具 14、居家織品 12、袋包收納 12、居家用品 12。
- Registry manifest 從 2 shards → **3 shards**，總筆數正式鎖定 100。
- `scripts/build_public_catalog.py` 改為依 manifest 自動決定 Registry 規模，不再硬編碼 50。
- `scripts/report_registry_expiry.py` 同樣改為依 manifest 自動處理 100 筆。
- 保留 V3.1 50 筆回歸測試；新增 `scripts/validate_v3_3_catalog.py` 驗證完整 104 筆真實研究候選。
- 新增 `scripts/validate_category_balance.py`，任一分類占比不得超過 40%，家電不得超過 40／100，至少維持 8 個分類。
- `scripts/validate_registry_scale.py` 升級到 100 筆／3 shards，驗證 100 個 Registry ID 與 100 個 MIT 標章編號全域唯一。
- `assets/catalog-v3-1.js` 已接受 V3.3 deploy-time `catalog.public.json`：104 records／100 MIT／4 deep／3 shards／0 published。
- 新增 `assets/scale-v3-3.js`，前台顯示 Scale 100 版本與實際分類集中度摘要。
- V3.2 Lifecycle 完整保留；Lifecycle validator 已升級為跟 manifest 走。
- `build-info.json` 升級為 V3.3：104 real／100 MIT／4 deep／6 demo／3 shards／0 published。
- GitHub Actions／Pages workflow 已加入 V3.3 catalog、分類集中度與 Scale 100 JS 驗證。

## V3.3 資料狀態

```text
真實研究候選：104
├─ 深度多圖案例：4
│  ├─ TENDAYS
│  ├─ SAMPO
│  ├─ 大同
│  └─ O'right
└─ MIT 有效精確型號：100
   ├─ Seed shard：15
   ├─ Appliance shard：35
   └─ Lifestyle shard：50

隔離示範資料：6
正式發布：0
Registry shards：3
已過期 Registry：0
```

### Lifestyle shard

```text
寢具       14
居家織品   12
袋包收納   12
居家用品   12
```

代表資料涵蓋 YYMe／NINO1881 毛巾、TENDAYs／Caliphil 寢具、UnMe／YESON／收納包，以及米松防焰全遮光布窗簾等精確型號。品牌名稱只依來源欄位記錄；除非另有品牌國籍證據，不自動改成台灣品牌。

## 分類集中度 Gate

```text
任一分類占比 <= 40%
家電 <= 40 / 100
分類數 >= 8
Lifestyle 四類合計 >= 50
```

此 Gate 只限制資料庫多樣性，不代表產品品質排行，也不能升級發布狀態。

## Registry Lifecycle

V3.2 到期管理完整保留：

- 已過期／30／90／180／365 天內到期。
- 下一筆到期型號與剩餘天數。
- `data/registry-expiry.json` deploy-time build artifact。
- 過期 MIT Registry 阻擋驗證。
- 到期狀態不自動改品牌身分、現售、圖片權利或發布狀態。

## 公開資料 Pipeline

```text
products.demo.json + deep cases
registry.manifest.json
├─ products.registry.json (15)
├─ products.registry.appliances.json (35)
└─ products.registry.lifestyle.json (50)
          │
          ├─ build_public_catalog.py → catalog.public.json
          └─ report_registry_expiry.py → registry-expiry.json
```

正式前台仍是 public-catalog-first，manifest/shards 保留 fallback。

## Pages / CI

- Pages recovery 已完成。
- `pages-production-result.json` 寫回 main 不再觸發自我部署循環。
- V3.3 workflow 已加入 Scale 100、分類平衡與新 JS 驗證。
- 最新 V3.3 production deploy 必須以 `docs/deployment/pages-production-result.json` 的 trigger SHA／build／deploy 結果驗收，不以搜尋引擎快照判定。

## 證據治理

- 台灣品牌 ≠ 台灣製造。
- MIT 有效紀錄只套用該 Registry 的精確型號。
- MIT 製造證據不得自動升級品牌國籍。
- `evidence_level: A` 不等於正式發布。
- 所有 Registry 一律 `publication_status: unpublished`。
- MIT 標章圖樣不直接複製進網站。
- 圖片權利與製造證據分離。
- 搜尋、收藏、圖片、排序、Lifecycle、分類 Gate 與 metadata 都不得升級發布狀態。

## 核心檔案

```text
index.html
assets/catalog-v3.js
assets/catalog-v3-1.js
assets/catalog-v3.css
assets/lifecycle-v3-2.js
assets/lifecycle-v3-2.css
assets/scale-v3-3.js
assets/magazine.js
assets/product-image-enhancements.js

data/products.demo.json
data/products.registry.json
data/products.registry.appliances.json
data/products.registry.lifestyle.json
data/registry.manifest.json
data/product.media.overrides.json

scripts/build_public_catalog.py
scripts/report_registry_expiry.py
scripts/validate_registry.py
scripts/validate_registry_scale.py
scripts/validate_v3_catalog.py
scripts/validate_v3_1_catalog.py
scripts/validate_v3_3_catalog.py
scripts/validate_category_balance.py
scripts/validate_lifecycle_v3_2.py
scripts/validate_site.py

.github/workflows/validate.yml
.github/workflows/pages.yml
build-info.json
```

## 尚未完成

- 逐步替 100 筆 Registry 補「台灣品牌身分」「是否現售」「品牌官方產品頁」與可合法使用的產品圖片。
- Lifestyle shard 目前增加了生活類廣度，但餐廚／清潔用品仍可在下一輪官方 Registry 擴充中補強。
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
- V3.1 shard／manifest 與 public-catalog-first 架構。
- V3.2 Registry Lifecycle。
- V3.3 Scale 100／分類集中度 Gate。
- 臺灣品牌 ≠ 臺灣製造。
- MIT 精確型號證據不得外推同品牌其他產品。

## 下一步

1. 驗收 V3.3 production build／deploy。
2. 建立 Registry enrichment queue：品牌身分、現售、官方產品頁、圖片權利。
3. 優先挑 10–20 筆消費者熟悉產品做深度 enrichment，而不是繼續盲目擴筆數。
4. 補餐廚與清潔用品類別。
5. 第一筆正式發布仍必須完整通過現有 Gate。
