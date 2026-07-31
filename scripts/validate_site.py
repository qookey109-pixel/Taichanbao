from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
index = (ROOT / "index.html").read_text(encoding="utf-8")
preview = (ROOT / "versions_review/v2.5/index.html").read_text(encoding="utf-8")
js = (ROOT / "assets/app.js").read_text(encoding="utf-8")
css = (ROOT / "assets/styles.css").read_text(encoding="utf-8")

# 正式首頁採用使用者偏好的雜誌型版本。
for token in [
    "台灣品牌選品誌",
    "今日台產",
    "產品專題",
    "品牌索引",
    "本月台產榜",
    "目前為介面示範資料",
]:
    assert token in index, token

# V2.5 Recovery Baseline 保留為可開啟的預覽版本。
for token in [
    "V2.5 Recovery Baseline",
    "研究預覽",
    "正式發布",
    "正式發布 Gate",
    '<base href="../../">',
]:
    assert token in preview, token

for token in ["publicationGate", "localStorage", "favorites"]:
    assert token in js, token

assert ".ticker" in css
assert ".layout" in css
assert ".mobile-nav" in css

print("OK: magazine homepage is official; V2.5 recovery remains available as preview")
