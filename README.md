# United States of America Motor Vehicle Collisions Dashboard

This Streamlit dashboard provides insights into motor vehicle collisions in the United States. It allows users to explore data related to injuries, collisions by hour and minute, and identify the top cities with the highest rate of collisions.

## Getting Started

To run this dashboard locally, you need to install the following Python libraries:

- streamlit
- pandas
- numpy
- pydeck
- plotly.express

You can install these libraries using pip or conda, for example:

```bash
  pip install requirements.txt
```


## Usage

1. Run the Streamlit app by executing the following command in your terminal:

```bash
  streamlit run dashboard.py
```


2. Open a web browser and go to `http://localhost:8501` to access the dashboard.

3. Use the different inputs and visualizations in the dashboard to explore the data on motor vehicle collisions in the United States.

## Features

The dashboard includes the following sections:

### Map of Injuries by number of reported injuries

- Users can select the number of people affected by injuries in vehicle collisions using a slider input.
- A map visualization shows the locations with injured persons greater than or equal to the selected value.

### Collisions by Hour and Minute

- Users can select an hour range using a selectbox input.
- A plot visualization displays the frequency of collisions during the selected time period using scatterplot markers on a map.

### Top Cities with Highest Rate of Collisions

- Users can select the affected people type (Pedestrians, Cyclists, or Motorists) using a selectbox input.
- The top 10 cities in the United States with the highest rate of collisions for the selected affected people type are displayed.

Additionally, users can also show raw data by checking the "Show Raw Data" checkbox.

## Data Source

The data for this dashboard is sourced from the following URL: ["https://www.dropbox.com/s/7uyen8z14lhnxf7/US-Accidents%5BEdited%5D.csv?dl=1"]
