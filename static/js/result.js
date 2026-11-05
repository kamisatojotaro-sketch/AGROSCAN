/* ══════════════════════════════════════════════
   AgroScan — Diagnosis Result, Voice Readout, Field Notes & AgroBot
   ══════════════════════════════════════════════ */

let scanData = null;
let activeTab = "immediate";

document.addEventListener("DOMContentLoaded", async () => {
  const params = new URLSearchParams(window.location.search);
  const scanId = params.get("id");

  // Load from API if scanId given, else fallback to sessionStorage
  if (scanId) scanData = Store.getScan(scanId);

  if (!scanData) {
    window.location.href = "/";
    return;
  }

  renderResult();
  initTabs();
  initChat();
  updateQuickDosage();

  // Re-render when user switches EN <-> Tamil
  window.addEventListener("langchange", () => {
    renderResult();
    updateQuickDosage();
  });

  // Printable PDF Report button
  document.getElementById("download-pdf-btn").addEventListener("click", () => {
    window.open(`/report?id=${scanData.scan_id}&lang=${currentLang}`, "_blank");
  });
});

function renderResult() {
  if (!scanData) return;
  const d = scanData.disease[currentLang] || scanData.disease.en;

  document.getElementById("res-image").src = scanData.image_url;
  document.getElementById("res-scan-id").textContent = `#${scanData.scan_id}`;
  const cropBadge = document.getElementById("res-crop-badge");
  if (cropBadge) cropBadge.textContent = `🌾 ${scanData.crop || d.crop || "Specimen"}`;
  document.getElementById("res-timestamp").textContent = formatDate(scanData.timestamp);
  document.getElementById("res-confidence").textContent = `${scanData.confidence}%`;

  // Populate saved notes & status
  const noteInput = document.getElementById("scan-note-input");
  const statusSelect = document.getElementById("scan-status-select");
  if (noteInput && scanData.notes !== undefined) noteInput.value = scanData.notes;
  if (statusSelect && scanData.status) statusSelect.value = scanData.status;

  // Animate circular gauge (circumference = 2 * pi * 32 ≈ 201)
  const offset = 201 - (201 * Math.min(scanData.confidence, 100)) / 100;
  setTimeout(() => {
    document.getElementById("conf-circle").style.strokeDashoffset = offset;
  }, 100);

  // Disease header
  document.getElementById("res-emoji").textContent = d.emoji || "🌿";
  document.getElementById("res-name").textContent = d.name;
  document.getElementById("res-cause").textContent = d.cause;
  document.getElementById("res-severity-badge").innerHTML = getSeverityBadge(d.severity, currentLang);
  document.getElementById("res-symptoms").textContent = d.symptoms;

  const weatherEl = document.getElementById("res-weather");
  if (weatherEl) weatherEl.textContent = d.weather || "Warm humid weather (22–30°C)";
  const recoveryEl = document.getElementById("res-recovery");
  if (recoveryEl) recoveryEl.textContent = d.recovery || "10–14 days";

  // Treatment tab content
  document.getElementById("res-treatment-text").textContent = d[activeTab] || d.immediate;

  // Top-5 Probability bars
  const top5Container = document.getElementById("top5-list");
  top5Container.innerHTML = scanData.top5.map(item => {
    const label = currentLang === "ta" ? (item.name_ta || item.name_en) : item.name_en;
    return `
      <div class="prob-row">
        <div class="prob-header">
          <span style="font-weight:500;">${label}</span>
          <span style="font-family:var(--font-mono);color:var(--accent-primary);">${item.prob}%</span>
        </div>
        <div class="prob-bar-bg">
          <div class="prob-bar-fill" style="width:${Math.max(item.prob, 2)}%"></div>
        </div>
      </div>
    `;
  }).join("");
}

function initTabs() {
  document.querySelectorAll(".tab-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      activeTab = btn.getAttribute("data-tab");
      const d = scanData.disease[currentLang] || scanData.disease.en;
      document.getElementById("res-treatment-text").textContent = d[activeTab] || d.immediate;
    });
  });
}

