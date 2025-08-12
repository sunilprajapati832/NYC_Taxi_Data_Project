import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load your cleaned dataset
df = pd.read_parquet('yellow_tripdata_2025-06_cleaned.parquet')

# 1. Feature Engineering
df['pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

df['trip_duration'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds() / 60  # minutes
df['pickup_hour'] = df['pickup_datetime'].dt.hour
df['day_of_week'] = df['pickup_datetime'].dt.day_name()
df['trip_speed_mph'] = df['trip_distance'] / (df['trip_duration'] / 60)

df['is_weekend'] = df['day_of_week'].isin(['Saturday', 'Sunday'])
df['rush_hour_flag'] = df['pickup_hour'].isin([7, 8, 9, 16, 17, 18])

def time_of_day(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'
df['time_of_day'] = df['pickup_hour'].apply(time_of_day)

# ------------------------------
# 2. Visualization
sns.set(style="whitegrid")
output_path = "outputs/feature_engineering/"
import os; os.makedirs(output_path, exist_ok=True)

# A. Trip Duration Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['trip_duration'], bins=100, kde=True)
plt.title('Trip Duration Distribution (in minutes)')
plt.xlim(0, 100)
plt.xlabel("Trip Duration (minutes)")
plt.savefig(f"{output_path}trip_duration_distribution.png")
plt.show()

# B. Trip Speed Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['trip_speed_mph'], bins=100, kde=True)
plt.title('Trip Speed Distribution (in mph)')
plt.xlim(0, 60)
plt.xlabel("Speed (mph)")
plt.savefig(f"{output_path}trip_speed_distribution.png")
plt.show()

# C. Trips by Time of Day
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='time_of_day', order=['Morning', 'Afternoon', 'Evening', 'Night'])
plt.title('Trips by Time of Day')
plt.savefig(f"{output_path}trips_by_time_of_day.png")
plt.show()

# D. Trips by Day of Week
plt.figure(figsize=(8,4))
sns.countplot(data=df, x='day_of_week', order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
plt.title('Trips by Day of the Week')
plt.xticks(rotation=45)
plt.savefig(f"{output_path}trips_by_day_of_week.png")
plt.show()

# E. Rush Hour vs Non-Rush Hour
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='rush_hour_flag')
plt.title('Rush Hour Trip Count')
plt.xticks([0, 1], ['Non-Rush Hour', 'Rush Hour'])
plt.savefig(f"{output_path}rush_hour_trip_count.png")
plt.show()
