/* ══════════════════════════════════════════════
   AgroScan — Private per-browser data store
   Every person's scans, field notes and reports live ONLY in their own
   browser (localStorage). Nothing personal is saved on the server, so users
   can never see or influence each other's records.
   ══════════════════════════════════════════════ */
const Store = (() => {
  const SCANS_KEY = "agroscan_scans_v1";
  const NOTES_KEY = "agroscan_notes_v1";

  function read(key, fallback) {
    try {
      const v = JSON.parse(localStorage.getItem(key));
      return v == null ? fallback : v;
    } catch (e) { return fallback; }
  }

  function write(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
      return true;
    } catch (e) {
      return false;
    }
  }

  // ── Scans ──
  function getScans() { return read(SCANS_KEY, []); }

  function saveScan(scan) {
    const scans = getScans().filter(s => s.scan_id !== scan.scan_id);
    scans.unshift(scan);
    // If storage is full, drop photos from the oldest scans first, then oldest scans.
    while (!write(SCANS_KEY, scans)) {
      const withImg = scans.slice().reverse().find(s => s.image_url);
      if (withImg) { withImg.image_url = ""; continue; }
      if (scans.length <= 1) break;
      scans.pop();
    }
    return scan;
  }

  function getScan(id) { return getScans().find(s => s.scan_id === id) || null; }

  function updateScan(id, patch) {
    const scans = getScans();
    const s = scans.find(x => x.scan_id === id);
    if (!s) return null;
    Object.assign(s, patch);
    write(SCANS_KEY, scans);
    return s;
  }

  function deleteScan(id) { write(SCANS_KEY, getScans().filter(s => s.scan_id !== id)); }
  function clearScans() { write(SCANS_KEY, []); }

  function sevOf(scan) {
    const d = scan.disease || {};
    return (d.en && d.en.severity) || "moderate";
  }

  function historyRows() {
    return getScans().map(s => {
      const d = s.disease || { en: {}, ta: {} };
      return {
        scan_id: s.scan_id, timestamp: s.timestamp, image_url: s.image_url,
        class_name: s.class_name, crop: s.crop || d.crop, confidence: s.confidence,
        name_en: d.en.name, name_ta: (d.ta && d.ta.name) || d.en.name,
        severity: sevOf(s), emoji: d.en.emoji || "🌿",
        notes: s.notes || "", status: s.status || "Monitoring"
      };
    });
  }

  function stats() {
    const scans = getScans();
    const sev = { critical: 0, high: 0, moderate: 0, none: 0 };
    const counts = {};
    scans.forEach(s => {
      const k = sevOf(s);
      sev[k] = (sev[k] || 0) + 1;
      const d = s.disease || { en: {} };
      const key = s.class_name;
      if (!counts[key]) counts[key] = { class_name: key, display: d.en.name || key, emoji: d.en.emoji, count: 0 };
      counts[key].count++;
    });
    const top = Object.values(counts).sort((a, b) => b.count - a.count).slice(0, 8);
    return { total: scans.length, severity_breakdown: sev, top_diseases: top };
  }

  // ── Field notes ──
  function getNotes() {
    let notes = read(NOTES_KEY, null);
    if (notes === null) {
      const now = new Date().toISOString().slice(0, 19).replace("T", " ");
      notes = [
        { id: "note01", title: "Monsoon Blight Prevention Schedule", crop: "Tomato & Potato", is_pinned: 1, created_at: now,
          content: "During high humidity (>85%), inspect lower tomato and potato leaves every 3 days. Keep neem oil (5ml/L) and Trichoderma viride ready for preventive spraying before heavy rains." },
        { id: "note02", title: "Sprayer Calibration Checklist", crop: "General", is_pinned: 0, created_at: now,
          content: "1 knapsack sprayer tank = 15 Liters. Standard organic neem dosage = 75 ml per tank (5 ml/L). Standard Mancozeb 75% WP dosage = 37.5 g per tank (2.5 g/L). Always add 5 ml wetting agent." }
      ];
      write(NOTES_KEY, notes);
    }
    return notes.slice().sort((a, b) => (b.is_pinned - a.is_pinned) || (b.created_at > a.created_at ? 1 : -1));
  }

  function addNote(title, content, crop) {
    const notes = read(NOTES_KEY, []) || [];
    const note = {
      id: "n_" + Math.random().toString(36).slice(2, 8), title, content,
      crop: crop || "General", is_pinned: 0,
      created_at: new Date().toISOString().slice(0, 19).replace("T", " ")
    };
    getNotes(); // ensure seeded
    const all = read(NOTES_KEY, []);
    all.push(note);
    write(NOTES_KEY, all);
    return note;
  }

  function deleteNote(id) { getNotes(); write(NOTES_KEY, read(NOTES_KEY, []).filter(n => n.id !== id)); }

  function togglePin(id) {
    getNotes();
    const all = read(NOTES_KEY, []);
    const n = all.find(x => x.id === id);
    if (n) n.is_pinned = n.is_pinned ? 0 : 1;
    write(NOTES_KEY, all);
  }

  // ── CSV export (built in the browser from the user's own scans) ──
  function exportCSV() {
    const esc = v => `"${String(v == null ? "" : v).replace(/"/g, '""')}"`;
    const rows = [["Scan ID", "Timestamp", "Crop", "Disease (EN)", "Disease (TA)", "Confidence (%)",
                   "Severity", "Status", "Immediate Action", "Organic Treatment", "Farmer Notes"]];
    getScans().forEach(s => {
      const d = s.disease || { en: {}, ta: {} };
      rows.push([s.scan_id, s.timestamp, s.crop, d.en.name, d.ta && d.ta.name, s.confidence,
                 (d.en.severity || "").toUpperCase(), s.status, d.en.immediate, d.en.organic, s.notes]);
    });
    const csv = "\ufeff" + rows.map(r => r.map(esc).join(",")).join("\r\n");
    const blob = new Blob([csv], { type: "text/csv;charset=utf-8" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "AgroScan_Field_Archive.csv";
    document.body.appendChild(a);
    a.click();
    a.remove();
  }

  return { getScans, saveScan, getScan, updateScan, deleteScan, clearScans,
           historyRows, stats, getNotes, addNote, deleteNote, togglePin, exportCSV };
})();
