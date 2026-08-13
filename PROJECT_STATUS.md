# 台產報 PROJECT STATUS

更新日期：2026-08-13

## Version

`V3.0 Evidence Catalog`

## 正式網站方向

雜誌型介面仍是正式首頁基準，但 V3.0 從「四個品牌圖片案例」擴張成「雜誌選品＋精確型號證據資料庫」。品牌身分、產品型號、製造地、政府標章、圖片權利與正式發布狀態分開管理。

## V3.0 本次大更新

- 正式首頁重構為 `V3.0 Evidence Catalog`。
- 保留原本雜誌式封面、三欄布局、收藏、搜尋、場景、排序與 Formal Publication Gate。
- 新增正式導覽「證據資料庫」。
- 新增 `data/products.registry.json`，第一批收錄 15 筆經濟部 MIT 微笑標章有效精確型號。
- 保留 4 筆深度多圖案例：TENDAYS、SAMPO、大同、O'right。
- V3 真實研究候選共 19 筆：4 深度案例＋15 MIT Registry。
- 6 筆 `demo_only` 仍隔離為介面測試資料，不進入 V3 證據資料庫。
- 新增 A–D 證據等級。
- 新增來源、證據等級、產品分類、品牌身分、排序篩選。
- 全站搜尋可搜尋品牌、公司、產品、型號、標章編號、分類與標籤。
- Registry 卡片可查看標章編號、有效期限、申請公司、來源、查閱日期與證據範圍。
- 新增 O'right 前台「精確型號／同系列補充」圖片標籤。
- MIT 標章只以文字記錄，不複製標章圖樣。
- 新增 `scripts/validate_registry.py` 與 `scripts/validate_v3_catalog.py`。
- CI 與 GitHub Pages deployment 都新增 V3 Registry、跨資料集與 V3 JavaScript 驗證。
- V2.5 Recovery 預覽與既有 SQLite／匯入治理成果保留。
- 正式發布仍維持 0。

## V3.0 資料狀態

```text
真實研究候選：19
├─ 深度多圖案例：4
│  ├─ TENDAYS
│  ├─ SAMPO
│  ├─ 大同
│  └─ O'right
└─ MIT 有效精確型號：15

隔離示範資料：6
正式發布：0
```

## 證據分級

```text
A：政府有效標章／可發布級證據來源
B：精確型號官方來源一致
C：精確型號部分官方證據
D：官方宣稱、資料不足或待交叉查證
```

分級是「證據強度」，不是品牌或產品品質排名。

## 第一批 MIT Registry 範圍

涵蓋服飾配件、鞋履、眼鏡、居家織品、寢具與家電。每筆都保存：

- 精確型號
- 產品名稱
- 申請公司
- 品牌欄位或品牌待確認
- MIT 標章編號
- 通過日期
- 有效期限
- 官方政府來源 URL
- 最後查閱日期

其中包含 TENDAYs 保潔墊、日象電鍋、尚朋堂不鏽鋼電鍋、Panasonic 冰箱等型號，但任何 MIT 記錄都只套用到其精確型號，不得外推同品牌其他產品。

## 核心檔案

```text
index.html
assets/catalog-v3.css
assets/catalog-v3.js
assets/magazine.css
assets/magazine.js
assets/product-images.css
assets/product-image-enhancements.js

data/products.demo.json
data/products.registry.json
data/product.media.overrides.json

scripts/validate_data.py
scripts/validate_registry.py
scripts/validate_v3_catalog.py
scripts/validate_media_rights.py
scripts/validate_sampo_media.py
scripts/validate_tatung_media.py
scripts/validate_oright_media.py
scripts/validate_site.py
```

## 資料治理

- 台灣品牌不等於台灣製造。
- 臺灣製造證據不等於品牌國籍證據。
- 所有產地／製造證據以精確型號為最小單位。
- MIT 標章不得外推到同品牌其他型號。
- 政府 Registry 存在不代表已完成現售狀態、圖片權利與台產報編輯審核。
- 精確型號圖片與同系列補充圖片必須區分。
- 台灣原料不得表述成成品台灣製造。
- `permission_pending` 不代表取得圖片使用授權。
- 前台搜尋、排序、收藏、圖片、分級顯示都不得修改資料查證或發布狀態。
- 未知維持待確認，衝突不得隱藏。

## 已知限制與風險

- 15 筆 Registry 是 V3 第一批種子資料，不是 MIT 產品完整鏡像。
- 部分 MIT Registry 記錄的品牌名稱仍需另行核對；公司與產品獲證資訊不能自動等同品牌國籍。
- 四個深度案例的官方圖片仍有 `permission_pending`。
- 尚未取得 TENDAYS、SAMPO、大同、O'right 完整實體標示照片。
- 原先遺失的 20 筆候選與完整研究證據尚未取回，不得自行重建成「原資料」。
- SQLite 到公開 JSON 的正式受控發布 pipeline 尚未完成。

## 不可覆蓋

- 使用者選定的雜誌型正式首頁方向。
- V2.3 Formal Publication Gate。
- V2.5 Recovery Baseline 預覽。
- V2.8 Complete Media Architecture。
- V2.9 TENDAYS、V2.10 SAMPO、V2.11 大同、V2.11.1 O'right 案例。
- 既有 SQLite 與資料匯入治理成果。
- V3.0 的精確型號優先與品牌／製造證據分離原則。

## 下一步

1. 把 Registry 從 15 筆擴大到至少 50 筆，增加家電、食品接觸用品、居家用品等類別。
2. 建立 Registry 的受控匯入／更新工具，不再手工維護大量 JSON。
3. 為政府 Registry 加入 `last_verified_at` 與過期／即將到期自動檢查。
4. 取得一筆圖片權利與實體證據完整的產品，跑第一筆 Formal Publication Gate。
5. 完成 SQLite → 公開 Catalog JSON 的發布 pipeline。
