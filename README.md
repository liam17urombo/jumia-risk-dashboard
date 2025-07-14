# 🛡️ Jumia Seller Risk Dashboard

An interactive Streamlit dashboard that identifies high-risk sellers on the Jumia marketplace using classification models and seller behavior analysis. Built as part of the **Dataverse Challenge**, this dashboard supports data-driven decisions to improve customer trust and seller accountability.

---

## 🚀 Demo

🌐 [Live Dashboard](https://yourusername-jumia-risk-dashboard.streamlit.app)  
📁 [GitHub Repo](https://github.com/yourusername/jumia-risk-dashboard)

---

## 📌 Project Overview

This project analyzes seller performance using complaint rates, return rates, and classification model outputs to:

- Flag high-risk sellers for suspension
- Visualize seller risk patterns and distributions
- Provide a 3-point customer trust policy
- Offer tools for data exploration, filtering, and transparency

---

## 📂 Files in this Project

| File                      | Description                                        |
|--------------------------|----------------------------------------------------|
| `app.py`                 | Streamlit dashboard application                    |
| `phase3_model_summary.csv` | Summary of classification model predictions       |
| `sellers_to_suspend.csv` | Top 5 highest-risk sellers to flag                 |
| `seller_risk_table.csv`  | All seller-level risk scores and metrics           |
| `customer_trust_policy.txt` | 3-point customer trust and safety policy         |
| `requirements.txt`       | Python dependencies for Streamlit Cloud deployment |

---

## 📊 Dashboard Features

- 🔍 **Seller Lookup:** Search individual sellers by ID
- 🎯 **Risk Filter:** Adjust risk score threshold to view different risk tiers
- 📈 **Risk Distribution:** Visual histogram of seller risk scores
- 🚨 **Top 5 High-Risk Sellers:** Table with sellers to be suspended
- 📥 **Downloadable Filtered Table:** Export suspicious sellers
- 📜 **Trust Policy:** Simple customer safety rules
- 🧠 **Suspension Logic Explained:** Transparent decision framework

---

## 🧠 Model Summary (Phase 3)

The classification model (e.g., logistic regression or XGBoost) predicted the likelihood of seller misconduct based on historical behavior data. Key features used:

- Complaint rate  
- Return rate  
- Review sentiment (if available)  
- Past delivery performance  

The model's predicted probabilities were used to assign a **risk score**, which guided seller suspension recommendations.

---

## 🏗️ Tech Stack

- 🐍 Python (Pandas, Matplotlib, scikit-learn)
- 📊 Streamlit (Interactive dashboard)
- 📁 GitHub + Streamlit Cloud (Deployment)
- 🔬 Optional NLP (Phase 1 & 3)

---

## 📜 Customer Trust Policy

1. ✅ Prioritize verified, high-rated sellers  
2. 🚨 Flag sellers with consistent complaints or returns  
3. 🛑 Suspend sellers with high risk scores from future listings

---

## 🧩 How to Run Locally

```bash
git clone https://github.com/yourusername/jumia-risk-dashboard.git
cd jumia-risk-dashboard
pip install -r requirements.txt
streamlit run app.py
