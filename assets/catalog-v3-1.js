(() => {
  "use strict";

  const VERSION = "V3.3 REGISTRY SCALE 100";
  const state = { records: [], query: "", category: "all", evidence: "all", brand: "all", source: "all", sort: "evidence", loadMode: "fallback" };
  const $ = selector => document.querySelector(selector);
  const els = {
    grid: $("#catalogGrid"), count: $("#catalogVisibleCount"), total: $("#catalogTotal"), mit: $("#mitCertifiedCount"),
    deep: $("#deepCaseCount"), published: $("#catalogPublishedCount"), demo: $("#demoCount"), category: $("#catalogCategoryFilter"),
    evidence: $("#catalogEvidenceFilter"), brand: $("#catalogBrandFilter"), source: $("#catalogSourceFilter"), sort: $("#catalogSort"),
    search: $("#globalSearch"), drawer: $("#drawer"), backdrop: $("#drawerBackdrop"), drawerContent: $("#drawerContent"), summary: $("#catalogSummary")
  };

  boot();

  async function json(url, required = true) {
    const response = await fetch(url, { cache: "no-store" });
    if (!response.ok) {
      if (required) throw new Error(`${url} HTTP ${response.status}`);
      return null;
    }
    return response.json();
  }

  async function boot() {
    try {
      const publicCatalog = await json("data/catalog.public.json", false);
      if (validPublicCatalog(publicCatalog)) {
        state.records = publicCatalog.records.map(normalizePublicRecord);
        state.loadMode = "public_catalog";
        finishBoot(publicCatalog.counts.isolated_demo_records, publicCatalog.counts.registry_shards);
        return;
      }
      await bootFromResearchSources();
    } catch (error) {
      console.warn("V3.3 evidence catalog unavailable:", error);
      if (els.grid) els.grid.innerHTML = '<div class="catalog-empty">證據資料庫載入失敗；編輯專題仍可使用。</div>';
    }
  }

  function validPublicCatalog(catalog) {
    return catalog
      && catalog.catalog_version === "V3.3 Registry Scale 100"
      && Array.isArray(catalog.records)
      && catalog.records.length === 104
      && catalog.counts?.mit_active_exact_models === 100
      && catalog.counts?.deep_editorial_cases === 4
      && catalog.counts?.registry_shards === 3
      && catalog.counts?.formal_published === 0;
  }

  async function bootFromResearchSources() {
    const [base, overrides, manifest] = await Promise.all([
      json("data/products.demo.json"),
      json("data/product.media.overrides.json", false),
      json("data/registry.manifest.json")
    ]);
    const shards = Array.isArray(manifest?.shards) ? manifest.shards : [];
    if (!shards.length) throw new Error("registry manifest has no shards");
    const shardRows = await Promise.all(shards.map(shard => json(shard.path)));
    const registry = shardRows.flatMap(rows => Array.isArray(rows) ? rows : []);
    const expected = Number(manifest.total_records || 0);
    if (expected && registry.length !== expected) throw new Error(`registry count mismatch ${registry.length}/${expected}`);

    const overrideMap = new Map((Array.isArray(overrides) ? overrides : []).map(row => [row.id, row]));
    const deep = base.filter(row => row.verification_status !== "demo_only").map(row => normalizeDeep(merge(row, overrideMap.get(row.id))));
    const mit = registry.map(normalizeRegistry);
    state.records = [...deep, ...mit];
    state.loadMode = "manifest_fallback";
    finishBoot(base.filter(row => row.verification_status === "demo_only").length, shards.length);
  }

  function finishBoot(demoCount, shardCount) {
    updateVersion(demoCount, shardCount);
    hydrateFilters();
    render();
  }

  function normalizePublicRecord(row) {
    if (row.catalog_source === "mit_registry") return normalizeRegistry(row);
    const level = row.evidence_level || evidenceLevel(row.origin_evidence_status);
    return {
      ...row,
      catalog_source: "deep_case",
      evidence_level: level,
      evidence_label: evidenceLabel(level),
      manufacturing_evidence_status: row.origin_evidence_status || row.manufacturing_evidence_status || "insufficient",
      brand_origin_status: row.brand_origin_status || (row.taiwan_brand === true ? "taiwan_brand_confirmed" : "unverified"),
      record_scope: row.record_scope || "exact_model",
      source_url: row.source_url || firstSource(row),
      source_name: row.source_name || firstSourceName(row)
    };
  }

  function merge(base, override) {
    if (!override || typeof override !== "object") return base;
    const bm = base.media && typeof base.media === "object" ? base.media : {};
    const om = override.media && typeof override.media === "object" ? override.media : {};
    return {
      ...base,
      ...override,
      media: {
        ...bm,
        ...om,
        main: om.main || bm.main,
        gallery: Array.isArray(om.gallery) ? om.gallery : (bm.gallery || []),
        evidence: Array.isArray(om.evidence) ? om.evidence : (bm.evidence || [])
      },
      external_evidence: Array.isArray(override.external_evidence) ? override.external_evidence : (base.external_evidence || [])
    };
  }

  function normalizeDeep(row) {
    const level = evidenceLevel(row.origin_evidence_status);
    return {
      ...row,
      catalog_source: "deep_case",
      evidence_level: level,
      evidence_label: evidenceLabel(level),
      manufacturing_evidence_status: row.origin_evidence_status || "insufficient",
      brand_origin_status: row.taiwan_brand === true ? "taiwan_brand_confirmed" : "unverified",
      company: row.company || "",
      record_scope: "exact_model",
      source_url: firstSource(row),
      source_name: firstSourceName(row),
      certification: row.certification || null,
      source_checked_at: row.source_checked_at || "2026-08-01"
    };
  }

  function normalizeRegistry(row) {
    return {
      ...row,
      catalog_source: "mit_registry",
      evidence_level: row.evidence_level || "A",
      evidence_label: evidenceLabel(row.evidence_level || "A"),
      taiwan_brand: row.brand_origin_status === "taiwan_brand_confirmed",
      current_sale_confirmed: null,
      external_evidence: []
    };
  }

  function evidenceLevel(status) {
    if (status === "publishable") return "A";
    if (status === "official_sources_consistent") return "B";
    if (status === "partial_official_record") return "C";
    return "D";
  }

  function evidenceLabel(level) {
    return ({
      A: "A · 政府／可發布級證據",
      B: "B · 精確型號官方來源一致",
      C: "C · 精確型號部分官方證據",
      D: "D · 品牌宣稱／仍待補證據"
    })[level] || "待分級";
  }

  function firstSource(row) {
    return row.external_evidence?.[0]?.source_url || row.image_source_url || row.brand_product_url || "";
  }

  function firstSourceName(row) {
    return row.external_evidence?.[0]?.source_name || row.image_source_name || "官方來源";
  }

  function updateVersion(demoCount, shardCount) {
    document.querySelectorAll(".side-note strong").forEach(node => node.textContent = VERSION);
    const edition = $(".edition");
    if (edition) edition.textContent = "VOL. 004 · 2026 AUGUST · REGISTRY SCALE 100";
    const mitCount = state.records.filter(row => row.catalog_source === "mit_registry").length;
    const sourceText = state.loadMode === "public_catalog" ? "Public catalog · deploy build" : `Registry shards ${shardCount} · fallback`;
    const sequence = [
      "V3.3：Registry Scale 100",
      `真實研究候選 ${state.records.length} 筆`,
      `MIT 有效精確型號 ${mitCount} 筆`,
      sourceText
    ];
    document.querySelectorAll(".ticker-track span").forEach((node, index) => node.textContent = sequence[index % sequence.length]);
    if (els.demo) els.demo.textContent = String(demoCount);
  }

  function hydrateFilters() {
    if (!els.category) return;
    const values = [...new Set(state.records.map(row => row.category).filter(Boolean))].sort((a, b) => a.localeCompare(b, "zh-Hant"));
    els.category.innerHTML = '<option value="all">全部分類</option>' + values.map(value => `<option value="${esc(value)}">${html(value)}</option>`).join("");
  }

  function filtered() {
    const q = state.query.trim().toLowerCase();
    return state.records.filter(row => {
      const hay = [row.brand, row.company, row.name, row.model, row.category, row.scene, row.origin_summary, row.certification?.certificate_no, ...(row.tags || [])].join(" ").toLowerCase();
      return (state.category === "all" || row.category === state.category)
        && (state.evidence === "all" || row.evidence_level === state.evidence)
        && (state.brand === "all" || row.brand_origin_status === state.brand)
        && (state.source === "all" || row.catalog_source === state.source)
        && (!q || hay.includes(q));
    }).sort((a, b) => {
      if (state.sort === "name") return a.name.localeCompare(b.name, "zh-Hant");
      if (state.sort === "brand") return a.brand.localeCompare(b.brand, "zh-Hant");
      if (state.sort === "valid") return String(b.certification?.valid_until || "").localeCompare(String(a.certification?.valid_until || ""));
      if (state.sort === "checked") return String(b.source_checked_at || "").localeCompare(String(a.source_checked_at || ""));
      return rank(a.evidence_level) - rank(b.evidence_level)
        || String(b.certification?.passed_at || b.source_checked_at || "").localeCompare(String(a.certification?.passed_at || a.source_checked_at || ""));
    });
  }

  function rank(level) { return ({ A: 1, B: 2, C: 3, D: 4 })[level] || 9; }

  function render() {
    const rows = filtered();
    const mitCount = state.records.filter(row => row.catalog_source === "mit_registry").length;
    const deepCount = state.records.filter(row => row.catalog_source === "deep_case").length;
    const published = state.records.filter(row => row.publication_status === "published").length;
    if (els.total) els.total.textContent = String(state.records.length);
    if (els.mit) els.mit.textContent = String(mitCount);
    if (els.deep) els.deep.textContent = String(deepCount);
    if (els.published) els.published.textContent = String(published);
    if (els.count) els.count.textContent = String(rows.length);
    if (els.summary) {
      const mode = state.loadMode === "public_catalog" ? "公開建置產物" : "研究資料 fallback";
      els.summary.textContent = `目前資料庫含 ${state.records.length} 筆真實研究候選：${mitCount} 筆政府 MIT 有效精確型號＋${deepCount} 筆深度編輯案例。正式發布仍為 ${published}。資料來源模式：${mode}。`;
    }
    if (!els.grid) return;
    if (!rows.length) {
      els.grid.innerHTML = '<div class="catalog-empty">找不到符合目前篩選條件的研究資料。</div>';
      return;
    }
    els.grid.innerHTML = rows.map(row => `
      <article class="catalog-card" data-catalog-id="${esc(row.id)}" tabindex="0">
        <div class="catalog-card-top">
          <span class="catalog-emoji" aria-hidden="true">${html(row.emoji || "📦")}</span>
          <div class="catalog-badges">
            <span class="evidence-badge level-${esc(row.evidence_level)}">${html(row.evidence_label)}</span>
            <span class="scope-badge">${row.catalog_source === "mit_registry" ? "政府標章" : "深度案例"}</span>
          </div>
        </div>
        <div class="catalog-kicker">${html(row.brand || "品牌待確認")} · ${html(row.category || "未分類")}</div>
        <h3>${html(row.name)}</h3>
        <p class="catalog-model">${row.model ? `型號 ${html(row.model)}` : "型號待確認"}</p>
        <p class="catalog-copy">${html(row.origin_summary || "")}</p>
        <div class="catalog-meta">
          ${row.certification ? `<span>標章 ${html(row.certification.certificate_no)}</span><span>有效至 ${html(row.certification.valid_until)}</span>` : `<span>${html(statusShort(row.manufacturing_evidence_status))}</span>`}
          <span>${html(brandLabel(row.brand_origin_status))}</span>
        </div>
        <button class="catalog-open" type="button" data-catalog-open="${esc(row.id)}">查看證據履歷 →</button>
      </article>`).join("");
  }

  function statusShort(status) {
    return ({
      official_sources_consistent: "官方來源一致",
      partial_official_record: "部分官方紀錄",
      official_claim_only: "官方宣稱待交叉",
      insufficient: "製造地待確認",
      mit_certified_active: "MIT 有效"
    })[status] || "證據待確認";
  }

  function brandLabel(status) {
    return ({
      taiwan_brand_confirmed: "台灣品牌已確認",
      non_taiwan_brand: "非台灣品牌",
      unverified: "品牌身分待確認"
    })[status] || "品牌身分待確認";
  }

  function openRecord(id) {
    const row = state.records.find(item => item.id === id);
    if (!row || !els.drawerContent) return;
    const cert = row.certification ? `
      <section class="catalog-drawer-block"><h3>政府標章紀錄</h3><dl class="catalog-facts">
        <div><dt>標章</dt><dd>${html(row.certification.scheme)}</dd></div>
        <div><dt>標章編號</dt><dd>${html(row.certification.certificate_no)}</dd></div>
        <div><dt>通過日期</dt><dd>${html(row.certification.passed_at)}</dd></div>
        <div><dt>有效日期</dt><dd>${html(row.certification.valid_until)}</dd></div>
        <div><dt>狀態</dt><dd>${html(row.certification.status)}</dd></div>
      </dl></section>` : "";
    const external = Array.isArray(row.external_evidence) && row.external_evidence.length ? `
      <section class="catalog-drawer-block"><h3>外部查證來源</h3>${row.external_evidence.map(source => `
        <article class="catalog-source-item"><strong>${html(source.title || source.source_name || "查證來源")}</strong>
          <p>${(source.findings || []).map(html).join("、")}</p>
          ${safe(source.source_url) ? `<a href="${esc(source.source_url)}" target="_blank" rel="noopener noreferrer">開啟來源 ↗</a>` : ""}
          <small>${html(source.scope_note || "")}</small>
        </article>`).join("")}</section>` : "";
    els.drawerContent.innerHTML = `
      <div class="drawer-label">TAICHAN EVIDENCE CATALOG · ${html(row.evidence_level)}</div>
      <h2 id="drawerTitle">${html(row.name)}</h2>
      <p><strong>${html(row.brand || "品牌待確認")}</strong><br>${html(row.origin_summary || "")}</p>
      <div class="feature-meta"><span class="tag">${html(row.category || "未分類")}</span><span class="tag">${html(row.scene || "未分類")}</span><span class="tag">${html(row.evidence_label)}</span></div>
      <section class="catalog-drawer-block"><h3>產品識別</h3><dl class="catalog-facts">
        <div><dt>產品型號</dt><dd>${html(row.model || "待確認")}</dd></div>
        <div><dt>申請／公司</dt><dd>${html(row.company || "待確認")}</dd></div>
        <div><dt>品牌身分</dt><dd>${html(brandLabel(row.brand_origin_status))}</dd></div>
        <div><dt>證據範圍</dt><dd>${html(row.record_scope === "exact_model" ? "精確型號" : row.record_scope || "待確認")}</dd></div>
        <div><dt>發布狀態</dt><dd>${html(row.publication_status || "unpublished")}</dd></div>
        <div><dt>最後查閱</dt><dd>${html(row.source_checked_at || "未記錄")}</dd></div>
      </dl></section>
      ${cert}${external}
      <section class="catalog-drawer-block"><h3>主要來源</h3><p>${html(row.source_name || "來源未記錄")}</p>
        ${safe(row.source_url) ? `<a class="catalog-source-link" href="${esc(row.source_url)}" target="_blank" rel="noopener noreferrer">開啟原始來源 ↗</a>` : ""}
        <p class="catalog-scope-note">來源只支持記錄的型號與事實範圍，不得外推同品牌其他產品。</p>
      </section>`;
    els.drawer.classList.add("open");
    els.backdrop?.classList.add("open");
    document.body.style.overflow = "hidden";
  }

  function enhanceMediaScopes() {
    if (!els.drawerContent) return;
    const title = els.drawerContent.querySelector("#drawerTitle")?.textContent?.trim();
    const row = state.records.find(item => item.name === title);
    if (!row?.media) return;
    const raw = [];
    if (row.media.main) raw.push({ ...row.media.main, media_role: "main" });
    (row.media.gallery || []).forEach(item => raw.push({ ...item, media_role: "gallery" }));
    (row.media.evidence || []).forEach(item => raw.push({ ...item, media_role: "evidence" }));
    const thumbs = [...els.drawerContent.querySelectorAll(".media-thumb")];
    thumbs.forEach((button, index) => {
      const item = raw[index];
      const small = button.querySelector("small");
      if (!item || !small) return;
      small.textContent = item.media_role === "evidence" ? "查證" : item.relation_scope === "same_product_family_not_exact_model" ? "同系列" : item.media_role === "main" ? "精確型號" : "產品圖";
    });
    if (!thumbs.length) return;
    const activeIndex = Number(els.drawerContent.querySelector(".media-thumb.active")?.dataset.mediaIndex || 0);
    const active = raw[activeIndex];
    const gallery = els.drawerContent.querySelector(".media-gallery");
    if (!active || !gallery) return;
    gallery.querySelector(".media-scope-row")?.remove();
    const scope = document.createElement("div");
    scope.className = "media-scope-row";
    const pill = document.createElement("span");
    const exact = active.relation_scope !== "same_product_family_not_exact_model";
    pill.className = `media-scope-pill ${exact ? "exact" : "series"}`;
    pill.textContent = exact ? "精確型號／直接產品圖" : "同系列補充圖 · 不作為精確型號證據";
    scope.appendChild(pill);
    const source = gallery.querySelector(".media-architecture-source");
    if (source) source.before(scope); else gallery.appendChild(scope);
  }

  function safe(value) {
    try {
      const url = new URL(String(value || ""), location.href);
      return ["https:", "http:"].includes(url.protocol) ? url.href : "";
    } catch {
      return "";
    }
  }

  function bind(el, key) {
    el?.addEventListener("change", () => {
      state[key] = el.value;
      render();
    });
  }

  bind(els.category, "category");
  bind(els.evidence, "evidence");
  bind(els.brand, "brand");
  bind(els.source, "source");
  bind(els.sort, "sort");
  els.search?.addEventListener("input", () => { state.query = els.search.value; render(); });

  document.addEventListener("click", event => {
    const opener = event.target.closest("[data-catalog-open],[data-catalog-id]");
    if (!opener) return;
    const id = opener.dataset.catalogOpen || opener.dataset.catalogId;
    if (!id) return;
    event.preventDefault();
    event.stopPropagation();
    openRecord(id);
  });

  document.addEventListener("keydown", event => {
    const card = event.target.closest?.("[data-catalog-id]");
    if (card && (event.key === "Enter" || event.key === " ")) {
      event.preventDefault();
      openRecord(card.dataset.catalogId);
    }
  });

  if (els.drawerContent) new MutationObserver(enhanceMediaScopes).observe(els.drawerContent, { childList: true, subtree: true });

  function html(value) {
    return String(value ?? "").replace(/[&<>"']/g, char => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;" })[char]);
  }
  function esc(value) { return html(value); }
})();
