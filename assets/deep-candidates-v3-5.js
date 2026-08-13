(() => {
  "use strict";
  boot();

  async function j(url){const r=await fetch(url,{cache:"no-store"});if(!r.ok)throw new Error(`${url} HTTP ${r.status}`);return r.json();}
  async function boot(){try{const [payload,catalog]=await Promise.all([j("data/deep_case.candidates.json"),j("data/catalog.public.json")]);const records=new Map((catalog.records||[]).map(r=>[r.id,r]));inject(payload,records);updateVersion();}catch(e){console.warn("V3.5 deep candidate gate unavailable",e);}}

  function inject(payload,records){if(document.querySelector("#deepCandidates"))return;const anchor=document.querySelector("#enrichment")||document.querySelector("#lifecycle")||document.querySelector("#database");if(!anchor)return;const items=payload.items||[];const section=document.createElement("section");section.id="deepCandidates";section.className="deep-candidate-section sans";section.innerHTML=`
    <div class="deep-candidate-head"><div><div class="deep-candidate-kicker">V3.5 · DEEP CANDIDATE GATE</div><h2>證據夠強，<br>也不代表可以直接發布。</h2><p>這一層只收「值得升級成深度專題」的候選。品牌、精確型號、製造證據、現售與官方頁先通過；圖片權利、編輯審核或任何重大衝突仍可阻擋 promotion。</p></div><div class="deep-candidate-status"><b>CANDIDATE STATUS</b><strong>${items.length} 筆候選</strong><span>${items.filter(i=>i.candidate_status.startsWith("blocked")).length} 筆目前被 Gate 阻擋 · 正式發布 0</span></div></div>
    <div class="deep-candidate-grid">${items.map(i=>card(i,records.get(i.source_record_id)||{})).join("")}</div>
    <div class="deep-candidate-note">Deep candidate 不是正式 deep editorial case，也不是 publication。只有所有必要 Gate 通過後，才可進下一層人工編輯審核。</div>`;
    anchor.after(section);
    section.addEventListener("click",ev=>{if(ev.target.closest("a"))return;const card=ev.target.closest("[data-catalog-id]");if(card){document.querySelector(`[data-catalog-open="${CSS.escape(card.dataset.catalogId)}"]`)?.click();}});
  }

  function card(i,r){const gate=i.gate||{};const sources=i.evidence||[];return `<article class="deep-candidate-card" data-catalog-id="${h(i.source_record_id)}" tabindex="0"><div class="deep-candidate-card-top"><div><div class="deep-candidate-model">${h(i.brand)} · ${h(i.model)}</div><h3>${h(i.name)}</h3><p>${h(i.why_selected)}</p></div><span class="deep-candidate-badge">${h(statusLabel(i.candidate_status))}</span></div><div class="deep-gates">${Object.entries(gate).map(([k,v])=>`<span class="deep-gate ${gateClass(v)}"><b>${h(gateLabel(k))}</b><br>${h(valueLabel(v))}</span>`).join("")}</div><div class="deep-blockers"><strong>目前阻擋原因</strong><ul>${(i.blocking_reasons||[]).map(x=>`<li>${h(x)}</li>`).join("")}</ul></div><div class="deep-evidence-links">${sources.map(s=>`<a href="${attr(s.source_url)}" target="_blank" rel="noopener noreferrer">${h(s.source_name)} ↗</a>`).join("")}</div>${r.official_product_page_url?`<div class="deep-candidate-note">Public catalog 已保存精確型號官方頁；publication_status 仍為 ${h(r.publication_status||"unpublished")}。</div>`:""}</article>`;}

  function updateVersion(){document.querySelectorAll(".side-note strong").forEach(n=>n.textContent="V3.5 DEEP CANDIDATE GATE");const e=document.querySelector(".edition");if(e)e.textContent="VOL. 003 · 2026 AUGUST · DEEP CANDIDATE GATE";}
  function gateClass(v){if(String(v).startsWith("pass"))return"pass";if(v==="blocked")return"blocked";return"pending";}
  function gateLabel(k){return({brand_identity:"品牌身分",exact_model_identity:"精確型號",mit_manufacturing_evidence:"MIT 製造證據",current_sale_or_supply:"現售／供應",exact_official_product_page:"官方型號頁",key_conflict_review:"重大衝突",image_rights:"圖片權利",editorial_review:"編輯審核",formal_publication:"正式發布"})[k]||k;}
  function valueLabel(v){return({pass:"PASS",pass_no_conflict_found:"PASS · 未見重大衝突",blocked:"BLOCKED",pending:"PENDING"})[v]||v;}
  function statusLabel(v){return({blocked_assets:"候選 · 圖片權利阻擋"})[v]||v;}
  function h(v){return String(v??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"})[c]);}
  function attr(v){const s=String(v||"");return s.startsWith("https://")?h(s):"#";}
})();
