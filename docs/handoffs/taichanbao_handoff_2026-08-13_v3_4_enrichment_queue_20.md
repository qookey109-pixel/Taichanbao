# 台產報 Handoff — V3.4 Enrichment Queue 20

日期：2026-08-13

## 專案名稱
台產報 / Taichanbao

## Repository
`qookey109-pixel/Taichanbao`

## 目前狀態

```text
Version: V3.4 Enrichment Queue 20
Real research candidates: 104
MIT active exact models: 100
Deep editorial cases: 4
Registry shards: 3
Enrichment queue: 20
Enrichment task types: 4
Verified enrichment tasks: 0
Formal published: 0
```

## 本次已完成

- 確認 V3.3 已在 main 完成 Registry 50 → 100，不重做。
- 驗收 V3.3 production build/deploy success。
- 新增 `data/enrichment.queue.json`，20 筆優先深化查證候選。
- 每筆四個任務：品牌身分、現售、官方產品頁、圖片權利。
- 新增 `scripts/validate_enrichment_v3_4.py`。
- 新增 `assets/enrichment-v3-4.js` 與 `assets/enrichment-v3-4.css`。
- `assets/catalog-v3.js` 已載入 enrichment workbench。
- CI / Pages workflow 已加入 V3.4 enrichment validator 與 Node syntax Gate。
- `scripts/validate_site.py` 升級到 V3.4。
- `build-info.json` 與 `PROJECT_STATUS.md` 升級到 V3.4。

## Queue 治理

- Queue 只安排研究工作，不改 verification/publication。
- `brand_identity` 與 MIT 製造證據分離。
- `current_sale` 必須是精確型號現售證據。
- `official_product_page` 同系列頁不能冒充精確型號頁。
- `image_rights` 未取得明確授權時保持 pending/blocked。
- 任務 verified 不代表正式發布。

## 重要檔案

```text
PROJECT_STATUS.md
build-info.json
data/enrichment.queue.json
assets/enrichment-v3-4.js
assets/enrichment-v3-4.css
assets/catalog-v3.js
scripts/validate_enrichment_v3_4.py
scripts/validate_site.py
.github/workflows/validate.yml
.github/workflows/pages.yml
```

## 已知風險

- 20 筆 Queue 初始任務全部 pending，尚未開始逐筆外部查核。
- Panasonic 等可能有台灣製精確型號，但品牌身分不應因 MIT 證據被視為台灣品牌。
- 圖片存在不代表可合法再利用。
- Registry 有效不代表目前現售。

## 禁止執行事項

- 不得把 enrichment progress 自動映射成 publication status。
- 不得因公司名稱／MIT 標章自行判斷台灣品牌。
- 不得把同系列產品頁當成精確型號產品頁。
- 不得下載／重製未獲授權的官方產品圖片到 repo。
- 不得降低 Formal Publication Gate。

## 明確下一步

1. 驗收 V3.4 production build/deploy。
2. 從 P1 Queue 開始逐筆查核。
3. 第一批至少完成 5 筆的 `brand_identity`、`current_sale`、`official_product_page`。
4. `image_rights` 若無授權證據維持 pending/blocked。
5. 再決定哪些產品值得升級成新的 deep editorial case。

## 新對話可直接使用的接續指令

繼續台產報 `qookey109-pixel/Taichanbao`。以 GitHub main 最新內容、`PROJECT_STATUS.md` 與 `docs/handoffs/taichanbao_handoff_2026-08-13_v3_4_enrichment_queue_20.md` 為基準。不要重做 V3.3 Scale 100 或 V3.4 Queue。先驗收 V3.4 Pages production result，然後直接處理 P1 enrichment queue，優先完成至少 5 筆品牌身分、現售與精確型號官方產品頁查核；圖片權利無明確授權就維持 pending/blocked。Formal Publication Gate 不降低，正式發布維持 0。
