from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
index = (ROOT / "index.html").read_text(encoding="utf-8")
js = (ROOT / "assets/app.js").read_text(encoding="utf-8")
css = (ROOT / "assets/styles.css").read_text(encoding="utf-8")

for token in ["研究預覽", "正式發布", "正式發布 Gate", "assets/styles.css", "assets/app.js"]:
    assert token in index, token

for token in ["publicationGate", "localStorage", "data-scene", "favorites"]:
    assert token in js or token in index, token

assert ".ticker" in css
assert ".layout" in css
assert ".mobile-nav" in css

print("OK: V2.5 site structure, gate, discovery and responsive assets")