// Voice Readout (Text-to-Speech)
function speakCurrentResult(btnEl) {
  if (!scanData) return;
  const d = scanData.disease[currentLang] || scanData.disease.en;
  const text = currentLang === "ta"
    ? `${d.name}. காரணம்: ${d.cause}. அறிகுறிகள்: ${d.symptoms}. உடனடி நடவடிக்கை: ${d.immediate}. இயற்கை தீர்வு: ${d.organic}`
    : `Diagnosis: ${d.name}, with ${scanData.confidence} percent confidence. Cause: ${d.cause}. Symptoms: ${d.symptoms}. Immediate Action: ${d.immediate}. Organic Remedy: ${d.organic}`;
  speakAdvisory(text, currentLang, btnEl);
}

// Quick Plot Dosage Estimator
function updateQuickDosage() {
  const acreInput = document.getElementById("quick-acre-input");
  const out = document.getElementById("quick-dosage-output");
  if (!acreInput || !out) return;
  const acres = Math.max(parseFloat(acreInput.value) || 1, 0.1);
  const waterL = Math.round(acres * 200);
  const tanks = Math.max(1, Math.round(waterL / 15));
  const neemMl = Math.round(waterL * 5);
  const chemG = Math.round(waterL * 2.5);

  if (currentLang === "ta") {
    out.textContent = `${acres} ஏக்கருக்கு: ~${waterL} லி தண்ணீர் (${tanks} டேங்க்) • ${neemMl} மி.லி வேப்பெண்ணெய் அல்லது ${chemG} கி பூஞ்சைக்கொல்லி`;
  } else {
    out.textContent = `For ${acres} Acre(s): ~${waterL}L water (${tanks} × 15L tanks) • ${neemMl} ml Neem Oil OR ${chemG} g Fungicide`;
  }
}

// Save Farmer Note & Status to SQLite
async function saveScanNote() {
  if (!scanData) return;
  const notes = document.getElementById("scan-note-input").value;
  const status = document.getElementById("scan-status-select").value;

  if (Store.updateScan(scanData.scan_id, { notes, status })) {
    scanData.notes = notes;
    scanData.status = status;
    showToast(currentLang === "ta" ? "குறிப்பு உங்கள் தனிப்பட்ட காப்பகத்தில் சேமிக்கப்பட்டது!" : "Field note saved to your private archive!", "success");
  } else {
    showToast("Failed to save note", "error");
  }
}

function initChat() {
  const messagesEl = document.getElementById("chat-messages");
  const form = document.getElementById("chat-form");
  const input = document.getElementById("chat-input");

  const d = scanData.disease[currentLang] || scanData.disease.en;
  const greeting = currentLang === "ta"
    ? `வணக்கம்! உங்கள் இலையில் **${d.name}** (${scanData.confidence}% உறுதி) கண்டறியப்பட்டுள்ளது. இயற்கை தீர்வு, மருந்து அளவு அல்லது தடுப்பு முறைகள் பற்றி என்னிடம் கேளுங்கள்!`
    : `Hello farmer! I've analyzed your leaf specimen: **${d.name}** (${scanData.confidence}% confidence). Ask me anything about organic sprays, exact dosage, or next-season prevention!`;

  appendMessage("bot", greeting);

  document.querySelectorAll(".chip").forEach(chip => {
    chip.addEventListener("click", () => {
      const q = chip.getAttribute(`data-q-${currentLang}`) || chip.getAttribute("data-q-en");
      sendQuestion(q);
    });
  });

  form.addEventListener("submit", e => {
    e.preventDefault();
    const q = input.value.trim();
    if (!q) return;
    input.value = "";
    sendQuestion(q);
  });

  async function sendQuestion(question) {
    appendMessage("user", question);
    try {
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          message: question,
          disease_class: scanData.class_name,
          lang: currentLang
        })
      });
      const data = await res.json();
      appendMessage("bot", data.reply || "Sorry, I couldn't process that.");
    } catch (err) {
      appendMessage("bot", "Network error. Please try again.");
    }
  }

  function appendMessage(role, text) {
    const div = document.createElement("div");
    div.className = `msg msg-${role}`;
    div.innerHTML = text
      .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
      .replace(/\n/g, "<br>");
    messagesEl.appendChild(div);
    messagesEl.scrollTop = messagesEl.scrollHeight;
  }
}
