# EXPORT_MANIFEST

匯出日期：2026-07-29  
專案：台產報（Taichanbao）  
匯出性質：ChatGPT Project 可取得資料恢復與本機比對包  
GitHub：未連接、未讀取、未修改  
本機正式路徑：待確認

## 批次結果

| 批次 | 狀態 | 說明 |
|---|---|---|
| `01_core_source` | 未建立 ZIP | 兩個 HTML 只能從 File Library 原始檔案卡另外下載；未重建 |
| `02_docs_handoffs` | 已建立 | 含可完整取得的 Markdown 原檔、版本保留及 Handoff |
| `03_data` | 未建立 ZIP | 沒有取得任何原始 JSON／CSV／資料集 |
| `04_scripts_tests_workflows` | 未建立 ZIP | 沒有取得任何原始 script／test／workflow |
| `05_assets` | 未建立 ZIP | 沒有取得任何獨立原始資產檔 |
| `06_chat_only_decisions` | 已建立 | 含聊天決策、缺檔、來源、本機更新與 Codex 接續文件 |

## 匯出檔案

| 相對路徑 | 類型 | 來源 | 版本／日期 | 最新判斷 | 衝突 | ZIP |
|---|---|---|---|---|---|---|
| `README.md` | 原始 Markdown | File Library `file_00000000ef3481f68b9d80b7f4648a0c` | V2.3／2026-07-27 | 最新可取得，不保證整體最新版 | V2.4 版缺失 | `02_docs_handoffs` |
| `PROJECT_STATUS.md` | 原始 Markdown | File Library `file_00000000ee5481f6876f78e88086564d` | V2.3／2026-07-27 | 最新可取得，不保證整體最新版 | V2.4 版缺失 | `02_docs_handoffs` |
| `versions_review/v0.1/README.md` | 原始 Markdown | File Library `file_00000000e84082079e99f40a0dba9d98` | V0.1／2026-07-27 | 舊版 | 已被 V2.3 更新 | `02_docs_handoffs` |
| `versions_review/v0.1/PROJECT_STATUS.md` | 原始 Markdown | File Library `file_00000000548882079e5823dbf280e276` | V0.1／2026-07-27 | 舊版 | 已被 V2.3 更新 | `02_docs_handoffs` |
| `versions_review/v2.4/INSTALL.md` | 原始 Markdown | File Library `file_0000000064f081f6a6c4085f1da8f3ff` | V2.4／2026-07-27 | 最新階段說明 | 六個套件原檔缺失 | `02_docs_handoffs` |
| `docs/handoffs/taichanbao_handoff_2026-07-29_project_export.md` | 新建衍生文件 | 本次盤點 | 2026-07-29 | 最新匯出 Handoff | 無 | `02_docs_handoffs` |
| `EXPORT_MANIFEST.md` | 新建衍生文件 | 本次盤點 | 2026-07-29 | 最新匯出清單 | 無 | `02_docs_handoffs`、standalone |
| `CHAT_ONLY_DECISIONS.md` | 新建衍生文件 | Project 聊天摘要 | 2026-07-29 | 最新聊天決策整理 | 與未來 GitHub 內容仍需比對 | `06_chat_only_decisions`、standalone |
| `MISSING_OR_UNAVAILABLE.md` | 新建衍生文件 | 本次盤點 | 2026-07-29 | 最新缺檔清單 | 無 | `06_chat_only_decisions`、standalone |
| `LOCAL_UPDATE_INSTRUCTIONS.md` | 新建衍生文件 | 本次盤點 | 2026-07-29 | 最新安全更新流程 | 本機路徑待確認 | `06_chat_only_decisions`、standalone |
| `SOURCE_PROVENANCE.md` | 新建衍生文件 | File Library metadata | 2026-07-29 | 最新來源紀錄 | 無 | `06_chat_only_decisions`、standalone |
| `CODEX_HANDOFF.md` | 新建衍生文件 | 本次盤點 | 2026-07-29 | 最新 Codex 接續指令 | 無 | `06_chat_only_decisions`、standalone |
| `export_audit/previous_recovery_attempt/Taichanbao_Project_Recovery_2026-07-29.zip` | 先前生成檔案 | 本對話 | 2026-07-29 | 非原始專案來源 | 內容較不完整 | `06_chat_only_decisions` |

## File Library 原檔引用，未收進 ZIP

| 原檔 | File Library ID | 建議位置 | 原因 |
|---|---|---|---|
| V0.1 `index.html` | `file_00000000a80c8207b7aaf2df79db0cc6` | `versions_review/v0.1/index.html` | 只能取得截斷顯示，不能可靠重建 |
| V0.3 `taichanbao_v0_3.html` | `file_0000000054708206ade79b8ade516a9f` | `versions_review/v0.3/taichanbao_v0_3.html` | 只能取得截斷顯示，不能可靠重建 |

## 建議採用版本

- `README.md`：V2.3 是最新可完整取得版本；僅供比較，不可直接取代本機可能較新的版本。
- `PROJECT_STATUS.md`：V2.3 是最新可完整取得版本；僅供比較。
- V0.1／V0.3：全部保留在 `versions_review`，不得作為正式網站根檔。
- V2.4：目前只有 `INSTALL.md`，不能執行完整套用。
