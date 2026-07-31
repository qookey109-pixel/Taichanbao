# 台產報檔案比較報告

建立日期：2026-07-29  
模式：唯讀比對；本報告未複製、覆蓋、刪除或重新命名正式專案檔案。

## 結論摘要

- 目前能確認的是兩個**歷史單檔 HTML 原型**與一組 ChatGPT 匯出說明文件，不是可還原的正式 Repository。
- `/Users/qoo/Downloads/index.html` 自標為 **V0.1 概念原型**；`/Users/qoo/Downloads/taichanbao_v0_3.html` 為 **V0.3**。兩者 SHA-256 不同，且 V0.3 的來源建立時間比 V0.1 晚約 9 分鐘，因此 V0.3 是較新的原型，但不能據此認定為正式網站最新版本。
- 沒有可供逐路徑比較的「正式本機專案樹」或 Git 工作樹。本次不應以任何匯出內容覆蓋 `index.html`，更不能據此生成或套用 V2.4。
- Web 匯出文件明確指出：V2.3／V2.4 的網站、資料、腳本與工作流程原檔並未取得；V2.4 只有安裝說明，不是可套用的完整套件。

## 比對範圍與來源角色

| 代號 | 路徑 | 角色 | 檔案數 |
|---|---|---|---:|
| W1 | `/Users/qoo/Downloads/00_manifest_instructions/` | Web GPT 匯出之 manifest／決策說明副本 | 7 |
| W2 | `/Users/qoo/Downloads/06_chat_only_decisions-2/` | Web GPT 匯出之決策包與前次恢復稽核物 | 9 |
| W3 | `/Users/qoo/Downloads/taichanbao_v0_3.html` | 從 File Library 另行下載的 V0.3 HTML 原型 | 1 |
| L1 | `/Users/qoo/Downloads/index.html` | 使用者提供的本機單檔 HTML；內容自標 V0.1 | 1 |

W1、W2、W3 合稱「Web GPT 匯出集合」。L1 是目前唯一明確提供的本機程式檔；它不是 Git 工作樹，沒有可檢查的提交基準。

## 雜湊與版本證據

| 檔案 | SHA-256 | 版本／來源判讀 | 結論 |
|---|---|---|---|
| `index.html` | `249d1145250c868d17f8e31888ffd2529098941480c26e3542cd79697c23288a` | 頁尾自標 `V0.1 概念原型`；來源文件列為 File Library V0.1 | 較舊原型；正式性待確認 |
| `taichanbao_v0_3.html` | `c1de2fd84549ecfbb3ff56f3e7918bb05a358fd094a64e5a28dd8c33f7567130` | 檔名與來源文件列為 V0.3；File Library 建立時間晚於 V0.1 | 較新的原型；僅供版本保留／比較 |

下載到本機的修改時間僅表示下載或檔案落地時間，不能當成原始程式版本時間。

## 檔案分類

### 只存在於 Web GPT 匯出集合

| 路徑／檔案 | 判讀 |
|---|---|
| `00_manifest_instructions/` 下 7 份 Markdown／校驗檔 | Web 匯出說明；不是 Repository 原始程式 |
| `06_chat_only_decisions-2/` 下 7 份同名說明／校驗檔 | Web 匯出說明；其中 6 份與 W1 完全相同 |
| `06_chat_only_decisions-2/export_audit/previous_recovery_attempt/README_FIRST.md` | 前次恢復嘗試的稽核說明，屬衍生檔 |
| `06_chat_only_decisions-2/export_audit/previous_recovery_attempt/Taichanbao_Project_Recovery_2026-07-29.zip` | 前次生成的恢復包；manifest 明定非原始專案來源、內容較不完整 |
| `taichanbao_v0_3.html` | V0.3 原型，不是 V2.3／V2.4 正式根檔 |

### 只存在於目前提供的本機來源

| 路徑／檔案 | 判讀 |
|---|---|
| `/Users/qoo/Downloads/index.html` | V0.1 單檔原型；無同層資料、assets、scripts、JSON、測試或 Git 歷史可驗證 |

### 同路徑但內容不同

在 Web GPT 匯出集合與 L1 之間，沒有一對可判定為「相同專案相對路徑」的檔案，因此**沒有可安全判定的跨來源同路徑內容差異**。

Web 匯出集合內部唯一同相對檔名但不同內容的是 `SHA256SUMS.txt`：W2 比 W1 多兩筆 `export_audit/previous_recovery_attempt/` 檔案校驗值。這是 W2 多出稽核物的預期差異，不是程式衝突。

### 完全相同

下列 W1 與 W2 同相對路徑檔案經逐位元比較完全相同：

- `CHAT_ONLY_DECISIONS.md`
- `CODEX_HANDOFF.md`
- `EXPORT_MANIFEST.md`
- `LOCAL_UPDATE_INSTRUCTIONS.md`
- `MISSING_OR_UNAVAILABLE.md`
- `SOURCE_PROVENANCE.md`

沒有任何檔案在 Web GPT 匯出集合與 L1 之間完全相同。

## HTML 內容差異

