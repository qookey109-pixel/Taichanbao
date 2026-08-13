# 台產報 Handoff — V3.1 Registry Scale 50

日期：2026-08-13

## 專案名稱

台產報 / Taichanbao

## Repository

`qookey109-pixel/Taichanbao`

## 目前狀態

```text
Version: V3.1 Registry Scale 50
Real research candidates: 54
MIT active exact models: 50
Deep editorial cases: 4
Isolated demos: 6
Formal published: 0
Registry shards: 2
Frontend source priority: catalog.public.json → manifest/shards fallback
Pages production build: SUCCESS
Pages production deploy: SUCCESS
```

## 本次已完成

- MIT Registry 15 → 50。
- 新增 35 筆家電精確型號。
- 新增 `data/products.registry.appliances.json`。
- 新增 `data/registry.manifest.json`。
- 新增 `assets/catalog-v3-1.js`，支援 public catalog 優先、manifest/shard fallback。
- `assets/catalog-v3.js` 保留為穩定 loader。
- 新增跨 shard 50 筆驗證器 `scripts/validate_registry_scale.py`。
- 新增 54 筆 catalog 驗證器 `scripts/validate_v3_1_catalog.py`。
- 新增 MIT 到期報表 `scripts/report_registry_expiry.py`，CI 會檢查過期狀態。
- 新增 deterministic public catalog builder `scripts/build_public_catalog.py`。
- Pages build 會在上傳 artifact 前生成 `data/catalog.public.json`。
- public catalog 保存 deep cases 的主要來源 URL／來源名稱。
- CI 已加入 public catalog deterministic check、Registry expiry check 與 V3.1 frontend 驗證。
- 更新 `build-info.json` 為 54／50／4／6／0／2 shards。
- 完成 GitHub Pages deployment recovery。

## Pages Recovery 結論

本次用三層證據確認：

1. 一次性最小 Pages Recovery workflow：`deploy_result = success`。
2. 一次性 Build Gate Diagnostic：production workflow 17 個 Python／Node 檢查全部 PASS。
3. 正式 `.github/workflows/pages.yml`：`build_result = success`、`deploy_result = success`，page URL 為正式站。

一次性 recovery／build-diagnostic workflow 已刪除，只保留結果 JSON。正式 `pages.yml` 現在會自我回報 production build/deploy 結果。

因此 **Pages deployment recovery 已完成，不要再重做這一階段**。外部搜尋爬蟲可能仍顯示舊頁面快照，但不能以快照落後推翻 GitHub Actions 的 production success 證據。

## 本批資料來源

經濟部產業發展署臺灣製產品 MIT 微笑標章官方家電查詢：

- `?classid=10&p=2`
- `?classid=10&p=4`
- `?classid=10&p=5`

新增代表型號包括 Panasonic 冰箱／冷氣、奇美烘碗機、東元捕蚊燈、ALASKA 通風扇、ESUN 空氣淨化機及冰點冷氣。

## 資料治理

- MIT 證據只套用精確型號。
- `brand_origin_status` 不因 MIT 標章自動升級。
- 所有 Registry 仍為 `unpublished`。
- A 級證據不等於正式發布。
- 過期標章必須阻擋驗證。
- MIT 標章圖樣不直接複製進網站。
- 圖片權利與製造證據分開。
- `catalog.public.json` 是 deploy-time build artifact，不是人工維護的 source of truth。

## 重要檔案

```text
PROJECT_STATUS.md
README.md
build-info.json

data/registry.manifest.json
data/products.registry.json
data/products.registry.appliances.json
data/products.demo.json
data/product.media.overrides.json

assets/catalog-v3.js
assets/catalog-v3-1.js
assets/catalog-v3.css

scripts/build_public_catalog.py
scripts/validate_registry.py
scripts/validate_registry_scale.py
scripts/validate_v3_catalog.py
scripts/validate_v3_1_catalog.py
scripts/report_registry_expiry.py
scripts/import_registry_batch.py
scripts/validate_site.py

.github/workflows/pages.yml
docs/deployment/pages-recovery-result.json
docs/deployment/pages-build-diagnostic.json
docs/deployment/pages-production-result.json
docs/research/2026-08-13_mit_appliance_scale_50.md
```

## 已知錯誤與風險

- 外部搜尋／爬蟲快照可能晚於實際 Pages deployment，不得直接當作即時站況。
- Repository 既有 SQLite schema 尚未從可搜尋文字檔可靠定位；不得猜測或修改未知 SQLite 表。
- 家電占 Registry 比例偏高；下一批應優先非家電類。
- 50 筆 Registry 是研究資料，不代表 50 筆都已確認現售或台灣品牌身分。
- 四個深度案例圖片權利仍有 `permission_pending`。

## 禁止執行事項

- 不得重做已結案的 Pages deployment recovery。
- 不得把 MIT 標章外推至同品牌其他型號。
- 不得把 `government_registry_verified` 自動改為 `published`。
- 不得因申請公司名稱或品牌熟悉度自行判斷台灣品牌。
- 不得刪除 V2.5 Recovery Baseline、四個深度案例或 Formal Publication Gate。
- 不得把官方圖片存在視為使用授權。
- 不得直接猜 SQLite schema。

## 明確下一步

1. 建立 Registry expiry dashboard／管理頁。
2. Registry 50 → 100 時優先擴充餐廚、居家用品、清潔與其他生活類別。
3. 同時替既有 50 筆補 `brand_origin_status` 與現售狀態，降低「只有 MIT、沒有品牌身分／現售」的資料缺口。
4. 若定位到既有 SQLite 正式 schema，再新增 adapter，不修改原始資料庫。
5. 第一筆正式發布仍需完成現售、實體證據、圖片權利與編輯審核。

## 新對話可直接使用的接續指令

繼續台產報 `qookey109-pixel/Taichanbao`。以 GitHub main 最新內容及 `docs/handoffs/taichanbao_handoff_2026-08-13_v3_1_registry_scale_50.md` 為基準。不要重做 V3.1 Registry Scale 50，也不要重做 Pages deployment recovery；production build/deploy 已成功。下一步先建立 Registry expiry dashboard，之後將 Registry 50→100，優先補餐廚、居家用品、清潔與其他非家電類，並逐步補品牌身分與現售狀態。Formal Publication Gate 不降低，正式發布維持 0，除非完整通過既有 Gate。
