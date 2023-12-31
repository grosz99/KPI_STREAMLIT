import streamlit as st
import pandas as pd


# Load the dataset
data_url = "https://raw.githubusercontent.com/grosz99/KPI_STREAMLIT/main/Sample_Superstore_Streamlit_Proper.csv"
data = pd.read_csv(data_url)


# Streamlit app setup
st.title("KPI Dashboard")


# Filters
st.sidebar.header("Filters")
selected_country = st.sidebar.selectbox("Country", data['Country'].unique())
selected_states = st.sidebar.multiselect("State", data[data['Country'] == selected_country]['State'].unique())
selected_cities = st.sidebar.multiselect("City", data[data['State'].isin(selected_states)]['City'].unique())

# Filtered data based on user selection
filtered_data = d
