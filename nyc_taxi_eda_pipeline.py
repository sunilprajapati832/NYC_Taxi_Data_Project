import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set styles
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

# Load the cleaned dataset
data_path = "yellow_tripdata_2025-06_cleaned.parquet"
df = pd.read_parquet(data_path)

# Create output directory for charts
os.makedirs("outputs/eda_charts", exist_ok=True)

# 1. Basic Information
print("\nShape of Dataset:", df.shape)
print("\nInfo:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# 2. Feature Engineering
df['pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'], errors='coerce')
df['dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'], errors='coerce')
df['trip_duration'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds() / 60
df['pickup_hour'] = df['pickup_datetime'].dt.hour
df['pickup_day'] = df['pickup_datetime'].dt.day_name()

# 3. Univariate Analysis

# Passenger Count Distribution
sns.countplot(x='passenger_count', hue='passenger_count', data=df, palette='viridis', legend=False)
plt.title("Passenger Count Distribution")
plt.savefig("outputs/eda_charts/passenger_count_distribution.png")
plt.clf()

# Payment Type
sns.countplot(x='payment_type', hue='payment_type', data=df, palette='Set2', legend=False)
plt.title("Payment Type Distribution")
plt.savefig("outputs/eda_charts/payment_type_distribution.png")
plt.clf()

# Trip Distance Histogram
sns.histplot(df['trip_distance'], bins=50, kde=True, color='skyblue')
plt.title("Trip Distance Distribution")
plt.savefig("outputs/eda_charts/trip_distance_distribution.png")
plt.clf()

# Fare Amount Histogram
sns.histplot(df['fare_amount'], bins=50, kde=True, color='orange')
plt.title("Fare Amount Distribution")
plt.savefig("outputs/eda_charts/fare_amount_distribution.png")
plt.clf()

# Trip Duration Histogram
sns.histplot(df['trip_duration'], bins=50, kde=True, color='green')
plt.title("Trip Duration Distribution (min)")
plt.savefig("outputs/eda_charts/trip_duration_distribution.png")
plt.clf()

# 4. Bivariate Analysis

# Fare vs Distance
sns.scatterplot(x='trip_distance', y='fare_amount', data=df, alpha=0.3)
plt.title("Fare vs Trip Distance")
plt.savefig("outputs/eda_charts/fare_vs_distance.png")
plt.clf()

# Fare vs Duration
sns.scatterplot(x='trip_duration', y='fare_amount', data=df, alpha=0.3)
plt.title("Fare vs Trip Duration")
plt.savefig("outputs/eda_charts/fare_vs_duration.png")
plt.clf()

# 5. Temporal Analysis

# Hourly Trends
hourly_stats = df.groupby('pickup_hour')[['fare_amount', 'trip_distance', 'trip_duration']].mean().reset_index()
sns.lineplot(x='pickup_hour', y='fare_amount', data=hourly_stats, label='Avg Fare ($)')
sns.lineplot(x='pickup_hour', y='trip_distance', data=hourly_stats, label='Avg Distance (miles)')
sns.lineplot(x='pickup_hour', y='trip_duration', data=hourly_stats, label='Avg Duration (min)')
plt.title("Hourly Trip Metrics")
plt.legend()
plt.savefig("outputs/eda_charts/hourly_trip_metrics.png")
plt.clf()

# Weekday Trip Count
sns.countplot(x='pickup_day', data=df, order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'], hue='pickup_day', palette='coolwarm', legend=False)
plt.title("Trips by Day of the Week")
plt.xticks(rotation=45)
plt.savefig("outputs/eda_charts/weekday_trip_counts.png")
plt.clf()

print("EDA pipeline executed successfully. Charts saved to outputs/eda_charts/")
