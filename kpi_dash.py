import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# Load the dataset
data_url = "https://raw.githubusercontent.com/grosz99/KPI_STREAMLIT/main/Sample_Superstore_Streamlit_Proper.csv"
data = pd.read_csv(data_url)

# Convert 'Order Date' to datetime
data['Order Date'] = pd.to_datetime(data['Order Date'])

# Streamlit app setup
st.title("KPI Dashboard")

# Filters
st.sidebar.header("Filters")
selected_country = st.sidebar.selectbox("Country", data['Country'].unique())
states_in_country = data[data['Country'] == selected_country]['State'].unique()
cities_in_country = data[data['Country'] == selected_country]['City'].unique()

selected_states = st.sidebar.multiselect("State", states_in_country, default=list(states_in_country))
selected_cities = st.sidebar.multiselect("City", cities_in_country, default=list(cities_in_country))

# Filtered data based on user selection
filtered_data = data[(data['Country'] == selected_country) & (data['State'].isin(selected_states)) & (data['City'].isin(selected_cities))]

# Function to calculate KPIs
def calculate_kpis(data, year):
    year_data = data[data['Order Date'].dt.year == year]
    total_sales = year_data['Sales'].sum()
    total_profit = year_data['Profit'].sum()
    total_quantity = year_data['Quantity'].sum()
    profit_margin = np.where(total_sales > 0, (total_profit / total_sales) * 100, 0)
    return total_sales, total_profit, total_quantity, profit_margin

# Calculate KPIs for 2017 and 2016
ty_sales, ty_profit, ty_quantity, ty_profit_margin = calculate_kpis(filtered_data, 2017)
ly_sales, ly_profit, ly_quantity, ly_profit_margin = calculate_kpis(filtered_data, 2016)

# Calculate YoY changes
sales_change = ((ty_sales - ly_sales) / ly_sales) * 100 if ly_sales > 0 else 0
profit_change = ((ty_profit - ly_profit) / ly_profit) * 100 if ly_profit > 0 else 0
quantity_change = ((ty_quantity - ly_quantity) / ly_quantity) * 100 if ly_quantity > 0 else 0
profit_margin_change = ty_profit_margin - ly_profit_margin

# Displaying KPIs
st.header("Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)
col1.metric("TY Sales", f"${ty_sales:,.2f}", f"{sales_change:.2f}%")
col2.metric("TY Profit", f"${ty_profit:,.2f}", f"{profit_change:.2f}%")
col3.metric("TY Quantity", f"{ty_quantity}", f"{quantity_change:.2f}%")
col4.metric("TY Profit %", f"{ty_profit_margin:.2f}%", f"{profit_margin_change:.2f}%")

# Function to prepare data for the YoY chart
def prepare_chart_data(filtered_data, kpi):
    # Extract year and month from 'Order Date'
    filtered_data['Year'] = filtered_data['Order Date'].dt.year
    filtered_data['Month'] = filtered_data['Order Date'].dt.month

    # Grouping by month and year
    monthly_data = filtered_data.groupby(['Year', 'Month'])[kpi].sum().reset_index()
    return monthly_data

# KPI selection for the chart
selected_kpi = st.selectbox("Select KPI for YoY Trend Chart", ["Sales", "Profit", "Quantity"])

# Prepare data for the selected KPI
chart_data = prepare_chart_data(filtered_data, selected_kpi)

# Create and display the YoY trend chart
fig = px.line(chart_data, x="Month", y=selected_kpi, color='Year', title=f'YoY {selected_kpi} Trend')
st.plotly_chart(fig)
