import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your parquet file
df = pd.read_parquet("yellow_tripdata_2025-06_cleaned.parquet")

# Creating day of week column
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['day_of_week'] = df['tpep_pickup_datetime'].dt.day_name()

# Create weekday/weekend column
df['day_type'] = df['day_of_week'].apply(lambda x: 'Weekend' if x in ['Saturday', 'Sunday'] else 'Weekday')

# Grouping by day_type
fare_trends = df.groupby('day_type').agg(
    avg_fare=('fare_amount', 'mean'),
    avg_tip=('tip_amount', 'mean'),
    avg_distance=('trip_distance', 'mean'),
    total_rides=('fare_amount', 'count')
).reset_index()

print(fare_trends)

# Group by each day of week
daily_trends = df.groupby('day_of_week').agg(
    avg_fare=('fare_amount', 'mean'),
    avg_tip=('tip_amount', 'mean'),
    avg_distance=('trip_distance', 'mean'),
    total_rides=('fare_amount', 'count')
).reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
]).reset_index()

print(daily_trends)




plt.figure(figsize=(8, 5))
sns.barplot(data=fare_trends, x='day_type', y='avg_fare')
plt.title('Average Fare: Weekdays vs Weekends')
plt.ylabel('Average Fare ($)')
plt.xlabel('Day Type')
plt.tight_layout()
plt.show()
