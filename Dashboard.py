import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px

# Dataset URL
DATA_URL = "https://www.dropbox.com/s/7uyen8z14lhnxf7/US-Accidents%5BEdited%5D.csv?dl=1"

# Create a title for the dashboard
st.header("United States of America Motor Vehicle Collisions dashboard")

# Add a description for the dashboard
st.write("This dashboard provides insights into motor vehicle collisions in the United States 🇺🇸.")

# Define a function to read the data (CSV file)


@st.cache_data(persist=True)
def read_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=["date/time"])
    return data


# Read the data for 233174 rows
data = read_data(233174)

# Create a copy of the data
data_copy = data.copy()

# Section 1: Map of injuries by location
st.header("Which area in the United States experienced the highest number of reported injuries?")

# Create a slider input for selecting the number of people affected by injuries in vehicle collisions
injured = st.slider("People affected by injuries in vehicle collisions", 0, 19)

# Create a map visualization using latitude and longitude data for locations with injured_persons greater than or equal to the selected value
st.map(data.query("injured_persons >= @injured")
       [["latitude", "longitude"]].dropna(how="any"))

# Section 4: Top cities with highest rate of collisions
st.header("Identifying the top 10 cities in the United States with the highest rate of collisions")

# Create a selectbox input for selecting the affected people type (Pedestrians, Cyclists, Motorists)
types = st.selectbox("Affected people type", [
                     "Pedestrians", "Cyclists", "Motorists"])

# If the selected type is Pedestrians
if types == "Pedestrians":
    # Filter the data to include only rows where injured_pedestrians is greater than or equal to 1
    filtered_data = data_copy.query("injured_pedestrians >= 1")

    # Sort the filtered data by injured_pedestrians in descending order and select the top 10 cities
    top_cities = filtered_data[["city", "injured_pedestrians"]].sort_values(
        by=["injured_pedestrians"],
        ascending=False).dropna(how="any")[:10]["city"]

    # Display the top cities in the output
    st.write(top_cities)

# Create a checkbox input to show raw data
if st.checkbox("Show Raw Data", False):
    st.subheader('Raw Data')
    st.write(data)
