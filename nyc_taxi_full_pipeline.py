import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import sqrt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

import xgboost as xgb

# Set style for plots
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# === Load cleaned & filtered dataset ===
df = pd.read_parquet('yellow_tripdata_2025-06_cleaned.parquet')

# Print columns for sanity check
print("Available columns:", df.columns)

# Ensure datetime column exists and convert
if 'pickup_datetime' in df.columns:
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], errors='coerce')
elif 'tpep_pickup_datetime' in df.columns:
    df['pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'], errors='coerce')
else:
    raise ValueError("pickup_datetime column not found!")

# Create time features
df['hour'] = df['pickup_datetime'].dt.hour
df['day_of_week'] = df['pickup_datetime'].dt.dayofweek

# === Prepare features and target ===
features = ['passenger_count', 'trip_distance', 'hour', 'day_of_week', 'payment_type']
target = 'fare_amount'

# Drop rows with missing features or target
df = df.dropna(subset=features + [target])

X = df[features]
y = df[target]

# === Split data into train-test ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === Preprocessing pipeline ===
categorical_features = ['day_of_week', 'payment_type']
numerical_features = ['passenger_count', 'trip_distance', 'hour']

preprocessor = ColumnTransformer(transformers=[
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
], remainder='passthrough')

# === Helper function to train, evaluate & plot model ===
def train_evaluate_model(model, model_name):
    pipe = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', model)
    ])
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"--- {model_name} Evaluation ---")
    print(f"RMSE: {rmse:.4f}")
    print(f"MAE: {mae:.4f}")
    print(f"R²: {r2:.4f}")
    print()

    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.3)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel('Actual Fare Amount')
    plt.ylabel('Predicted Fare Amount')
    plt.title(f'{model_name}: Actual vs Predicted Fare Amount')
    plt.tight_layout()
    plt.show()

    return pipe

# === Train & evaluate models ===
lr_model = LinearRegression()
lr_pipe = train_evaluate_model(lr_model, "Linear Regression")

rf_model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
rf_pipe = train_evaluate_model(rf_model, "Random Forest Regressor")

xgb_model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, random_state=42, n_jobs=-1)
xgb_pipe = train_evaluate_model(xgb_model, "XGBoost Regressor")

# === Visualizations - Ride Patterns & Data Insights ===

# Trip Distance Distribution
plt.figure()
sns.histplot(df['trip_distance'], bins=50, kde=True)
plt.title('Trip Distance Distribution')
plt.xlabel('Distance (miles)')
plt.ylabel('Frequency')
plt.xlim(0, 30)
plt.show()

# Rides by Hour of Day
plt.figure()
sns.countplot(x='hour', data=df)
plt.title('Rides by Hour of Day')
plt.xlabel('Hour (0–23)')
plt.ylabel('Number of Rides')
plt.show()

# Passenger Count Distribution
plt.figure()
sns.countplot(x='passenger_count', data=df)
plt.title('Passenger Count Distribution')
plt.xlabel('Passenger Count')
plt.ylabel('Number of Rides')
plt.show()

# Average Fare by Day of Week
plt.figure()
avg_fare_by_day = df.groupby('day_of_week')['fare_amount'].mean()
avg_fare_by_day.plot(kind='bar', color='skyblue')
plt.title('Average Fare by Day of Week')
plt.xlabel('Day of Week (0=Monday)')
plt.ylabel('Average Fare Amount ($)')
plt.show()

# Fare Amount Distribution
plt.figure()
sns.histplot(df['fare_amount'], bins=50, kde=True, color='green')
plt.title('Fare Amount Distribution')
plt.xlabel('Fare Amount ($)')
plt.ylabel('Frequency')
plt.xlim(0, 100)
plt.show()

# Fare Amount vs Trip Distance
plt.figure()
sns.scatterplot(x='trip_distance', y='fare_amount', data=df, alpha=0.3)
plt.title('Fare Amount vs Trip Distance')
plt.xlabel('Trip Distance (miles)')
plt.ylabel('Fare Amount ($)')
plt.xlim(0, 30)
plt.ylim(0, 100)
plt.show()

# Fare Amount by Hour of Day
plt.figure()
sns.boxplot(x='hour', y='fare_amount', data=df)
plt.title('Fare Amount by Hour of Day')
plt.xlabel('Hour (0–23)')
plt.ylabel('Fare Amount ($)')
plt.ylim(0, 100)
plt.show()

# === Feature Importance from Random Forest ===
encoded_features = list(rf_pipe.named_steps['preprocessor'].transformers_[0][1].get_feature_names_out()) + numerical_features
importances = rf_pipe.named_steps['regressor'].feature_importances_

feat_imp = pd.Series(importances, index=encoded_features).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=feat_imp.values, y=feat_imp.index)
plt.title('Feature Importance - Random Forest')
plt.tight_layout()
plt.show()

# === Actual vs Predicted Fare (Random Forest) ===
y_pred_rf = rf_pipe.predict(X_test)

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred_rf, alpha=0.3)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Actual Fare Amount')
plt.ylabel('Predicted Fare Amount')
plt.title('Random Forest: Actual vs Predicted Fare Amount')
plt.tight_layout()
plt.show()
