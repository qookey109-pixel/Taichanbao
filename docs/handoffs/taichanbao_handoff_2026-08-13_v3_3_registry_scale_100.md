# 台產報 Handoff — V3.3 Registry Scale 100

日期：2026-08-13

## 專案名稱
台產報 / Taichanbao

## Repository
`qookey109-pixel/Taichanbao`

## 目前狀態

```text
Version: V3.3 Registry Scale 100
Real research candidates: 104
MIT active exact models: 100
Deep editorial cases: 4
Isolated demos: 6
Formal published: 0
Registry shards: 3
Lifecycle: enabled
Category concentration Gate: <= 40%
```

## 本次已完成

- Registry 50 → 100。
- 新增 50 筆 lifestyle MIT 精確型號。
- 新增 `data/products.registry.lifestyle.json`。
- Manifest 升為 3 shards／100 records。
- Lifestyle 組成：寢具 14、居家織品 12、袋包收納 12、居家用品 12。
- Public catalog builder 改為 manifest-driven，不再硬編碼 50。
- Expiry report 改為 manifest-driven。
- V3.1 50 筆 regression baseline 保留。
- 新增 `validate_v3_3_catalog.py`。
- 新增 `validate_category_balance.py`，任一分類與家電占比不得超過 40%。
- `validate_registry_scale.py` 升為 100 ID／100 certificate unique Gate。
- Catalog frontend 接受 V3.3 `catalog.public.json`：104／100／4／3 shards／0 published。
- 新增 `assets/scale-v3-3.js` 顯示 Scale 100 與分類平衡摘要。
- V3.2 Lifecycle 保留並支援 100 筆。
- build-info、CI、Pages workflow、README、PROJECT_STATUS 已同步 V3.3。

## 新增官方資料來源範圍

經濟部產業發展署 MIT 微笑標章：

- 毛巾 `classid=5`
- 寢具 `classid=6`
- 袋包箱 `classid=9`
- 布窗簾 `classid=20`

所有資料維持精確型號 scope；品牌國籍與現售狀態不因 MIT 記錄自動升級。

## 重要檔案

```text
PROJECT_STATUS.md
README.md
build-info.json

data/registry.manifest.json
data/products.registry.json
data/products.registry.appliances.json
data/products.registry.lifestyle.json
data/products.demo.json
data/product.media.overrides.json

assets/catalog-v3.js
assets/catalog-v3-1.js
assets/lifecycle-v3-2.js
assets/lifecycle-v3-2.css
assets/scale-v3-3.js

scripts/build_public_catalog.py
scripts/report_registry_expiry.py
scripts/validate_registry.py
scripts/validate_registry_scale.py
scripts/validate_v3_1_catalog.py
scripts/validate_v3_3_catalog.py
scripts/validate_category_balance.py
scripts/validate_lifecycle_v3_2.py
scripts/validate_site.py

.github/workflows/validate.yml
.github/workflows/pages.yml
```

## 資料治理

- 台灣品牌 ≠ 台灣製造。
- MIT 有效紀錄只支持該精確型號。
- MIT 製造證據不自動證明品牌國籍或現售。
- Registry 全部 `unpublished`。
- A 級證據不等於正式發布。
- 分類平衡 Gate 不影響產品發布狀態。
- Lifecycle 到期提醒只影響證據維護優先級。
- MIT 標章圖樣不直接複製進網站。
- 圖片權利與製造證據分開。

## 已知風險／待確認

- V3.3 最後一輪 production build/deploy 必須以 `docs/deployment/pages-production-result.json` 對應最新 V3.3 trigger SHA 驗收。
- 新 lifestyle shard 多數 `brand_origin_status` 仍為 `unverified`。
- Registry 目前只證明 MIT 精確型號，不等於 100 筆都已確認現售。
- 部分產品來源頁為類別列表頁；後續 enrichment 可補精確產品明細頁。
- 既有 SQLite schema 尚未可靠定位，不得猜測後硬接。

## 禁止執行事項

- 不得把 MIT 證據外推至同品牌其他型號。
- 不得把 `government_registry_verified` 自動改為 `published`。
- 不得因公司名稱／熟悉品牌自行判斷台灣品牌。
- 不得降低 Formal Publication Gate。
- 不得刪除 V2.5 Recovery、四個深度案例、V3.1 regression、V3.2 Lifecycle 或 V3.3 category Gate。

## 明確下一步

1. 驗收最新 V3.3 Pages production build/deploy。
2. 建立 enrichment queue，優先選 10–20 筆消費者熟悉產品補品牌身分、現售、官方產品頁與圖片權利。
3. 補餐廚／清潔等仍偏少類別，不再以單純總筆數為唯一目標。
4. 逐步把高品質 Registry 候選轉成深度案例，但不正式發布，除非完整通過 Gate。

## 新對話接續指令

繼續台產報 `qookey109-pixel/Taichanbao`。以 GitHub main 最新內容、`PROJECT_STATUS.md` 與 `docs/handoffs/taichanbao_handoff_2026-08-13_v3_3_registry_scale_100.md` 為基準。不要重做 V3.3。先確認 V3.3 production build/deploy 是否 PASS；若 PASS，進入 Registry enrichment，優先 10–20 筆消費者熟悉產品補台灣品牌身分、現售狀態、官方產品頁與圖片權利。Formal Publication Gate 不降低，正式發布維持 0，除非完整通過既有 Gate。
