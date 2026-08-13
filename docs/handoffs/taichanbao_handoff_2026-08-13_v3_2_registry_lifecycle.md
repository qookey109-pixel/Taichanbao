# 台產報 Handoff — V3.2 Registry Lifecycle

日期：2026-08-13

## 專案名稱

台產報 / Taichanbao

## Repository

`qookey109-pixel/Taichanbao`

## 目前狀態

```text
Version: V3.2 Registry Lifecycle
Real research candidates: 54
MIT active exact models: 50
Deep editorial cases: 4
Isolated demos: 6
Formal published: 0
Registry shards: 2
Expired Registry: 0
Expiring within 90 days: 1
Frontend catalog source: catalog.public.json → manifest/shards fallback
Lifecycle source: registry-expiry.json → public catalog / shards fallback
```

## 本次已完成

- 建立前台 Registry Lifecycle Dashboard。
- 新增「到期管理」導覽。
- 顯示已過期、30／90／180／365 天內到期與下一筆到期型號。
- 到期項目可點回原 Catalog Drawer。
- 365 天內到期 Registry 會在 Catalog 卡片增加剩餘天數標籤。
- 新增 `assets/lifecycle-v3-2.js`、`assets/lifecycle-v3-2.css`。
- 新增 `scripts/validate_lifecycle_v3_2.py`。
- Pages build 產生 `data/registry-expiry.json`。
- 前台在 expiry artifact 缺失時可從 public catalog 或 shards 自動重算。
- `build-info.json` 升級到 V3.2。
- `scripts/validate_site.py` 升級到 V3.2。
- CI／Pages 加入 lifecycle Python 與 Node checks。
- 抓到並修正 Pages production report 自我觸發循環：`pages-production-result.json` 已加入 Pages trigger `paths-ignore`。

## 部署狀態

在加入 V3.2 lifecycle 與 self-loop 修正後，production workflow 已出現：

```text
build_result: success
deploy_result: success
page_url: https://qookey109-pixel.github.io/Taichanbao/
```

外部搜尋爬蟲可能仍顯示上週快照；不要用搜尋快照覆蓋 GitHub Actions 的正式 deploy 結果。

## 重要檔案

```text
PROJECT_STATUS.md
build-info.json

assets/catalog-v3.js
assets/catalog-v3-1.js
assets/catalog-v3.css
assets/lifecycle-v3-2.js
assets/lifecycle-v3-2.css

data/products.registry.json
data/products.registry.appliances.json
data/registry.manifest.json
# deploy-time only:
data/catalog.public.json
data/registry-expiry.json

scripts/build_public_catalog.py
scripts/report_registry_expiry.py
scripts/validate_lifecycle_v3_2.py
scripts/validate_registry_scale.py
scripts/validate_v3_1_catalog.py
scripts/validate_site.py

.github/workflows/validate.yml
.github/workflows/pages.yml

docs/deployment/pages-production-result.json
```

## 資料治理

- MIT 有效證據只套用精確型號。
- 標章到期會使該政府證據失效，不代表產品品質或品牌身分突然改變。
- 到期 Dashboard 不能自動改 publication status。
- `government_registry_verified`／A 級證據仍不等於正式發布。
- 圖片權利、品牌國籍、現售狀態與製造證據分開。
- Formal Publication Gate 不降低，正式發布維持 0。

## 已知風險

- 現有 50 筆 Registry 中家電比例偏高；下一批不可再由家電主導。
- 一筆 Registry 在 90 天內到期，需要在到期前重新查證官方紀錄。
- 多數 Registry 的品牌身分與現售狀態仍未補完。
- 既有 SQLite schema 尚未可靠定位，不得猜 schema。
- 外部搜尋爬蟲的 Pages 快照有延遲，不適合作為即時部署真相來源。

## 禁止執行事項

- 不得把 MIT 標章外推至同品牌其他型號。
- 不得因到期 UI 或 A 級證據直接改成 `published`。
- 不得自行猜品牌國籍。
- 不得直接複製 MIT 標章圖樣。
- 不得刪除 V2.5 Recovery、四個深度案例或 Formal Publication Gate。
- 不得猜 SQLite schema。

## 明確下一步

1. Registry 50 → 100，優先餐廚、居家用品、清潔、日用品與其他非家電類。
2. 新增「分類集中度 Gate」，限制單一類別占比，避免資料庫被家電或服飾灌水。
3. 逐步替現有 50 筆補品牌身分、現售狀態、官方商品頁與圖片狀態。
4. 到期前重新查證最近一筆 2026-10-27 到期 Registry。
5. 若找到正式 SQLite schema，再建立 adapter，不修改原始資料庫。
6. 第一筆正式發布仍需完整通過現有 Gate。

## 新對話可直接使用的接續指令

繼續台產報 `qookey109-pixel/Taichanbao`。以 GitHub main、`PROJECT_STATUS.md` 與 `docs/handoffs/taichanbao_handoff_2026-08-13_v3_2_registry_lifecycle.md` 為正式基準，不要重做 V3.2。下一主線是 Registry 50→100，優先非家電類，並新增分類集中度 Gate。Formal Publication Gate 不降低；MIT 證據只能套用精確型號，正式發布維持 0，除非完整通過既有 Gate。
