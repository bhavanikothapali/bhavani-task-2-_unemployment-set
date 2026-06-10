import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("India Unemployment Analysis Dashboard")

df = pd.read_csv("data/unemployment_india.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Dataset Shape")
st.write(df.shape)

# Column cleaning
df.columns = df.columns.str.strip()

# Example visualization
if 'Estimated Unemployment Rate (%)' in df.columns:

    fig, ax = plt.subplots(figsize=(8,5))

    df['Estimated Unemployment Rate (%)'].hist(ax=ax)

    st.pyplot(fig)
