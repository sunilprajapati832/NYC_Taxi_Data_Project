# A. Ride Pattern Visualizations:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Set plot style and size
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Load your cleaned dataframe (adjust the path if needed)
df = pd.read_parquet('yellow_tripdata_2025-06_cleaned.parquet')

# Ensure datetime and derived columns exist
if 'pickup_datetime' in df.columns:
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], errors='coerce')
elif 'tpep_pickup_datetime' in df.columns:
    df['pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'], errors='coerce')

df['hour'] = df['pickup_datetime'].dt.hour
df['day_of_week'] = df['pickup_datetime'].dt.dayofweek

# --- A1. Trip Distance Distribution ---
plt.figure()
sns.histplot(df['trip_distance'], bins=50, kde=True)
plt.title('Trip Distance Distribution')
plt.xlabel('Distance (miles)')
plt.ylabel('Frequency')
plt.xlim(0, 30)
plt.show()

# --- A2. Pickup Hour vs Number of Rides ---
plt.figure()
sns.countplot(x='hour', data=df)
plt.title('Rides by Hour of Day')
plt.xlabel('Hour (0–23)')
plt.ylabel('Number of Rides')
plt.show()

# --- A3. Passenger Count Distribution ---
plt.figure()
sns.countplot(x='passenger_count', data=df)
plt.title('Passenger Count Distribution')
plt.xlabel('Passenger Count')
plt.ylabel('Number of Rides')
plt.show()

# --- A4. Day of Week vs Average Fare ---
plt.figure()
avg_fare_by_day = df.groupby('day_of_week')['fare_amount'].mean()
avg_fare_by_day.plot(kind='bar', color='skyblue')
plt.title('Average Fare by Day of Week')
plt.xlabel('Day of Week (0=Monday)')
plt.ylabel('Average Fare Amount ($)')
plt.show()


# --- B1. Fare Amount Distribution ---
plt.figure()
sns.histplot(df['fare_amount'], bins=50, kde=True, color='green')
plt.title('Fare Amount Distribution')
plt.xlabel('Fare Amount ($)')
plt.ylabel('Frequency')
plt.xlim(0, 100)  # Limit extreme values for better visualization
plt.show()

# --- B2. Fare Amount vs Trip Distance ---
plt.figure()
sns.scatterplot(x='trip_distance', y='fare_amount', data=df, alpha=0.3)
plt.title('Fare Amount vs Trip Distance')
plt.xlabel('Trip Distance (miles)')
plt.ylabel('Fare Amount ($)')
plt.xlim(0, 30)
plt.ylim(0, 100)
plt.show()

# --- B3. Fare Amount by Hour of Day ---
plt.figure()
sns.boxplot(x='hour', y='fare_amount', data=df)
plt.title('Fare Amount by Hour of Day')
plt.xlabel('Hour (0–23)')
plt.ylabel('Fare Amount ($)')
plt.ylim(0, 100)
plt.show()

#Assuming 'rf_pipe' is your trained Random Forest pipeline from ML step
# and 'X_test', 'y_test' are your test datasets


# Predict using Random Forest
y_pred_rf = rf_pipe.predict(X_test)

# --- C1. Feature Importance (Random Forest) ---
encoded_features = list(rf_pipe.named_steps['preprocessor'].transformers_[0][1].get_feature_names_out()) + ['passenger_count', 'trip_distance', 'hour']
importances = rf_pipe.named_steps['regressor'].feature_importances_
feat_imp = pd.Series(importances, index=encoded_features).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=feat_imp.values, y=feat_imp.index)
plt.title('Feature Importance - Random Forest')
plt.tight_layout()
plt.show()

# --- C2. Actual vs Predicted Fare Amount (Random Forest) ---
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred_rf, alpha=0.3)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Actual Fare Amount')
plt.ylabel('Predicted Fare Amount')
plt.title('Random Forest: Actual vs Predicted Fare Amount')
plt.tight_layout()
plt.show()