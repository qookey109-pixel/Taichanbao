# 台產報（Taichanbao）V3.6 Brand-Origin Separation

台產報是一個「雜誌選品＋精確型號證據資料庫」。V3.6 把專案最重要的規則真正落到資料與前台：**台灣品牌身分與台灣製造證據是兩條獨立證據鏈**。

## 線上位置

- Repository：`qookey109-pixel/Taichanbao`
- 正式網站：`https://qookey109-pixel.github.io/Taichanbao/`
- V2.5 Recovery：`https://qookey109-pixel.github.io/Taichanbao/versions_review/v2.5/`
- Default branch：`main`

## V3.6 快照

```text
真實研究候選：104
MIT 有效精確型號：100
既有 deep editorial cases：4
Deep editorial candidates：1
Formal published：0

Enrichment Queue：20
已研究：15
verified：21
not_found：33
blocked：6
pending：20

台灣品牌已確認：7 records
非台灣品牌已確認：3 records
現售／供應已確認：9 records
exact official product page：2 records
```

## V3.6 核心案例：Panasonic

Panasonic 官方歷史資料確認品牌／公司源自 **1918 年日本大阪**。因此：

```text
Panasonic brand identity       non_taiwan_brand
```

但以下三個精確冰箱型號同時有有效的經濟部 MIT 微笑標章臺灣製造證據：

```text
NR-C507XVS   MIT active to 2029-06-15
NR-D507XVS   MIT active to 2029-06-15
NR-C617XVS   MIT active to 2029-06-15
```

所以台產報會呈現為：

> **非台灣品牌已確認｜此精確型號 MIT 台灣製造證據有效**

不能因為台灣松下是申請／製造公司，就把 Panasonic 改成台灣品牌。

## 對照案例：CHIMEI KD-703HP1

奇美家電官方可確認 CHIMEI 品牌的台灣發展脈絡；`KD-703HP1` 官方 exact-model 頁也明列 `製造產地：台灣`，目前官方烘碗機列表仍列該型號。

因此這筆可以同時呈現：

> **台灣品牌已確認｜此精確型號台灣製造證據有效**

仍然不能把 KD-703HP1 的產地證據外推到其他奇美型號。

## Brand-Origin Separation 前台

新增：

```text
assets/brand-origin-v3-6.js
assets/brand-origin-v3-6.css
```

前台會並排展示：
- 台灣品牌＋MIT exact-model
- 非台灣品牌＋MIT exact-model
- 已研究但品牌身分仍待確認

品牌身分只影響品牌分類，不會改寫 MIT 製造證據、圖片權利或 publication status。

## Enrichment Results

```text
data/enrichment.results.manifest.json
├─ enrichment.results.v1.json  # 10
├─ enrichment.results.v2.json  # 1
└─ enrichment.results.v3.json  # 4, first P2 batch
```

目前 15 / 20 Queue records 已研究。剩餘 5 筆全部是 P2。

Builder `scripts/build_public_catalog.py` 只把人工 verified 的 enrichment 結果合併至 deploy-time `catalog.public.json`；**raw MIT Registry 不改寫**。

## V3.5 Deep Candidate 保留

CHIMEI `KD-884HP0` 仍是第一筆 Deep Candidate：

```text
品牌／型號／MIT／現售／官方頁／衝突初查   PASS
圖片權利                                BLOCKED
編輯審核                                PENDING
正式發布                                BLOCKED
```

Candidate ≠ deep editorial case ≠ published。

## 驗證

```bash
python scripts/validate_enrichment_v3_4.py
python scripts/validate_deep_candidates_v3_5.py
python scripts/build_public_catalog.py --check-only
python scripts/validate_site.py

node --check assets/catalog-v3.js
node --check assets/enrichment-v3-4.js
node --check assets/deep-candidates-v3-5.js
node --check assets/brand-origin-v3-6.js
```

CI / Pages 另外保留 Registry 100、分類集中度、Lifecycle、Media 與 V2.5 Recovery 的既有驗證。

## 資料治理

- **台灣品牌 ≠ 台灣製造。**
- 非台灣品牌也可能有特定台灣製造型號。
- 台灣品牌也不能把一個型號的臺灣產地外推到全品牌。
- MIT 精確型號證據不得外推到其他型號。
- 有效 MIT ≠ 即時庫存。
- 銷售通路紀錄 ≠ 即時庫存。
- 同系列頁 ≠ exact-model 官方頁。
- 官方圖片公開可見 ≠ 已取得重用授權。
- Deep candidate ≠ formal publication。
- Formal Publication Gate 維持不變，目前正式發布 **0**。
