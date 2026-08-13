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
```

## 本次已完成

- MIT Registry 從 15 → 50。
- 新增 35 筆家電精確型號。
- 新增 `data/products.registry.appliances.json`。
- 新增 `data/registry.manifest.json`。
- 新增 `assets/catalog-v3-1.js`，改為 manifest/shard 載入。
- `assets/catalog-v3.js` 改為穩定 loader。
- 新增跨 shard 50 筆驗證器 `scripts/validate_registry_scale.py`。
- 新增 54 筆 catalog 驗證器 `scripts/validate_v3_1_catalog.py`。
- 新增 MIT 到期報表 `scripts/report_registry_expiry.py`。
- GitHub Actions／Pages Gate 加入 V3.1 驗證。
- 更新 `build-info.json` 為 54／50／4／6／0／2 shards。
- 更新 README、PROJECT_STATUS、研究紀錄。

## 本批資料來源

經濟部產業發展署臺灣製產品 MIT 微笑標章官方家電查詢：

- `?classid=10&p=2`
- `?classid=10&p=4`
- `?classid=10&p=5`

## 資料治理

- MIT 證據只套用到精確型號。
- `brand_origin_status` 不因 MIT 標章自動升級。
- 所有 Registry 仍為 `unpublished`。
- A 級證據不等於正式發布。
- 過期標章必須阻擋驗證。
- MIT 標章圖樣不直接複製進網站。
- 圖片權利與製造證據分開。

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

scripts/validate_registry.py
scripts/validate_registry_scale.py
scripts/validate_v3_catalog.py
scripts/validate_v3_1_catalog.py
scripts/report_registry_expiry.py
scripts/import_registry_batch.py
scripts/validate_site.py

docs/research/2026-08-13_mit_appliance_scale_50.md
```

## 已知錯誤與風險

- GitHub connector 不一定會回傳 push-triggered Actions status，因此不能只以 commit 成功判斷部署 PASS。
- 公開 Pages 必須以 `build-info.json` 實際內容核對版本。
- V3.1 本批新增大量家電，資料類別集中度變高；下一批應優先補非家電類。
- 50 筆 Registry 是研究資料，不代表 50 筆都已確認現售或品牌國籍。

## 禁止執行事項

- 不得把 MIT 標章外推至同品牌其他型號。
- 不得把 `government_registry_verified` 自動改為 `published`。
- 不得因申請公司名稱或品牌熟悉度自行判斷台灣品牌。
- 不得刪除 V2.5 Recovery Baseline、四個深度案例或 Formal Publication Gate。
- 不得把官方圖片存在視為使用授權。

## 明確下一步

1. 驗證公開 Pages 的 `build-info.json` 是否已為 V3.1。
2. 建立 SQLite → `catalog.public.json` 的可重建 build pipeline。
3. 將到期報表納入 CI artifact 或管理頁。
4. Registry 50 → 100 時優先擴充餐廚、居家用品、清潔與其他生活類別。
5. 第一筆正式發布仍需另外完成現售、實體證據、圖片權利與編輯審核。

## 新對話可直接使用的接續指令

繼續台產報 `qookey109-pixel/Taichanbao`。以 GitHub main 最新內容及 `docs/handoffs/taichanbao_handoff_2026-08-13_v3_1_registry_scale_50.md` 為基準。不要重做 V3.1。先核對公開 `build-info.json` 是否部署到 V3.1；再建立 SQLite → public catalog 的可重建發布管線，並規劃 Registry 50 → 100 的非家電擴充。Formal Publication Gate 不降低，正式發布維持 0，除非證據完整通過既有 Gate。
