(() => {
  "use strict";
  const drawerContent = document.querySelector("#drawerContent");
  if (!drawerContent) return;

  let products = [];
  fetch("data/products.demo.json", { cache: "no-store" })
    .then(response => response.ok ? response.json() : [])
    .then(rows => { products = Array.isArray(rows) ? rows : []; enhanceDrawer(); })
    .catch(() => { products = []; });

  function safeUrl(value) {
    try {
      const url = new URL(String(value || ""), location.href);
      return ["http:", "https:"].includes(url.protocol) ? url.href : "";
    } catch {
      return "";
    }
  }

  function enhanceDrawer() {
    const title = drawerContent.querySelector("#drawerTitle")?.textContent?.trim();
    if (!title || drawerContent.querySelector(".drawer-media")) return;
    const product = products.find(item => item.name === title);
    if (!product || product.verification_status !== "official_source_found") return;

    const imageUrl = safeUrl(product.image_url);
    const sourceUrl = safeUrl(product.image_source_url);
    const intro = drawerContent.querySelector("h2 + p");
    if (imageUrl && intro) {
      const figure = document.createElement("figure");
      figure.className = "drawer-media";
      const frame = document.createElement("div");
      frame.className = "drawer-media-frame";
      const image = document.createElement("img");
      image.src = imageUrl;
      image.alt = `${product.brand} ${product.name} 官方產品圖`;
      image.referrerPolicy = "no-referrer";
      image.addEventListener("error", () => {
        frame.textContent = product.emoji?.replace(/<[^>]+>/g, "") || "📦";
      }, { once: true });
      frame.appendChild(image);
      const caption = document.createElement("figcaption");
      caption.innerHTML = `圖片來源：${escapeHtml(product.image_source_name || "官方產品頁")}；權利狀態：<span class="rights-pending">待取得或確認使用授權</span>`;
      figure.append(frame, caption);
      intro.insertAdjacentElement("afterend", figure);
    }

    if (sourceUrl) {
      const source = document.createElement("div");
      source.className = "drawer-source";
      const link = document.createElement("a");
      link.href = sourceUrl;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      link.textContent = product.image_source_name || "開啟官方產品頁";
      source.append("官方來源：", link, document.createElement("br"), `查閱日期：${product.source_checked_at || "未記錄"}`);
      drawerContent.appendChild(source);
    }

    const paragraphs = drawerContent.querySelectorAll("p");
    const last = paragraphs[paragraphs.length - 1];
    if (last) {
      last.innerHTML = "<strong>重要：</strong>這是官方來源圖片候選。官方頁面可確認圖片、名稱或型號，但不代表產地已完成獨立查證；圖片權利仍待確認，因此不會進入正式發布。";
    }
  }

  function escapeHtml(value) {
    return String(value ?? "").replace(/[&<>"']/g, char => ({
      "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"
    })[char]);
  }

  new MutationObserver(enhanceDrawer).observe(drawerContent, { childList: true, subtree: true });
})();