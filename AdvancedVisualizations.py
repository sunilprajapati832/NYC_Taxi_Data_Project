import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import joblib  # to load saved model pipelines

# Set consistent plotting style
sns.set(style="whitegrid")

# Load cleaned data
df = pd.read_parquet('yellow_tripdata_2025-06_cleaned.parquet')

# ✅ Convert to datetime format
df['pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'], errors='coerce')

# ✅ Extract time components
df['hour'] = df['pickup_datetime'].dt.hour
df['day'] = df['pickup_datetime'].dt.day
df['month'] = df['pickup_datetime'].dt.month
df['year'] = df['pickup_datetime'].dt.year
df['day_of_week'] = df['pickup_datetime'].dt.dayofweek
df['date'] = df['pickup_datetime'].dt.date  # ✅ For daily average analysis

# --------------------------
# Load saved model and test data
# --------------------------
rf_pipe = joblib.load('rf_pipe.joblib')
X_test = pd.read_parquet('X_test.parquet')
y_test = pd.read_parquet('y_test.parquet')

# Predict for analysis
y_pred_rf = rf_pipe.predict(X_test)

# ----------------------------------------------------
# 1. Time Series: Average Fare Amount Over Time
# ----------------------------------------------------
avg_fare_per_day = df.groupby('date')['fare_amount'].mean()

plt.figure(figsize=(12, 6))
avg_fare_per_day.plot()
plt.title('Average Fare Amount Over Time')
plt.xlabel('Date')
plt.ylabel('Average Fare ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ------------------------------------------------------
# 2. Heatmap: Hour of Day vs Day of Week Ride Counts
# ------------------------------------------------------
ride_counts = df.groupby(['day_of_week', 'hour']).size().unstack()

plt.figure(figsize=(12, 6))
sns.heatmap(ride_counts, cmap='YlGnBu')
plt.title('Heatmap: Number of Rides by Day and Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Day of Week (0=Monday)')
plt.tight_layout()
plt.show()

# ----------------------------------------------------
# 3. Correlation Matrix of Numeric Features
# ----------------------------------------------------
numeric_cols = ['fare_amount', 'trip_distance', 'passenger_count', 'hour', 'day_of_week']
corr = df[numeric_cols].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()

# -----------------------------------------------------
# 4. Residuals vs Predicted (Model Error Analysis)
# -----------------------------------------------------
print("y_test shape:", y_test.shape)
print("y_pred_rf shape:", y_pred_rf.shape)
residuals = np.ravel(y_test) - y_pred_rf


plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_pred_rf, y=residuals, alpha=0.5)
plt.axhline(0, color='red', linestyle='--')
plt.title('Residuals vs Predicted Fare (Random Forest)')
plt.xlabel('Predicted Fare')
plt.ylabel('Residuals')
plt.tight_layout()
plt.show()

# -----------------------------------------------------
# 5. Actual vs Predicted Fare (Model Performance Plot)
# -----------------------------------------------------
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test.values.ravel(), y=y_pred_rf, alpha=0.4)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')
plt.title('Actual vs Predicted Fare Amount')
plt.xlabel('Actual Fare')
plt.ylabel('Predicted Fare')
plt.tight_layout()
plt.show()

# ------------------------------------------------------
# 6. Feature Importance from Random Forest Model
# ------------------------------------------------------
print("Pipeline steps:", rf_pipe.named_steps)

feature_importances = rf_pipe.named_steps['model'].feature_importances_
feature_names = X_test.columns

importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importances})
importance_df = importance_df.sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=importance_df)
plt.title('Feature Importances from Random Forest')
plt.tight_layout()
plt.show()

# -----------------------------------------------------
# 7. Geospatial Plot: Pickup Location Distribution
# -----------------------------------------------------
if 'pickup_longitude' in df.columns and 'pickup_latitude' in df.columns:
    plt.figure(figsize=(10, 8))
    plt.scatter(df['pickup_longitude'], df['pickup_latitude'], alpha=0.1, s=1)
    plt.title('Pickup Location Distribution')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.tight_layout()
    plt.show()
else:
    print("Pickup latitude/longitude not available in this dataset.")
