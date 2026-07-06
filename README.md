# 📊 PhonePe Pulse Analytics Dashboard

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B.svg)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive-3D9970.svg)](https://plotly.com)

> An interactive multi-page analytics dashboard built with Streamlit to visualize 
> PhonePe Pulse data across India — covering digital transactions, insurance adoption, 
> and registered user trends with India choropleth maps.

---

## 🖥️ Live Demo
> 🚀 [View Live Dashboard](https://your-app.streamlit.app) ← Deploy on Streamlit Cloud (free!)

---
## 📸 Dashboard Preview

### 🏠 Main Dashboard
| PhonePe Pulse Analytics Dashboard |
|---|
| ![Main Dashboard](screenshots/Screenshot%20(94).png) |

### 💳 Transactions Dashboard
| Transaction Type Distribution | India State-wise Transaction Map |
|---|---|
| ![Transaction Types](screenshots/Screenshot%20(95).png) | ![Transaction Map](screenshots/Screenshot%20(96).png) |

### 🛡️ Insurance Dashboard
| Insurance KPI Overview | Insurance Type & Map |
|---|---|
| ![Insurance Overview](screenshots/Screenshot%20(97).png) | ![Insurance Map](screenshots/Screenshot%20(99).png) |

### 👥 Users Dashboard
| Users Overview | State-wise Registered Users | India Users Map |
|---|---|---|
| ![Users Overview](screenshots/Screenshot%20(100).png) | ![Users Bar](screenshots/Screenshot%20(101).png) | ![Users Map](screenshots/Screenshot%20(102).png) |
---

## 🎯 Key Features

- **Transactions Dashboard** — KPI cards, state-wise analysis, transaction type distribution, India choropleth map
- **Insurance Dashboard** — Insurance amount analysis, type distribution, state-wise map
- **Users Dashboard** — Registered user trends, state-wise user map, growth insights
- **Dynamic Filters** — Filter by state, year, and quarter across all dashboards
- **India Choropleth Maps** — Built with Plotly Express + GeoJSON for geo-visualizations

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming |
| Streamlit | Web dashboard framework |
| Pandas | Data processing & analysis |
| Plotly Express | Interactive charts & maps |
| GeoJSON | India state boundary maps |

---

## 📁 Project Structure
phonepe-pulse-dashboard/
├── dashboards.py          # Main multi-page Streamlit app
├── main.py                # Entry point / app launcher
├── agg_transaction.csv    # Aggregated transactions data
├── agg_insurence.csv      # Aggregated insurance data
├── agg_user.csv           # Aggregated user data
├── screenshots/           # Dashboard preview images
├── requirements.txt       # Python dependencies
└── README.md
---

## ⚙️ Installation & Run

```bash
# Clone the repo
git clone https://github.com/bsaiteja447/phonepe-pulse-dashboard.git
cd phonepe-pulse-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run dashboards.py
```

---

## 📊 Data Source

Data sourced from [PhonePe Pulse](https://github.com/PhonePe/pulse) — India's digital payment public dataset covering transactions, insurance, and user metrics across all Indian states from 2018–2024.

---

## 💡 Key Insights Uncovered

- Maharashtra, Karnataka, and Telangana lead in digital transaction volumes
- Insurance adoption is highest in southern states
- User growth shows consistent YoY increase post-2020 with UPI adoption surge

---

## 👤 Author

**B. Sai Teja** — Data Analyst | Python • SQL • Power BI  
📧 bsaiteja562@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/bsaiteja447) | [GitHub](https://github.com/bsaiteja447)
