# 台產報 PROJECT STATUS

更新日期：2026-08-13

## Version

`V3.4 Enrichment Queue 20`

## 正式網站方向

台產報維持「雜誌選品＋精確型號證據資料庫」雙層架構。品牌身分、單一產品型號、臺灣製造證據、政府標章、圖片權利、證據有效期限、深化查證進度與正式發布狀態必須分開管理。

## V3.4 本次完成

- V3.3 Registry Scale 100 完整保留：100 筆 MIT 有效精確型號＋4 筆深度案例＝104 筆真實研究候選。
- 新增 `data/enrichment.queue.json`，建立第一批 **20 筆深化查證候選**。
- 每筆拆成 4 個獨立任務：`brand_identity`、`current_sale`、`official_product_page`、`image_rights`，合計 80 個研究任務。
- Queue 初始狀態全部為 `pending`；任務狀態不會自動修改 Registry verification 或 publication status。
- 新增 `scripts/validate_enrichment_v3_4.py`：20 個 Queue ID 必須全部存在 100 筆 Registry、不得重複、不得指向 published 資料，且至少涵蓋 4 個分類。
- 新增 `assets/enrichment-v3-4.js` / `assets/enrichment-v3-4.css`，前台顯示「深化查證工作台」。
- 工作台顯示 Queue 總數、P1 數量、已完成任務、待處理任務，並可切換 P1／P2。
- Queue 項目沿用 Catalog `data-catalog-id`，可直接開啟精確型號證據履歷。
- `assets/catalog-v3.js` 已串接 V3.4 workbench，並保留 V3.3 Scale 100、V3.2 Lifecycle、V3.1 public-catalog-first 架構。
- CI 與 Pages workflow 加入 enrichment validator 與 JavaScript syntax Gate。
- `scripts/validate_site.py` 升級到 V3.4，鎖定 enrichment queue、workbench、Scale 100、Lifecycle 與 V2.5 Preview 共存。
- `build-info.json` 升級為 V3.4：104 real／100 MIT／20 enrichment queue／80 tasks／0 verified tasks／0 published。

## 資料狀態

```text
真實研究候選：104
├─ 深度多圖案例：4
└─ MIT 有效精確型號：100
   ├─ Seed shard：15
   ├─ Appliance shard：35
   └─ Lifestyle shard：50

Enrichment Queue：20
├─ 每筆任務：4
├─ 總研究任務：80
├─ 已完成任務：0
└─ 待處理任務：80

隔離示範資料：6
正式發布：0
Registry shards：3
已過期 Registry：0
```

## Enrichment 原則

- `brand_identity`：只查品牌國籍／品牌歸屬，不因 MIT 製造證據自動判定為台灣品牌。
- `current_sale`：只確認精確型號是否仍有可靠現售證據。
- `official_product_page`：只保存品牌／公司官方產品頁；同系列頁不可冒充精確型號頁。
- `image_rights`：官方圖片存在不等於有使用授權；權利狀態必須獨立記錄。
- 任一 enrichment 任務變成 `verified` 都不會自動升級 `publication_status`。

## V3.3 Scale 100 基線

- Registry：100 筆／3 shards。
- 真實研究候選：104。
- 分類集中度 Gate：任一分類 <= 40%；家電 <= 40／100；至少 8 個分類。
- Lifestyle shard：寢具 14、居家織品 12、袋包收納 12、居家用品 12。
- public catalog 由 `scripts/build_public_catalog.py` 依 manifest deterministic 重建。

## V3.2 Lifecycle 基線

- 已過期／30／90／180／365 天到期 Dashboard。
- `data/registry-expiry.json` 為 deploy-time artifact。
- 過期 MIT Registry 阻擋驗證。
- 到期狀態不影響品牌身分、現售、圖片權利或發布狀態。

## Pages / CI

- Pages recovery 已完成。
- production report commit 已用 `paths-ignore` 阻止自我觸發循環。
- V3.4 production 必須以 `docs/deployment/pages-production-result.json` 的 trigger SHA／build／deploy 結果驗收。
- 搜尋引擎舊快照不得作為 deployment failure 判據。

## 核心檔案

```text
index.html
assets/catalog-v3.js
assets/catalog-v3-1.js
assets/catalog-v3.css
assets/lifecycle-v3-2.js
assets/lifecycle-v3-2.css
assets/scale-v3-3.js
assets/enrichment-v3-4.js
assets/enrichment-v3-4.css
assets/magazine.js
assets/product-image-enhancements.js

data/products.demo.json
data/products.registry.json
data/products.registry.appliances.json
data/products.registry.lifestyle.json
data/registry.manifest.json
data/enrichment.queue.json
data/product.media.overrides.json

scripts/build_public_catalog.py
scripts/report_registry_expiry.py
scripts/validate_registry.py
scripts/validate_registry_scale.py
scripts/validate_v3_3_catalog.py
scripts/validate_category_balance.py
scripts/validate_lifecycle_v3_2.py
scripts/validate_enrichment_v3_4.py
scripts/validate_site.py

.github/workflows/validate.yml
.github/workflows/pages.yml
build-info.json
```

## 證據治理 / 禁止事項

- 台灣品牌 ≠ 台灣製造。
- MIT 精確型號證據不得外推同品牌其他型號。
- `evidence_level: A` 不等於正式發布。
- Registry 與 Queue 均不得自動改成 `published`。
- 搜尋、收藏、圖片、排序、Lifecycle、分類 Gate、Queue 任務與 metadata 都不得升級發布狀態。
- MIT 標章圖樣不直接複製進網站。
- 圖片來源與圖片使用權分開。
- 未定位既有 SQLite schema 前，不猜測、不修改未知資料表。

## 尚未完成

- V3.4 production build／deploy 最終驗收。
- 開始處理 P1 Queue：逐筆補品牌身分、現售、官方產品頁、圖片權利。
- 優先選 5–10 筆把四項 enrichment 做完整，再決定是否擴 Queue。
- 補餐廚與清潔用品 Registry 類別。
- 取得四個深度案例的圖片授權與實體標示證據。
- 第一筆正式發布仍必須完整通過現有 Formal Publication Gate。

## 下一步

1. 驗收 V3.4 production deploy。
2. 從 P1 Queue 開始逐筆做 enrichment，不再盲目增加 Registry 筆數。
3. 第一批優先完成至少 5 筆的品牌身分＋現售＋官方頁查核。
4. 圖片權利若無明確授權，一律維持 pending／blocked。
5. Formal Publication Gate 維持不變，正式發布仍為 0。
