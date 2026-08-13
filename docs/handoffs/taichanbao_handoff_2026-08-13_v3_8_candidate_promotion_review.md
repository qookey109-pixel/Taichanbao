# 台產報 Handoff — V3.8 Candidate Promotion Review

日期：2026-08-13

## 專案名稱
台產報 / Taichanbao

## Repository
`qookey109-pixel/Taichanbao`

## 目前狀態

```text
Version: V3.8 Candidate Promotion Review
Real research candidates: 104
MIT active exact models: 100
Existing deep editorial cases: 4
Registered Deep Candidates: 2
Candidate editorial review PASS: 2
Image-rights BLOCKED: 2
Publication editorial review PENDING: 2
Media-rights requests ready_to_contact: 2
Media-rights requests sent: 0
Formal published: 0
```

## 本次已完成

- 不重做 V3.7 Enrichment Complete 20/20、V3.6 Brand-Origin Separation、V3.5 Candidate Gate、V3.3 Registry Scale 100、V3.2 Lifecycle。
- 重新查核 CHIMEI `KD-884HP0` / `KD-703HP1` 官方產品線、品牌故事、MIT exact-model 與網站使用條款。
- `KD-703HP1` 由 V3.7 的 `eligible_for_deep_candidate_review` 人工升級為第二筆正式 Deep Candidate。
- `KD-884HP0` / `KD-703HP1` 的 candidate editorial review 均 PASS。
- 兩筆圖片權利均維持 BLOCKED；CHIMEI 使用條款明確要求影像／圖片重用須取得授權。
- 兩筆 publication editorial review 維持 PENDING；formal publication BLOCKED / unpublished。
- 新增 `data/media-rights.requests.json`：兩筆均 `permission_required / ready_to_contact / request_sent=false`。
- 新增 `docs/media-rights/chimei_kd884_kd703_permission_request.md`：已準備 CHIMEI 圖片授權申請草稿，但沒有擅自寄出。
- 官方聯絡信箱：`lcd@mail.chimei.com.tw`（來源：CHIMEI 官方聯絡頁）。
- `scripts/validate_deep_candidates_v3_5.py` 已升級為 V3.8 雙候選＋授權追蹤 Gate。
- `scripts/build_promotion_audit.py` / `scripts/validate_promotion_audit_v3_7.py` 已改為 `registered_deep_candidates=2`、`eligible_unregistered=0`。
- `assets/deep-candidates-v3-5.js` / `assets/promotion-audit-v3-7.js` / `assets/catalog-v3.js` 已顯示 V3.8。
- `build-info.json` / `scripts/validate_site.py` / Pages workflow / README / PROJECT_STATUS 已同步 V3.8。

## 兩筆 Candidate Gate

```text
brand_identity                  PASS
exact_model_identity            PASS
mit_manufacturing_evidence      PASS
current_sale_or_supply          PASS
exact_official_product_page     PASS
key_conflict_review             PASS · no conflict found
candidate_editorial_review      PASS
image_rights                    BLOCKED
publication_editorial_review    PENDING
formal_publication              BLOCKED
publication_status              unpublished
```

## 圖片授權狀態

`data/media-rights.requests.json`

```text
KD-884HP0  permission_required / ready_to_contact / request_sent=false
KD-703HP1  permission_required / ready_to_contact / request_sent=false
```

未取得 CHIMEI 書面同意前：
- 不下載官方圖片進 repo。
- 不標 `permission_granted`。
- 不解除 image-rights blocker。
- 不執行正式發布。

## 重要來源

- CHIMEI 品牌故事：`https://www.chimei.com.tw/brand-story`
- CHIMEI 使用條款：`https://www.chimei.com.tw/conditions`
- CHIMEI 聯絡頁：`https://www.chimei.com.tw/contact`
- KD-884HP0：`https://electronics.chimei.com.tw/dish-dryer/ultraviolet%20%20rays/kd-884hp0`
- KD-703HP1：`https://www.chimei.com.tw/dish-dryer/ultraviolet%20%20rays/kd-703hp1`
- MIT KD-884HP0：`https://keid.nat.gov.tw/mittw/products/prod_more?id=287272`
- MIT KD-703HP1：`https://keid.nat.gov.tw/mittw/products/prod_more?id=287273`

## 尚未完成

- V3.8 final production build/deploy 驗收。
- CHIMEI 圖片授權信尚未寄出。
- 尚未取得圖片書面授權或合法替代素材。
- Publication editorial review 尚未執行。
- Formal published 仍為 0。

## 禁止執行事項

- 不把 candidate editorial review PASS 解讀為正式發布通過。
- 不因官方圖片可公開瀏覽就下載／重製。
- 不改弱 Formal Publication Gate。
- 不重做 Enrichment 20/20、Registry 100、Panasonic brand-origin regression。
- 不把 MIT exact-model 製造證據外推到其他型號。

## 明確下一步

1. 先驗收 V3.8 final production。
2. 若使用者明確要送出授權申請，再使用既有草稿聯絡 CHIMEI；未明確指示前保持 `request_sent=false`。
3. 若取得授權，保存授權範圍、期限、署名與裁切／縮圖條件，再更新 media-rights 狀態。
4. 圖片 Gate 通過後才進 Publication editorial review。
5. 只有完整通過 Formal Publication Gate 才能產生第一筆 published。

## 新對話可直接使用的接續指令

繼續台產報 `qookey109-pixel/Taichanbao`。以 GitHub main、`PROJECT_STATUS.md` 與 V3.8 Handoff 為準。KD-884HP0、KD-703HP1 已是兩筆 blocked Deep Candidates，candidate editorial review 均 PASS，但 image rights BLOCKED、publication editorial review PENDING、published=0。先核對最新 Pages production；不要重做 Enrichment/Registry。若要處理圖片，優先使用 `data/media-rights.requests.json` 與 `docs/media-rights/chimei_kd884_kd703_permission_request.md`，未取得使用者明確指示不得將 request_sent 改成 true，也不得假設 CHIMEI 已授權。
