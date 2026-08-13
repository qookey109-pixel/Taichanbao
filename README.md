# 台產報（Taichanbao）V3.2 Registry Lifecycle

台產報是一個以「雜誌選品＋精確型號證據資料庫」呈現台灣品牌與台灣製產品研究的網站。V3.2 在 V3.1 的 50 筆 MIT 精確型號 Registry 上加入證據生命週期管理：標章有效期限會被持續追蹤，到期前顯示提醒，過期後阻擋驗證。

## 線上位置

- Repository：`qookey109-pixel/Taichanbao`
- 正式網站：`https://qookey109-pixel.github.io/Taichanbao/`
- V2.5 Recovery 預覽：`https://qookey109-pixel.github.io/Taichanbao/versions_review/v2.5/`
- Default branch：`main`

## V3.2 資料快照

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

隔離介面示範資料：6
正式發布：0
Registry shards：2
已過期 Registry：0
90 天內到期：1
```

## V3.2 Registry Lifecycle Dashboard

正式前台新增「到期管理」：

- 已過期 Registry 數量。
- 30／90／180／365 天內到期數量。
- 最近一筆到期的品牌、型號、日期與剩餘天數。
- 30／90／180／365 天到期清單切換。
- 到期項目可直接打開原 Catalog 證據履歷。
- Catalog 卡片會對 365 天內到期的 MIT 紀錄標示剩餘天數；90 天內與 30 天內提高提醒強度。

到期資訊只影響「政府標章證據是否仍有效」，不會自動改變品牌身分、現售狀態、圖片權利或正式發布狀態。

## 部署資料來源

正式 Pages build 會生成兩個公開產物：

```text
scripts/build_public_catalog.py
        → data/catalog.public.json

scripts/report_registry_expiry.py
        → data/registry-expiry.json
```

前台資料優先順序：

```text
Catalog:
catalog.public.json
    ↓ unavailable / invalid
registry.manifest.json + shards

Lifecycle:
registry-expiry.json
    ↓ unavailable / invalid
catalog.public.json
    ↓ unavailable
registry.manifest.json + shards
```

因此正式站可使用 deploy-time 建置產物，本機／研究環境仍保留 fallback。

## Sharded Registry

```text
data/registry.manifest.json
├─ data/products.registry.json              # 15 筆 seed
└─ data/products.registry.appliances.json   # 35 筆家電擴充
```

目前 50 筆中家電比重偏高；下一批 50→100 優先補餐廚、居家用品、清潔、日用品與其他非家電類。

## 證據資料庫功能

- A–D 證據分級。
- 來源、證據等級、分類、品牌身分與排序篩選。
- 搜尋品牌、公司、產品、型號、標章編號與標籤。
- Registry 卡片顯示標章編號與有效期限。
- 點擊後查看精確型號、申請公司、品牌身分、來源、證據範圍與最後查閱日期。
- O'right 圖片明確區分「精確型號」與「同系列補充」。
- MIT 標章只保存文字型證據，不直接複製標章圖樣。

## 證據分級

```text
A  政府有效標章／可發布級證據來源
B  精確型號官方來源一致
C  精確型號部分官方證據
D  官方宣稱、資料不足或仍待交叉查證
```

等級描述證據強度，不是產品品質排名，也不代表已正式發布。

## 核心前端

```text
index.html
assets/magazine.css
assets/magazine.js
assets/product-images.css
assets/product-image-enhancements.js
assets/catalog-v3.css
assets/catalog-v3.js        # stable loader
assets/catalog-v3-1.js      # V3.1 sharded catalog
assets/lifecycle-v3-2.css
assets/lifecycle-v3-2.js    # V3.2 expiry dashboard
```

## 驗證與維護

```bash
python scripts/validate_data.py
python scripts/validate_registry.py
python scripts/validate_registry_scale.py
python scripts/validate_v3_catalog.py
python scripts/validate_v3_1_catalog.py
python scripts/build_public_catalog.py --check-only
python scripts/report_registry_expiry.py --check-only
python scripts/validate_lifecycle_v3_2.py
python scripts/validate_media_rights.py
python scripts/validate_sampo_media.py
python scripts/validate_tatung_media.py
python scripts/validate_oright_media.py
python scripts/validate_site.py

node --check assets/magazine.js
node --check assets/product-image-enhancements.js
node --check assets/catalog-v3.js
node --check assets/catalog-v3-1.js
node --check assets/lifecycle-v3-2.js
node --check assets/app.js
```

## Pages workflow

V3.2 同時修正 production Pages 自我觸發循環。`pages.yml` 的 production result commit 已加入 `paths-ignore`，因此寫回 `docs/deployment/pages-production-result.json` 後不會再觸發下一輪 Pages build。

GitHub Actions 已提供正式 production `build_result: success`／`deploy_result: success` 的部署證據。

## 資料治理

- 台灣品牌 ≠ 台灣製造。
- 有臺灣製造證據 ≠ 自動證明品牌是台灣品牌。
- 以單一產品與精確型號為查證單位。
- MIT 標章只套用到 Registry 實際列出的型號，不能外推同品牌其他商品。
- `brand_origin_status: unverified` 必須保留，不能因 MIT 標章存在就自動改成台灣品牌。
- 標章到期只能改變該證據的有效性，不能自動改其他欄位。
- 圖片來源與圖片使用權是兩件事；`permission_pending` 不代表已授權。
- `demo_only`、`official_source_found`、`government_registry_verified` 都不會自動變成 `published`。
- 搜尋、排序、收藏、圖片、metadata、到期 Dashboard 都只能改變前台呈現或維護優先級，不能升級查證／發布狀態。
- 未知維持待確認，衝突不得隱藏。

## Formal Publication Gate

V3.2 正式發布仍為 0。第一筆正式發布仍必須完成：精確型號識別、現售狀態、可公開產地／製造證據、重大衝突審核、圖片使用權處理與編輯審核。
