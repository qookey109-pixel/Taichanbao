# 台產報（Taichanbao）V3.7 Enrichment Complete 20/20

台產報是一個「雜誌選品＋精確型號證據資料庫」。V3.7 完成第一輪 20 筆優先產品的完整 Enrichment Research，並新增 Promotion Audit：**研究做完，不代表全部都該推薦；品牌國籍、台灣製造、現售、官方頁、圖片權利與正式發布仍各自獨立。**

## 線上位置

- Repository：`qookey109-pixel/Taichanbao`
- 正式網站：`https://qookey109-pixel.github.io/Taichanbao/`
- V2.5 Recovery：`https://qookey109-pixel.github.io/Taichanbao/versions_review/v2.5/`
- Default branch：`main`

## V3.7 快照

```text
真實研究候選：104
MIT 有效精確型號：100
既有 deep editorial cases：4
已登錄 Deep Candidate：1
Formal published：0

Enrichment Queue：20 / 20 complete
verified：22
not_found：51
blocked：7
pending：0

台灣品牌已確認：8 records
非台灣品牌已確認：3 records
現售／供應已確認：9 records
exact official product page：2 records
```

`not_found` 與 `blocked` 都是正式研究結果，不會為了提高成功率而被改成正面結論。

## Promotion Audit

V3.7 對研究完成的 20 筆再做一次 promotion audit：

```text
Deep Candidate 條件已達、但資產／編輯 Gate 阻擋：2
台灣品牌 research-only：6
非台灣品牌，但有台灣製 exact-model：3
品牌身分仍待確認 research-only：9
```

其中：

- `KD-884HP0`：已登錄 Deep Candidate，但圖片權利 BLOCKED、editorial review PENDING。
- `KD-703HP1`：符合 Deep Candidate review 條件，但**尚未自動升級成 candidate**。
- Panasonic `NR-C507XVS`／`NR-D507XVS`／`NR-C617XVS`：已確認為非台灣品牌，但保留各自有效 MIT 台灣製造 exact-model 證據，並排除「台灣品牌推薦」。

Promotion Audit 只決定下一步研究／編輯路徑，不修改 raw Registry 或 publication status。

部署時產生：

```text
data/promotion-audit.json
```

來源 builder：

```text
scripts/build_promotion_audit.py
scripts/validate_promotion_audit_v3_7.py
```

## Brand-Origin Separation

台產報永久維持：

> **台灣品牌 ≠ 台灣製造**

Panasonic 官方歷史確認品牌源自日本大阪；但以下 exact models 同時有有效 MIT 台灣製造證據：

```text
NR-C507XVS
NR-D507XVS
NR-C617XVS
```

因此正確表示為：

> **非台灣品牌已確認｜此精確型號 MIT 台灣製造證據有效**

對照 CHIMEI `KD-703HP1`，則可表示為：

> **台灣品牌已確認｜此精確型號台灣製造證據有效**

兩者都不能把單一型號證據外推至其他產品。

## Enrichment Results 分片

```text
data/enrichment.results.manifest.json
├─ enrichment.results.v1.json  # 10
├─ enrichment.results.v2.json  # 1
├─ enrichment.results.v3.json  # 4
└─ enrichment.results.v4.json  # 5
```

目前 20 筆全數研究完成。Builder `scripts/build_public_catalog.py` 依 manifest 合併受控 enrichment findings；**raw MIT Registry、manufacturing evidence、verification status 與 publication status 不被改寫**。

## 前台層

```text
assets/catalog-v3.js
assets/catalog-v3-1.js
assets/lifecycle-v3-2.js
assets/scale-v3-3.js
assets/enrichment-v3-4.js
assets/deep-candidates-v3-5.js
assets/brand-origin-v3-6.js
assets/promotion-audit-v3-7.js
```

最後一層 V3.7 Promotion Audit 讓讀者看到研究完成後真正的去向，而不是把全部 20 筆包裝成推薦清單。

## 驗證

```bash
python scripts/validate_enrichment_v3_4.py
python scripts/validate_deep_candidates_v3_5.py
python scripts/build_promotion_audit.py --check-only
python scripts/validate_promotion_audit_v3_7.py
python scripts/build_public_catalog.py --check-only
python scripts/validate_site.py

node --check assets/catalog-v3.js
node --check assets/enrichment-v3-4.js
node --check assets/deep-candidates-v3-5.js
node --check assets/brand-origin-v3-6.js
node --check assets/promotion-audit-v3-7.js
```

CI / Pages 另保留 Registry 100、分類集中度、Lifecycle、Media 與 V2.5 Recovery 的既有驗證。

## 資料治理

- 台灣品牌 ≠ 台灣製造。
- 非台灣品牌也可能有特定台灣製造型號。
- MIT exact-model 證據不得外推到其他型號。
- 有效 MIT ≠ 即時庫存；銷售通路 ≠ 即時庫存。
- 同系列頁 ≠ exact-model 官方頁。
- 官方圖片公開可見 ≠ 已取得重用授權。
- Enrichment completed ≠ verified。
- Promotion Audit ≠ promotion。
- Deep Candidate ≠ formal publication。
- Formal Publication Gate 維持不變，目前正式發布 **0**。
