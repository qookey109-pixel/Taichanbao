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
- public catalog 會保存 4 筆 deep cases 的主要來源 URL／來源名稱，不因 build 遺失證據鏈。
- CI 已加入 public catalog `--check-only` 與 Registry expiry `--check-only`。
- `scripts/validate_site.py` 已鎖定 public-catalog-first 與 fallback 行為。
- 更新 `build-info.json` 為 54／50／4／6／0／2 shards。
- README、PROJECT_STATUS、研究紀錄同步。

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

docs/research/2026-08-13_mit_appliance_scale_50.md
```

## 已知錯誤與風險

- 公開 GitHub Pages 外部讀取仍顯示舊 `VOL. 001 · 2026 JULY`，因此 **V3.1 deployment 尚未驗證成功**。
- GitHub connector 無法可靠列出 push-triggered Actions run；commit 成功不能當作 deploy PASS。
- Pages workflow 已包含 `catalog.public.json` build；但將 expiry report JSON 一併寫進 Pages 的第二次 workflow update 被工具安全層阻擋，所以目前 expiry 先作 CI Gate。
- Repository 既有 SQLite schema 尚未從可搜尋文字檔可靠定位；本次沒有猜測或修改未知 SQLite 表。
- 家電占 Registry 比例偏高；下一批應優先非家電類。

## 禁止執行事項

- 不得把 MIT 標章外推至同品牌其他型號。
- 不得把 `government_registry_verified` 自動改為 `published`。
- 不得因申請公司名稱或品牌熟悉度自行判斷台灣品牌。
- 不得刪除 V2.5 Recovery Baseline、四個深度案例或 Formal Publication Gate。
- 不得把官方圖片存在視為使用授權。
- 不得直接猜 SQLite schema。

## 明確下一步

1. **最高優先：Pages deployment recovery**，找出為何公開站仍是 VOL.001。
2. 成功部署後，核對公開 `build-info.json` 應為 V3.1，並確認 `data/catalog.public.json` 可讀。
3. 建立 Registry expiry dashboard／管理頁。
4. Registry 50 → 100 時優先擴充餐廚、居家用品、清潔與其他生活類別。
5. 若定位到既有 SQLite 正式 schema，再新增 adapter，不修改原始資料庫。
6. 第一筆正式發布仍需完成現售、實體證據、圖片權利與編輯審核。

## 新對話可直接使用的接續指令

繼續台產報 `qookey109-pixel/Taichanbao`。以 GitHub main 最新內容及 `docs/handoffs/taichanbao_handoff_2026-08-13_v3_1_registry_scale_50.md` 為基準。不要重做 V3.1。最高優先先處理 GitHub Pages deployment recovery：公開站目前仍是 VOL.001。確認部署後核對 `build-info.json`、`data/catalog.public.json`，再做 Registry expiry dashboard 與 50→100 的非家電擴充。Formal Publication Gate 不降低，正式發布維持 0。
