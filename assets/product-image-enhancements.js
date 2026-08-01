(() => {
  "use strict";

  const VERSION = "V2.11 TATUNG MULTI-IMAGE + TAIWAN ORIGIN EVIDENCE";
  const productsById = new Map();
  const productsByName = new Map();
  const activeMedia = new Map();
  const storyList = document.querySelector("#storyList");
  const drawerContent = document.querySelector("#drawerContent");

  updateVersionLabels();
  loadProducts();

  async function loadProducts() {
    try {
      const [baseResponse, overrideResponse] = await Promise.all([
        fetch("data/products.demo.json", { cache: "no-store" }),
        fetch("data/product.media.overrides.json", { cache: "no-store" })
      ]);
      if (!baseResponse.ok) throw new Error(`products HTTP ${baseResponse.status}`);
      const products = await baseResponse.json();
      const overrides = overrideResponse.ok ? await overrideResponse.json() : [];
      const overrideMap = new Map(
        (Array.isArray(overrides) ? overrides : []).map(item => [item.id, item])
      );

      products.forEach(product => {
        const merged = mergeProduct(product, overrideMap.get(product.id));
        productsById.set(merged.id, merged);
        productsByName.set(merged.name, merged);
      });
      enhanceCards();
      enhanceDrawer();
    } catch (error) {
      console.warn("Complete media architecture unavailable:", error);
    }
  }

  function mergeProduct(base, override) {
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

  function updateVersionLabels() {
    const version = document.querySelector(".side-note strong");
    if (version) version.textContent = VERSION;
    document.querySelectorAll(".ticker-track span").forEach(note => {
      if (
        note.textContent.includes("完整圖片架構") ||
        note.textContent.includes("6 筆示範＋4 筆官方圖片候選") ||
        note.textContent.includes("兩個多圖案例")
      ) {
        note.textContent = "三個多圖案例：TENDAYS／SAMPO／大同";
      }
    });
  }

  function enhanceCards() {
    if (!storyList || !productsById.size) return;
    storyList.querySelectorAll("[data-product]").forEach(card => {
      const product = productsById.get(card.dataset.product);
      const art = card.querySelector(".story-art");
      if (!product || !art) return;
      const main = normalizeMedia(product).main;
      if (!main || main.kind !== "image") return;
      const existing = art.querySelector("img");
      if (existing?.src === main.url) return;
      art.classList.add("has-image");
      art.replaceChildren(createImage(main, cleanEmoji(product.emoji) || "📦", "product-image"));
    });
  }

  function enhanceDrawer() {
    if (!drawerContent || !productsByName.size) return;
    const title = drawerContent.querySelector("#drawerTitle")?.textContent?.trim();
    if (!title) return;

    const product = productsByName.get(title);
    if (!product) return;

    const media = allMedia(product);
    const signature = `${product.id}:${media.length}:${(product.external_evidence || []).length}`;
    if (drawerContent.dataset.mediaSignature === signature && drawerContent.querySelector(".media-gallery")) return;
    drawerContent.dataset.mediaSignature = signature;
    drawerContent.querySelectorAll(
      ".media-gallery,.media-inventory,.media-external-evidence,.drawer-source.media-architecture-source"
    ).forEach(node => node.remove());

    const intro = drawerContent.querySelector("h2 + p");
    if (intro && media.length) {
      const currentIndex = Math.min(activeMedia.get(product.id) || 0, media.length - 1);
      activeMedia.set(product.id, currentIndex);
      intro.insertAdjacentHTML("afterend", renderGallery(product, media, currentIndex));
      bindImageFallbacks(drawerContent);
    }

    const journey = drawerContent.querySelector(".journey");
    if (journey) {
      journey.insertAdjacentHTML("afterend", renderInventory(product));
      const inventory = drawerContent.querySelector(".media-inventory");
      if (inventory) inventory.insertAdjacentHTML("afterend", renderExternalEvidence(product));
    }

    const paragraphs = drawerContent.querySelectorAll("p");
    const last = paragraphs[paragraphs.length - 1];
    if (last) {
      last.innerHTML = product.verification_status === "demo_only"
        ? "<strong>重要：</strong>目前為介面示範資料，不能視為正式產品、產地或圖片來源結論。"
        : "<strong>重要：</strong>官方圖片、品牌官方頁、官方商城、獎項與政府資料只支援各自的事實範圍；是否可正式發布仍需依實體證據、圖片權利與編輯審核判斷。";
    }
  }

  function renderGallery(product, items, activeIndex) {
    const active = items[activeIndex] || items[0];
    const viewer = active.kind === "image"
      ? `<img src="${escapeAttribute(active.url)}" alt="${escapeAttribute(active.alt)}" referrerpolicy="no-referrer" data-fallback="${escapeAttribute(cleanEmoji(product.emoji) || "📦")}">`
      : `<span class="drawer-media-placeholder" role="img" aria-label="${escapeAttribute(active.alt)}">${escapeHtml(active.emoji || "📦")}</span>`;

    const thumbnails = items.length > 1
      ? `<div class="media-thumbnails" aria-label="產品圖片選擇">${items.map((item, index) => `
          <button type="button" class="media-thumb ${index === activeIndex ? "active" : ""}"
            data-media-product="${escapeAttribute(product.id)}" data-media-index="${index}"
            aria-label="顯示${roleLabel(item.role)} ${index + 1}">
            ${item.kind === "image"
              ? `<img src="${escapeAttribute(item.url)}" alt="" loading="lazy" referrerpolicy="no-referrer" data-fallback="${escapeAttribute(cleanEmoji(product.emoji) || "📦")}">`
              : `<span>${escapeHtml(item.emoji || "📦")}</span>`}
            <small>${roleLabel(item.role)}</small>
          </button>`).join("")}</div>`
      : "";

    return `<section class="media-gallery" aria-label="產品圖片">
      <figure class="drawer-media">
        <div class="drawer-media-frame">${viewer}</div>
        <figcaption>
          <span>${escapeHtml(active.caption || active.alt || "產品圖片")}</span>
          ${active.kind === "image" ? `<span class="media-rights ${rightsClass(active.rights_status)}">${escapeHtml(rightsLabel(active.rights_status))}</span>` : ""}
        </figcaption>
      </figure>
      ${thumbnails}
      ${renderSource(active)}
    </section>`;
  }

  function renderSource(item) {
    if (!item || item.kind !== "image") return "";
    const source = item.source_url
      ? `<a href="${escapeAttribute(item.source_url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(item.source_name || "開啟圖片來源")}</a>`
      : escapeHtml(item.source_name || "來源未記錄");
    return `<div class="drawer-source media-architecture-source">
      <strong>目前圖片來源</strong><br>
      ${source}<br>
      類型：${escapeHtml(item.source_type || "未分類")}<br>
      查閱日期：${escapeHtml(item.checked_at || "未記錄")}
    </div>`;
  }

  function renderInventory(product) {
    const media = normalizeMedia(product);
    return `<section class="media-inventory">
      <h3>圖片資料結構</h3>
      <div>
        <span><b>${media.main ? 1 : 0}</b>主圖</span>
        <span><b>${media.gallery.length}</b>圖片集</span>
        <span><b>${media.evidence.length}</b>查證照片</span>
      </div>
      <p>主圖用於卡片；圖片集保存其他角度與功能；查證照片專門保存型號、產地、製造商與標章。</p>
    </section>`;
  }

  function renderExternalEvidence(product) {
    const records = Array.isArray(product.external_evidence) ? product.external_evidence : [];
    if (!records.length) return "";
    return `<section class="drawer-source media-external-evidence">
      <strong>外部查證紀錄</strong>
      ${records.map(record => {
        const source = safeUrl(record.source_url)
          ? `<a href="${escapeAttribute(record.source_url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(record.source_name || record.title || "開啟來源")}</a>`
          : escapeHtml(record.source_name || record.title || "來源未記錄");
        const facts = Array.isArray(record.findings) && record.findings.length
          ? `<ul>${record.findings.map(item => `<li>${escapeHtml(item)}</li>`).join("")}</ul>`
          : "";
        return `<article>
          <p><b>${escapeHtml(record.title || "查證紀錄")}</b><br>${source}</p>
          ${facts}
          <p>證據範圍：${escapeHtml(record.scope_note || "未記錄")}<br>
          查閱日期：${escapeHtml(record.checked_at || "未記錄")}</p>
        </article>`;
      }).join("")}
    </section>`;
  }

  function normalizeMedia(product) {
    const raw = product.media && typeof product.media === "object" ? product.media : {};
    const legacyMain = product.image_url ? {
      kind: "image",
      url: product.image_url,
      alt: `${product.brand || ""} ${product.name || ""} 產品主圖`.trim(),
      source_url: product.image_source_url || "",
      source_name: product.image_source_name || "",
      source_type: product.image_source_type || "",
      rights_status: product.image_rights_status || "unknown",
      checked_at: product.source_checked_at || ""
    } : {
      kind: "placeholder",
      emoji: cleanEmoji(product.emoji) || "📦",
      alt: `${product.name || "產品"}圖示`,
      rights_status: "not_applicable"
    };

    return {
      main: normalizeItem(raw.main || legacyMain, product, "main"),
      gallery: normalizeList(raw.gallery, product, "gallery"),
      evidence: normalizeList(raw.evidence, product, "evidence")
    };
  }

  function normalizeList(value, product, role) {
    if (!Array.isArray(value)) return [];
    return value.map(item => normalizeItem(item, product, role)).filter(Boolean);
  }

  function normalizeItem(item, product, role) {
    if (!item || typeof item !== "object") return null;
    if (item.kind === "placeholder" || (!item.url && item.emoji)) {
      return {
        kind: "placeholder",
        emoji: cleanEmoji(item.emoji) || cleanEmoji(product.emoji) || "📦",
        alt: String(item.alt || `${product.name || "產品"}圖示`),
        rights_status: "not_applicable",
        role
      };
    }
    const url = safeUrl(item.url);
    if (!url) return null;
    return {
      kind: "image",
      url,
      alt: String(item.alt || `${product.brand || ""} ${product.name || ""} 圖片`).trim(),
      caption: String(item.caption || ""),
      source_url: safeUrl(item.source_url),
      source_name: String(item.source_name || ""),
      source_type: String(item.source_type || ""),
      rights_status: String(item.rights_status || "unknown"),
      checked_at: String(item.checked_at || ""),
      role
    };
  }

  function allMedia(product) {
    const media = normalizeMedia(product);
    const result = [];
    if (media.main) result.push({ ...media.main, role: "main" });
    media.gallery.forEach(item => result.push({ ...item, role: "gallery" }));
    media.evidence.forEach(item => result.push({ ...item, role: "evidence" }));
    return result;
  }

  function createImage(item, fallbackEmoji, className) {
    const image = document.createElement("img");
    image.className = className;
    image.src = item.url;
    image.alt = item.alt;
    image.loading = "lazy";
    image.referrerPolicy = "no-referrer";
    image.dataset.fallback = fallbackEmoji;
    image.addEventListener("error", replaceWithFallback, { once: true });
    return image;
  }

  function bindImageFallbacks(root) {
    root.querySelectorAll("img[data-fallback]").forEach(image => {
      image.addEventListener("error", replaceWithFallback, { once: true });
    });
  }

  function replaceWithFallback(event) {
    const image = event.currentTarget;
    const fallback = document.createElement("span");
    fallback.className = image.closest(".drawer-media-frame") ? "drawer-media-placeholder" : "image-fallback";
    fallback.setAttribute("role", "img");
    fallback.setAttribute("aria-label", "圖片載入失敗，顯示替代圖示");
    fallback.textContent = image.dataset.fallback || "📦";
    image.replaceWith(fallback);
  }

  function switchMedia(productId, index) {
    const product = productsById.get(productId);
    const items = product ? allMedia(product) : [];
    if (!product || !Number.isInteger(index) || index < 0 || index >= items.length) return;
    activeMedia.set(productId, index);
    drawerContent.dataset.mediaSignature = "";
    enhanceDrawer();
  }

  function safeUrl(value) {
    try {
      const url = new URL(String(value || ""), location.href);
      return ["http:", "https:"].includes(url.protocol) ? url.href : "";
    } catch {
      return "";
    }
  }

  function cleanEmoji(value) {
    const text = String(value || "").replace(/<[^>]*>/g, "").trim();
    return text && text.length <= 8 ? text : "";
  }

  function rightsLabel(status) {
    return ({
      permission_pending: "權利待確認",
      permission_granted: "已取得使用許可",
      owned: "自有圖片",
      public_domain: "公有領域",
      creative_commons: "Creative Commons",
      not_applicable: "不適用",
      unknown: "權利未知"
    })[status] || "權利未知";
  }

  function rightsClass(status) {
    if (["permission_granted", "owned", "public_domain", "creative_commons"].includes(status)) return "rights-ok";
    if (status === "not_applicable") return "rights-na";
    return "rights-pending";
  }

  function roleLabel(role) {
    return role === "evidence" ? "查證" : role === "gallery" ? "圖片" : "主圖";
  }

  function escapeHtml(value) {
    return String(value ?? "").replace(/[&<>"']/g, char => ({
      "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"
    })[char]);
  }

  function escapeAttribute(value) {
    return escapeHtml(value);
  }

  document.addEventListener("click", event => {
    const button = event.target.closest("[data-media-product]");
    if (!button) return;
    event.preventDefault();
    event.stopPropagation();
    switchMedia(button.dataset.mediaProduct, Number(button.dataset.mediaIndex));
  });

  if (storyList) new MutationObserver(enhanceCards).observe(storyList, { childList: true, subtree: true });
  if (drawerContent) new MutationObserver(enhanceDrawer).observe(drawerContent, { childList: true, subtree: true });
})();