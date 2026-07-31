# PROJECT STATUS

更新日期：2026-07-31

## Version

`Magazine Homepage Official + V2.5 Recovery Preview`

## 目前正式網站

正式首頁採用使用者偏好的雜誌型選品誌介面：

- 橘色跑馬燈
- 左側導覽、中央專題、右側資訊欄
- 「今日台產」封面主題
- 產品專題、品牌索引、本月台產榜
- 搜尋、分類與產品履歷 Drawer
- 手機版底部導覽

正式網址：

```text
https://qookey109-pixel.github.io/Taichanbao/
```

## V2.5 預覽

V2.5 Recovery Baseline 沒有刪除，保存在：

```text
versions_review/v2.5/index.html
```

預覽網址：

```text
https://qookey109-pixel.github.io/Taichanbao/versions_review/v2.5/
```

V2.5 預覽包含：

- 研究預覽／正式發布雙檢視
- Formal Publication Gate
- 四種場景、收藏、五種排序與三種 intake 說明
- 6 筆明確標示為 `demo_only`、`unpublished` 的 JSON 展示資料

## 已完成

- 恢復並採用原始雜誌型首頁作為正式網站。
- 保留 V2.5 Recovery Baseline 為可直接開啟的預覽版本。
- 保留既有 SQLite schema、資料庫與 `scripts/import_data.py` 匯入流程。
- 建立資料與網站驗證 scripts。
- 驗證正式首頁與 V2.5 預覽可同時存在。
- 建立 GitHub Actions 驗證流程。
- 建立 GitHub Pages 發布 workflow。
- 正式發布資料維持 0。

## 未完成

- 取回原先 20 筆候選 JSON。
- 取回來源、研究文件與查證紀錄。
- 取回圖片權利資料。
- 重新核對 AREX 09、TENDAYs、花伴小方巾、HITACHI NTB、聲寶 SR-C58DV。
- 建立正式 intake 表單或後端。
- 把 SQLite 正式資料與前台公開 JSON 建立受控發布流程。
- 將雜誌型首頁的內嵌示範資料改接正式且可驗證的資料來源。

## 不可重做

- 候選 01–05 既有查證成果；原檔取回前不得重新猜測。
- 雜誌型 V0.3／V1.2 介面基準。
- V0.4 候選資料基礎。
- V0.5 研究預覽。
- V2.3 Formal Publication Gate。
- V2.5 Recovery 預覽。
- 既有 SQLite 與資料匯入治理成果。

## 重要決策

- 雜誌型介面是正式網站的視覺主線。
- V2.5 功能保留為預覽，不覆蓋正式首頁。
- 台灣品牌不等於台灣製造。
- 以單一產品／型號為查證單位。
- 正式首頁目前的產品仍是示範資料。
- `demo_only` 不得進入正式發布。
- `ready_for_editorial_review` 不等於 `published`。
- 正式資料不得由前台、排序、收藏或 metadata 自動升級。
- 未知維持待確認，衝突不得隱藏。

## 下一步

以雜誌型首頁為基礎，逐步把 V2.3／V2.4／V2.5 的資料治理、Gate、搜尋與 Discovery 功能整合進去；在正式候選與證據原檔取回前，不以示範資料冒充正式產品資料。
