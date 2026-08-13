# 台產報 Handoff — V3.0 Evidence Catalog

日期：2026-08-13

## 專案名稱

台產報 / Taichanbao

## Repository

`qookey109-pixel/Taichanbao`

Default branch：`main`

## 目前狀態

正式基準：`V3.0 Evidence Catalog`

台產報已從「4 筆品牌圖片試作」擴張成「雜誌選品＋精確型號證據資料庫」。正式首頁仍維持雜誌型視覺，但加入獨立的 Evidence Catalog。

```text
真實研究候選：19
├─ 深度多圖案例：4
│  ├─ TENDAYS
│  ├─ SAMPO
│  ├─ 大同
│  └─ O'right
└─ MIT 有效精確型號：15

隔離 demo：6
正式發布：0
```

## 本次已完成事項

### 1. 大幅更新正式首頁

- 新版標題：台灣製證據資料誌。
- 左側導覽新增「證據資料庫」。
- 保留雜誌封面、編輯專題、品牌索引、收藏、搜尋與 Formal Publication Gate。
- 新增 Evidence Catalog Hero。
- 新增五個即時指標：真實候選、MIT 型號、深度案例、正式發布、demo。
- 新增 A／B／C／D 證據等級。
- 新增來源、證據、分類、品牌身分與排序篩選。
- 全站搜尋可查品牌、公司、產品、型號、標章編號與標籤。
- Registry 卡片可開啟證據履歷 Drawer。

### 2. 拓展資料庫

新增：`data/products.registry.json`

第一批 15 筆全部來自經濟部產業發展署 MIT 微笑標章官方 Registry，且查閱日 2026-08-13 仍在有效期限內。

涵蓋：

- 服飾配件
- 鞋履
- 眼鏡
- 居家織品
- 寢具
- 家電

代表性型號包括：

- TENDAYs `DMIT017-5(白)`
- 日象 `ZOR-1550SA`
- 尚朋堂 `SSC-12LDCE`
- Panasonic `NR-C387HVLS`
- ADHOC `GENTLE 102(金)`

所有 Registry 記錄：

```text
verification_status: government_registry_verified
manufacturing_evidence_status: mit_certified_active
evidence_level: A
record_scope: exact_model
publication_status: unpublished
```

### 3. 證據範圍治理

- 台灣品牌與台灣製造分成不同欄位。
- MIT 標章不得外推到同品牌其他型號。
- Panasonic MIT 型號不得被用來宣稱 Panasonic 是台灣品牌。
- TENDAYs `DMIT017-5` MIT 記錄不得外推到既有 TENDAYS 隨身枕 `TDT01-T017A`。
- O'right 精確型號主圖與同系列補充圖在前台顯示不同標籤。
- 台灣原料不得被表述為成品台灣製造。

### 4. 圖片與商標治理

- 既有四品牌官方圖片仍維持 `permission_pending`。
- MIT 標章只記錄文字、標章編號、有效期限與官方來源。
- 不將 MIT 標章圖樣複製到前台素材。

### 5. 新增 V3 驗證器

新增：

```text
scripts/validate_registry.py
scripts/validate_v3_catalog.py
```

`validate_registry.py`：

- 驗證必要欄位。
- 驗證精確型號。
- 驗證官方 `keid.nat.gov.tw` HTTPS 網域。
- 驗證 MIT 標章狀態。
- 以實際執行日期檢查有效期限；過期資料會阻擋部署。
- Registry 記錄不得自行 published。

`validate_v3_catalog.py`：

- 6 demo 必須隔離。
- 4 deep cases 必須存在。
- 15 Registry 必須存在。
- 真實候選必須 = 19。
- Registry ID 不得與既有 ID 衝突。
- override 只能指向 deep cases。
- A／B／C／D 等級映射必須符合現行治理。
- 正式發布仍為 0。

### 6. CI / Pages Gate

`.github/workflows/validate.yml` 與 `.github/workflows/pages.yml` 已加入：

- `validate_registry.py`
- `validate_v3_catalog.py`
- `node --check assets/catalog-v3.js`

部署不是只看 HTML 能不能開，而是先過資料、證據、媒體與 JavaScript Gate。

### 7. 可控 Registry 擴充

新增：

`scripts/import_registry_batch.py`

功能：

