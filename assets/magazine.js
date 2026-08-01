(() => {
  "use strict";

  const FALLBACK_PRODUCTS = [
    {"id":"demo-001","brand":"山嶼果作","name":"金鑽鳳梨果乾","category":"食品飲品","scene":"送禮","taiwan_brand":true,"verification_status":"demo_only","publication_status":"unpublished","origin_summary":"示範：台灣農產／台灣加工","score":92,"emoji":"🍍","tags":["台灣農產","台灣加工","產地可追溯"]},
    {"id":"demo-002","brand":"日常製所","name":"植萃洗碗精","category":"清潔用品","scene":"居家","taiwan_brand":true,"verification_status":"demo_only","publication_status":"unpublished","origin_summary":"示範：配方與製造資訊待查證","score":84,"emoji":"🧼","tags":["生活清潔","資料待查證"]},
    {"id":"demo-003","brand":"島嶼織品","name":"純棉擦拭巾","category":"生活用品","scene":"居家","taiwan_brand":true,"verification_status":"demo_only","publication_status":"unpublished","origin_summary":"示範：設計在台灣，原料與織造待查證","score":80,"emoji":"🧺","tags":["台灣設計","製程待查證"]},
    {"id":"demo-004","brand":"暖日茶房","name":"高山烏龍茶包","category":"食品飲品","scene":"辦公","taiwan_brand":true,"verification_status":"demo_only","publication_status":"unpublished","origin_summary":"示範：茶葉來源與包裝待查證","score":88,"emoji":"🍵","tags":["茶飲","來源待查證"]},
    {"id":"demo-005","brand":"木日生活","name":"桌上收納盒","category":"生活用品","scene":"辦公","taiwan_brand":true,"verification_status":"demo_only","publication_status":"unpublished","origin_summary":"示範：台灣設計，材料與加工待查證","score":77,"emoji":"🗃️","tags":["台灣設計","材料待查證"]},
    {"id":"demo-006","brand":"海風點心","name":"鹽花米香","category":"食品飲品","scene":"送禮","taiwan_brand":true,"verification_status":"demo_only","publication_status":"unpublished","origin_summary":"示範：原料、加工與包裝待查證","score":86,"emoji":"🍘","tags":["伴手禮","資料待查證"]}
  ];

  const state = {
    products: [],
    view: new URLSearchParams(location.search).get("view") === "published" ? "published" : "research",
    category: "全部",
    scene: "全部",
    query: "",
    sort: "score",
    favoritesOnly: false,
    favorites: new Set(JSON.parse(localStorage.getItem("taichanbao-favorites") || "[]"))
  };

  const els = {
    storyList: document.querySelector("#storyList"),
    brandTable: document.querySelector("#brandTable"),
    ranking: document.querySelector("#ranking"),
    search: document.querySelector("#globalSearch"),
    sort: document.querySelector("#sortSelect"),
    favoritesOnly: document.querySelector("#favoritesOnly"),
    favoriteCount: document.querySelector("#favoriteCount"),
    visibleCount: document.querySelector("#visibleCount"),
    researchCount: document.querySelector("#researchCount"),
    publishedCount: document.querySelector("#publishedCount"),
    currentViewLabel: document.querySelector("#currentViewLabel"),
    storyHeading: document.querySelector("#storyHeading"),
    drawer: document.querySelector("#drawer"),
    backdrop: document.querySelector("#drawerBackdrop"),
    drawerContent: document.querySelector("#drawerContent"),
    ticker: document.querySelector(".ticker"),
    tickerToggle: document.querySelector("#tickerToggle")
  };

  function publicationGate(product) {
    return product.publication_status === "published"
      && product.verification_status === "ready_for_editorial_review"
      && product.taiwan_brand === true
      && product.model_confirmed === true
      && product.current_sale_confirmed === true
      && product.origin_evidence_status === "publishable"
      && product.has_key_conflict !== true;
  }

  function saveFavorites() {
    localStorage.setItem("taichanbao-favorites", JSON.stringify([...state.favorites]));
  }

  function setView(view, updateHistory = true) {
    state.view = view;
    document.querySelectorAll("[data-view]").forEach(button => {
      button.classList.toggle("active", button.dataset.view === view);
    });
    if (updateHistory) {
      const url = new URL(location.href);
      if (view === "published") url.searchParams.set("view", "published");
      else url.searchParams.delete("view");
      history.pushState({ view }, "", url);
    }
    renderAll();
  }

  function baseProducts() {
    return state.view === "published"
      ? state.products.filter(publicationGate)
      : state.products;
  }

  function filteredProducts() {
    const query = state.query.trim().toLowerCase();
    const list = baseProducts().filter(product => {
      const matchesCategory = state.category === "全部"
        || (state.category === "台灣品牌" ? product.taiwan_brand : product.category === state.category);
      const matchesScene = state.scene === "全部" || product.scene === state.scene;
      const matchesFavorite = !state.favoritesOnly || state.favorites.has(product.id);
      const haystack = [product.name, product.brand, product.category, product.scene, product.origin_summary, ...(product.tags || [])].join(" ").toLowerCase();
      return matchesCategory && matchesScene && matchesFavorite && (!query || haystack.includes(query));
    });

    return list.sort((a, b) => {
      if (state.sort === "name") return a.name.localeCompare(b.name, "zh-Hant");
      if (state.sort === "brand") return a.brand.localeCompare(b.brand, "zh-Hant");
      if (state.sort === "category") return a.category.localeCompare(b.category, "zh-Hant");
      if (state.sort === "favorites") {
        const favoriteDifference = Number(state.favorites.has(b.id)) - Number(state.favorites.has(a.id));
        return favoriteDifference || b.score - a.score;
      }
      return b.score - a.score;
    });
  }

  function renderStories() {
    const products = filteredProducts();
    els.visibleCount.textContent = String(products.length);
    els.currentViewLabel.textContent = state.view === "published" ? "正式發布" : "研究預覽";
    els.storyHeading.textContent = state.view === "published" ? "正式發布專題" : "產品專題";

    if (!products.length) {
      const message = state.view === "published"
        ? "目前沒有通過正式發布 Gate 的產品。示範資料不會顯示在正式發布。"
        : "找不到符合條件的產品。請改用其他搜尋、分類或場景。";
      els.storyList.innerHTML = `<div class="empty">${message}</div>`;
      return;
    }

    els.storyList.innerHTML = products.map(product => {
      const favorite = state.favorites.has(product.id);
      return `<article class="story" data-product="${product.id}" tabindex="0">
        <div class="story-art">${product.emoji || "📦"}</div>
        <div><div class="story-kicker">${escapeHtml(product.brand)} · ${escapeHtml(product.category)} <span class="demo-label">${product.verification_status === "demo_only" ? "示範" : "查證"}</span></div>
        <div class="story-title">${escapeHtml(product.name)}</div><div class="story-copy">${escapeHtml(product.origin_summary)}</div></div>
        <div class="story-actions"><div class="score"><b>${Number(product.score) || 0}</b><small>展示分數</small></div>
        <button class="favorite-btn ${favorite ? "active" : ""}" type="button" data-favorite="${product.id}" aria-label="${favorite ? "取消收藏" : "加入收藏"}">${favorite ? "★" : "☆"}</button></div>
      </article>`;
    }).join("");
  }

  function renderBrands() {
    const grouped = new Map();
    filteredProducts().forEach(product => {
      const existing = grouped.get(product.brand);
      if (!existing || product.score > existing.score) grouped.set(product.brand, product);
    });
    els.brandTable.innerHTML = `<div class="brand-row head"><span>品牌</span><span>代表分類</span><span>場景</span><span>資料狀態</span></div>
      ${[...grouped.values()].map(product => `<div class="brand-row"><span class="brand-name">${escapeHtml(product.brand)}</span><span>${escapeHtml(product.category)}</span><span>${escapeHtml(product.scene)}</span><span class="status demo">${product.verification_status === "demo_only" ? "示範" : "查證中"}</span></div>`).join("") || '<div class="empty">目前檢視沒有可列出的品牌。</div>'}`;
  }

  function renderRanking() {
    const ranking = [...state.products].sort((a, b) => b.score - a.score).slice(0, 4);
    els.ranking.innerHTML = ranking.map((product, index) => `<div class="rank" data-product="${product.id}" tabindex="0"><span class="rank-num">${String(index + 1).padStart(2, "0")}</span><div><div class="rank-name">${escapeHtml(product.name)}</div><div class="rank-meta">${escapeHtml(product.brand)} · ${escapeHtml(product.scene)}</div></div><span class="rank-score">${product.score}</span></div>`).join("");
  }

  function renderCounts() {
    els.researchCount.textContent = String(state.products.length);
    els.publishedCount.textContent = String(state.products.filter(publicationGate).length);
    els.favoriteCount.textContent = String(state.favorites.size);
  }

  function renderAll() { renderCounts(); renderStories(); renderBrands(); renderRanking(); }

  function toggleFavorite(id) {
    if (state.favorites.has(id)) state.favorites.delete(id); else state.favorites.add(id);
    saveFavorites();
    renderAll();
  }

  function openProduct(id) {
    const product = state.products.find(item => item.id === id);
    if (!product) return;
    const favorite = state.favorites.has(id);
    els.drawerContent.innerHTML = `<div class="drawer-label">TAICHAN TRACE · ${escapeHtml(product.verification_status)}</div>
      <h2 id="drawerTitle">${escapeHtml(product.name)}</h2><p><strong>${escapeHtml(product.brand)}</strong><br>${escapeHtml(product.origin_summary)}</p>
      <div class="feature-meta"><span class="tag">${escapeHtml(product.category)}</span><span class="tag">${escapeHtml(product.scene)}</span><span class="tag">${product.publication_status === "published" ? "正式發布" : "未發布"}</span></div>
      <div class="drawer-actions"><button class="primary" type="button" data-favorite="${product.id}">${favorite ? "★ 已收藏" : "☆ 加入收藏"}</button><button type="button" data-scroll="method">查看發布規則</button></div>
      <div class="journey"><div class="journey-row"><span>品牌身分</span><strong>${product.taiwan_brand ? "示範標記：台灣品牌" : "待確認"}</strong></div><div class="journey-row"><span>查證狀態</span><strong>${escapeHtml(product.verification_status)}</strong></div><div class="journey-row"><span>發布狀態</span><strong>${escapeHtml(product.publication_status)}</strong></div><div class="journey-row"><span>資料標籤</span><strong>${(product.tags || []).map(escapeHtml).join("、") || "無"}</strong></div></div>
      <p><strong>重要：</strong>目前為介面示範資料，不能視為正式產地結論。正式資料必須補上來源、證據摘要、型號範圍與最後查證日期。</p>`;
    els.drawer.classList.add("open"); els.backdrop.classList.add("open"); document.body.style.overflow = "hidden"; els.drawer.querySelector("button")?.focus();
  }

  function openIntake() {
    els.drawerContent.innerHTML = `<div class="drawer-label">DATA INTAKE</div><h2 id="drawerTitle">提供品牌或產品線索</h2><p>目前可整理三類線索，但本版本不會直接將資料發布：</p><div class="journey"><div class="journey-row"><span>官方資料</span><strong>品牌官網、產品頁、公司公開資訊</strong></div><div class="journey-row"><span>實體標示</span><strong>包裝、型號、產地或製造商照片</strong></div><div class="journey-row"><span>公開來源</span><strong>政府資料、標章查詢或可信報導網址</strong></div></div><p>收到線索後仍須人工核對，不能因提交者或品牌宣稱而自動升級為正式結論。</p>`;
    els.drawer.classList.add("open"); els.backdrop.classList.add("open"); document.body.style.overflow = "hidden";
  }

  function closeDrawer() { els.drawer.classList.remove("open"); els.backdrop.classList.remove("open"); document.body.style.overflow = ""; }
  function showFavorites() { state.favoritesOnly = true; els.favoritesOnly.checked = true; setView("research"); document.querySelector("#stories").scrollIntoView({ behavior: "smooth" }); }
  function escapeHtml(value) { return String(value ?? "").replace(/[&<>"']/g, character => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"}[character])); }

  async function loadProducts() {
    try {
      const response = await fetch("data/products.demo.json", { cache: "no-store" });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      state.products = await response.json();
    } catch (error) {
      console.warn("Using embedded demo fallback:", error);
      state.products = FALLBACK_PRODUCTS;
    }
    setView(state.view, false);
  }

  document.addEventListener("click", event => {
    const favoriteButton = event.target.closest("[data-favorite]");
    if (favoriteButton) { event.stopPropagation(); toggleFavorite(favoriteButton.dataset.favorite); if (els.drawer.classList.contains("open")) openProduct(favoriteButton.dataset.favorite); return; }
    const product = event.target.closest("[data-product]");
    if (product) { openProduct(product.dataset.product); return; }
    const scroll = event.target.closest("[data-scroll]");
    if (scroll) { closeDrawer(); document.getElementById(scroll.dataset.scroll)?.scrollIntoView({ behavior: "smooth" }); return; }
    const view = event.target.closest("[data-view]");
    if (view) { setView(view.dataset.view); return; }
    const category = event.target.closest("[data-category]");
    if (category) { state.category = category.dataset.category; document.querySelectorAll("[data-category]").forEach(button => button.classList.toggle("active", button === category)); renderAll(); return; }
    const scene = event.target.closest("[data-scene]");
    if (scene) { state.scene = scene.dataset.scene; document.querySelectorAll("[data-scene]").forEach(button => button.classList.toggle("active", button === scene)); renderAll(); }
  });

  document.addEventListener("keydown", event => { if (event.key === "Escape") closeDrawer(); if (event.key === "Enter" && event.target.matches("[data-product]")) openProduct(event.target.dataset.product); });
  els.search.addEventListener("input", () => { state.query = els.search.value; renderAll(); });
  els.sort.addEventListener("change", () => { state.sort = els.sort.value; renderAll(); });
  els.favoritesOnly.addEventListener("change", () => { state.favoritesOnly = els.favoritesOnly.checked; renderAll(); });
  els.tickerToggle.addEventListener("click", () => { const paused = els.ticker.classList.toggle("paused"); els.tickerToggle.textContent = paused ? "繼續" : "暫停"; els.tickerToggle.setAttribute("aria-pressed", String(paused)); });
  document.querySelector("#searchBtn").addEventListener("click", () => document.querySelector("#stories").scrollIntoView({ behavior: "smooth" }));
  document.querySelector("#drawerClose").addEventListener("click", closeDrawer);
  els.backdrop.addEventListener("click", closeDrawer);
  document.querySelector("#openIntake").addEventListener("click", openIntake);
  document.querySelector("#showFavorites").addEventListener("click", showFavorites);
  document.querySelector("#openFavorites").addEventListener("click", showFavorites);
  document.querySelector("#mobileFavorites").addEventListener("click", showFavorites);
  addEventListener("popstate", () => { const view = new URLSearchParams(location.search).get("view") === "published" ? "published" : "research"; setView(view, false); });

  loadProducts();
})();
