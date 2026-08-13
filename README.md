# 台產報（Taichanbao）V3.1 Registry Scale 50

台產報是一個以「雜誌選品＋精確型號證據資料庫」呈現台灣品牌與台灣製產品研究的網站。V3.1 把 Registry 從單一 JSON 擴張成可分片的資料層，讓資料庫能持續從 50 筆向 100、500 筆擴充，同時維持精確型號、證據範圍與正式發布 Gate。

## 線上位置

- Repository：`qookey109-pixel/Taichanbao`
- 正式網站：`https://qookey109-pixel.github.io/Taichanbao/`
- V2.5 Recovery 預覽：`https://qookey109-pixel.github.io/Taichanbao/versions_review/v2.5/`
- Default branch：`main`

## V3.1 資料快照

```text
真實研究候選：54
├─ 深度多圖案例：4
│  ├─ TENDAYS
│  ├─ SAMPO
│  ├─ 大同
│  └─ O'right
└─ MIT 有效精確型號：50
   ├─ Seed shard：15
   └─ Appliance shard：35

隔離介面示範資料：6
正式發布：0
Registry shards：2
```

## V3.1 家電擴充

新增 35 筆經濟部產業發展署 MIT 微笑標章有效家電精確型號，主要涵蓋：

- Panasonic 冰箱與冷氣
- 奇美烘碗機／家電
- 東元捕蚊燈
- ALASKA 浴室通風扇
- ESUN 空氣淨化機
- 冰點分離式冷氣

官方來源集中在 MIT 家電查詢第 2、4、5 頁；每筆保存精確型號、公司、品牌欄位、標章編號、通過日期、有效期限、來源 URL 與最後查閱日期。

## Sharded Registry

V3.1 不再假設 MIT Registry 只能是一個檔案：

```text
data/registry.manifest.json
├─ data/products.registry.json              # 15 筆 seed
└─ data/products.registry.appliances.json   # 35 筆家電擴充
```

前端 `assets/catalog-v3-1.js` 會先讀 manifest，再並行載入所有 shard。`assets/catalog-v3.js` 保留為穩定 loader，因此既有首頁引用不需要破壞性更動。

## 證據資料庫功能

- A–D 證據分級。
- 來源、證據等級、分類、品牌身分與排序篩選。
- 搜尋品牌、公司、產品、型號、標章編號與標籤。
- Registry 卡片顯示標章編號與有效期限。
- 點擊後可查看精確型號、申請公司、品牌身分、來源、證據範圍與最後查閱日期。
- O'right 圖片明確區分「精確型號」與「同系列補充」。
- MIT 標章只保存文字型證據，不直接複製標章圖樣。

## 證據分級

```text
A  政府有效標章／可發布級證據來源
B  精確型號官方來源一致
C  精確型號部分官方證據
D  官方宣稱、資料不足或仍待交叉查證
```

等級描述證據強度，不是產品品質排名，也不代表已正式發布。

## 核心資料層

```text
data/products.demo.json
data/products.registry.json
data/products.registry.appliances.json
data/registry.manifest.json
data/product.media.overrides.json

data/image_rights.json
data/image_rights.sampo.json
data/image_rights.tatung.json
data/image_rights.oright.json
```

## 核心前端

```text
index.html
assets/magazine.css
assets/magazine.js
assets/product-images.css
assets/product-image-enhancements.js
assets/catalog-v3.css
assets/catalog-v3.js        # stable loader
assets/catalog-v3-1.js      # V3.1 sharded catalog implementation
```

## 驗證與維護

```bash
python scripts/validate_data.py
python scripts/validate_registry.py
python scripts/validate_registry_scale.py
python scripts/validate_v3_catalog.py
python scripts/validate_v3_1_catalog.py
python scripts/validate_media_rights.py
python scripts/validate_sampo_media.py
python scripts/validate_tatung_media.py
python scripts/validate_oright_media.py
python scripts/validate_site.py
python scripts/report_registry_expiry.py

node --check assets/magazine.js
node --check assets/product-image-enhancements.js
node --check assets/catalog-v3.js
node --check assets/catalog-v3-1.js
node --check assets/app.js
```

`validate_registry_scale.py` 會跨 shard 檢查 50 筆 Registry 的 ID、MIT 標章編號、官方來源與有效期限。`validate_v3_1_catalog.py` 會強制完整 catalog 必須是 54 筆真實研究候選、6 筆 Demo 隔離、正式發布 0。

`report_registry_expiry.py` 可輸出 30／90／180／365 天內即將到期的 MIT 紀錄，供後續重驗。

## 批次匯入

`scripts/import_registry_batch.py` 提供受控批次匯入：預設 dry-run，只有 `--write` 才寫入。匯入器必須阻擋錯誤官方來源、標章編號碰撞與 `published` 注入。

## 資料治理

- 台灣品牌 ≠ 台灣製造。
- 有臺灣製造證據 ≠ 自動證明品牌是台灣品牌。
- 以單一產品與精確型號為查證單位。
- MIT 標章只套用到 Registry 實際列出的型號，不能外推同品牌其他商品。
- `brand_origin_status: unverified` 必須保留，不能因 MIT 標章存在就自動改成台灣品牌。
- 精確型號圖片與同系列圖片必須分開記錄。
- 台灣原料不等於成品在台灣製造。
- 圖片來源與圖片使用權是兩件事；`permission_pending` 不代表已授權。
- `demo_only`、`official_source_found`、`government_registry_verified` 都不會自動變成 `published`。
- 搜尋、排序、收藏、圖片與 metadata 只能改變前台呈現，不能升級查證狀態。
- 未知維持待確認，衝突不得隱藏。

## Formal Publication Gate

V3.1 正式發布仍為 0。第一筆正式發布仍必須完成：精確型號識別、現售狀態、可公開產地／製造證據、重大衝突審核、圖片使用權處理與編輯審核。