- 預設 dry-run。
- `--write` 才真正寫入 Registry。
- 拒絕缺欄位。
- 拒絕非官方 MIT 網域。
- 拒絕把批次資料直接設成 published。
- 拒絕標章編號碰撞不同產品 ID。
- 可更新既有 ID 或新增新 ID。

## 重要 GitHub 檔案

```text
index.html
assets/catalog-v3.css
assets/catalog-v3.js
assets/magazine.css
assets/magazine.js
assets/product-images.css
assets/product-image-enhancements.js

data/products.demo.json
data/products.registry.json
data/product.media.overrides.json

docs/DATA_MODEL_V3.md
docs/research/2026-08-13_mit_registry_expansion.md
PROJECT_STATUS.md
README.md

scripts/validate_data.py
scripts/validate_registry.py
scripts/validate_v3_catalog.py
scripts/validate_media_rights.py
scripts/validate_sampo_media.py
scripts/validate_tatung_media.py
scripts/validate_oright_media.py
scripts/validate_site.py
scripts/import_registry_batch.py

.github/workflows/validate.yml
.github/workflows/pages.yml
```

## 尚未完成事項

1. Registry 仍只有第一批 15 筆，不是 MIT 完整鏡像。
2. 尚未建立自動抓取官方 Registry 的 scraper／API adapter；目前使用受控 normalized batch 匯入。
3. 尚未完成 SQLite → 公開 Catalog JSON 的正式 pipeline。
4. 四個深度案例仍缺部分實體型號／製造地照片。
5. 四品牌圖片使用權仍待確認。
6. 尚未有第一筆 `published`。
7. 原先遺失的 20 筆候選與完整研究證據尚未取回，不得自行偽造還原。

## 已知錯誤與風險

- 執行環境目前無法從 container 解析 GitHub 網域，因此無法用本地 `git clone` 跑全 repo 驗證；必須以 GitHub 上的 CI／檔案核對為準。
- Registry 某些產品的品牌名稱未能由政府頁明確辨識，已標 `品牌待確認`／`brand_origin_status: unverified`。
- `data/products.demo.json` 為歷史相容資料，仍同時含 6 demo 與 4 deep cases；V3 前端及跨資料集 validator 會明確隔離，後續可再做 physical split migration。
- MIT Registry 的有效狀態會過期，`validate_registry.py` 已改為依執行日期阻擋過期紀錄。

## 禁止執行事項

- 不得把台灣品牌直接等同台灣製造。
- 不得把 MIT 某型號外推到同品牌所有產品。
- 不得把品牌公司所在地當成產品產地證據。
- 不得把同系列圖片冒充精確型號圖片。
- 不得把 `permission_pending` 寫成已取得授權。
- 不得讓 Registry importer 自動 published。
- 不得降低 Formal Publication Gate 來製造第一筆正式產品。
- 不得刪除 V2.5 Recovery、既有 SQLite、V2.8+ media governance 或四個深度案例。

## 明確下一步

### Phase V3.1 — Registry Scale 50

1. 使用受控 batch importer，把 MIT Registry 從 15 擴到至少 50 筆。
2. 優先增加家電、餐廚、居家用品與不同生活分類，避免只堆服飾／襪類。
3. 每批資料先 dry-run，再跑 Registry + cross-catalog validator。
4. 建立 `last_verified_at`／即將到期清單。
5. 再開始 SQLite → public catalog pipeline。

### Phase V3.2 — First Publishable Product

優先選大同 `TAC-11HN-M` 或其他能取得完整實體證據與圖片權利的產品，跑完整 Formal Publication Gate；不得為了得到 `published=1` 降低標準。

## 新對話可直接使用的接續指令

```text
繼續台產報 V3.0 Evidence Catalog。

Repository：qookey109-pixel/Taichanbao
正式基準：V3.0 Evidence Catalog

先讀：
- PROJECT_STATUS.md
- README.md
- docs/DATA_MODEL_V3.md
- docs/handoffs/taichanbao_handoff_2026-08-13_v3_0_evidence_catalog.md

目前：
- 19 筆真實研究候選
- 15 筆 MIT 有效精確型號 Registry
- 4 筆深度多圖案例
- 6 筆 demo 隔離
- 正式發布 0

下一步做 V3.1 Registry Scale 50：使用受控批次匯入，把 Registry 擴大到至少 50 筆，保持精確型號、官方來源、有效期限、證據範圍與 Formal Publication Gate，不要重做既有功能。
```
