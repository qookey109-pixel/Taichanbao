# CHAT_ONLY_DECISIONS

建立日期：2026-07-29  
性質：本次匯出新建文件，不是原 Repository 原檔。

## 專案定位

台產報同時維持兩條主軸：

1. 推薦值得支持的台灣品牌。
2. 透明揭露個別產品實際產地、製程與資料缺口。

不得把「台灣品牌」自動等同於「台灣製造」。

## 不可重做或覆蓋的既有工作

下列里程碑在 Project 聊天中被明確列為已完成或不可重做：

- 候選 01–05 查證。
- V0.3 介面基準。
- V0.4 候選資料基礎。
- V0.5 研究預覽網站。
- V1.2 雜誌型三欄介面與跑馬燈。
- V2.3 Formal Publication Gate 與正式發布專區。

因相關原始檔目前未全部取得，Codex 不得根據本匯出包重新生成後直接覆蓋本機既有成果。

## Repository 恢復後的優先核對順序

1. `PROJECT_STATUS.md`
2. `README.md`
3. `docs/handoffs/taichanbao_handoff_2026-07-27_v0_5_research_preview.md`
4. `docs/VERIFICATION_METHOD.md`
5. `docs/research/2026-07-27_candidates_01_05_verification.md`
6. `data/candidates/2026_mit_gold_candidates_06_10.json`
7. `scripts/validate_data.py`
8. `.github/workflows/validate-data.yml`
9. `index.html`

## 版本與資料治理

- GitHub 恢復後，重新讀取最新 `main`，不得沿用聊天中的 SHA 當成已確認最新版本。
- 若聊天、Handoff、本匯出包與最新 Repository 衝突，以最新 Repository 及可驗證資料為準。
- `ready_for_editorial_review` 不等於 `published`。
- 正式專區只能顯示通過 Gate 的正式 JSON。
- 前台、metadata、收藏、排序或 discovery 功能不得自行升級產品狀態。
- 正式候選 JSON 是產品事實來源。
- 未知維持 `to_verify`。
- 衝突維持 `conflicting`。
- 不用 AI 猜測產地後直接公開。
- 不無聲覆蓋歷史產地紀錄。
- 廠商贊助不得改變查證結論或排序。

## V2.4 邊界

V2.4 應由六個檔案組成：

- `index.html`
- `README.md`
- `PROJECT_STATUS.md`
- `assets/discovery.css`
- `assets/discovery.js`
- `scripts/validate_discovery.py`

目前只取得 `INSTALL.md`，不能把 GitHub 上曾成功提交的三個 discovery 檔案視為完整 V2.4。
