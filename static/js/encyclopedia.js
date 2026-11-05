/* ══════════════════════════════════════════════
   AgroScan — 42-Class SQLite Disease Encyclopedia Logic
   ══════════════════════════════════════════════ */

let encyList = [];
let activeSev = "all";
let activeCrop = "all";
let searchQuery = "";
let activeModalItem = null;

document.addEventListener("DOMContentLoaded", async () => {
  await loadEncyclopedia();

  const searchInput = document.getElementById("ency-search");
  searchInput.addEventListener("input", e => {
    searchQuery = e.target.value.toLowerCase();
    renderEncyclopedia();
  });

  document.querySelectorAll("#sev-filters button").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll("#sev-filters button").forEach(b => {
        b.className = "btn btn-outline btn-sm";
      });
      btn.className = "btn btn-primary btn-sm";
      activeSev = btn.getAttribute("data-sev");
      renderEncyclopedia();
    });
  });

  // Modal close handlers
  const modal = document.getElementById("ency-modal");
  document.getElementById("modal-close").addEventListener("click", () => {
    if ("speechSynthesis" in window) window.speechSynthesis.cancel();
    modal.classList.remove("open");
  });
  modal.addEventListener("click", e => {
    if (e.target === modal) {
      if ("speechSynthesis" in window) window.speechSynthesis.cancel();
      modal.classList.remove("open");
    }
  });

  window.addEventListener("langchange", () => {
    renderCropFilters();
    renderEncyclopedia();
    if (activeModalItem && modal.classList.contains("open")) {
      openModal(activeModalItem.class_id);
    }
  });
});

async function loadEncyclopedia() {
  try {
    const res = await fetch("/api/encyclopedia");
    encyList = await res.json();
    renderCropFilters();
    renderEncyclopedia();
  } catch (err) {
    showToast("Failed to load encyclopedia", "error");
  }
}

function renderCropFilters() {
  const container = document.getElementById("crop-filters");
  if (!container) return;
  const crops = Array.from(new Set(encyList.map(i => i.crop))).sort();

  const allLabel = currentLang === "ta" ? `🌾 அனைத்து பயிர்கள் (${encyList.length})` : `🌾 All 17 Crops (${encyList.length})`;
  let html = `<button class="chip ${activeCrop === 'all' ? 'active-chip' : ''}"
                style="${activeCrop === 'all' ? 'background:var(--accent-primary);color:#fff;border-color:var(--accent-primary);' : ''}"
                onclick="selectCropFilter('all')">${allLabel}</button>`;

  crops.forEach(c => {
    const isSel = activeCrop === c;
    const style = isSel ? "background:var(--accent-primary);color:#fff;border-color:var(--accent-primary);" : "";
    html += `<button class="chip" style="${style}" onclick="selectCropFilter('${c.replace(/'/g, "\\'")}')">${c}</button>`;
  });
  container.innerHTML = html;
}

function selectCropFilter(crop) {
  activeCrop = crop;
  renderCropFilters();
  renderEncyclopedia();
}

function renderEncyclopedia() {
  const grid = document.getElementById("ency-grid");
  const countLabel = document.getElementById("ency-count-label");

  const filtered = encyList.filter(item => {
    const d = item[currentLang] || item.en;
    const sevMatch = activeSev === "all" || d.severity === activeSev;
    const cropMatch = activeCrop === "all" || item.crop === activeCrop;
    const textMatch = !searchQuery ||
      d.name.toLowerCase().includes(searchQuery) ||
      d.cause.toLowerCase().includes(searchQuery) ||
      d.symptoms.toLowerCase().includes(searchQuery) ||
      (item.crop && item.crop.toLowerCase().includes(searchQuery)) ||
      item.en.name.toLowerCase().includes(searchQuery);
    return sevMatch && cropMatch && textMatch;
  });

  if (countLabel) {
    countLabel.textContent = currentLang === "ta"
      ? `${filtered.length} / ${encyList.length} நோய் வகைகள்`
      : `Showing ${filtered.length} of ${encyList.length} SQLite classes`;
  }

  grid.innerHTML = filtered.map(item => {
    const d = item[currentLang] || item.en;
    return `
      <div class="card ency-card" onclick="openModal('${item.class_id}')">
        <div style="display:flex;align-items:center;justify-content:space-between;">
          <div style="display:flex;align-items:center;gap:8px;">
            <span class="ency-emoji">${d.emoji}</span>
            <span style="font-size:0.72rem;font-family:var(--font-mono);padding:3px 8px;border-radius:6px;background:var(--bg-elevated);color:var(--text-secondary);">
              ${item.crop}
            </span>
          </div>
          ${getSeverityBadge(d.severity, currentLang)}
        </div>
        <div class="ency-name" style="margin-top:6px;">${d.name}</div>
        <div class="ency-cause">${d.cause}</div>
        <p style="font-size:0.82rem;color:var(--text-secondary);line-height:1.5;margin-top:4px;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;">
          ${d.symptoms}
        </p>
        <div style="margin-top:auto;padding-top:10px;display:flex;align-items:center;justify-content:space-between;font-size:0.76rem;color:var(--accent-primary);font-weight:600;">
          <span>${currentLang === "ta" ? "முழு சிகிச்சை & தடுப்பு →" : "Full Treatment & Prevention →"}</span>
          <span style="font-family:var(--font-mono);color:var(--text-muted);font-weight:400;">⏱️ ${d.recovery || "10–14d"}</span>
        </div>
      </div>
    `;
  }).join("");
}

