import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px

# Dataset URL
DATA_URL = "https://www.dropbox.com/s/7uyen8z14lhnxf7/US-Accidents%5BEdited%5D.csv?dl=1"

# Create a title for the dashboard
st.header("United States of America🇺🇸 Motor Vehicle Collisions dashboard")

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


# Section 2: Collisions by hour and minute
st.header(
    "What is the frequency of collisions during specific time periods of the day?")

# Create a selectbox input for selecting an hour range
hour = st.selectbox("Select an hour range", range(24))

# Filter the data based on the selected hour
data = data[data["date/time"].dt.hour == hour]

# Calculate the midpoint of latitude and longitude for initial view state of the map
midpoint = (np.average(data["latitude"]), np.average(data["longitude"]))

# Display the hour range in the markdown
st.markdown("Vehicle collision between %i:00 and %i:00" %
            (hour, (hour+1) % 24))

# Create a plot visualization
st.write(pdk.Deck(
    map_style="mapbox://styles/mapbox/dark-v11",
    initial_view_state=pdk.ViewState(
        latitude=32.993213,
        longitude=-96.94766,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=data[['latitude', 'longitude']],
            get_position=['longitude', 'latitude'],
            get_color='[255, 0, 0, 200]',
            get_radius=100,
            pickable=True,
        )
    ],
))

st.subheader("Analysis of Collisions by Minute during %i:00 to %i:00" %
             (hour, (hour+1) % 24))
filtered = data[
    (data["date/time"].dt.hour >= hour)
    &
    (data["date/time"].dt.hour < (hour+1))
]
hist = np.histogram(filtered["date/time"].dt.minute, bins=60, range=(0, 60))[0]
chart_data = pd.DataFrame({'Minutes': range(60), 'Number of Crashes': hist})
fig = px.bar(chart_data, x='Minutes', y="Number of Crashes",
             hover_data=["Minutes", "Number of Crashes"], height=380)
st.write(fig)


# Section 3: Top cities with highest rate of collisions
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
