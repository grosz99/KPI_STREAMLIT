import streamlit as st
import pandas as pd


# Load the dataset
data_url = "https://raw.githubusercontent.com/grosz99/KPI_STREAMLIT/main/Sample_Superstore_Streamlit_Proper.csv"
data = pd.read_csv(data_url)


# Streamlit app setup
st.title("KPI Dashboard")