| 面向 | L1 `index.html`（V0.1） | W3 `taichanbao_v0_3.html`（V0.3） |
|---|---|---|
| 頁面定位 | 品牌推薦與產地透明平台 | 台灣品牌選品誌／雜誌型介面 |
| 版面 | 傳統頂部導覽、hero、產品卡、原則區 | 跑馬燈、側欄、主內容區、右側欄、行動版底部導覽 |
| 探索 | 搜尋＋標籤篩選 | 全站搜尋、分類、產品抽屜、品牌索引、排行榜 |
| 資料呈現 | 產品卡與參與程度 | 產品履歷，分列研發、原料、製造、包裝等環節 |
| 資料來源 | 6 筆內嵌示範資料 | 6 筆內嵌示範資料，仍無外部來源、JSON 或驗證器 |
| 資料聲明 | 明示「示範資料不代表正式查證結果」 | 明示「介面示範資料」，並稱正式上線前須補來源、證據、日期 |

兩檔為完整重構，並非可以以 patch 或單向覆蓋合併的微小變更。

## 可能較新／較舊的版本

| 項目 | 判定 | 依據與限制 |
|---|---|---|
| W3 V0.3 相對 L1 V0.1 | **可能較新** | 版本號與 File Library 建立時間皆較晚；僅代表原型演進 |
| L1 V0.1 相對 W3 V0.3 | **可能較舊** | 頁尾自標 V0.1，且來源文件將 V0.1 定義為概念原型 |
| V2.3 Markdown | **較新但僅文件可取得** | manifest 列為最新可完整取得文件；不能推導目前程式內容 |
| V2.4 `INSTALL.md` | **較新的安裝規格，不是程式版本** | 六個預期檔只有說明可取得，禁止依此重建後宣稱為原檔 |

## 命名與路徑衝突

1. `index.html` 名稱衝突：L1 是 V0.1；V2.4 安裝說明也預期有一個要覆蓋的 `index.html`，但該 V2.4 原檔缺失。**不得把 L1 當成 V2.4 或用 V2.4 說明覆蓋它。**
2. `taichanbao_v0_3.html` 是歷史版本名稱，與正式根檔 `index.html` 的職責重疊。應在日後核准後放入版本保存區，而不是改名為正式首頁。
3. W1／W2 的 6 份同名 Markdown 是重複副本；若日後納入專案，只能選一份並保留來源紀錄，不能視為兩套獨立決策。
4. W2 的恢復 ZIP 為衍生稽核物，名稱含「Recovery」不表示它是可覆蓋的完整恢復來源。

## 聊天決策與目前程式碼的差異

以下為可證實的落差；因兩個 HTML 都自稱示範原型，除非已被部署為正式頁面，不能判定為已發生的正式資料違規。

| 聊天／匯出決策 | HTML 現況 | 判讀 |
|---|---|---|
| 正式產品事實應由 JSON 支撐；正式專區只顯示通過 Gate 的資料 | 兩檔均將產品資料硬編碼在 JavaScript，未見 JSON、Gate、來源 URL 或驗證器 | 原型與正式資料治理不一致；不可拿來發布正式產品 |
| 未知應為 `to_verify`、衝突應為 `conflicting`，不得用 AI 推測產地公開 | V0.3 示範履歷使用「已確認／部分確認／已收錄」，但無證據連結；V0.1 使用推薦與 A/B/C 等級 | 原型標示與正式狀態機不一致；只能保留為 mock UI |
| 正式發布數為 0，`ready_for_editorial_review` 不等於 `published` | 兩檔有分數、推薦語與「全流程台產」等展示 | 在「示範資料」標示下不構成正式發布；移除示範標示或接正式頁面前必須改接受控資料 |
| V1.2 三欄與跑馬燈為不可破壞基準 | V0.3 含三欄與跑馬燈；V0.1 不含 | V0.3 視覺方向看似相容，但無 V1.2 原檔，不能聲稱相同或據此覆蓋 |
| V2.4 必須是六檔套件，且不得改動既有 assets、候選資料、研究資料 | 目前僅有 V2.4 `INSTALL.md`，任何對應原檔均未提供 | 完全不可執行套用；屬待確認／阻擋項 |

## 本機未提交修改保護結果

- `/Users/qoo/Downloads/` 不是 Git 工作樹，無法判定 `index.html` 是否相對某次提交有未提交修改。
- 提供的 Web 匯出目錄也不是 Git 工作樹。
- 報告工作區 `/Users/qoo/Documents/台產報` 在建立本報告前為無提交的空 Git 工作樹；它不是可作為網站原始碼基準的正式 Repository。
- 因此：**沒有可驗證的「可覆蓋本機未提交修改」清單，但這不是安全可覆蓋的證據。**在取得正式專案根目錄與 `git status` 前，所有本機檔案都應視為不可覆蓋。

## 比對限制

本次未連接 GitHub、未 fetch／pull／push，且未對任何正式專案執行寫入。缺少下列項目，所以無法做 Repository 等級差異判定：V2.3／V2.4 `index.html`、assets、候選 JSON、研究文件、scripts、tests、workflows、正式 Git 提交歷史。
