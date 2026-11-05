# AgroScan — AI Crop Disease Detection Platform

> **SDG 2: Zero Hunger** | MobileNetV2 + Flask + SQLite | HTML/CSS/JS Frontend

## 🌿 Overview

AgroScan is a full-stack AI-powered web application that helps farmers identify crop diseases from leaf photos in seconds. Upload a photo, get an AI diagnosis with confidence score, treatment advice in English & Tamil, and download a PDF report.

---

## 🚀 Quick Start

### 1. Install dependencies
```bash
python -m pip install flask werkzeug numpy
```

### 2. Run the web server (Demo mode — no model needed)
```bash
python app.py
```

Open: **http://localhost:5050**

---

## 🤖 Train the AI Model

### Dataset: PlantVillage (Kaggle)
1. Download from: https://www.kaggle.com/datasets/emmarex/plantdisease
2. Extract to: `agroscan/dataset/PlantVillage/`

### Install ML dependencies
```bash
python -m pip install tensorflow scikit-learn matplotlib seaborn
```

### Train
```bash
python train.py
```

Training output:
- `model/agroscan_mobilenetv2.h5` — trained model
- `model/reports/confusion_matrix.png` — confusion matrix
- `model/reports/training_history.png` — accuracy/loss curves
- `model/reports/classification_report.json` — per-class metrics

---

## 📁 Project Structure

```
agroscan/
├── app.py               ← Flask backend (all API routes)
├── train.py             ← MobileNetV2 training script
├── requirements.txt
├── agroscan.db          ← SQLite database (auto-created)
├── uploads/             ← User-uploaded leaf images
├── model/
│   ├── agroscan_mobilenetv2.h5   ← Trained model (after training)
│   └── reports/                  ← Plots & metrics
├── static/
│   ├── css/style.css    ← Full design system
│   └── js/
│       ├── app.js       ← Global: language switching, toasts, PDF
│       ├── scan.js      ← Scan page: file upload, preview, API call
│       ├── result.js    ← Result: confidence ring, treatment tabs, chatbot
│       ├── dashboard.js ← Charts.js: bar + donut charts
│       ├── history.js   ← Scan history table
│       └── encyclopedia.js ← Disease grid + search/filter
└── templates/
    ├── base.html        ← Navbar, footer, language toggle
    ├── index.html       ← Upload page
    ├── result.html      ← Diagnosis result page
    ├── history.html     ← Scan history
    ├── dashboard.html   ← Analytics dashboard
    └── encyclopedia.html ← Disease knowledge base
```

---

## 🌐 Pages

| Page | Route | Description |
|---|---|---|
| Scan | `/` | Upload leaf image, run AI scan |
| Result | `/result?id=<scan_id>` | AI diagnosis, treatment tabs, chatbot |
| History | `/history` | All past scans with severity badges |
| Dashboard | `/dashboard` | Chart.js analytics: top diseases, severity |
| Encyclopedia | `/encyclopedia` | Searchable/filterable disease database |

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/predict` | Upload image → AI prediction |
| `GET`  | `/api/history` | List all scans |
| `GET`  | `/api/stats` | Counts for dashboard charts |
| `GET`  | `/api/encyclopedia` | Full disease database |
| `GET`  | `/api/scan/:id` | Single scan by ID |
| `POST` | `/api/chat` | AgroBot chatbot (Gemini or rule-based) |

---

## 🌍 Languages

Toggle between **English** and **Tamil (தமிழ்)** using the navbar button. All UI text, disease names, treatment advice are bilingual.

---

## 🤖 AI Chatbot (AgroBot)

AgroBot is a context-aware chatbot on the result page. It uses:
1. **Gemini API** (if `GEMINI_API_KEY` env var is set)
2. **Rule-based fallback** (always works offline)

To enable Gemini:
```bash
set GEMINI_API_KEY=your_key_here   # Windows
python app.py
```

---

## 🌱 Supported Crops & Diseases (20 classes)

| Crop | Diseases |
|---|---|
| 🍅 Tomato | Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Mosaic Virus, Healthy |
| 🥔 Potato | Early Blight, Late Blight, Healthy |
| 🍎 Apple | Apple Scab, Black Rot, Cedar Rust, Healthy |
| 🌽 Corn | Common Rust, Healthy |
| 🍇 Grape | Black Rot, Healthy |

---

## 📊 Logbook Metrics

| Metric | Expected Result |
|---|---|
| Training Accuracy | >95% |
| Validation Accuracy | >92% |
| Top-3 Accuracy | >98% |
| Model Parameters | ~2.3M |
| Inference Time | <500ms |

---

## 🎯 SDG Alignment

- **SDG 2 (Zero Hunger)**: Early disease detection reduces crop losses
- **SDG 3 (Good Health)**: Promotes safe pesticide use with organic alternatives
- **SDG 11 (Sustainable Cities)**: Urban farming support
- **SDG 13 (Climate Action)**: Reduces food waste from crop disease
