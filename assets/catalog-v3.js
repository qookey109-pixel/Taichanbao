(() => {
  "use strict";

  for (const href of ["assets/lifecycle-v3-2.css", "assets/enrichment-v3-4.css", "assets/deep-candidates-v3-5.css"]) {
    const style = document.createElement("link");
    style.rel = "stylesheet";
    style.href = href;
    style.dataset.taichanVersion = "V3.5 Deep Candidate Gate";
    document.head.appendChild(style);
  }

  const catalog = document.createElement("script");
  catalog.src = "assets/catalog-v3-1.js";
  catalog.defer = true;
  catalog.dataset.taichanVersion = "V3.5 Deep Candidate Gate";
  catalog.addEventListener("load", () => {
    const lifecycle = document.createElement("script");
    lifecycle.src = "assets/lifecycle-v3-2.js";
    lifecycle.defer = true;
    lifecycle.dataset.taichanVersion = "V3.5 · Lifecycle";
    lifecycle.addEventListener("load", () => {
      const scale = document.createElement("script");
      scale.src = "assets/scale-v3-3.js";
      scale.defer = true;
      scale.dataset.taichanVersion = "V3.5 · Scale 100";
      scale.addEventListener("load", () => {
        const enrichment = document.createElement("script");
        enrichment.src = "assets/enrichment-v3-4.js";
        enrichment.defer = true;
        enrichment.dataset.taichanVersion = "V3.5 · Enrichment P1 Complete";
        enrichment.addEventListener("load", () => {
          const deep = document.createElement("script");
          deep.src = "assets/deep-candidates-v3-5.js";
          deep.defer = true;
          deep.dataset.taichanVersion = "V3.5 Deep Candidate Gate";
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
