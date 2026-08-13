# MIT Appliance Registry Expansion — V3.1 Scale 50

日期：2026-08-13

## 目標

把 V3.0 的 15 筆 MIT seed Registry 擴充到 50 筆，同時維持精確型號、官方來源、有效期限與 unpublished 治理。

## 本批新增

新增 35 筆家電精確型號，全部來自經濟部產業發展署臺灣製產品 MIT 微笑標章官方家電查詢。

來源頁：

- https://keid.nat.gov.tw/mittw/products/?classid=10&p=2
- https://keid.nat.gov.tw/mittw/products/?classid=10&p=4
- https://keid.nat.gov.tw/mittw/products/?classid=10&p=5

## 產品組成

### Page 2

- Panasonic 電冰箱：NR-C507XVS、NR-D507XVS、NR-C507XGS、NR-D507XGS、NR-C617XVS、NR-D617XVS、NR-C617XGS、NR-D617XGS
- 奇美／奇美家電：KD-703HP1、KD-884HP0(白)、KD-853HM0(白)
- Panasonic 窗型變頻冷氣：CW-U68LCA2

### Page 4

- Panasonic 室內機：CS-UK28BA2、CS-UK22BA2
- 東元銀離子抑菌捕蚊燈：XYFYK106(無)
- ALASKA 浴室通風扇：768ADH(營業型)、768ADH、768AD(營業型)、768AD
- ESUN 空氣淨化機：E-SUN LM515E2F-CK、E-SUN LM435E2F-UV72、E-SUN LM515E2B-CK、E-SUN LM435E2B-UV72、E-SUN LM515E2H-CK

### Page 5

- 冰點分離式冷氣：BEC120SGU2、BEC120SGI2、BEC101SGU2、BEC101SGI2、BEC80SGU2、BEC80SGI2、BEC73SGU2、BEC73SGI2、BEH63SGU2、BEH63SGI2、BEH52SGU2

## 治理判斷

每筆新增資料：

```text
record_origin: mit_registry
verification_status: government_registry_verified
manufacturing_evidence_status: mit_certified_active
evidence_level: A
record_scope: exact_model
publication_status: unpublished
brand_origin_status: unverified
```

MIT 有效標章證據只適用 Registry 列出的精確型號。即使申請公司名稱包含「台灣」或品牌在台灣市場常見，也不能因此自動把品牌國籍改成台灣品牌。

## 架構改動

V3.1 開始使用 Registry shards：

```text
data/registry.manifest.json
├─ data/products.registry.json              15
└─ data/products.registry.appliances.json   35
```

總計：50 MIT exact-model records。

前端透過 manifest 載入所有 shard；跨 shard validator 負責阻擋 ID 或 MIT 標章編號碰撞。

## 後續

下一批擴充不應繼續大量加入家電，而應優先補餐廚、居家用品、清潔用品與其他生活類別，降低單一產業集中度。
