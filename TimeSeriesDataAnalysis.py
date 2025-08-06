import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_parquet('yellow_tripdata_2025-06_cleaned.parquet')

#  1. Fare Amount Patterns Over Time

# Convert to datetime
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])

# Set datetime as index for time-series analysis
df.set_index('tpep_pickup_datetime', inplace=True)

# Resample fare amount
monthly_fare = df['fare_amount'].resample('ME').mean()
daily_fare = df['fare_amount'].resample('D').mean()

# Plot monthly fare trend
plt.figure(figsize=(12, 6))
monthly_fare.plot()
plt.title('Monthly Average Fare Amount')
plt.xlabel('Month')
plt.ylabel('Average Fare ($)')
plt.grid(True)
plt.tight_layout()
plt.show()

#Weekday vs Weekend
#Time of Day (Hour-wise)

df['hour'] = df.index.hour
df['day_of_week'] = df.index.day_name()

# Hourly fare trend
hourly_avg_fare = df.groupby('hour')['fare_amount'].mean()

plt.figure(figsize=(10, 5))
hourly_avg_fare.plot(kind='bar')
plt.title('Average Fare by Hour of Day')
plt.xlabel('Hour')
plt.ylabel('Average Fare ($)')
plt.grid(True)
plt.tight_layout()
plt.show()


# 2. Passenger Count & Trends

# Passenger distribution by hour
hourly_passengers = df.groupby('hour')['passenger_count'].sum()

plt.figure(figsize=(10, 5))
hourly_passengers.plot(kind='bar')
plt.title('Total Passengers by Hour')
plt.xlabel('Hour')
plt.ylabel('Passenger Count')
plt.grid(True)
plt.tight_layout()
plt.show()


#  3. Payment Type Trends Over Time

# Count of payment types
payment_counts = df['payment_type'].value_counts()

plt.figure(figsize=(7, 5))
payment_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribution of Payment Types')
plt.ylabel('')
plt.tight_layout()
plt.show()

payment_map = {
    1: 'Credit Card',
    2: 'Cash',
    3: 'No Charge',
    4: 'Dispute',
    5: 'Unknown',
    6: 'Voided Trip'
}
df['payment_type'] = df['payment_type'].map(payment_map)

# Daily usage of payment types
daily_payment = df.groupby([df.index.date, 'payment_type']).size().unstack().fillna(0)

plt.figure(figsize=(14, 6))
daily_payment.plot()
plt.title('Daily Trends in Payment Types')
plt.xlabel('Date')
plt.ylabel('Number of Payments')
plt.grid(True)
plt.tight_layout()
plt.show()

# 4. Correlation Between Fare Amount vs Passenger Count

plt.figure(figsize=(8, 6))
sns.regplot(x='passenger_count', y='fare_amount', data=df, scatter_kws={'alpha':0.3})
plt.title('Correlation: Fare Amount vs Passenger Count')
plt.xlabel('Passenger Count')
plt.ylabel('Fare Amount ($)')
plt.grid(True)
plt.tight_layout()
plt.show()

correlation = df['fare_amount'].corr(df['passenger_count'])
print(f"Correlation Coefficient: {correlation:.2f}")

"""
Interpretation:
Close to 0 → Weak/no correlation
Close to 1 → Strong positive correlation
Close to -1 → Strong negative correlation
"""

#  5. Time-Based Trends of Trip Distance
# Daily Average Trip Distance
daily_distance = df['trip_distance'].resample('D').mean()

plt.figure(figsize=(12, 6))
daily_distance.plot()
plt.title('Daily Average Trip Distance')
plt.xlabel('Date')
plt.ylabel('Distance (miles)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Hourly Average Distance
hourly_distance = df.groupby(df.index.hour)['trip_distance'].mean()

plt.figure(figsize=(10, 5))
hourly_distance.plot(kind='bar')
plt.title('Average Trip Distance by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Distance (miles)')
plt.grid(True)
plt.tight_layout()
plt.show()

# 6. Patterns in Extra Charges (Surcharges, Taxes, Tolls, etc.)

# Total Extra Charges Distribution
extra_columns = ['extra', 'mta_tax', 'tolls_amount', 'improvement_surcharge']

# Sum over entire dataset
total_extras = df[extra_columns].sum()

plt.figure(figsize=(8, 5))
total_extras.plot(kind='bar')
plt.title('Total Extra Charges Distribution')
plt.ylabel('Amount ($)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Time-Based Trends in Extra Charges
monthly_extras = df[extra_columns].resample('ME').mean()

plt.figure(figsize=(12, 6))
monthly_extras.plot()
plt.title('Monthly Trends of Extra Charges')
plt.xlabel('Month')
plt.ylabel('Average Amount ($)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df[['fare_amount', 'passenger_count', 'trip_distance'] + extra_columns].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()
