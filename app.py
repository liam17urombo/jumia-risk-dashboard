
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Jumia Seller Risk Dashboard", layout="wide")

st.title("📦 Jumia Seller Risk Dashboard")
st.markdown("An interactive dashboard to analyze seller risks, classification results, and trust policy recommendations.")

# === Load data ===
df_model = pd.read_csv('phase3_model_summary.csv')
df_suspicious = pd.read_csv('sellers_to_suspend.csv')
df_risk = pd.read_csv('seller_risk_table.csv')

# === Summary Metrics ===
st.header("📊 Summary Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Sellers", len(df_risk))
col2.metric("High-Risk Sellers", len(df_risk[df_risk['risk_score'] > 0.8]))
if 'predicted_probability' in df_model.columns:
    col3.metric("Avg Predicted Probability", f"{df_model['predicted_probability'].mean():.2%}")
else:
    col3.metric("Avg Predicted Probability", "N/A")

# === Risk Score Distribution ===
st.header("📈 Seller Risk Score Distribution")
fig, ax = plt.subplots()
df_risk['risk_score'].hist(bins=20, color='salmon', edgecolor='black', ax=ax)
ax.set_xlabel("Risk Score")
ax.set_ylabel("Number of Sellers")
st.pyplot(fig)

# === Top Risky Sellers Table ===
st.header("🚨 Top 5 Sellers to Suspend")
st.table(df_suspicious)

# === Full Seller Risk Table with Filter ===
st.header("🧮 Full Seller Risk Table")
min_score = st.slider("Filter by Minimum Risk Score", 0.0, 1.0, 0.5)
filtered_risk = df_risk[df_risk['risk_score'] >= min_score]

# Style risk score with color gradient
styled_df = filtered_risk.style.background_gradient(cmap='OrRd', subset=['risk_score'])
st.dataframe(styled_df, use_container_width=True)

# === Seller Lookup ===
st.header("🔎 Seller Lookup")
search_id = st.text_input("Enter Seller ID to Lookup")
if search_id:
    found = df_risk[df_risk['seller_id'].astype(str) == search_id]
    if not found.empty:
        st.success("Seller found:")
        st.dataframe(found)
    else:
        st.warning("Seller ID not found.")

# === Download Filtered Table ===
st.download_button("📥 Download Filtered Seller Risk Table", 
                   filtered_risk.to_csv(index=False), 
                   file_name="filtered_seller_risks.csv")

# === Trust Policy Section ===
st.header("🛡️ Customer Trust Policy")
with open('customer_trust_policy.txt', 'r') as file:
    policy_text = file.read()
st.text(policy_text)

# === Suspension Criteria Explanation ===
with st.expander("🧠 How Suspension Criteria Works"):
    st.markdown("""
    **Sellers are flagged if they meet any of these conditions:**
    
    - Return Rate > 15%
    - Complaint Rate > 10%
    - Risk Score > 0.8

    These thresholds help identify potentially fraudulent or poor-quality sellers.
    """)
