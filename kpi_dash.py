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
selected_city = st.sidebar.selectbox("City", data[data['Country'] == selected_country]['City'].unique())
selected_state = st.sidebar.selectbox("State", data[data['City'] == selected_city]['State'].unique())

# Filtered data based on user selection
filtered_data = data[(data['Country'] == selected_country) & (data['City'] == selected_city) & (data['State'] == selected_state)]
