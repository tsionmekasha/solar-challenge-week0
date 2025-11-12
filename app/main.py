import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, load_all_countries  # fixed import

# Page config
st.set_page_config(page_title="🌞 Solar Data Discovery Dashboard", layout="wide")

st.title("🌞 Solar Data Discovery Dashboard")
st.write("Explore and compare solar farm data from Benin, Sierra Leone, and Togo.")

# Sidebar: Select country or all
option = st.sidebar.selectbox(
    "Select country",
    ["All", "Benin", "Sierra Leone", "Togo"]
)

# Load data based on selection
if option == "All":
    df = load_all_countries()
else:
    df = load_data(option)

st.write(f"### Dataset Overview - {option}")
st.write(f"Shape: {df.shape}")
st.dataframe(df.head())

# GHI Distribution
st.write("### GHI Distribution")
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(df['GHI'], bins=50, kde=True, ax=ax)
st.pyplot(fig)

# Top Regions by Average GHI
st.write("### Top Regions by Average GHI")

try:
    top_regions = df.groupby(['Country', 'Comments'])['GHI'].mean().reset_index()
    top_regions = top_regions.sort_values('GHI', ascending=False).head(10)
    st.dataframe(top_regions)
except KeyError:
    st.warning("The 'Country' or 'Comments' column is missing in the dataset.")

# Correlation Heatmap
st.write("### Correlation Heatmap")
fig, ax = plt.subplots(figsize=(10, 6))
cols_to_corr = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB']
existing_cols = [c for c in cols_to_corr if c in df.columns]
sns.heatmap(df[existing_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)
