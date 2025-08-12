import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_parquet('yellow_tripdata_2025-06_cleaned.parquet')

# Optional: if trip_duration is not in dataset
if 'trip_duration' not in df.columns:
    df['pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'], errors='coerce')
    df['dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'], errors='coerce')
    df['trip_duration'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds() / 60
    df = df[df['trip_duration'] > 0]

# 1. Continue EDA
print("Data Summary:")
print(df.info())

# 2. Distribution of Key Numeric Variables

plt.figure(figsize=(16, 5))

plt.subplot(1, 3, 1)
sns.histplot(df['trip_distance'], bins=50, kde=True)
plt.title('Trip Distance Distribution (miles)')

plt.subplot(1, 3, 2)
sns.histplot(df['fare_amount'], bins=50, kde=True)
plt.title('Fare Amount Distribution ($)')

plt.subplot(1, 3, 3)
sns.histplot(df['trip_duration'], bins=50, kde=True)
plt.title('Trip Duration Distribution (minutes)')

plt.tight_layout()
plt.show()

# 3. Passenger Count Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='passenger_count', data=df, hue='passenger_count', palette='viridis', legend=False)
plt.title('Passenger Count Distribution')
plt.show()

# 4. Trips by Hour of Day
df['pickup_hour'] = df['pickup_datetime'].dt.hour

plt.figure(figsize=(10, 5))
sns.countplot(x='pickup_hour', data=df, hue='pickup_hour', palette='coolwarm', legend=False)
plt.title('Number of Trips by Hour of Day')
plt.xlabel('Hour of Day (0-23)')
plt.ylabel('Number of Trips')
plt.show()

# 5. Average Fare and Distance by Hour of Day
hourly_stats = df.groupby('pickup_hour').agg({
    'fare_amount': 'mean',
    'trip_distance': 'mean',
    'trip_duration': 'mean'
}).reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x='pickup_hour', y='fare_amount', data=hourly_stats, label='Avg Fare ($)', color='blue')
sns.lineplot(x='pickup_hour', y='trip_distance', data=hourly_stats, label='Avg Distance (miles)', color='green')
sns.lineplot(x='pickup_hour', y='trip_duration', data=hourly_stats, label='Avg Duration (min)', color='red')
plt.title('Average Fare, Distance, and Duration by Hour of Day')
plt.xlabel('Hour of Day (0-23)')
plt.ylabel('Average Values')
plt.legend()
plt.show()

# 6. Correlation Heatmap of Numeric Variables
plt.figure(figsize=(8, 6))
sns.heatmap(df[['fare_amount', 'trip_distance', 'trip_duration', 'passenger_count']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()