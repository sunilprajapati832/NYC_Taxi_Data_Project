from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd

df = pd.read_parquet('yellow_tripdata_2025-06_cleaned.parquet')

# Example: using some cleaned dataframe `df`
X = df[['trip_distance', 'passenger_count']]  # example features
y = df['total_amount']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build pipeline
rf_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train the pipeline
rf_pipe.fit(X_train, y_train)

# Save the pipeline
joblib.dump(rf_pipe, 'rf_pipe.joblib')

# Save the test sets
X_test.to_parquet('X_test.parquet')
y_test.to_frame().to_parquet('y_test.parquet')