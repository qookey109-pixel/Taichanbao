# 建議更新計畫（待確認，不執行）

建立日期：2026-07-29  
狀態：**只提出計畫；尚未複製、覆蓋、刪除或重新命名任何正式本機檔案。**

## 建議決策

目前不建議更新任何正式程式檔。Web GPT 匯出不完整，唯一的 V0.1／V0.3 HTML 是原型；V2.4 缺少五個以上必要原檔與所有資料／驗證檔。最安全的下一步是先取得正式本機 Repository 根目錄並建立唯讀基準。

## 分階段計畫

| 階段 | 動作 | 寫入正式專案？ | 核准門檻 |
|---|---|---:|---|
| 0 | 指定正式專案根目錄，確認它是否為 `qoo109/Taichanbao` 的 clone | 否 | 使用者提供路徑 |
| 1 | 讀取 `git status --short --branch`、目前 SHA、檔案樹、雜湊清單 | 否 | 無，唯讀 |
| 2 | 對照正式樹與本次 Web 匯出，逐檔重做比較報告 | 否 | 無，唯讀 |
| 3 | 將 W1/W2 文件作為外部參考資料保存提案，不作為覆蓋來源 | 否 | 使用者核准保存位置 |
| 4 | 只在能定位到來源且內容可驗證時，建立逐檔變更清單與 patch | 否 | 使用者核准每個檔案／群組 |
| 5 | 先在新分支或獨立工作副本套用已核准 patch，執行既有驗證 | 是 | 使用者確認更新計畫 |
| 6 | 驗證通過後才更新正式工作樹 | 是 | 使用者再次確認或明確授權 |

## 檔案層級建議

| 項目 | 建議動作 | 理由 |
|---|---|---|
| `/Users/qoo/Downloads/index.html` | 保留，不覆蓋 | V0.1 原型；無 Git 基準且其正式性待確認 |
| `/Users/qoo/Downloads/taichanbao_v0_3.html` | 僅保留為 V0.3 比較來源 | 較新的原型不是正式網站根檔 |
| W1／W2 的 6 份重複 Markdown | 不匯入正式根目錄 | 多為衍生說明文件，且沒有確認正式專案版本 |
| W2 的恢復 ZIP 與 audit README | 不解壓到正式專案 | 明定是前次生成的稽核／恢復物，不完整、非原始來源 |
| V2.4 `INSTALL.md` | 僅作規格參考 | 缺少 `index.html`、README、PROJECT_STATUS、CSS、JS、驗證器；不能據此補造原檔 |

## 待核准後的安全保存方案

若你希望把這次匯出資料納入正式 Repository，建議只新增一個清楚隔離的參考目錄，例如：

```text
docs/imports/chatgpt-export-2026-07-29/
  EXPORT_MANIFEST.md
  CHAT_ONLY_DECISIONS.md
  MISSING_OR_UNAVAILABLE.md
  SOURCE_PROVENANCE.md
```

條件：

1. 只放參考／來源紀錄，不覆蓋 `README.md`、`PROJECT_STATUS.md` 或任何程式檔。
2. 同名重複文件只保留一份，並在提交說明記錄原始下載位置與 SHA-256。
3. V0.1／V0.3 HTML 僅在確定需要歷史保存時，放入 `versions_review/`；不得改名成正式根目錄 `index.html`。
4. ZIP 保持在專案外，或只保存其雜湊／來源紀錄；不要解壓混入正式樹。

## 驗證門檻（正式更新前）

在任何程式更新前，必須先具備：

- 正式本機專案路徑與 Git 狀態。
- 目前 `main` 或工作分支 SHA。
- `PROJECT_STATUS.md`、`README.md`、候選 JSON、驗證 scripts／workflows 的實際內容。
- 對 V2.4 六檔是否完整存在的確認。
- 對所有候選資料來源、狀態與正式發布 Gate 的驗證。

若正式專案確實包含 V2.4 六檔，才可依其既有驗證程序進行：JavaScript 語法檢查、資料驗證、preview 驗證、discovery 驗證。未具備這些檔案時，不能聲稱更新成功。

## 明確不做事項

- 不以 V0.1 或 V0.3 覆蓋正式 `index.html`。
- 不依 `INSTALL.md` 補造缺失 V2.4 檔案並視為原始版本。
- 不覆蓋 `assets/styles.css`、`assets/app.js`、publication 檔、候選資料、研究資料。
- 不解壓、rsync、刪除、改名或連接 GitHub。
