(() => {
  "use strict";

  for (const href of ["assets/lifecycle-v3-2.css", "assets/enrichment-v3-4.css", "assets/deep-candidates-v3-5.css", "assets/brand-origin-v3-6.css"]) {
    const style = document.createElement("link");
    style.rel = "stylesheet";
    style.href = href;
    style.dataset.taichanVersion = "V3.6 Brand-Origin Separation";
    document.head.appendChild(style);
  }

  const catalog = document.createElement("script");
  catalog.src = "assets/catalog-v3-1.js";
  catalog.defer = true;
  catalog.dataset.taichanVersion = "V3.6 Brand-Origin Separation";
  catalog.addEventListener("load", () => {
    const lifecycle = document.createElement("script");
    lifecycle.src = "assets/lifecycle-v3-2.js";
    lifecycle.defer = true;
    lifecycle.dataset.taichanVersion = "V3.6 · Lifecycle";
    lifecycle.addEventListener("load", () => {
      const scale = document.createElement("script");
      scale.src = "assets/scale-v3-3.js";
      scale.defer = true;
      scale.dataset.taichanVersion = "V3.6 · Scale 100";
      scale.addEventListener("load", () => {
        const enrichment = document.createElement("script");
        enrichment.src = "assets/enrichment-v3-4.js";
        enrichment.defer = true;
        enrichment.dataset.taichanVersion = "V3.6 · Enrichment 15/20";
        enrichment.addEventListener("load", () => {
          const deep = document.createElement("script");
          deep.src = "assets/deep-candidates-v3-5.js";
          deep.defer = true;
          deep.dataset.taichanVersion = "V3.6 · Deep Candidate Gate";
          deep.addEventListener("load", () => {
            const origin = document.createElement("script");
            origin.src = "assets/brand-origin-v3-6.js";
            origin.defer = true;
            origin.dataset.taichanVersion = "V3.6 Brand-Origin Separation";
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
