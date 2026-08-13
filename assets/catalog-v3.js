(() => {
  "use strict";

  const style = document.createElement("link");
  style.rel = "stylesheet";
  style.href = "assets/lifecycle-v3-2.css";
  style.dataset.taichanVersion = "V3.3 Registry Scale 100";
  document.head.appendChild(style);

  const catalog = document.createElement("script");
  catalog.src = "assets/catalog-v3-1.js";
  catalog.defer = true;
  catalog.dataset.taichanVersion = "V3.3 Registry Scale 100";
  catalog.addEventListener("load", () => {
    const lifecycle = document.createElement("script");
    lifecycle.src = "assets/lifecycle-v3-2.js";
    lifecycle.defer = true;
    lifecycle.dataset.taichanVersion = "V3.3 Registry Scale 100 · Lifecycle";
    document.head.appendChild(lifecycle);
  });
  document.head.appendChild(catalog);
})();
