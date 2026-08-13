# 台產報（Taichanbao）V3.8 Candidate Promotion Review

台產報是一個「雜誌選品＋精確型號證據資料庫」。V3.8 在 20/20 Enrichment Complete 與 Promotion Audit 之上，完成第一輪 **Candidate Promotion Review**：`KD-884HP0` 與 `KD-703HP1` 都正式成為 Deep Candidate，但候選審核通過不代表可發布；圖片權利與 formal publication editorial review 仍是獨立 Gate。

## 線上位置

- Repository：`qookey109-pixel/Taichanbao`
- 正式網站：`https://qookey109-pixel.github.io/Taichanbao/`
- V2.5 Recovery：`https://qookey109-pixel.github.io/Taichanbao/versions_review/v2.5/`
- Default branch：`main`

## V3.8 快照

```text
真實研究候選：104
MIT 有效精確型號：100
既有 deep editorial cases：4
已登錄 Deep Candidate：2
Formal published：0

Candidate editorial review PASS：2
Image-rights BLOCKED：2
Publication editorial review PENDING：2

Media-rights requests：2
ready_to_contact：2
request_sent：0
```

## 兩個 Deep Candidate

### CHIMEI KD-884HP0

```text
品牌身分                    PASS
精確型號                    PASS
MIT exact-model 製造證據    PASS
現售／供應                  PASS
exact official product page PASS
重大衝突初查                PASS
候選層 editorial review     PASS
圖片權利                    BLOCKED
正式發布編輯審核            PENDING
formal publication           BLOCKED
```

### CHIMEI KD-703HP1

原本在 V3.7 僅為 `eligible_for_deep_candidate_review`。V3.8 完成人工候選審核後，已正式加入 `data/deep_case.candidates.json`，但同樣維持：

```text
candidate_status = blocked_assets
publication_status = unpublished
```

兩台的官方產品頁、MIT exact-model 紀錄與品牌身分證據目前一致；`KD-884HP0` 與 `KD-703HP1` 的 MIT 標章均有效至 2029-06-01。

## 圖片權利 Gate

CHIMEI 官方使用條款明確規定，網站影像、攝影、圖片等受智慧財產權保護，未經授權不得重製、改作、散佈或公開傳輸。因此：

> **官方圖片公開可見 ≠ 台產報可直接重用。**

V3.8 新增：

```text
data/media-rights.requests.json
```

目前兩筆：

```text
KD-884HP0  permission_required / ready_to_contact / request_sent=false
KD-703HP1  permission_required / ready_to_contact / request_sent=false
```

並新增授權申請草稿：

```text
docs/media-rights/chimei_kd884_kd703_permission_request.md
```

建議聯絡信箱依 CHIMEI 官方聯絡頁：`lcd@mail.chimei.com.tw`。

**系統目前沒有替使用者寄出授權信。** 在取得書面授權或找到合法替代素材以前，兩台都不能使用 CHIMEI 官方產品圖片進行 formal publication。

## Promotion Audit

研究完成 20 筆的分類仍維持：

```text
Deep Candidate／資產阻擋：2
台灣品牌 research-only：6
非台灣品牌＋台灣製 exact-model：3
品牌身分待確認 research-only：9
Formal published：0
```

V3.8 的差異是：原本 1 筆 registered + 1 筆 eligible，現在已變成：

```text
registered_deep_candidates = 2
eligible_unregistered_deep_candidates = 0
```

Promotion Audit 仍只負責分類與追蹤，不會自動修改 formal publication。

## Brand-Origin Separation 永久保留

> **台灣品牌 ≠ 台灣製造。**

Panasonic `NR-C507XVS`／`NR-D507XVS`／`NR-C617XVS` 仍維持：

```text
brand_origin_status = non_taiwan_brand
manufacturing_evidence_status = mit_certified_active
```

不得因 MIT 台灣製造證據把 Panasonic 改成台灣品牌，也不得因 Panasonic 是日本品牌否定這三個 exact models 的台灣製造證據。

## Enrichment Results

```text
data/enrichment.results.manifest.json
├─ enrichment.results.v1.json  # 10
├─ enrichment.results.v2.json  # 1
├─ enrichment.results.v3.json  # 4
└─ enrichment.results.v4.json  # 5
```

20 / 20 全部研究完成：

```text
verified：22
not_found：51
blocked：7
pending：0
```

## 核心前台

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

檔名保留歷史版本編號，但 loader 最終版本標記已升級為 `V3.8 Candidate Promotion Review`。

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
- Enrichment completed ≠ verified。
- Promotion Audit ≠ promotion。
- Candidate editorial review ≠ publication editorial review。
- Deep Candidate ≠ formal publication。
- 官方圖片公開可見 ≠ 已取得重用授權。
- 未取得授權時不得下載／複製官方圖片進 repository。
- MIT exact-model 證據不得外推到其他型號。
- Formal Publication Gate 維持不變，目前正式發布 **0**。
