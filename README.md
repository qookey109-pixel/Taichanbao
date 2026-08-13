# 台產報（Taichanbao）V3.3 Registry Scale 100

台產報是一個以「雜誌選品＋精確型號證據資料庫」呈現台灣品牌與台灣製產品研究的網站。V3.3 將 MIT 精確型號 Registry 從 50 筆擴充至 **100 筆**，同時保留 V3.2 證據生命週期管理，並新增分類集中度 Gate，避免資料庫被單一產品類別灌滿。

## 線上位置

- Repository：`qookey109-pixel/Taichanbao`
- 正式網站：`https://qookey109-pixel.github.io/Taichanbao/`
- V2.5 Recovery 預覽：`https://qookey109-pixel.github.io/Taichanbao/versions_review/v2.5/`
- Default branch：`main`

## V3.3 資料快照

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

隔離介面示範資料：6
正式發布：0
Registry shards：3
```

## V3.3 Lifestyle Expansion

新增 `data/products.registry.lifestyle.json`，共 50 筆官方 MIT 有效精確型號：

```text
寢具        14
居家織品    12
袋包收納    12
居家用品    12
```

這批主要涵蓋毛巾、床包／被單／枕套、收納包／背包／旅行袋、布窗簾等消費生活用品。每一筆仍保留精確型號、申請公司、標章編號、通過日期、有效期限、官方來源與最後查閱日期。

## Sharded Registry

```text
data/registry.manifest.json
├─ data/products.registry.json              # 15 seed
├─ data/products.registry.appliances.json   # 35 appliances
└─ data/products.registry.lifestyle.json    # 50 lifestyle
```

`registry.manifest.json` 是 Registry 規模與 shard 的 source of truth。Public catalog builder、expiry report 與前端 fallback 都會跟 manifest 自動擴充。

## 分類集中度 Gate

V3.3 新增 `scripts/validate_category_balance.py`：

- 任一分類不得超過 Registry 的 40%。
- 家電不得超過 40 筆／100 筆。
- Registry 至少維持 8 個分類。
- 新增的生活類資料必須實質降低原本家電集中度。

這個 Gate 是資料品質／多樣性限制，不代表分類之間有品質高低。

## Registry Lifecycle

V3.2 的到期管理完整保留：

- 已過期數量。
- 30／90／180／365 天內到期數量。
- 下一筆到期產品與剩餘天數。
- Catalog 卡片到期提醒。
- deploy-time `data/registry-expiry.json`。
- 過期 MIT 紀錄阻擋驗證。

Lifecycle 只管理政府標章證據有效期，不自動改品牌身分、現售狀態、圖片權利或正式發布狀態。

## 公開資料 Pipeline

```text
Deep cases + Registry manifest/shards
             │
             ├─ scripts/build_public_catalog.py
             │        → data/catalog.public.json
             │
             └─ scripts/report_registry_expiry.py
                      → data/registry-expiry.json
```

前台優先讀 deploy-time public catalog；若不存在或不符合完整性條件，才回退 manifest＋shards。

## 核心前端

```text
index.html
assets/magazine.css
assets/magazine.js
assets/product-images.css
assets/product-image-enhancements.js
assets/catalog-v3.css
assets/catalog-v3.js
assets/catalog-v3-1.js
assets/lifecycle-v3-2.css
assets/lifecycle-v3-2.js
assets/scale-v3-3.js
```

`assets/scale-v3-3.js` 負責 Scale 100 版本標示與前台分類平衡摘要；既有 Lifecycle 元件不被重做。

## 驗證與維護

```bash
python scripts/validate_data.py
python scripts/validate_registry.py
python scripts/validate_registry_scale.py
python scripts/validate_v3_catalog.py
python scripts/validate_v3_1_catalog.py
python scripts/validate_v3_3_catalog.py
python scripts/validate_category_balance.py
python scripts/build_public_catalog.py --check-only
python scripts/report_registry_expiry.py --check-only
python scripts/validate_lifecycle_v3_2.py
python scripts/validate_media_rights.py
python scripts/validate_sampo_media.py
python scripts/validate_tatung_media.py
python scripts/validate_oright_media.py
python scripts/validate_site.py

node --check assets/catalog-v3.js
node --check assets/catalog-v3-1.js
node --check assets/lifecycle-v3-2.js
node --check assets/scale-v3-3.js
```

V3.1 的 50 筆 catalog validator 仍保留為 regression baseline；V3.3 validator 驗證完整 100 筆 Registry／104 筆真實研究候選。

## 資料治理

- 台灣品牌 ≠ 台灣製造。
- MIT 證據只套用 Registry 實際列出的精確型號。
- MIT 製造證據不得自動升級 `brand_origin_status`。
- 品牌熟悉度、申請公司名稱或產品名稱都不能替代品牌國籍證據。
- 政府 Registry A 級證據不等於正式發布。
- 圖片來源與圖片使用權分開；`permission_pending` 不代表已授權。
- 搜尋、排序、收藏、圖片、metadata、Lifecycle 與分類 Gate 都不能升級正式發布狀態。
- 未知維持待確認，衝突不得隱藏。

## Formal Publication Gate

V3.3 正式發布仍為 **0**。第一筆正式發布仍必須另外完成精確型號識別、現售狀態、產地／製造證據、重大衝突審核、圖片使用權與編輯審核。