function openModal(classId) {
  const item = encyList.find(x => x.class_id === classId);
  if (!item) return;
  activeModalItem = item;
  const d = item[currentLang] || item.en;
  const modal = document.getElementById("ency-modal");
  const body = document.getElementById("modal-body");

  const labels = currentLang === "ta" ? {
    symptoms: "🔍 அறிகுறிகள்",
    immediate: "⚡ உடனடி நடவடிக்கை",
    organic: "🌿 இயற்கை தீர்வு",
    chemical: "🧪 வேதியியல் கட்டுப்பாடு",
    prevention: "🛡️ நீண்டகால தடுப்பு",
    weather: "🌦️ சாதகமான வானிலை",
    recovery: "⏱️ மீட்பு காலம்",
    listen: "🔊 குரலில் கேட்க"
  } : {
    symptoms: "🔍 Symptoms",
    immediate: "⚡ Immediate Action",
    organic: "🌿 Organic Remedy",
    chemical: "🧪 Chemical Control",
    prevention: "🛡️ Long-Term Prevention",
    weather: "🌦️ Favorable Weather Trigger",
    recovery: "⏱️ Expected Recovery",
    listen: "🔊 Listen Advisory"
  };

  body.innerHTML = `
    <div style="display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap;margin-bottom:16px;padding-right:28px;">
      <div style="display:flex;align-items:center;gap:14px;">
        <span style="font-size:2.6rem;">${d.emoji}</span>
        <div>
          <span style="font-size:0.72rem;font-family:var(--font-mono);color:var(--accent-primary);text-transform:uppercase;">${item.crop}</span>
          <h2 style="font-family:var(--font-serif);font-size:1.35rem;font-weight:700;">${d.name}</h2>
          <div style="font-size:0.82rem;color:var(--text-muted);font-style:italic;">${d.cause}</div>
        </div>
      </div>
      <div style="display:flex;align-items:center;gap:8px;">
        <button class="btn btn-outline btn-sm" onclick="speakEncyModal(this)">${labels.listen}</button>
        ${getSeverityBadge(d.severity, currentLang)}
      </div>
    </div>

    <div style="display:flex;flex-direction:column;gap:12px;">
      <div style="padding:12px 14px;background:var(--bg-base);border-radius:10px;border:1px solid var(--border-default);">
        <div style="font-size:0.75rem;font-family:var(--font-mono);color:var(--accent-primary);margin-bottom:4px;">${labels.symptoms}</div>
        <div style="font-size:0.88rem;line-height:1.55;">${d.symptoms}</div>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
        <div style="padding:10px 12px;background:var(--bg-base);border-radius:10px;border:1px solid var(--border-subtle);">
          <div style="font-size:0.72rem;font-family:var(--font-mono);color:var(--text-muted);">${labels.weather}</div>
          <div style="font-size:0.82rem;margin-top:3px;font-weight:500;">${d.weather || "Warm humid weather"}</div>
        </div>
        <div style="padding:10px 12px;background:var(--bg-base);border-radius:10px;border:1px solid var(--border-subtle);">
          <div style="font-size:0.72rem;font-family:var(--font-mono);color:var(--text-muted);">${labels.recovery}</div>
          <div style="font-size:0.82rem;margin-top:3px;font-weight:600;color:var(--accent-primary);">${d.recovery || "10–14 days"}</div>
        </div>
      </div>

      <div style="padding:12px 14px;background:var(--bg-base);border-radius:10px;border:1px solid var(--border-default);">
        <div style="font-size:0.75rem;font-family:var(--font-mono);color:var(--accent-amber);margin-bottom:4px;">${labels.immediate}</div>
        <div style="font-size:0.88rem;line-height:1.55;">${d.immediate}</div>
      </div>

      <div style="padding:12px 14px;background:var(--bg-base);border-radius:10px;border:1px solid var(--border-default);">
        <div style="font-size:0.75rem;font-family:var(--font-mono);color:var(--accent-primary);margin-bottom:4px;">${labels.organic}</div>
        <div style="font-size:0.88rem;line-height:1.55;">${d.organic}</div>
      </div>

      <div style="padding:12px 14px;background:var(--bg-base);border-radius:10px;border:1px solid var(--border-default);">
        <div style="font-size:0.75rem;font-family:var(--font-mono);color:var(--accent-danger);margin-bottom:4px;">${labels.chemical}</div>
        <div style="font-size:0.88rem;line-height:1.55;">${d.chemical}</div>
      </div>

      <div style="padding:12px 14px;background:var(--bg-base);border-radius:10px;border:1px solid var(--border-default);">
        <div style="font-size:0.75rem;font-family:var(--font-mono);color:var(--text-secondary);margin-bottom:4px;">${labels.prevention}</div>
        <div style="font-size:0.88rem;line-height:1.55;">${d.prevention || "Practice crop rotation and field sanitation."}</div>
      </div>
    </div>
  `;

  modal.classList.add("open");
}

function speakEncyModal(btnEl) {
  if (!activeModalItem) return;
  const d = activeModalItem[currentLang] || activeModalItem.en;
  const text = `${d.name}. ${d.cause}. ${d.symptoms}. ${d.immediate}. ${d.organic}`;
  speakAdvisory(text, currentLang, btnEl);
}
