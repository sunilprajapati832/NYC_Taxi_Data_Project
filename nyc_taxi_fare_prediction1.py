import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

import xgboost as xgb
from math import sqrt

# Set style
sns.set(style="whitegrid")

# === Step 1: Load cleaned dataset ===
df = pd.read_parquet('yellow_tripdata_2025-06_cleaned.parquet')

# ✅ Convert to datetime format
df['pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'], errors='coerce')
df['hour'] = df['pickup_datetime'].dt.hour
df['day'] = df['pickup_datetime'].dt.day
df['month'] = df['pickup_datetime'].dt.month
df['year'] = df['pickup_datetime'].dt.year


# Now safely extract hour
df['hour'] = df['pickup_datetime'].dt.hour
df['day_of_week'] = df['pickup_datetime'].dt.dayofweek



# === Step 2: Define features and target ===
features = ['passenger_count', 'trip_distance', 'hour', 'day_of_week', 'payment_type']
target = 'fare_amount'
df = df.dropna(subset=features + [target])

X = df[features]
y = df[target]

# === Step 3: Train-test split ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === Step 4: Preprocessing (OneHot for categorical) ===
categorical = ['day_of_week', 'payment_type']
numerical = ['passenger_count', 'trip_distance', 'hour']

preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical)
], remainder='passthrough')

# === Step 5: Define XGBoost model ===
xgb_model = xgb.XGBRegressor(
    objective='reg:squarederror',
    n_estimators=100,
    random_state=42,
    n_jobs=-1,
    verbosity=0
)

# === Step 6: Build pipeline ===
xgb_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', xgb_model)
])

# === Step 7: Train and evaluate ===
xgb_pipeline.fit(X_train, y_train)
y_pred = xgb_pipeline.predict(X_test)

rmse = sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("--- XGBoost Evaluation ---")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"R²: {r2:.4f}")

# === Step 8: Plot actual vs predicted ===
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.3)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Actual Fare Amount')
plt.ylabel('Predicted Fare Amount')
plt.title('XGBoost: Actual vs Predicted Fare Amount')
plt.tight_layout()
plt.show()

# === Step 9: Feature importance ===
# Get proper feature names after encoding
encoded_cat_features = xgb_pipeline.named_steps['preprocessor'].transformers_[0][1].get_feature_names_out(categorical)
final_features = list(encoded_cat_features) + numerical
importances = xgb_pipeline.named_steps['regressor'].feature_importances_

feat_imp = pd.Series(importances, index=final_features).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=feat_imp.values, y=feat_imp.index)
plt.title('Feature Importance - XGBoost')
plt.tight_layout()
plt.show()
