# LOCAL_UPDATE_INSTRUCTIONS

建立日期：2026-07-29  
目標：讓 Codex 安全比較本匯出內容與 Mac 本機專案，不直接覆蓋整個資料夾。

## 重要前提

- 本匯出包不是完整 Repository clone。
- 本匯出包沒有 V2.3／V2.4 網站程式、JSON、scripts 或 workflows 原檔。
- `README.md` 與 `PROJECT_STATUS.md` 是最新「可取得」的 V2.3 版本，不保證是整個專案最終最新版。
- 本機正式路徑尚未提供，Codex 必須先用 `pwd` 或請使用者指定，不得自行猜測。

## 建議工作區

把 ZIP 解壓到本機專案以外，例如：

```bash
mkdir -p ~/Desktop/taichanbao-chatgpt-export
```

不要直接解壓到正式專案根目錄。

## 第一階段：只讀盤點

請 Codex 先執行：

```bash
pwd
git status --short --branch 2>/dev/null || true
find . -maxdepth 4 -type f | sort
```

對匯出包與本機專案分別建立檔名及 SHA-256 清單：

```bash
find /path/to/export -type f -print0 | sort -z | xargs -0 shasum -a 256
find /path/to/local-project -type f -not -path '*/.git/*' -print0 | sort -z | xargs -0 shasum -a 256
```

## 第二階段：乾跑比較

```bash
rsync -avn --itemize-changes   --exclude '.git/'   /path/to/export/02_docs_handoffs/   /path/to/local-project/
```

也可使用：

```bash
diff -ruN   --exclude='.git'   /path/to/local-project   /path/to/export/02_docs_handoffs
```

這些命令只用來比較。不得立即執行沒有 `-n` 的 rsync。

## 第三階段：逐檔分類

每個差異都要分類為：

- 本機較新：保留本機。
- 匯出包較新：提出逐檔更新建議。
- 內容分支不同：放入 `versions_review/`，不得直接覆蓋。
- 匯出包缺檔：保留本機，並回填 Manifest。
- 無法判斷：標示「待確認」。

## 禁止操作

- 不得 `rm -rf` 正式專案。
- 不得 `rsync --delete`。
- 不得整個資料夾直接覆蓋。
- 不得把 V0.1／V0.3 HTML 當成目前正式首頁。
- 不得把 V2.3 文件自動覆蓋本機可能較新的 V2.4 文件。
- 不得依 `INSTALL.md` 重新生成缺失的 V2.4 六檔後冒充原檔。
- 不得修改或連接 GitHub。

## 建議產出

Codex 比較完成後，先產生：

- `LOCAL_COMPARISON_REPORT.md`
- `PROPOSED_FILE_ACTIONS.md`
- `UNRESOLVED_CONFLICTS.md`

在使用者審核前，不執行實際覆蓋。
