/* ══════════════════════════════════════════════════════════════════
   AgroScan Dashboard — dashboard.js
   Chart.js charts styled with warm botanical palette
   (Sage green, terracotta, amber ochre, warm charcoal)
   ══════════════════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {
  loadDashboard();
});

window.addEventListener('langchange', loadDashboard);
window.addEventListener('themechange', loadDashboard);

async function loadDashboard() {
  try {
    const res  = await fetch('/api/stats');
    const data = await res.json();
    renderDashboard(data);
  } catch (err) {
    console.error('Dashboard load error:', err);
  }
}

function renderDashboard(data) {
  const total    = data.total || 0;
  const sev      = data.severity_breakdown || {};
  const diseases = data.top_diseases || [];

  // Update badge
  const badge = document.getElementById('scan-count-badge');
  if (badge) badge.textContent = `${total} Field Records`;

  // Stat cards
  const elTotal = document.getElementById('d-total');
  if (elTotal) elTotal.textContent = total;
  
  const elCrit = document.getElementById('d-critical');
  if (elCrit) elCrit.textContent = sev.critical || 0;

  const elMod = document.getElementById('d-moderate');
  if (elMod) elMod.textContent = (sev.moderate || 0) + (sev.high || 0);

  const elHlth = document.getElementById('d-healthy');
  if (elHlth) elHlth.textContent = sev.none || 0;

  // Bar chart — top diseases
  buildBarChart(diseases);

  // Donut chart — severity
  buildDonutChart(sev);

  // Disease list
  buildDiseaseList(diseases, total);
}

let _barChart, _donutChart;

function buildBarChart(diseases) {
  const ctx = document.getElementById('barChart');
  if (!ctx) return;

  if (_barChart) _barChart.destroy();

  const isDark = document.documentElement.classList.contains('dark');
  const textColor = isDark ? '#e8e0d4' : '#3d3329';
  const gridColor = isDark ? 'rgba(255,255,255,0.06)' : 'rgba(0,0,0,0.05)';

  const labels = diseases.slice(0, 8).map(d => d.display || d.class_name);
  const counts = diseases.slice(0, 8).map(d => d.count);

  _barChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels,
      datasets: [{
        label: 'Detections',
        data: counts,
        backgroundColor: counts.map((_, i) =>
          i === 0 ? '#6b7f5e' :
          i === 1 ? '#c75b3b' :
          i === 2 ? '#d4a843' :
          isDark ? 'rgba(139, 159, 126, 0.4)' : 'rgba(107, 127, 94, 0.3)'
        ),
        borderColor: isDark ? '#4a5a42' : '#e8dfd0',
        borderWidth: 1,
        borderRadius: 8,
        borderSkipped: false,
      }],
    },
    options: {
      indexAxis: 'y',
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          backgroundColor: isDark ? '#2a3325' : '#ffffff',
          borderColor: isDark ? '#4a5a42' : '#e8dfd0',
          borderWidth: 1,
          titleColor: textColor,
          bodyColor: isDark ? '#b8afa3' : '#5c5346',
          titleFont: { family: 'Playfair Display', weight: 'bold' },
          bodyFont: { family: 'Inter' },
          padding: 10,
          callbacks: {
            label: ctx => ` ${ctx.raw} Field Examinations`,
          },
        },
      },
      scales: {
        x: {
          grid: { color: gridColor },
          ticks: { color: isDark ? '#8c8377' : '#8c8377', font: { family: 'JetBrains Mono', size: 11 } },
        },
        y: {
          grid: { display: false },
          ticks: { color: textColor, font: { family: 'Inter', size: 11 } },
        },
      },
    },
  });
}

function buildDonutChart(sev) {
  const ctx = document.getElementById('donutChart');
  if (!ctx) return;

  if (_donutChart) _donutChart.destroy();

  const isDark = document.documentElement.classList.contains('dark');
  const textColor = isDark ? '#e8e0d4' : '#3d3329';
  const hasData = Object.values(sev).some(v => v > 0);

  _donutChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Healthy Foliage', 'Moderate Risk', 'High Risk', 'Critical Alert'],
      datasets: [{
        data: hasData ? [
          sev.none     || 0,
          sev.moderate || 0,
          sev.high     || 0,
          sev.critical || 0,
        ] : [1, 1, 1, 1],
        backgroundColor: [
          '#6b7f5e', // Sage Green
          '#d4a843', // Amber Ochre
          '#c75b3b', // Terracotta
          '#a84c32', // Deep Rust
        ],
        borderColor: isDark ? '#2a3325' : '#ffffff',
        borderWidth: 2,
        hoverOffset: 6,
      }],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      cutout: '70%',
      plugins: {
        legend: {
          position: 'bottom',
          labels: {
            color: textColor,
            font: { family: 'Inter', size: 11 },
            padding: 14,
            usePointStyle: true,
            pointStyleWidth: 8,
          },
        },
        tooltip: {
          backgroundColor: isDark ? '#2a3325' : '#ffffff',
          borderColor: isDark ? '#4a5a42' : '#e8dfd0',
          borderWidth: 1,
          titleColor: textColor,
          bodyColor: isDark ? '#b8afa3' : '#5c5346',
          titleFont: { family: 'Playfair Display', weight: 'bold' },
          bodyFont: { family: 'Inter' },
          padding: 10,
        },
      },
    },
  });
}

function buildDiseaseList(diseases, total) {
  const container = document.getElementById('disease-list');
  if (!container) return;

  if (!diseases.length) {
    container.innerHTML = `
      <div class="empty-state" style="padding:32px 0;">
        <div class="empty-icon">📊</div>
        <p>No pathology scans recorded in the database yet. <a href="/" style="color:var(--accent-primary);text-decoration:underline;">Scan your first leaf specimen</a></p>
      </div>`;
    return;
  }

  const max = diseases[0].count || 1;
  container.innerHTML = diseases.map((d, i) => `
    <div style="display:flex;align-items:center;gap:14px;padding:12px 0;border-bottom:1px solid var(--border-subtle);">
      <span style="font-size:1.4rem;width:32px;text-align:center;">${d.emoji || '🌿'}</span>
      <div style="flex:1;min-width:0;">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;">
          <span style="font-size:0.88rem;font-weight:600;color:var(--text-primary);font-family:var(--font-serif);">${d.display || d.class_name}</span>
          <span class="font-mono" style="font-size:0.75rem;color:var(--text-muted);">${d.count} specimen${d.count !== 1 ? 's' : ''}</span>
        </div>
        <div class="prog-bar-track">
          <div class="prog-bar-fill" style="width:0%;" data-w="${(d.count / max) * 100}%"></div>
        </div>
      </div>
      <span class="font-mono" style="font-size:0.75rem;color:var(--text-muted);min-width:44px;text-align:right;">
        ${total ? Math.round((d.count / total) * 100) : 0}%
      </span>
    </div>
  `).join('');

  setTimeout(() => {
    container.querySelectorAll('.prog-bar-fill').forEach(bar => {
      bar.style.width = bar.getAttribute('data-w');
    });
  }, 100);
}
