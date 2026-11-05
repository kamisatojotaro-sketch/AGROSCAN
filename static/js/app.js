/* ══════════════════════════════════════════════
   AgroScan — Global Utilities (Theme, Language, Nav, Toast, Voice TTS)
   ══════════════════════════════════════════════ */

// ── Theme State (Light Botanical Paper default, Dark Botanical Forest optional) ──
let currentTheme = localStorage.getItem("agroscan_theme") || "light";

function applyTheme(theme) {
  currentTheme = theme;
  localStorage.setItem("agroscan_theme", theme);
  const root = document.documentElement;
  const icon = document.getElementById("theme-icon");
  const iconMobile = document.getElementById("theme-icon-mobile");
  const label = document.getElementById("theme-label");

  if (theme === "dark") {
    root.classList.add("dark");
    root.setAttribute("data-theme", "dark");
    if (icon) icon.textContent = "☀️";
    if (iconMobile) iconMobile.textContent = "☀️";
    if (label) {
      label.setAttribute("data-en", "Light Mode");
      label.setAttribute("data-ta", "ஒளி முறை");
      label.textContent = (localStorage.getItem("agroscan_lang") === "ta") ? "ஒளி முறை" : "Light Mode";
    }
  } else {
    root.classList.remove("dark");
    root.setAttribute("data-theme", "light");
    if (icon) icon.textContent = "🌙";
    if (iconMobile) iconMobile.textContent = "🌙";
    if (label) {
      label.setAttribute("data-en", "Dark Mode");
      label.setAttribute("data-ta", "இருள் முறை");
      label.textContent = (localStorage.getItem("agroscan_lang") === "ta") ? "இருள் முறை" : "Dark Mode";
    }
  }
  window.dispatchEvent(new CustomEvent("themechange", { detail: { theme } }));
}

function toggleTheme() {
  applyTheme(currentTheme === "dark" ? "light" : "dark");
}

// Apply theme immediately to prevent flash
applyTheme(currentTheme);

// ── Language State (EN / Tamil) ──
let currentLang = localStorage.getItem("agroscan_lang") || "en";

function setLang(lang) {
  currentLang = lang;
  localStorage.setItem("agroscan_lang", lang);
  document.documentElement.setAttribute("data-lang", lang);

  ["btn-en", "btn-en-m"].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.classList.toggle("active", lang === "en");
  });
  ["btn-ta", "btn-ta-m"].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.classList.toggle("active", lang === "ta");
  });

  // Translate all elements with data-en / data-ta attributes
  document.querySelectorAll("[data-en]").forEach(el => {
    const text = el.getAttribute(`data-${lang}`) || el.getAttribute("data-en");
    if (el.tagName === "INPUT" || el.tagName === "TEXTAREA") {
      el.placeholder = text;
    } else {
      el.textContent = text;
    }
  });

  window.dispatchEvent(new CustomEvent("langchange", { detail: { lang } }));
}

// ── Active Nav Highlight (Desktop Sidebar + Mobile Bottom Nav) ──
function highlightNav() {
  const path = window.location.pathname;
  const map = {
    "/": "nav-home",
    "/result": "nav-home",
    "/history": "nav-history",
    "/dashboard": "nav-dashboard",
    "/encyclopedia": "nav-ency",
    "/model": "nav-model",
    "/tools": "nav-tools"
  };
  const mobileMap = {
    "/": "m-nav-home",
    "/result": "m-nav-home",
    "/history": "m-nav-history",
    "/dashboard": "m-nav-dashboard",
    "/encyclopedia": "m-nav-ency",
    "/model": "m-nav-model",
    "/tools": "m-nav-tools"
  };

  const activeId = map[path] || "nav-home";
  const el = document.getElementById(activeId);
  if (el) el.classList.add("active");

  const mActiveId = mobileMap[path] || "m-nav-home";
  const mEl = document.getElementById(mActiveId);
  if (mEl) mEl.classList.add("active");
}

// ── Toast Notifications ──
function showToast(msg, type = "success") {
  const container = document.getElementById("toast-container");
  if (!container) return;
  const toast = document.createElement("div");
  toast.className = `toast toast-${type}`;
  const icon = type === "success" ? "🌿" : type === "error" ? "⚠️" : "ℹ️";
  toast.innerHTML = `<span>${icon}</span><span>${msg}</span>`;
  container.appendChild(toast);
  setTimeout(() => {
    toast.style.opacity = "0";
    toast.style.transform = "translateX(20px)";
    toast.style.transition = "all 0.3s ease";
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}

// ── Severity Badge Helper ──
function getSeverityBadge(severity, lang = currentLang) {
  const labels = {
    en: {
      critical: "🚨 CRITICAL",
      high: "🔴 HIGH RISK",
      moderate: "⚠️ MODERATE",
      none: "✅ HEALTHY"
    },
    ta: {
      critical: "🚨 அதி தீவிரம்",
      high: "🔴 அதிக ஆபத்து",
      moderate: "⚠️ மிதமானது",
      none: "✅ ஆரோக்கியமானது"
    }
  };
  const l = (labels[lang] || labels.en)[severity] || severity;
  return `<span class="badge badge-${severity}">${l}</span>`;
}

// ── Voice Readout (Text-to-Speech for Farmers in English & Tamil) ──
let isSpeaking = false;
function speakAdvisory(text, lang = currentLang, btnEl = null) {
  if (!("speechSynthesis" in window)) {
    showToast(lang === "ta" ? "உங்கள் உலாவி குரல் வாசிப்பை ஆதரிக்கவில்லை" : "Browser does not support voice readout", "error");
    return;
  }
  if (window.speechSynthesis.speaking && isSpeaking) {
    window.speechSynthesis.cancel();
    isSpeaking = false;
    if (btnEl) {
      btnEl.innerHTML = lang === "ta" ? "🔊 குரலில் கேட்க" : "🔊 Listen Advisory";
    }
    return;
  }
  window.speechSynthesis.cancel();
  const utter = new SpeechSynthesisUtterance(text);
  utter.lang = lang === "ta" ? "ta-IN" : "en-US";
  utter.rate = 0.96;

  // Pick a matching voice if available
  const voices = window.speechSynthesis.getVoices();
  const match = voices.find(v => v.lang.toLowerCase().startsWith(lang === "ta" ? "ta" : "en"));
  if (match) utter.voice = match;

  isSpeaking = true;
  if (btnEl) {
    btnEl.innerHTML = lang === "ta" ? "⏹️ நிறுத்து" : "⏹️ Stop Audio";
  }
  utter.onend = () => {
    isSpeaking = false;
    if (btnEl) {
      btnEl.innerHTML = lang === "ta" ? "🔊 குரலில் கேட்க" : "🔊 Listen Advisory";
    }
  };
  utter.onerror = () => {
    isSpeaking = false;
    if (btnEl) {
      btnEl.innerHTML = lang === "ta" ? "🔊 குரலில் கேட்க" : "🔊 Listen Advisory";
    }
  };
  window.speechSynthesis.speak(utter);
}

// ── Format Date ──
function formatDate(ts) {
  if (!ts) return "";
  const d = new Date(ts.replace(" ", "T"));
  if (isNaN(d)) return ts;
  return d.toLocaleDateString("en-IN", {
    day: "numeric", month: "short", year: "numeric",
    hour: "2-digit", minute: "2-digit"
  });
}

// ── Init on DOM ready ──
document.addEventListener("DOMContentLoaded", () => {
  applyTheme(currentTheme);
  highlightNav();
  setLang(currentLang);
});
