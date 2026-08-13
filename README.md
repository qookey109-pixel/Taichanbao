# 台產報（Taichanbao）V3.5 Deep Candidate Gate

台產報是一個「雜誌選品＋精確型號證據資料庫」。V3.5 在 100 筆 MIT 精確型號 Registry、證據生命週期與 Enrichment Queue 之上，新增 **Deep Candidate Gate**：只有證據鏈已足以進入深度專題評估的產品才成為候選，而且候選仍不等於正式發布。

## 線上位置

- Repository：`qookey109-pixel/Taichanbao`
- 正式網站：`https://qookey109-pixel.github.io/Taichanbao/`
- V2.5 Recovery 預覽：`https://qookey109-pixel.github.io/Taichanbao/versions_review/v2.5/`
- Default branch：`main`

## V3.5 快照

```text
真實研究候選：104
MIT 有效精確型號：100
既有深度編輯案例：4
Deep editorial candidates：1
正式發布：0

Enrichment Queue：20
P1：11 / 11 已完成
已研究：11
verified tasks：12
not_found：27
blocked：5
pending P2 tasks：36
```

## 第一個 Deep Candidate：CHIMEI KD-884HP0

`KD-884HP0` 目前是第一筆通過 Deep Candidate 前置條件、但仍被資產權利 Gate 阻擋的產品：

```text
品牌身分                 PASS
精確型號                 PASS
MIT 精確型號製造證據      PASS
現售／供應證據            PASS
品牌官方 exact-model 頁   PASS
重大衝突初查              PASS
圖片權利                 BLOCKED
編輯審核                 PENDING
正式發布                 BLOCKED
```

官方精確型號頁列 `KD-884HP0`、88L 規格與「製造產地：台灣」；MIT 微笑標章紀錄 `02000038-02030` 目前有效至 2029-06-01。這些證據只適用此型號，不得外推到其他奇美產品。

候選資料：`data/deep_case.candidates.json`

## Enrichment Results 分片

V3.5 不再把所有 enrichment findings 持續塞進單一大型檔案：

```text
data/enrichment.results.manifest.json
├─ data/enrichment.results.v1.json   # 前兩批，10 records
└─ data/enrichment.results.v2.json   # 第三批，1 record
```

目前 P1 11 筆已全部研究完成。`not_found` 與 `blocked` 都是正式研究結果，不會因為想提高成功率而被改成正面結論。

## Public Catalog Pipeline

```text
Registry manifest / shards
Deep editorial cases
Enrichment results manifest / batches
        │
        ▼
scripts/build_public_catalog.py
        │
        ▼
data/catalog.public.json   # deploy-time artifact
```

Enrichment 只能把人工已驗證的品牌身分、現售狀態與 exact-model 官方頁資訊合併進 public catalog；**raw MIT Registry、manufacturing evidence、verification status、publication status 不會被改寫**。

## Registry / Lifecycle 基線

```text
Registry：100 exact models / 3 shards
Real research candidates：104
Category concentration Gate：enabled
Lifecycle Dashboard：enabled
Expired Registry：0
Formal published：0
```

V3.3 的分類集中度 Gate 與 V3.2 的到期管理完整保留。

## 核心檔案

```text
index.html
assets/catalog-v3.js
assets/catalog-v3-1.js
assets/lifecycle-v3-2.js
assets/scale-v3-3.js
assets/enrichment-v3-4.js
assets/enrichment-v3-4.css
assets/deep-candidates-v3-5.js
assets/deep-candidates-v3-5.css

data/registry.manifest.json
data/enrichment.queue.json
data/enrichment.results.manifest.json
data/enrichment.results.v1.json
data/enrichment.results.v2.json
data/deep_case.candidates.json

scripts/build_public_catalog.py
scripts/validate_enrichment_v3_4.py
scripts/validate_deep_candidates_v3_5.py
scripts/validate_site.py
```

## 驗證

```bash
python scripts/validate_data.py
python scripts/validate_registry.py
python scripts/validate_registry_scale.py
python scripts/validate_v3_3_catalog.py
python scripts/validate_category_balance.py
python scripts/validate_enrichment_v3_4.py
python scripts/validate_deep_candidates_v3_5.py
python scripts/build_public_catalog.py --check-only
python scripts/report_registry_expiry.py --check-only
python scripts/validate_lifecycle_v3_2.py
python scripts/validate_site.py

node --check assets/catalog-v3.js
node --check assets/catalog-v3-1.js
node --check assets/lifecycle-v3-2.js
node --check assets/scale-v3-3.js
node --check assets/enrichment-v3-4.js
node --check assets/deep-candidates-v3-5.js
```

## 資料治理

- 台灣品牌 ≠ 台灣製造。
- MIT 精確型號證據不得外推到同品牌其他產品。
- 有效 MIT 標章 ≠ 現售。
- 銷售通路紀錄 ≠ 即時庫存。
- 同系列頁 ≠ exact-model 官方頁。
- 官方圖片公開可見 ≠ 已取得重用授權。
- Deep candidate ≠ deep editorial case ≠ formal publication。
- 搜尋、收藏、圖片、metadata、Enrichment、Lifecycle、Candidate Gate 都不能自動升級發布狀態。
- Formal Publication Gate 維持不變，目前正式發布為 **0**。
