import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# 1. Load Data
# =========================
# Replace file paths with your dataset paths
df = pd.read_parquet("yellow_tripdata_2025-06_cleaned.parquet")
zones_df = pd.read_csv("taxi+_zone_lookup.csv")

# =========================
# 2. Find Top Pickup Locations
# =========================
top_pickups = (
    df.groupby('PULocationID')
    .size()
    .reset_index(name='total_rides')
    .sort_values(by='total_rides', ascending=False)
    .head(10)
)

# Merge with zone names
top_pickups = top_pickups.merge(
    zones_df[['LocationID', 'Zone']],
    left_on='PULocationID',
    right_on='LocationID',
    how='left'
)[['Zone', 'total_rides']]

# =========================
# 3. Find Top Dropoff Locations
# =========================
top_dropoffs = (
    df.groupby('DOLocationID')
    .size()
    .reset_index(name='total_rides')
    .sort_values(by='total_rides', ascending=False)
    .head(10)
)

# Merge with zone names
top_dropoffs = top_dropoffs.merge(
    zones_df[['LocationID', 'Zone']],
    left_on='DOLocationID',
    right_on='LocationID',
    how='left'
)[['Zone', 'total_rides']]

# =========================
# 4. Visualization
# =========================
sns.set_style("whitegrid")

# --- Top Pickups Chart ---
plt.figure(figsize=(10, 6))
sns.barplot(
    data=top_pickups,
    x='total_rides',
    y='Zone',
    palette='Blues_r'
)
plt.title("Top 10 Pickup Locations in NYC (June 2025)")
plt.xlabel("Total Rides")
plt.ylabel("Pickup Zone")
plt.tight_layout()
plt.show()

# --- Top Dropoffs Chart ---
plt.figure(figsize=(10, 6))
sns.barplot(
    data=top_dropoffs,
    x='total_rides',
    y='Zone',
    palette='Greens_r'
)
plt.title("Top 10 Dropoff Locations in NYC (June 2025)")
plt.xlabel("Total Rides")
plt.ylabel("Dropoff Zone")
plt.tight_layout()
plt.show()

# =========================
# 5. Save Results (Optional)
# =========================
top_pickups.to_csv("Top_10_Pickup_Locations.csv", index=False)
top_dropoffs.to_csv("Top_10_Dropoff_Locations.csv", index=False)

print("✅ Analysis complete! CSV files and charts generated.")
