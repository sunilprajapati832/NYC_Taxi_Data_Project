import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Load the cleaned taxi dataset
df = pd.read_parquet("yellow_tripdata_2025-06_cleaned.parquet")

# Step 2: Load the NYC Taxi Zone GeoJSON file
geojson_path = "sample_taxi_zones.geojson"
zones_gdf = gpd.read_file(geojson_path)

# Step 3: Quick geometry check
print("GeoJSON CRS:", zones_gdf.crs)
print("First 5 geometries:", zones_gdf.geometry.head())

# Step 4: Count pickups per zone
pickup_counts = df['PULocationID'].value_counts().reset_index()
pickup_counts.columns = ['LocationID', 'pickup_count']

# Step 5: Merge zone data with pickup counts
zones_gdf['LocationID'] = zones_gdf['LocationID'].astype(int)
merged_gdf = zones_gdf.merge(pickup_counts, how='left', on='LocationID')
merged_gdf['pickup_count'] = merged_gdf['pickup_count'].fillna(0)

# Step 6: Debug – Check data before plotting
print("\nTop 5 zones by pickup count:")
print(merged_gdf[['LocationID', 'pickup_count']].sort_values('pickup_count', ascending=False).head())
print("\nMissing geometries count:", merged_gdf.geometry.isnull().sum())

# Step 7: Save folder
os.makedirs("outputs/zone_analysis", exist_ok=True)

# Step 8: Plot pickup counts by zone
fig, ax = plt.subplots(figsize=(12, 10))
merged_gdf.plot(column='pickup_count', cmap='OrRd', linewidth=0.8, edgecolor='black', legend=True, ax=ax)
ax.set_title("NYC Taxi Pickup Counts by Zone", fontsize=15)
ax.set_axis_off()

# Step 9: Save the figure
output_path = "outputs/zone_analysis/zone_pickup_distribution.png"
plt.savefig(output_path, dpi=300)
plt.close()

print(f"✅ Zone-level map saved to: {output_path}")
