/* ══════════════════════════════════════════════
   AgroScan — Leaf Upload, Camera Capture, 1-Click Sample Scan & Archive Preview
   ══════════════════════════════════════════════ */

let selectedFile = null;
let recentScansCache = [];

document.addEventListener("DOMContentLoaded", () => {
  const dropZone = document.getElementById("drop-zone");
  const fileInput = document.getElementById("file-input");
  const cameraInput = document.getElementById("camera-input");
  const previewWrap = document.getElementById("preview-wrap");
  const previewImg = document.getElementById("preview-img");
  const previewRemove = document.getElementById("preview-remove");
  const scanBtn = document.getElementById("scan-btn");
  const scanLoader = document.getElementById("scan-loader");

  // Click to browse
  dropZone.addEventListener("click", () => fileInput.click());

  // Drag & Drop events
  ["dragenter", "dragover"].forEach(evt => {
    dropZone.addEventListener(evt, e => {
      e.preventDefault();
      e.stopPropagation();
      dropZone.classList.add("dragover");
    });
  });

  ["dragleave", "drop"].forEach(evt => {
    dropZone.addEventListener(evt, e => {
      e.preventDefault();
      e.stopPropagation();
      dropZone.classList.remove("dragover");
    });
  });

  dropZone.addEventListener("drop", e => {
    const files = e.dataTransfer.files;
    if (files && files.length > 0) handleFile(files[0]);
  });

  fileInput.addEventListener("change", e => {
    if (e.target.files && e.target.files.length > 0) {
      handleFile(e.target.files[0]);
    }
  });

  if (cameraInput) {
    cameraInput.addEventListener("change", e => {
      if (e.target.files && e.target.files.length > 0) {
        handleFile(e.target.files[0]);
      }
    });
  }

  function handleFile(file) {
    if (!file.type.startsWith("image/")) {
      showToast(currentLang === "ta" ? "படக் கோப்பை மட்டும் பதிவேற்றவும்" : "Please upload a valid image file (JPG, PNG, WEBP)", "error");
      return;
    }
    selectedFile = file;
    const reader = new FileReader();
    reader.onload = ev => {
      previewImg.src = ev.target.result;
      previewWrap.style.display = "block";
      dropZone.style.display = "none";
      scanBtn.disabled = false;
    };
    reader.readAsDataURL(file);
  }

  previewRemove.addEventListener("click", () => {
    selectedFile = null;
    fileInput.value = "";
    if (cameraInput) cameraInput.value = "";
    previewWrap.style.display = "none";
    dropZone.style.display = "block";
    scanBtn.disabled = true;
  });

  // Submit scan to /api/predict
  scanBtn.addEventListener("click", async () => {
    if (!selectedFile) return;
    scanBtn.disabled = true;
    scanLoader.style.display = "flex";

    const formData = new FormData();
    formData.append("file", selectedFile);
    formData.append("lang", currentLang);

    try {
      const res = await fetch("/api/predict", {
        method: "POST",
        body: formData
      });
      const data = await res.json();
      if (!res.ok || data.error) {
        throw new Error(data.error || "Prediction failed");
      }
      Store.saveScan(data);
      window.location.href = `/result?id=${data.scan_id}`;
    } catch (err) {
      showToast("Scan failed: " + err.message, "error");
      scanBtn.disabled = false;
      scanLoader.style.display = "none";
    }
  });

  loadRecentScansPreview();
  window.addEventListener("langchange", () => renderRecentPreview());
});

// 1-Click Sample Specimen Scan
async function runSampleScan(specimenKey) {
  const scanLoader = document.getElementById("scan-loader");
  const scanBtn = document.getElementById("scan-btn");
  if (scanLoader) scanLoader.style.display = "flex";
  if (scanBtn) scanBtn.disabled = true;

  try {
    const res = await fetch("/api/sample-scan", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ specimen: specimenKey, lang: currentLang })
    });
    const data = await res.json();
    if (!res.ok || data.error) {
      throw new Error(data.error || "Sample scan failed");
    }
    Store.saveScan(data);
    window.location.href = `/result?id=${data.scan_id}`;
  } catch (err) {
    showToast("Sample scan failed: " + err.message, "error");
    if (scanLoader) scanLoader.style.display = "none";
  }
}

async function loadRecentScansPreview() {
  try {
    recentScansCache = Store.historyRows();
    const statsRes = await fetch("/api/stats");
    const stats = await statsRes.json();

    const scanCountEl = document.getElementById("home-stat-scans");
    if (scanCountEl) scanCountEl.textContent = recentScansCache.length;
    const classesEl = document.getElementById("home-stat-classes");
    if (classesEl && stats.total_classes_db) classesEl.textContent = stats.total_classes_db;
    const cropsEl = document.getElementById("home-stat-crops");
    if (cropsEl && stats.total_crops_db) cropsEl.textContent = stats.total_crops_db;

    renderRecentPreview();
  } catch (e) {
    console.warn("Could not load preview:", e);
  }
}

function renderRecentPreview() {
  const container = document.getElementById("recent-scans-preview");
  if (!container) return;

  if (!recentScansCache || recentScansCache.length === 0) {
    container.style.gridTemplateColumns = "1fr";
    container.innerHTML = `
      <div class="card empty-state" style="padding:32px;">
        <div style="font-size:2rem;margin-bottom:8px;">🌱</div>
        <p style="font-family:var(--font-serif);font-size:1.05rem;color:var(--text-primary);margin-bottom:4px;">
          ${currentLang === "ta" ? "இன்னும் ஸ்கேன்கள் பதிவு செய்யப்படவில்லை" : "Your scan archive is fresh and empty"}
        </p>
        <p style="font-size:0.84rem;color:var(--text-muted);">
          ${currentLang === "ta"
            ? "மேலே உள்ள இலை புகைப்படத்தை பதிவேற்றவும் அல்லது 6 மாதிரி இலைகளில் ஒன்றை அழுத்தி உடனடியாக சோதிக்கவும்."
            : "Upload a leaf photo above or click any of the 6 sample specimens to log your first diagnosis."}
        </p>
      </div>
    `;
    return;
  }

  container.style.gridTemplateColumns = "";
  const top3 = recentScansCache.slice(0, 3);
  container.innerHTML = top3.map(r => {
    const name = currentLang === "ta" ? r.name_ta : r.name_en;
    return `
      <a href="/result?id=${r.scan_id}" class="card" style="padding:18px;text-decoration:none;display:flex;flex-direction:column;gap:12px;">
        <div style="display:flex;align-items:center;justify-content:space-between;">
          <div style="display:flex;align-items:center;gap:10px;">
            <span style="font-size:1.75rem;">${r.emoji}</span>
            <div>
              <div style="font-family:var(--font-serif);font-weight:700;font-size:0.98rem;color:var(--text-primary);">${name}</div>
              <div style="font-family:var(--font-mono);font-size:0.72rem;color:var(--text-muted);">${r.crop || ""} &bull; #${r.scan_id}</div>
            </div>
          </div>
          ${getSeverityBadge(r.severity, currentLang)}
        </div>
        <div style="display:flex;align-items:center;justify-content:space-between;padding-top:10px;border-top:1px solid var(--border-subtle);font-size:0.78rem;color:var(--text-secondary);">
          <span>${formatDate(r.timestamp)}</span>
          <span style="font-family:var(--font-mono);font-weight:600;color:var(--accent-primary);">${r.confidence}% match</span>
        </div>
      </a>
    `;
  }).join("");
}
