import streamlit as st
import pandas as pd


# Load the dataset
data = pd.read_csv(r'C:\Users\grosz justin\OneDrive - The Boston Consulting Group, Inc\Documents\AI\Sample_Superstore_Streamlit_Proper.csv')



# Streamlit app setup
st.title("KPI Dashboard")
