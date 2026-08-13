# 台產報 Handoff — V3.5 Deep Candidate Gate

日期：2026-08-13

## 專案名稱
台產報 / Taichanbao

## Repository
`qookey109-pixel/Taichanbao`

## 目前狀態

```text
Version: V3.5 Deep Candidate Gate
Real research candidates: 104
MIT active exact models: 100
Existing deep editorial cases: 4
Deep editorial candidates: 1
Deep candidates blocked: 1
Enrichment queue: 20
P1 enrichment: 11 / 11 complete
Researched records: 11
Verified tasks: 12
Not-found tasks: 27
Blocked tasks: 5
Pending P2 tasks: 36
Formal published: 0
```

## 本次已完成

- V3.4 Batch 2 最終 production 已確認 success。
- 完成最後 P1：YYMe `1147508(紫)`。
  - MIT exact model 有效至 2029-07-02。
  - brand_identity / current_sale / official_product_page / image_rights 均 `not_found`。
  - 不由元維棉織廠是台灣申請者推定 YYMe 為台灣品牌。
- P1 現在 11 / 11 全部研究完成；剩餘 Queue 全為 P2。
- 新增 `data/enrichment.results.v2.json`。
- 新增 `data/enrichment.results.manifest.json`，enrichment results 改成 batch / manifest 架構。
- `scripts/build_public_catalog.py` 改為依 results manifest 合併 findings，不再硬綁單一 v1 JSON。
- public catalog 現在可保存：verified brand identity、current sale、exact official product page URL、image-rights research status 與完整 enrichment findings。
- raw MIT Registry 不改寫。
- 新增 `data/deep_case.candidates.json`。
- 第一個 deep editorial candidate：CHIMEI 奇美 `KD-884HP0`。
- 新增 `scripts/validate_deep_candidates_v3_5.py`。
- 新增 `assets/deep-candidates-v3-5.js` / `.css`，前台可視化 Candidate Gate。
- `assets/catalog-v3.js` 已載入 V3.5 candidate layer。
- `scripts/validate_enrichment_v3_4.py` 已升級到 manifest 驗證，鎖定 P1 complete。
- `scripts/validate_site.py`、CI、Pages workflow、README、PROJECT_STATUS、build-info 已升級 V3.5。
- 新增研究紀錄 `docs/research/2026-08-13_chimei_kd884hp0_deep_candidate.md`。

## KD-884HP0 Candidate Gate

```text
brand_identity                  PASS
exact_model_identity             PASS
mit_manufacturing_evidence       PASS
current_sale_or_supply           PASS
exact_official_product_page      PASS
key_conflict_review              PASS · no conflict found
image_rights                     BLOCKED
editorial_review                 PENDING
formal_publication               BLOCKED
publication_status               unpublished
```

官方品牌：
`https://www.chimei.com.tw/brand-story`

官方 exact-model：
`https://www.chimei.com.tw/dish-dryer/ultraviolet%20%20rays/kd-884hp0`

MIT exact model：
`https://keid.nat.gov.tw/mittw/products/prod_more?id=287272`

官方 exact-model 頁明列 `製造產地：台灣`。MIT `02000038-02030` 有效至 2029-06-01。證據只適用 KD-884HP0。

圖片仍未有第三方重用授權，因此 candidate 保持 `blocked_assets`。

## Enrichment Results 架構

```text
data/enrichment.results.manifest.json
├─ data/enrichment.results.v1.json (10)
└─ data/enrichment.results.v2.json (1)
```

Builder 依 Manifest 合併；未來新增 P2 batch 不需要重寫大型歷史檔。

## 資料治理

- 台灣品牌 ≠ 台灣製造。
- MIT 製造證據不得推定品牌國籍或現售。
- 有效 MIT ≠ 即時在售。
- 銷售通路 ≠ 即時庫存。
- exact official product page 必須是品牌／公司官方精確型號頁。
- 同系列頁與第三方零售頁不可冒充 exact-model official page。
- 公開可見圖片 ≠ 已取得重用授權。
- Deep candidate ≠ deep editorial case ≠ formal publication。
- verified enrichment 只能由受控 builder 反映到 public catalog；不得改 raw Registry 的 manufacturing evidence / verification / publication。
- Formal Publication Gate 不降低，published 維持 0。

## 重要檔案

```text
PROJECT_STATUS.md
README.md
build-info.json

data/enrichment.queue.json
data/enrichment.results.manifest.json
data/enrichment.results.v1.json
data/enrichment.results.v2.json
data/deep_case.candidates.json

assets/enrichment-v3-4.js
assets/enrichment-v3-4.css
assets/deep-candidates-v3-5.js
assets/deep-candidates-v3-5.css

scripts/build_public_catalog.py
scripts/validate_enrichment_v3_4.py
scripts/validate_deep_candidates_v3_5.py
scripts/validate_site.py

.github/workflows/validate.yml
.github/workflows/pages.yml

docs/research/2026-08-13_chimei_kd884hp0_deep_candidate.md
```

## 已知風險／待處理

- V3.5 最終 production build/deploy 尚需以 `docs/deployment/pages-production-result.json` 驗收。
- KD-884HP0 圖片權利 blocked；不可直接下載官網產品圖。
- KD-884HP0 editorial review 尚未完成；不可加入正式 deep cases 或 published。
- P2 尚有 9 records / 36 tasks。
- Panasonic P2 型號雖有台灣 MIT 製造證據，但 Panasonic 品牌國籍必須另外查，不能標成台灣品牌。

## 禁止事項

- 不得把 KD-884HP0 的台灣產地證據外推到其他奇美型號。
- 不得因 candidate Gate 多數 PASS 就直接 published。
- 不得把 `blocked` 圖片改為可用，除非真的取得授權或合法替代素材。
- 不得把 MIT 有效等同現售。
- 不得重做或降低 V2.3 Publication Gate、V2.5 Recovery、V2.8 Media、V3.2 Lifecycle、V3.3 Scale 100。

## 明確下一步

1. 先驗收 V3.5 production build/deploy。
2. 進 P2 enrichment，優先：
   - 奇美 KD-703HP1
   - Panasonic NR-C507XVS
   - Panasonic NR-D507XVS
   - Panasonic NR-C617XVS
3. Panasonic brand_identity 必須查官方品牌起源，預期可能為非台灣品牌，但未查證前不要先寫結論。
4. 另外建立 KD-884HP0 圖片授權／合法替代素材工作流；權利未解決前保持 blocked candidate。
5. Formal published 維持 0。

## 新對話可直接使用的接續指令

繼續台產報 `qookey109-pixel/Taichanbao`。先讀 GitHub main 的 `PROJECT_STATUS.md`、`README.md` 與 `docs/handoffs/taichanbao_handoff_2026-08-13_v3_5_deep_candidate_gate.md`。不要重做 V3.5。先以 `docs/deployment/pages-production-result.json` 驗收 V3.5 production；成功後進 P2 enrichment，優先 KD-703HP1 與三筆 Panasonic 冰箱。KD-884HP0 目前只是 blocked deep candidate，圖片權利與 editorial review 未完成，不得加入正式 deep cases 或 published。Formal Publication Gate 維持 0 published。
