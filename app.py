import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Blood Donation Dashboard", layout="wide")

st.title("🩸 Give Life: Predict Blood Donations Dashboard")

# 1. Load Data
@st.cache_data
def load_data():
    return pd.read_csv("transfusion.data")

try:
    df = load_data()

    # Rename target column for clarity if present
    df.columns = [col.strip() for col in df.columns]
    
    # 2. Sidebar Filters
    st.sidebar.header("Filter Donors")
    
    if "Recency (months)" in df.columns:
        max_recency = int(df["Recency (months)"].max())
        recency_limit = st.sidebar.slider(
            "Max Months Since Last Donation", 
            min_value=0, 
            max_value=max_recency, 
            value=max_recency
        )
        filtered_df = df[df["Recency (months)"] <= recency_limit]
    else:
        filtered_df = df

    # 3. High-Level Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Donors Sampled", len(filtered_df))
    
    if "Frequency (times)" in df.columns:
        col2.metric("Avg Donation Frequency", f"{filtered_df['Frequency (times)'].mean():.1f} times")
    
    if "Monetary (c.c. blood)" in df.columns:
        col3.metric("Avg Total Blood Donated", f"{filtered_df['Monetary (c.c. blood)'].mean():.0f} c.c.")

    st.markdown("---")

    # 4. Data Preview
    st.subheader("Data Overview")
    st.dataframe(filtered_df, use_container_width=True)

    # 5. Visualizations
    st.subheader("Distribution & Analytics")
    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        if "Frequency (times)" in df.columns:
            st.write("**Donation Frequency Distribution**")
            st.bar_chart(filtered_df["Frequency (times)"].value_counts())

    with col_chart2:
        if "Recency (months)" in df.columns:
            st.write("**Recency (Months) Distribution**")
            st.line_chart(filtered_df["Recency (months)"].value_counts().sort_index())

except FileNotFoundError:
    st.error("Could not find `transfusion.data`. Make sure the file is saved directly inside your `CovidDashboardPython` folder.")
    
