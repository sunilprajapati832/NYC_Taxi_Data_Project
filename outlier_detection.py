import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set Seaborn style
sns.set(style="whitegrid")

# Create output directory
output_dir = 'outputs/outliers'
os.makedirs(output_dir, exist_ok=True)

df = pd.read_parquet('yellow_tripdata_2025-06_cleaned.parquet')


# Dummy data simulation (remove this part in real use)
import numpy as np
np.random.seed(42)
df = pd.DataFrame({
    'fare_amount': np.random.normal(15, 10, 1000),
    'trip_distance': np.random.normal(3, 2, 1000),
    'trip_duration_minutes': np.random.normal(15, 10, 1000)
})
df['fare_per_mile'] = df['fare_amount'] / df['trip_distance'].replace(0, 0.01)

# Remove invalid entries
df = df[(df['fare_amount'] > 0) & (df['trip_distance'] > 0) & (df['trip_duration_minutes'] > 0)]

# === Step 2: Boxplots for Outlier Detection ===
def save_boxplot(column, title, filename):
    plt.figure(figsize=(10, 5))
    sns.boxplot(x=df[column])
    plt.title(title)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, filename))
    plt.close()

save_boxplot('fare_amount', 'Fare Amount Outliers', 'fare_amount_boxplot.png')
save_boxplot('trip_distance', 'Trip Distance Outliers', 'trip_distance_boxplot.png')
save_boxplot('fare_per_mile', 'Fare per Mile Outliers', 'fare_per_mile_boxplot.png')

# === Step 3: Histograms Before Filtering ===
plt.figure(figsize=(10, 5))
sns.histplot(df['fare_amount'], kde=True, bins=40)
plt.title("Fare Amount Distribution (Before Filtering)")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'fare_distribution_before.png'))
plt.close()

# === Step 4: Apply Filters for Outlier Removal ===
filtered_df = df[
    df['fare_amount'].between(2, 100) &
    df['trip_distance'].between(0.1, 50) &
    df['trip_duration_minutes'].between(1, 120) &
    df['fare_per_mile'].between(0.5, 20)
]

# === Step 5: Histogram After Filtering ===
plt.figure(figsize=(10, 5))
sns.histplot(filtered_df['fare_amount'], kde=True, bins=40)
plt.title("Fare Amount Distribution (After Filtering)")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'fare_distribution_after.png'))
plt.close()

# === Step 6: Save Filtered Clean Data ===
filtered_data_path = os.path.join(output_dir, 'filtered_clean_data.csv')
filtered_df.to_csv(filtered_data_path, index=False)

print("✅ Outlier detection complete. Outputs saved in 'outputs/outliers/'")
