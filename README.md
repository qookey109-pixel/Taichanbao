# 台產報（Taichanbao）V3.0 Evidence Catalog

台產報是一個以「雜誌選品＋精確型號證據資料庫」呈現台灣品牌與台灣製產品研究的網站。V3.0 開始把品牌身分、精確型號、製造證據、圖片權利與正式發布狀態拆開管理，不再用單一「台灣製」標籤概括所有資訊。

## 線上位置

- Repository：`qookey109-pixel/Taichanbao`
- 正式網站：`https://qookey109-pixel.github.io/Taichanbao/`
- V2.5 Recovery 預覽：`https://qookey109-pixel.github.io/Taichanbao/versions_review/v2.5/`
- Default branch：`main`

## V3.0 資料快照

```text
真實研究候選：19
├─ 深度多圖案例：4
│  ├─ TENDAYS
│  ├─ SAMPO
│  ├─ 大同
│  └─ O'right
└─ MIT 有效精確型號：15

隔離介面示範資料：6
正式發布：0
```

15 筆 Registry 來源均為經濟部產業發展署 MIT 微笑標章官方查詢，並保存精確型號、標章編號、通過日期、有效期限、申請公司、來源 URL 與查閱日期。Registry 記錄全部維持 `unpublished`，不因政府標章存在就自動通過台產報正式發布 Gate。

## V3.0 首頁

正式首頁保留既有雜誌型視覺，新增：

- 「產品證據資料庫」主區塊。
- 真實研究候選／MIT 精確型號／深度案例／正式發布／示範資料五個即時指標。
- A–D 證據分級。
- 來源、證據等級、分類、品牌身分與排序篩選。
- 全站搜尋支援品牌、產品、型號、標章編號與標籤。
- 點擊資料卡可查看標章編號、有效期限、公司、證據範圍與官方來源。
- O'right 多圖案例可見「精確型號」與「同系列」標籤，避免同系列圖片冒充精確型號證據。
- MIT 標章只以文字記錄，不複製標章圖樣。

## 證據分級

```text
A  政府有效標章／可發布級證據來源
B  精確型號官方來源一致
C  精確型號部分官方證據
D  官方宣稱、資料不足或仍待交叉查證
```

證據等級描述「目前掌握的製造／產地證據強度」，不是品牌好壞或產品品質評分。

## 核心資料層

```text
data/products.demo.json            # 既有 6 demo + 4 深度案例相容資料
data/products.registry.json        # V3 MIT 精確型號 Registry（15）
data/product.media.overrides.json  # SAMPO／大同／O'right 深度媒體與外部證據

data/image_rights.json
data/image_rights.sampo.json
data/image_rights.tatung.json
data/image_rights.oright.json
```

V3 前端會把 `products.demo.json` 中的 4 筆非 demo 深度案例與 `products.registry.json` 的 15 筆政府 Registry 合併成 19 筆「真實研究候選」。6 筆 `demo_only` 只保留為介面測試資料，不進入 V3 證據資料庫。

## 核心前端

```text
index.html
assets/magazine.css
assets/magazine.js
assets/product-images.css
assets/product-image-enhancements.js
assets/catalog-v3.css
assets/catalog-v3.js
```

## 驗證

```bash
python scripts/validate_data.py
python scripts/validate_registry.py
python scripts/validate_v3_catalog.py
python scripts/validate_media_rights.py
python scripts/validate_sampo_media.py
python scripts/validate_tatung_media.py
python scripts/validate_oright_media.py
python scripts/validate_site.py
node --check assets/magazine.js
node --check assets/product-image-enhancements.js
node --check assets/catalog-v3.js
node --check assets/app.js
```

GitHub Actions 與 Pages deployment 都會執行上述 V3 Registry／跨資料集／媒體與網站檢查。

## 資料治理

- 台灣品牌 ≠ 台灣製造。
- 有臺灣製造證據 ≠ 自動證明品牌是台灣品牌。
- 以單一產品與精確型號為查證單位。
- 政府標章只套用到實際列出的型號，不能外推同品牌其他商品。
- 精確型號圖片與同系列圖片必須分開記錄。
- 台灣原料不等於成品在台灣製造。
- 圖片來源與圖片使用權是兩件事；`permission_pending` 不代表已授權。
- `demo_only`、`official_source_found`、`government_registry_verified` 都不會自動變成 `published`。
- 搜尋、排序、收藏、圖片與 metadata 只能改變前台呈現，不能升級查證狀態。
- 未知維持待確認，衝突不得隱藏。

## Formal Publication Gate

V3.0 正式發布仍為 0。第一筆正式發布必須至少完成：精確型號識別、現售狀態、可公開產地／製造證據、重大衝突審核、圖片使用權處理與編輯審核。
