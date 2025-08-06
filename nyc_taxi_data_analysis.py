import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# You can use either 'pyarrow' or 'fastparquet' as the engine
df = pd.read_parquet('yellow_tripdata_2025-06.parquet', engine='pyarrow')

# Quick checks
print(df.head())
print(df.columns)

# Initial Checks
print(df.shape)
print(df.info())
print(df.describe())

# Nulls
print(df.isnull().sum())


# Datetime Conversation
df['tpep_pickup_datetime']= pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

# Drop Duplicates
df = df.drop_duplicates()

# Remove invalid rows
df = df[df['trip_distance'] > 0]
df = df[df['passenger_count'] > 0]
df = df[df['fare_amount'] >= 0]

# Fix passenger count (replace zeros with median)
median_passenger = df['passenger_count'].median()
df.loc[df['passenger_count'] == 0, 'passenger_count'] = median_passenger

# Save cleaned dataset
df.to_parquet('yellow_tripdata_2025-06_cleaned.parquet')

