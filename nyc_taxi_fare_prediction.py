import pandas as pd
import numpy as np
# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

import xgboost as xgb
from math import sqrt

# Set style
sns.set(style="whitegrid")


# === Step 1: Load cleaned & filtered dataset ===
df = pd.read_parquet('yellow_tripdata_2025-06_cleaned.parquet')



# Print all column names
print("Available columns:", df.columns)

# If the column exists, convert it
if 'pickup_datetime' in df.columns:
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
elif 'tpep_pickup_datetime' in df.columns:
    df['pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])  # rename for consistency
else:
    raise ValueError("pickup_datetime column not found!")


# Create hour and day_of_week features
df['hour'] = df['pickup_datetime'].dt.hour
df['day_of_week'] = df['pickup_datetime'].dt.dayofweek


# === Step 2: Prepare features and target ===
features = ['passenger_count', 'trip_distance', 'hour', 'day_of_week', 'payment_type']
target = 'fare_amount'

# Drop rows with missing values in features or target
df = df.dropna(subset=features + [target])

X = df[features]
y = df[target]

# === Step 3: Split dataset ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === Step 4: Preprocessing pipeline for categorical variables ===
categorical_features = ['day_of_week', 'payment_type']
numerical_features = ['passenger_count', 'trip_distance', 'hour']

preprocessor = ColumnTransformer(transformers=[
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
], remainder='passthrough')

# === Helper function: Train, predict, evaluate model ===
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

    # Plot actual vs predicted
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.3)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel('Actual Fare Amount')
    plt.ylabel('Predicted Fare Amount')
    plt.title(f'{model_name}: Actual vs Predicted Fare Amount')
    plt.tight_layout()
    plt.show()

    return pipe

# === Step 5: Train & Evaluate Linear Regression ===
lr_model = LinearRegression()
lr_pipe = train_evaluate_model(lr_model, "Linear Regression")

# === Step 6: Train & Evaluate Random Forest Regressor ===
rf_model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
rf_pipe = train_evaluate_model(rf_model, "Random Forest Regressor")

# === Step 7: Train & Evaluate XGBoost Regressor ===
xgb_model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, random_state=42, n_jobs=-1)
xgb_pipe = train_evaluate_model(xgb_model, "XGBoost Regressor")

# === Step 8: Feature Importance from Random Forest ===
# Get feature names after one-hot encoding
encoded_feature_names = list(rf_pipe.named_steps['preprocessor'].transformers_[0][1].get_feature_names_out(categorical_features)) + numerical_features

importances = rf_pipe.named_steps['regressor'].feature_importances_

feat_imp = pd.Series(importances, index=encoded_feature_names).sort_values(ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(x=feat_imp.values, y=feat_imp.index)
plt.title('Feature Importance - Random Forest')
plt.tight_layout()
plt.show()
