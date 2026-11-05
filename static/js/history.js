/* ══════════════════════════════════════════════
   AgroScan — SQLite Scan Archive Page Logic
   ══════════════════════════════════════════════ */

let historyRows = [];
let historyFilter = "";

document.addEventListener("DOMContentLoaded", async () => {
  await loadHistory();

  const searchEl = document.getElementById("history-search");
  if (searchEl) {
    searchEl.addEventListener("input", e => {
      historyFilter = e.target.value.toLowerCase();
      renderHistory();
    });
  }

  window.addEventListener("langchange", () => renderHistory());
});

async function loadHistory() {
  historyRows = Store.historyRows();
  renderHistory();
}

function renderHistory() {
  const tbody = document.getElementById("history-tbody");

  const total = historyRows.length;
  const critical = historyRows.filter(r => r.severity === "critical" || r.severity === "high").length;
  const moderate = historyRows.filter(r => r.severity === "moderate").length;
  const healthy = historyRows.filter(r => r.severity === "none").length;

  document.getElementById("stat-total").textContent = total;
  document.getElementById("stat-critical").textContent = critical;
  document.getElementById("stat-moderate").textContent = moderate;
  document.getElementById("stat-healthy").textContent = healthy;

  const filtered = historyRows.filter(r => {
    if (!historyFilter) return true;
    return (
      (r.name_en && r.name_en.toLowerCase().includes(historyFilter)) ||
      (r.name_ta && r.name_ta.toLowerCase().includes(historyFilter)) ||
      (r.crop && r.crop.toLowerCase().includes(historyFilter)) ||
      (r.scan_id && r.scan_id.toLowerCase().includes(historyFilter)) ||
      (r.notes && r.notes.toLowerCase().includes(historyFilter))
    );
  });

  if (filtered.length === 0) {
    const emptyMsg = currentLang === "ta"
      ? "இன்னும் ஸ்கேன் பதிவுகள் இல்லை. புதிய இலையை ஸ்கேன் செய்யவும்!"
      : "No scans found in your SQLite archive yet. Upload a leaf or try a sample specimen!";
    tbody.innerHTML = `
      <tr>
        <td colspan="7" class="empty-state">
          <div class="empty-icon">🌿</div>
          <p>${emptyMsg}</p>
        </td>
      </tr>
    `;
    return;
  }

  const viewText = currentLang === "ta" ? "விவரம் →" : "Open →";

  tbody.innerHTML = filtered.map((r, idx) => {
    const name = currentLang === "ta" ? r.name_ta : r.name_en;
    const statusIcon = r.status === "Resolved" ? "✅" : r.status === "Treating" ? "🚿" : "🔍";
    return `
      <tr>
        <td style="font-family:var(--font-mono);color:var(--text-muted);">${idx + 1}</td>
        <td>
          <div style="display:flex;align-items:center;gap:12px;">
            <span style="font-size:1.5rem;">${r.emoji}</span>
            <div>
              <div style="font-weight:600;color:var(--text-primary);">${name}</div>
              <div style="font-size:0.74rem;color:var(--text-muted);font-family:var(--font-mono);">
                ${r.crop || "Crop"} &bull; #${r.scan_id}
              </div>
            </div>
          </div>
        </td>
        <td style="color:var(--text-secondary);font-size:0.82rem;">${formatDate(r.timestamp)}</td>
        <td>
          <span style="font-family:var(--font-mono);font-weight:600;color:var(--accent-primary);">
            ${r.confidence}%
          </span>
        </td>
        <td>${getSeverityBadge(r.severity, currentLang)}</td>
        <td style="max-width:200px;">
          <div style="font-size:0.78rem;font-weight:600;color:var(--text-secondary);">${statusIcon} ${r.status || "Monitoring"}</div>
          ${r.notes ? `<div style="font-size:0.74rem;color:var(--text-muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">"${r.notes}"</div>` : ""}
        </td>
        <td style="text-align:right;white-space:nowrap;">
          <a href="/result?id=${r.scan_id}" class="btn btn-outline btn-sm">${viewText}</a>
          <button class="btn btn-outline btn-sm" style="margin-left:4px;padding:6px 10px;" title="Delete scan" onclick="deleteScan('${r.scan_id}')">✕</button>
        </td>
      </tr>
    `;
  }).join("");
}

async function deleteScan(scanId) {
  Store.deleteScan(scanId);
  historyRows = Store.historyRows();
  renderHistory();
  showToast(currentLang === "ta" ? "பதிவு நீக்கப்பட்டது" : "Scan deleted from archive", "info");
}

async function clearAllHistory() {
  if (historyRows.length === 0) return;
  const confirmMsg = currentLang === "ta"
    ? "அனைத்து ஸ்கேன் பதிவுகளையும் அழிக்க விரும்புகிறீர்களா?"
    : "Are you sure you want to clear all scan records from your archive?";
  if (!confirm(confirmMsg)) return;

  Store.clearScans();
  historyRows = [];
  renderHistory();
  showToast(currentLang === "ta" ? "காப்பகம் அழிக்கப்பட்டது" : "Scan archive cleared", "info");
}
