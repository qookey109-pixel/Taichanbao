(() => {
  "use strict";

  const VERSION = "V3.0 EVIDENCE CATALOG";
  const state = {
    records: [],
    query: "",
    category: "all",
    evidence: "all",
    brand: "all",
    source: "all",
    sort: "evidence"
  };

  const els = {
    grid: document.querySelector("#catalogGrid"),
    count: document.querySelector("#catalogVisibleCount"),
    total: document.querySelector("#catalogTotal"),
    mit: document.querySelector("#mitCertifiedCount"),
    deep: document.querySelector("#deepCaseCount"),
    published: document.querySelector("#catalogPublishedCount"),
    demo: document.querySelector("#demoCount"),
    category: document.querySelector("#catalogCategoryFilter"),
    evidence: document.querySelector("#catalogEvidenceFilter"),
    brand: document.querySelector("#catalogBrandFilter"),
    source: document.querySelector("#catalogSourceFilter"),
    sort: document.querySelector("#catalogSort"),
    search: document.querySelector("#globalSearch"),
    drawer: document.querySelector("#drawer"),
    backdrop: document.querySelector("#drawerBackdrop"),
    drawerContent: document.querySelector("#drawerContent"),
    summary: document.querySelector("#catalogSummary")
  };

  boot();

  async function boot() {
    try {
      const [baseRes, overrideRes, registryRes] = await Promise.all([
        fetch("data/products.demo.json", { cache: "no-store" }),
        fetch("data/product.media.overrides.json", { cache: "no-store" }),
        fetch("data/products.registry.json", { cache: "no-store" })
      ]);
      if (!baseRes.ok || !registryRes.ok) throw new Error("catalog source unavailable");
      const base = await baseRes.json();
      const overrides = overrideRes.ok ? await overrideRes.json() : [];
      const registry = await registryRes.json();
      const overrideMap = new Map((Array.isArray(overrides) ? overrides : []).map(row => [row.id, row]));

      const deep = base
        .filter(row => row.verification_status !== "demo_only")
        .map(row => normalizeDeep(mergeRecord(row, overrideMap.get(row.id))));
      const mit = (Array.isArray(registry) ? registry : []).map(normalizeRegistry);

      state.records = [...deep, ...mit];
      updateGlobalVersion(base.filter(row => row.verification_status === "demo_only").length);
      hydrateFilters();
      render();
    } catch (error) {
      console.warn("V3 evidence catalog unavailable:", error);
      if (els.grid) els.grid.innerHTML = '<div class="catalog-empty">資料庫載入失敗，編輯專題仍可繼續使用。</div>';
    }
  }

  function mergeRecord(base, override) {
    if (!override || typeof override !== "object") return base;
    const baseMedia = base.media && typeof base.media === "object" ? base.media : {};
    const overrideMedia = override.media && typeof override.media === "object" ? override.media : {};
    return {
      ...base,
      ...override,
      media: {
        ...baseMedia,
        ...overrideMedia,
        main: overrideMedia.main || baseMedia.main,
        gallery: Array.isArray(overrideMedia.gallery) ? overrideMedia.gallery : (baseMedia.gallery || []),
        evidence: Array.isArray(overrideMedia.evidence) ? overrideMedia.evidence : (baseMedia.evidence || [])
      },
      external_evidence: Array.isArray(override.external_evidence)
        ? override.external_evidence
        : (base.external_evidence || [])
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

  function updateGlobalVersion(demoCount) {
    document.querySelectorAll(".side-note strong").forEach(node => node.textContent = VERSION);
    const edition = document.querySelector(".edition");
    if (edition) edition.textContent = "VOL. 003 · 2026 AUGUST · EVIDENCE CATALOG";
    document.querySelectorAll(".ticker-track span").forEach((node, index) => {
      const sequence = [
        "V3.0：台灣製證據資料庫上線",
        `真實研究候選 ${state.records.length} 筆`,
        `MIT 有效精確型號 ${state.records.filter(r => r.catalog_source === "mit_registry").length} 筆`,
        "台灣品牌 ≠ 台灣製造 · 必須分開查",
      ];
      node.textContent = sequence[index % sequence.length];
    });
    if (els.demo) els.demo.textContent = String(demoCount);
  }

  function hydrateFilters() {
    if (!els.category) return;
    const categories = [...new Set(state.records.map(row => row.category).filter(Boolean))].sort((a, b) => a.localeCompare(b, "zh-Hant"));
    els.category.innerHTML = '<option value="all">全部分類</option>' +
      categories.map(value => `<option value="${escapeAttr(value)}">${escapeHtml(value)}</option>`).join("");
  }

  function filtered() {
    const q = state.query.trim().toLowerCase();
    const rows = state.records.filter(row => {
      const haystack = [
        row.brand, row.company, row.name, row.model, row.category, row.scene,
        row.origin_summary, row.certification?.certificate_no, ...(row.tags || [])
      ].join(" ").toLowerCase();
      const categoryOk = state.category === "all" || row.category === state.category;
      const evidenceOk = state.evidence === "all" || row.evidence_level === state.evidence;
      const brandOk = state.brand === "all" || row.brand_origin_status === state.brand;
      const sourceOk = state.source === "all" || row.catalog_source === state.source;
      return categoryOk && evidenceOk && brandOk && sourceOk && (!q || haystack.includes(q));
    });

    return rows.sort((a, b) => {
      if (state.sort === "name") return a.name.localeCompare(b.name, "zh-Hant");
      if (state.sort === "brand") return a.brand.localeCompare(b.brand, "zh-Hant");
      if (state.sort === "valid") return String(b.certification?.valid_until || "").localeCompare(String(a.certification?.valid_until || ""));
      if (state.sort === "checked") return String(b.source_checked_at || "").localeCompare(String(a.source_checked_at || ""));
      return evidenceRank(a.evidence_level) - evidenceRank(b.evidence_level) ||
        String(b.certification?.passed_at || b.source_checked_at || "").localeCompare(String(a.certification?.passed_at || a.source_checked_at || ""));
    });
  }

  function evidenceRank(level) {
    return ({A:1,B:2,C:3,D:4})[level] || 9;
  }

  function render() {
    const rows = filtered();
    const mitCount = state.records.filter(r => r.catalog_source === "mit_registry").length;
    const deepCount = state.records.filter(r => r.catalog_source === "deep_case").length;
    const published = state.records.filter(r => r.publication_status === "published").length;

    if (els.total) els.total.textContent = String(state.records.length);
    if (els.mit) els.mit.textContent = String(mitCount);
    if (els.deep) els.deep.textContent = String(deepCount);
    if (els.published) els.published.textContent = String(published);
    if (els.count) els.count.textContent = String(rows.length);
    if (els.summary) {
      els.summary.textContent = `目前資料庫含 ${state.records.length} 筆真實研究候選：${mitCount} 筆政府 MIT 有效型號＋${deepCount} 筆深度編輯案例。正式發布仍為 ${published}。`;
    }

    if (!els.grid) return;
    if (!rows.length) {
      els.grid.innerHTML = '<div class="catalog-empty">找不到符合目前篩選條件的研究資料。</div>';
      return;
    }

    els.grid.innerHTML = rows.map(row => `
      <article class="catalog-card" data-catalog-id="${escapeAttr(row.id)}" tabindex="0">
        <div class="catalog-card-top">
          <span class="catalog-emoji" aria-hidden="true">${escapeHtml(row.emoji || "📦")}</span>
          <div class="catalog-badges">
            <span class="evidence-badge level-${escapeAttr(row.evidence_level)}">${escapeHtml(row.evidence_label)}</span>
            <span class="scope-badge">${row.catalog_source === "mit_registry" ? "政府標章" : "深度案例"}</span>
          </div>
        </div>
        <div class="catalog-kicker">${escapeHtml(row.brand || "品牌待確認")} · ${escapeHtml(row.category || "未分類")}</div>
        <h3>${escapeHtml(row.name)}</h3>
        <p class="catalog-model">${row.model ? `型號 ${escapeHtml(row.model)}` : "型號待確認"}</p>
        <p class="catalog-copy">${escapeHtml(row.origin_summary || "")}</p>
        <div class="catalog-meta">
          ${row.certification ? `<span>標章 ${escapeHtml(row.certification.certificate_no)}</span><span>有效至 ${escapeHtml(row.certification.valid_until)}</span>` : `<span>${escapeHtml(statusShort(row.manufacturing_evidence_status))}</span>`}
          <span>${escapeHtml(brandLabel(row.brand_origin_status))}</span>
        </div>
        <button class="catalog-open" type="button" data-catalog-open="${escapeAttr(row.id)}">查看證據履歷 →</button>
      </article>
    `).join("");
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

    const certification = row.certification ? `
      <section class="catalog-drawer-block">
        <h3>政府標章紀錄</h3>
        <dl class="catalog-facts">
          <div><dt>標章</dt><dd>${escapeHtml(row.certification.scheme)}</dd></div>
          <div><dt>標章編號</dt><dd>${escapeHtml(row.certification.certificate_no)}</dd></div>
          <div><dt>通過日期</dt><dd>${escapeHtml(row.certification.passed_at)}</dd></div>
          <div><dt>有效日期</dt><dd>${escapeHtml(row.certification.valid_until)}</dd></div>
          <div><dt>狀態</dt><dd>${escapeHtml(row.certification.status)}</dd></div>
        </dl>
      </section>` : "";

    const external = Array.isArray(row.external_evidence) && row.external_evidence.length ? `
      <section class="catalog-drawer-block">
        <h3>外部查證來源</h3>
        ${row.external_evidence.map(source => `<article class="catalog-source-item">
          <strong>${escapeHtml(source.title || source.source_name || "查證來源")}</strong>
          <p>${(source.findings || []).map(escapeHtml).join("、")}</p>
          ${safeUrl(source.source_url) ? `<a href="${escapeAttr(source.source_url)}" target="_blank" rel="noopener noreferrer">開啟來源 ↗</a>` : ""}
          <small>${escapeHtml(source.scope_note || "")}</small>
        </article>`).join("")}
      </section>` : "";

    els.drawerContent.innerHTML = `
      <div class="drawer-label">TAICHAN EVIDENCE CATALOG · ${escapeHtml(row.evidence_level)}</div>
      <h2 id="drawerTitle">${escapeHtml(row.name)}</h2>
      <p><strong>${escapeHtml(row.brand || "品牌待確認")}</strong><br>${escapeHtml(row.origin_summary || "")}</p>
      <div class="feature-meta">
        <span class="tag">${escapeHtml(row.category || "未分類")}</span>
        <span class="tag">${escapeHtml(row.scene || "未分類")}</span>
        <span class="tag">${escapeHtml(row.evidence_label)}</span>
      </div>
      <section class="catalog-drawer-block">
        <h3>產品識別</h3>
        <dl class="catalog-facts">
          <div><dt>產品型號</dt><dd>${escapeHtml(row.model || "待確認")}</dd></div>
          <div><dt>申請／公司</dt><dd>${escapeHtml(row.company || "待確認")}</dd></div>
          <div><dt>品牌身分</dt><dd>${escapeHtml(brandLabel(row.brand_origin_status))}</dd></div>
          <div><dt>證據範圍</dt><dd>${escapeHtml(row.record_scope === "exact_model" ? "精確型號" : row.record_scope || "待確認")}</dd></div>
          <div><dt>發布狀態</dt><dd>${escapeHtml(row.publication_status || "unpublished")}</dd></div>
          <div><dt>最後查閱</dt><dd>${escapeHtml(row.source_checked_at || "未記錄")}</dd></div>
        </dl>
      </section>
      ${certification}
      ${external}
      <section class="catalog-drawer-block">
        <h3>主要來源</h3>
        <p>${escapeHtml(row.source_name || "來源未記錄")}</p>
        ${safeUrl(row.source_url) ? `<a class="catalog-source-link" href="${escapeAttr(row.source_url)}" target="_blank" rel="noopener noreferrer">開啟原始來源 ↗</a>` : ""}
        <p class="catalog-scope-note">來源只能支持其記錄的型號與事實範圍；不得外推到同品牌其他產品。</p>
      </section>`;
    els.drawer.classList.add("open");
    els.backdrop?.classList.add("open");
    document.body.style.overflow = "hidden";
  }

  function enhanceMediaScopes() {
    if (!els.drawerContent) return;
    const title = els.drawerContent.querySelector("#drawerTitle")?.textContent?.trim();
    if (!title) return;
    const row = state.records.find(item => item.name === title);
    if (!row || !row.media) return;

    const rawMedia = [];
    if (row.media.main) rawMedia.push({ ...row.media.main, media_role: "main" });
    (row.media.gallery || []).forEach(item => rawMedia.push({ ...item, media_role: "gallery" }));
    (row.media.evidence || []).forEach(item => rawMedia.push({ ...item, media_role: "evidence" }));

    const thumbs = [...els.drawerContent.querySelectorAll(".media-thumb")];
    if (!thumbs.length) return;
    thumbs.forEach((button, index) => {
      const item = rawMedia[index];
      const small = button.querySelector("small");
      if (!item || !small) return;
      small.textContent = mediaScopeShort(item);
    });

    const activeButton = els.drawerContent.querySelector(".media-thumb.active");
    const activeIndex = activeButton ? Number(activeButton.dataset.mediaIndex) : 0;
    const active = rawMedia[Number.isInteger(activeIndex) ? activeIndex : 0];
    const gallery = els.drawerContent.querySelector(".media-gallery");
    if (!gallery || !active) return;
    gallery.querySelector(".media-scope-row")?.remove();
    const scope = document.createElement("div");
    scope.className = "media-scope-row";
    const pill = document.createElement("span");
    const exact = active.relation_scope !== "same_product_family_not_exact_model";
    pill.className = `media-scope-pill ${exact ? "exact" : "series"}`;
    pill.textContent = exact
      ? "精確型號／直接產品圖"
      : "同系列補充圖 · 不作為精確型號證據";
    scope.appendChild(pill);
    const source = gallery.querySelector(".media-architecture-source");
    if (source) source.before(scope); else gallery.appendChild(scope);
  }

  function mediaScopeShort(item) {
    if (item.media_role === "evidence") return "查證";
    if (item.relation_scope === "same_product_family_not_exact_model") return "同系列";
    if (item.media_role === "main") return "精確型號";
    return "產品圖";
  }

  function safeUrl(value) {
    try {
      const url = new URL(String(value || ""), location.href);
      return ["https:", "http:"].includes(url.protocol) ? url.href : "";
    } catch {
      return "";
    }
  }

  function bindSelect(el, key) {
    el?.addEventListener("change", () => {
      state[key] = el.value;
      render();
    });
  }

  bindSelect(els.category, "category");
  bindSelect(els.evidence, "evidence");
  bindSelect(els.brand, "brand");
  bindSelect(els.source, "source");
  bindSelect(els.sort, "sort");

  els.search?.addEventListener("input", () => {
    state.query = els.search.value;
    render();
  });

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

  if (els.drawerContent) {
    new MutationObserver(() => enhanceMediaScopes()).observe(els.drawerContent, { childList: true, subtree: true });
  }

  function escapeHtml(value) {
    return String(value ?? "").replace(/[&<>"']/g, char => ({
      "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"
    })[char]);
  }

  function escapeAttr(value) {
    return escapeHtml(value);
  }
})();