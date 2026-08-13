(() => {
  "use strict";

  const VERSION = "V3.3 REGISTRY SCALE 100";

  function applyVersion() {
    document.querySelectorAll(".side-note strong").forEach(node => node.textContent = VERSION);
    const edition = document.querySelector(".edition");
    if (edition) edition.textContent = "VOL. 004 · 2026 AUGUST · SCALE 100 + LIFECYCLE";
  }

  async function addBalanceNote() {
    const section = document.querySelector("#database .catalog-source-note");
    if (!section || document.querySelector("#v33BalanceNote")) return;
    try {
      const response = await fetch("data/registry.manifest.json", { cache: "no-store" });
      if (!response.ok) return;
      const manifest = await response.json();
      const shards = await Promise.all((manifest.shards || []).map(async shard => {
        const res = await fetch(shard.path, { cache: "no-store" });
        return res.ok ? res.json() : [];
      }));
      const rows = shards.flat();
      const counts = rows.reduce((map, row) => {
        map[row.category] = (map[row.category] || 0) + 1;
        return map;
      }, {});
      const sorted = Object.entries(counts).sort((a, b) => b[1] - a[1]);
      const [largest, count] = sorted[0] || ["—", 0];
      const note = document.createElement("div");
      note.id = "v33BalanceNote";
      note.className = "v33-balance-note";
      note.innerHTML = `<strong>V3.3 分類平衡 Gate：</strong>Registry ${rows.length} 筆、${sorted.length} 個分類；最大分類「${escapeHtml(largest)}」${count} 筆（${rows.length ? Math.round(count / rows.length * 100) : 0}%），上限 40%。`;
      section.after(note);
    } catch (error) {
      console.warn("V3.3 balance note unavailable:", error);
    }
  }

  function escapeHtml(value) {
    return String(value ?? "").replace(/[&<>"']/g, ch => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"})[ch]);
  }

  applyVersion();
  addBalanceNote();
})();
