# 台產報 Handoff — V2.6 Magazine Discovery

## 專案

- Repository：`qookey109-pixel/Taichanbao`
- 正式網站：`https://qookey109-pixel.github.io/Taichanbao/`
- 正式分支：`main`
- 版本：`V2.6 Magazine Discovery`

## 使用者偏好與正式方向

使用者明確偏好雜誌型版本。正式首頁必須保留「今日台產、封面專題、產品專題、品牌索引、本月台產榜、跑馬燈、三欄資訊架構」；不能改成一般資料庫 Dashboard。

## 本次完成

- 將搜尋、分類、四種場景、五種排序、收藏與正式發布 Gate 整合進雜誌型首頁。
- 收藏以 `localStorage` 保存。
- 加入研究預覽／正式發布檢視與 `?view=published`。
- 將六筆 `demo_only / unpublished` 示範 JSON 作為正式首頁資料來源。
- 保留內嵌 fallback，避免資料檔載入失敗時整頁空白。
- 保留 V2.5 Recovery Baseline 在 `versions_review/v2.5/`。
- 更新 README、PROJECT_STATUS、網站驗證與 GitHub Actions。

## 資料狀態

- 示範資料：6
- 正式發布：0
- 原先 20 筆候選與研究證據仍未取回。

## 關鍵限制

- 不得把示範品牌或產品視為正式查證成果。
- 不得重新猜測候選 01–05 或其他失落研究結論。
- 不得讓前台功能改寫查證或發布狀態。
- 不得刪除 SQLite、匯入工具、歷史版本或匯出稽核資料。

## 下一步

取回至少一筆具有品牌、型號、現售、產地／製程來源與查證日期的真實候選，先走完一筆正式 Gate，再擴大資料量。
