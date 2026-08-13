(() => {
  "use strict";

  const VERSION = "V3.2 REGISTRY LIFECYCLE";
  const state = { report: null, rows: [], window: 90 };
  const DAY = 86400000;

  boot();

  async function boot() {
    injectNavigation();
    injectDashboard();
    try {
      state.report = await fetchReport();
      state.rows = normalizeRows(state.report);
      render();
      decorateCatalogCards();
      observeCatalog();
      updateVersion();
    } catch (error) {
      console.warn("V3.2 lifecycle dashboard unavailable:", error);
      const list = document.querySelector("#lifecycleList");
      if (list) list.innerHTML = '<div class="lifecycle-empty">到期資料目前無法載入；主產品資料庫仍可正常使用。</div>';
    }
  }

  async function fetchJson(url, required = true) {
    const response = await fetch(url, { cache: "no-store" });
    if (!response.ok) {
      if (required) throw new Error(`${url} HTTP ${response.status}`);
      return null;
    }
    return response.json();
  }

  async function fetchReport() {
    const deployed = await fetchJson("data/registry-expiry.json", false);
    if (validReport(deployed)) return deployed;

    const publicCatalog = await fetchJson("data/catalog.public.json", false);
    if (publicCatalog?.records?.length) return deriveReport(publicCatalog.records);

    const manifest = await fetchJson("data/registry.manifest.json");
    const shardRows = await Promise.all((manifest.shards || []).map(shard => fetchJson(shard.path)));
    return deriveReport(shardRows.flat());
  }

  function validReport(report) {
    return report && Number(report.registry_records) >= 50 && Array.isArray(report.expiring_within_365_days);
  }

  function deriveReport(records) {
    const registry = records.filter(row => row.catalog_source === "mit_registry" || row.record_origin === "mit_registry");
    const today = startOfToday();
    const rows = registry.map(row => {
      const valid = parseDate(row.certification?.valid_until);
      const days = valid ? Math.floor((valid - today) / DAY) : null;
      return {
        id: row.id,
        brand: row.brand,
        model: row.model,
        name: row.name,
        certificate_no: row.certification?.certificate_no,
        valid_until: row.certification?.valid_until,
        days_remaining: days
      };
    }).filter(row => Number.isInteger(row.days_remaining));
    const within = limit => rows.filter(row => row.days_remaining >= 0 && row.days_remaining <= limit).sort(byDays);
    const expired = rows.filter(row => row.days_remaining < 0).sort(byDays);
    return {
      generated_at: localDate(),
      registry_records: registry.length,
      expired_count: expired.length,
      expired,
      expiring_within_30_days: within(30),
      expiring_within_90_days: within(90),
      expiring_within_180_days: within(180),
      expiring_within_365_days: within(365)
    };
  }

  function expiredCount(report) {
    if (Number.isInteger(report?.expired_count)) return report.expired_count;
    if (Array.isArray(report?.expired)) return report.expired.length;
    return Number(report?.expired || 0);
  }

  function normalizeRows(report) {
    return [...(report.expiring_within_365_days || [])].map(row => ({ ...row })).sort(byDays);
  }

  function injectNavigation() {
    const nav = document.querySelector(".sidebar-nav");
    if (!nav || nav.querySelector('[data-scroll="lifecycle"]')) return;
    const database = nav.querySelector('[data-scroll="database"]');
    const button = document.createElement("button");
    button.className = "nav-btn";
    button.type = "button";
    button.dataset.scroll = "lifecycle";
    button.innerHTML = "<span>到期管理</span><span>03</span>";
    database?.after(button);
    const order = ["top", "database", "lifecycle", "stories", "brands", "method"];
    order.forEach((key, index) => {
      const item = nav.querySelector(`[data-scroll="${key}"] span:last-child`);
      if (item) item.textContent = String(index + 1).padStart(2, "0");
    });
  }

  function injectDashboard() {
    if (document.querySelector("#lifecycle")) return;
    const anchor = document.querySelector(".catalog-hero");
    if (!anchor) return;
    const section = document.createElement("section");
    section.className = "lifecycle-section sans";
    section.id = "lifecycle";
    section.innerHTML = `
      <div class="lifecycle-head">
        <div>
          <div class="lifecycle-eyebrow">REGISTRY LIFECYCLE · V3.2</div>
          <h2>證據不是永久有效，<br>到期前就要重新查。</h2>
          <p>這裡追蹤 MIT Registry 的有效期限。到期狀態只影響政府標章證據是否仍有效，不會自動改變品牌身分、圖片授權或正式發布狀態。</p>
        </div>
        <div class="lifecycle-next" id="lifecycleNext"><b>NEXT EXPIRY</b><strong>資料載入中</strong><span>—</span></div>
      </div>
      <div class="lifecycle-metrics">
        <div class="lifecycle-metric"><b id="lifeExpired">—</b><span>已過期</span></div>
        <div class="lifecycle-metric"><b id="life30">—</b><span>30 天內</span></div>
        <div class="lifecycle-metric attention"><b id="life90">—</b><span>90 天內</span></div>
        <div class="lifecycle-metric"><b id="life180">—</b><span>180 天內</span></div>
        <div class="lifecycle-metric"><b id="life365">—</b><span>365 天內</span></div>
      </div>
      <div class="lifecycle-controls" aria-label="到期區間篩選">
        <button type="button" class="lifecycle-filter" data-life-window="30">30 天</button>
        <button type="button" class="lifecycle-filter active" data-life-window="90">90 天</button>
        <button type="button" class="lifecycle-filter" data-life-window="180">180 天</button>
        <button type="button" class="lifecycle-filter" data-life-window="365">365 天</button>
      </div>
      <div class="lifecycle-list" id="lifecycleList" aria-live="polite"><div class="lifecycle-empty">到期資料載入中。</div></div>
      <div class="lifecycle-source" id="lifecycleSource">由 Registry 有效期限即時計算；正式部署優先讀 build-time expiry report。</div>`;
    anchor.after(section);

    section.addEventListener("click", event => {
      const filter = event.target.closest("[data-life-window]");
      if (filter) {
        state.window = Number(filter.dataset.lifeWindow || 90);
        section.querySelectorAll("[data-life-window]").forEach(btn => btn.classList.toggle("active", btn === filter));
        renderRows();
      }
    });
  }

  function render() {
    const expired = expiredCount(state.report);
    setText("#lifeExpired", expired);
    setText("#life30", state.report.expiring_within_30_days?.length ?? 0);
    setText("#life90", state.report.expiring_within_90_days?.length ?? 0);
    setText("#life180", state.report.expiring_within_180_days?.length ?? 0);
    setText("#life365", state.report.expiring_within_365_days?.length ?? 0);
    const next = state.rows[0];
    const nextBox = document.querySelector("#lifecycleNext");
    if (nextBox) {
      nextBox.innerHTML = next
        ? `<b>NEXT EXPIRY</b><strong>${html(next.brand || "品牌待確認")} · ${html(next.model || "")}</strong><span>${html(next.valid_until)} · 剩 ${next.days_remaining} 天</span>`
        : '<b>NEXT EXPIRY</b><strong>365 天內無到期項目</strong><span>目前無需處理</span>';
    }
    const source = document.querySelector("#lifecycleSource");
    if (source) source.textContent = `Registry ${state.report.registry_records || 0} 筆 · 報表日期 ${state.report.generated_at || localDate()} · 已過期 ${expired} 筆。`;
    renderRows();
  }

  function renderRows() {
    const list = document.querySelector("#lifecycleList");
    if (!list) return;
    const rows = state.rows.filter(row => row.days_remaining <= state.window);
    if (!rows.length) {
      list.innerHTML = `<div class="lifecycle-empty">${state.window} 天內沒有即將到期的 Registry。</div>`;
      return;
    }
    list.innerHTML = rows.map(row => `
      <article class="lifecycle-row" data-catalog-id="${attr(row.id)}" tabindex="0">
        <div class="days ${row.days_remaining <= 30 ? "warning" : ""}">${row.days_remaining} 天</div>
        <div class="brand"><strong>${html(row.brand || "品牌待確認")}</strong></div>
        <div class="product"><strong>${html(row.model || "型號待確認")}</strong>${row.name ? `<small>${html(row.name)}</small>` : ""}</div>
        <div class="certificate"><small>標章 ${html(row.certificate_no || "—")}</small></div>
        <div class="valid">${html(row.valid_until || "—")}</div>
        <div class="open">→</div>
      </article>`).join("");
  }

  function decorateCatalogCards() {
    const map = new Map(state.rows.map(row => [row.id, row]));
    document.querySelectorAll(".catalog-card[data-catalog-id]").forEach(card => {
      const row = map.get(card.dataset.catalogId);
      card.querySelector(".lifecycle-pill")?.remove();
      if (!row) return;
      const pill = document.createElement("span");
      pill.className = `lifecycle-pill ${row.days_remaining <= 30 ? "urgent" : row.days_remaining <= 90 ? "soon" : ""}`;
      pill.textContent = `標章剩 ${row.days_remaining} 天`;
      const meta = card.querySelector(".catalog-meta");
      (meta || card).appendChild(pill);
    });
  }

  function observeCatalog() {
    const grid = document.querySelector("#catalogGrid");
    if (!grid) return;
    new MutationObserver(() => decorateCatalogCards()).observe(grid, { childList: true, subtree: true });
  }

  function updateVersion() {
    document.querySelectorAll(".side-note strong").forEach(node => node.textContent = VERSION);
    const edition = document.querySelector(".edition");
    if (edition) edition.textContent = "VOL. 003 · 2026 AUGUST · REGISTRY LIFECYCLE";
  }

  function setText(selector, value) {
    const node = document.querySelector(selector);
    if (node) node.textContent = String(value);
  }
  function byDays(a, b) { return a.days_remaining - b.days_remaining; }
  function parseDate(value) { return /^\d{4}-\d{2}-\d{2}$/.test(String(value || "")) ? new Date(`${value}T00:00:00`) : null; }
  function startOfToday() { const d = new Date(); return new Date(d.getFullYear(), d.getMonth(), d.getDate()); }
  function localDate() { const d = new Date(); return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,"0")}-${String(d.getDate()).padStart(2,"0")}`; }
  function html(value) { return String(value ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"})[c]); }
  function attr(value) { return html(value); }
})();
