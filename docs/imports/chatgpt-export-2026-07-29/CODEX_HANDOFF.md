# CODEX_HANDOFF

請接手「台產報（Taichanbao）」本機資料比對工作。

## 目前限制

- GitHub 暫時不可使用。
- 不連接、不 fetch、不 pull、不 push、不建立 PR。
- ChatGPT 匯出不是完整 Repository。
- 本機正式專案路徑尚未確認，先執行 `pwd` 並請使用者確認。
- 不直接覆蓋整個本機資料夾。

## 先讀取

1. `EXPORT_MANIFEST.md`
2. `MISSING_OR_UNAVAILABLE.md`
3. `CHAT_ONLY_DECISIONS.md`
4. `LOCAL_UPDATE_INSTRUCTIONS.md`
5. `02_docs_handoffs/README.md`
6. `02_docs_handoffs/PROJECT_STATUS.md`
7. `02_docs_handoffs/versions_review/v2.4/INSTALL.md`

## 任務

1. 盤點本機正式專案檔案、Git 狀態與現有版本。
2. 對照匯出 Manifest。
3. 逐檔判斷本機較新、匯出較新、分支衝突、匯出缺失或待確認。
4. 保護本機已完成的候選資料、研究文件、scripts、workflows、assets 與網站成果。
5. 只產生比較報告與建議動作，不先修改檔案。

## 必須產生

- `LOCAL_COMPARISON_REPORT.md`
- `PROPOSED_FILE_ACTIONS.md`
- `UNRESOLVED_CONFLICTS.md`

## 不可重做

- 候選 01–05 查證
- V0.3 介面基準
- V0.4 候選資料基礎
- V0.5 研究預覽網站
- V1.2 三欄介面與跑馬燈
- V2.3 Formal Publication Gate

不能確認的項目標示「待確認」，不得自行補造缺失原檔。
