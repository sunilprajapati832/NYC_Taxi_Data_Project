import pandas as pd
import numpy as np
import folium
import json
import os

# Set paths
data_path = 'C:/Users/HP-PC/PycharmProjects/NYC_Taxi_Data_Project/yellow_tripdata_2025-06_cleaned.parquet'
geojson_path = 'C:/Users/HP-PC/PycharmProjects/NYC_Taxi_Data_Project/sample_taxi_zones.geojson'
output_map_path = 'C:/Users/HP-PC/PycharmProjects/NYC_Taxi_Data_Project/outputs/nyc_pickups_map.html'

# Load the cleaned trip data
df = pd.read_parquet(data_path)

# Ensure pickup_borough exists (or simulate it using lat-long if not)
# For this demo, let's assume we have a 'pickup_borough' column

if 'pickup_borough' not in df.columns:
    # Simulating with random boroughs (for demo)
    boroughs = ['Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island']
    df['pickup_borough'] = np.random.choice(boroughs, size=len(df))

# Aggregate pickup counts by borough
borough_counts = df['pickup_borough'].value_counts().reset_index()
borough_counts.columns = ['borough', 'pickup_count']

# Load GeoJSON data
with open(geojson_path, 'r') as f:
    geo_data = json.load(f)

# Create Folium map centered on NYC
m = folium.Map(location=[40.7128, -74.0060], zoom_start=10)

# Add choropleth layer
folium.Choropleth(
    geo_data=geo_data,
    name='choropleth',
    data=borough_counts,
    columns=['borough', 'pickup_count'],
    key_on='feature.properties.borough',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Pickup Count by Borough'
).add_to(m)


# Save map to HTML
os.makedirs('outputs', exist_ok=True)
m.save(output_map_path)
print(f"Map saved to {output_map_path}")

