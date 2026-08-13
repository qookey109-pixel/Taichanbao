(() => {
  "use strict";

  for (const href of ["assets/lifecycle-v3-2.css", "assets/enrichment-v3-4.css", "assets/deep-candidates-v3-5.css", "assets/brand-origin-v3-6.css", "assets/promotion-audit-v3-7.css"]) {
    const style = document.createElement("link");
    style.rel = "stylesheet";
    style.href = href;
    style.dataset.taichanVersion = "V3.7 Enrichment Complete 20/20";
    document.head.appendChild(style);
  }

  const catalog = document.createElement("script");
  catalog.src = "assets/catalog-v3-1.js";
  catalog.defer = true;
  catalog.dataset.taichanVersion = "V3.7 Enrichment Complete 20/20";
  catalog.addEventListener("load", () => {
    const lifecycle = document.createElement("script");
    lifecycle.src = "assets/lifecycle-v3-2.js";
    lifecycle.defer = true;
    lifecycle.dataset.taichanVersion = "V3.7 · Lifecycle";
    lifecycle.addEventListener("load", () => {
      const scale = document.createElement("script");
      scale.src = "assets/scale-v3-3.js";
      scale.defer = true;
      scale.dataset.taichanVersion = "V3.7 · Scale 100";
      scale.addEventListener("load", () => {
        const enrichment = document.createElement("script");
        enrichment.src = "assets/enrichment-v3-4.js";
        enrichment.defer = true;
        enrichment.dataset.taichanVersion = "V3.7 · Enrichment 20/20";
        enrichment.addEventListener("load", () => {
          const deep = document.createElement("script");
          deep.src = "assets/deep-candidates-v3-5.js";
          deep.defer = true;
          deep.dataset.taichanVersion = "V3.7 · Deep Candidate Gate";
          deep.addEventListener("load", () => {
            const origin = document.createElement("script");
            origin.src = "assets/brand-origin-v3-6.js";
            origin.defer = true;
            origin.dataset.taichanVersion = "V3.7 · Brand-Origin Separation";
            origin.addEventListener("load", () => {
              const audit = document.createElement("script");
              audit.src = "assets/promotion-audit-v3-7.js";
              audit.defer = true;
              audit.dataset.taichanVersion = "V3.7 Enrichment Complete 20/20";
              document.head.appendChild(audit);
            });
            document.head.appendChild(origin);
          });
          document.head.appendChild(deep);
        });
        document.head.appendChild(enrichment);
      });
      document.head.appendChild(scale);
    });
    document.head.appendChild(lifecycle);
  });
  document.head.appendChild(catalog);
})();
