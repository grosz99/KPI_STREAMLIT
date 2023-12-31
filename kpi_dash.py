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

# Default to all states and cities for the selected country
default_states = data[data['Country'] == selected_country]['State'].unique()
default_cities = data[data['Country'] == selected_country]['City'].unique()

selected_states = st.sidebar.multiselect("State", default_states, default=default_states)
selected_cities = st.sidebar.multiselect("City", default_cities, default=default_cities)

# Filtered data based on user selection
filtered_data = data[(data['Country'] == selected_country) & (data['State'].isin(selected_states)) & (data['City'].isin(selected_cities))]
