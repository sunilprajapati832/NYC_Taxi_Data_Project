import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_parquet("yellow_tripdata_2025-06_cleaned.parquet")

# Columns: tpep_pickup_datetime, tpep_dropoff_datetime, trip_distance, fare_amount

# Ensure datetime format
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

# 1️⃣ Create Trip Duration (minutes)
df['trip_duration_min'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60

# Filter out unrealistic trips
df = df[(df['trip_duration_min'] > 0) & (df['trip_duration_min'] < 300)]  # less than 5 hours

# 2️⃣ Create Average Speed (mph)
df['avg_speed_mph'] = df['trip_distance'] / (df['trip_duration_min'] / 60)
df = df[(df['avg_speed_mph'] > 0) & (df['avg_speed_mph'] < 80)]  # filter unrealistic speeds

# 3️⃣ Create Surge-like Indicator
df['hour'] = df['tpep_pickup_datetime'].dt.hour
df['day_of_week'] = df['tpep_pickup_datetime'].dt.day_name()

# Mark surge hours (Morning 8-9 AM, Evening 3-7 PM)
df['surge_flag'] = df['hour'].apply(lambda x: 1 if (8 <= x <= 9) or (15 <= x <= 19) else 0)

# ---------------- PLOTS ---------------- #

# Plot 1: Trip Duration Distribution
plt.figure(figsize=(10,6))
sns.histplot(df['trip_duration_min'], bins=50, kde=True, color='skyblue')
plt.title('Trip Duration Distribution (Minutes)')
plt.xlabel('Trip Duration (min)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Plot 2: Average Speed by Hour (fixed warning)
plt.figure(figsize=(10,6))
sns.boxplot(x='hour', y='avg_speed_mph', data=df, palette='coolwarm')
plt.title('Average Speed by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Average Speed (mph)')
plt.tight_layout()
plt.show()

# Plot 3: Surge-like Demand Heatmap (fixed pivot)
heatmap_data = df.groupby(['day_of_week', 'hour']).size().reset_index(name='trip_count')

# Use keyword arguments for pivot
heatmap_pivot = heatmap_data.pivot(index='day_of_week', columns='hour', values='trip_count')

# Reorder days for better readability
order_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
heatmap_pivot = heatmap_pivot.reindex(order_days)

plt.figure(figsize=(12,6))
sns.heatmap(heatmap_pivot, cmap='YlOrRd', annot=False)
plt.title('Trip Demand Heatmap by Day and Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Day of Week')
plt.tight_layout()
plt.show()


# Save engineered dataset
df.to_csv('NYC_Taxi_with_Features.csv', index=False)
print("Feature engineered dataset saved as 'NYC_Taxi_with_Features.csv'")
