# 台產報 PROJECT STATUS

更新日期：2026-08-13

## Version

`V3.8 Candidate Promotion Review`

## 正式網站方向

台產報維持「雜誌選品＋精確型號證據資料庫」架構。V3.8 完成第一輪候選升級審核：`KD-884HP0` 與 `KD-703HP1` 均已正式登錄為 Deep Candidate，但 Candidate editorial review、圖片權利、Publication editorial review 與 Formal Publication 仍分開管理。

## V3.8 本次完成

- V3.7 Enrichment 20/20、V3.6 Brand-Origin Separation、V3.5 Deep Candidate Gate、V3.3 Registry Scale 100、V3.2 Lifecycle 全部保留。
- `KD-884HP0` 保留為 Deep Candidate；`KD-703HP1` 已由 `eligible_for_deep_candidate_review` 人工升級為第二筆正式 Deep Candidate。
- Deep Candidate 總數由 1 → **2**。
- 兩筆 candidate editorial review 均 PASS。
- 兩筆 image rights 均 BLOCKED。
- 兩筆 publication editorial review 均 PENDING。
- 兩筆 formal publication 均 BLOCKED / unpublished。
- CHIMEI 官方使用條款已重新確認：網站影像、攝影、圖片等未經授權不得重製、改作、散佈或公開傳輸。
- 新增 `data/media-rights.requests.json`，兩筆授權請求皆為：`permission_required / ready_to_contact / request_sent=false`。
- 新增 `docs/media-rights/chimei_kd884_kd703_permission_request.md`，保存可直接寄給 CHIMEI 的授權申請草稿。
- 官方聯絡頁列客服信箱 `lcd@mail.chimei.com.tw`；目前未擅自寄信。
- `scripts/validate_deep_candidates_v3_5.py` 已升級，交叉驗證兩筆 Registry、Enrichment、MIT 有效期、Candidate Gate 與 Media Rights Request 狀態。
- `scripts/build_promotion_audit.py` / `scripts/validate_promotion_audit_v3_7.py` 已升級：現在 `registered_deep_candidates=2`、`eligible_unregistered_deep_candidates=0`。
- `assets/deep-candidates-v3-5.js` 與 `assets/promotion-audit-v3-7.js` 前台已升級顯示 V3.8 雙候選狀態。
- `assets/catalog-v3.js` 最終 loader marker 已升級為 `V3.8 Candidate Promotion Review`。
- `scripts/validate_site.py`、Pages workflow、README、`build-info.json` 已同步 V3.8。

## 目前資料狀態

```text
真實研究候選：104
MIT exact models：100
既有 Deep editorial cases：4
Deep Candidates：2
├─ KD-884HP0 → blocked_assets
└─ KD-703HP1 → blocked_assets
Formal published：0

Candidate editorial review PASS：2
Image rights BLOCKED：2
Publication editorial review PENDING：2

Media-rights requests：2
├─ ready_to_contact：2
└─ request_sent：0
```

Enrichment 20/20 基線仍維持：

```text
verified tasks：22
not_found：51
blocked：7
pending：0

Taiwan-brand confirmed：8
Non-Taiwan-brand confirmed：3
Brand-origin unresolved：9
Current-sale/supply confirmed：9
Exact official product pages：2
```

## KD-884HP0 / KD-703HP1 Candidate Gate

兩筆目前都必須維持：

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

重要：candidate editorial review PASS 只表示值得做深度專題，不表示可以正式發布。

## 圖片權利工作流

```text
data/media-rights.requests.json
├─ CHIMEI KD-884HP0 → ready_to_contact / unsent
└─ CHIMEI KD-703HP1 → ready_to_contact / unsent
```

授權申請草稿：

```text
docs/media-rights/chimei_kd884_kd703_permission_request.md
```

申請範圍包含：台產報產品頁使用、響應式縮放／必要裁切、來源標示、非專屬且不可轉授權。

在取得 CHIMEI 書面授權或合法替代素材以前：

- 不下載官方產品圖片進 repository。
- 不把官方圖片標為 `permission_granted`。
- 不解除 `image_rights: blocked`。
- 不進 Formal Publication。

## Promotion Audit

```text
Deep Candidate／資產阻擋：2
├─ KD-884HP0 → registered_deep_candidate
└─ KD-703HP1 → registered_deep_candidate

台灣品牌 research-only：6
非台灣品牌＋台灣製 exact-model：3
品牌身分待確認 research-only：9
Formal published：0
```

Promotion Audit 仍只分類下一步，不會自動發布。

## Panasonic Regression 永久保留

```text
Panasonic brand_origin_status = non_taiwan_brand
NR-C507XVS manufacturing_evidence_status = mit_certified_active
NR-D507XVS manufacturing_evidence_status = mit_certified_active
NR-C617XVS manufacturing_evidence_status = mit_certified_active
```

不得因 MIT 台灣製造證據把 Panasonic 改成台灣品牌，也不得因 Panasonic 是日本品牌否定這三個 exact models 的台灣製造證據。

## 核心檔案

```text
data/deep_case.candidates.json
data/media-rights.requests.json
docs/media-rights/chimei_kd884_kd703_permission_request.md

assets/catalog-v3.js
assets/deep-candidates-v3-5.js
assets/promotion-audit-v3-7.js

scripts/validate_deep_candidates_v3_5.py
scripts/build_promotion_audit.py
scripts/validate_promotion_audit_v3_7.py
scripts/validate_site.py

.github/workflows/validate.yml
.github/workflows/pages.yml
build-info.json
README.md
PROJECT_STATUS.md
```

Enrichment / Registry / Lifecycle / Brand-Origin / Media / V2.5 Recovery 基線均保留，不得重做或降低標準。

## 尚未完成

- 驗收 V3.8 final production build／deploy。
- 兩筆 CHIMEI 圖片授權尚未實際送出，`request_sent=false`。
- 未取得書面圖片授權或合法替代素材。
- Publication editorial review 尚未執行。
- 第一筆 formal published 仍為 0。

## 下一步

1. 驗收 V3.8 final production。
2. 若使用者願意，由使用者或經明確指示後送出 CHIMEI 圖片授權申請；在此之前保持 `ready_to_contact`。
3. 取得授權後，先保存授權範圍／期限／署名條件，再更新 media rights 狀態與圖片素材。
4. 最後才執行 Publication editorial review；只有所有 Formal Publication Gate 通過後才可產生第一筆 published。
