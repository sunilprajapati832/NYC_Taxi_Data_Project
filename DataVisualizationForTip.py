import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your parquet file
df = pd.read_parquet("yellow_tripdata_2025-06_cleaned.parquet")

# Optional: map payment_type codes (based on NYC TLC docs)
payment_map = {
    1: "Credit Card",
    2: "Cash",
    3: "No Charge",
    4: "Dispute",
    5: "Unknown",
    6: "Voided Trip"
}
df['payment_type_label'] = df['payment_type'].map(payment_map)

summary = df.groupby('payment_type_label').agg(
    avg_tip=('tip_amount', 'mean'),
    tip_rate=('tip_amount', lambda x: (x > 0).mean())
).reset_index()

summary['tip_rate_percent'] = summary['tip_rate'] * 100  # convert to %
summary = summary.sort_values('avg_tip', ascending=False)

print(summary)


# Bar Chart 1: Average Tip Amount
plt.figure(figsize=(8, 4))
sns.barplot(data=summary, x='payment_type_label', y='avg_tip')
plt.title('Average Tip Amount by Payment Type')
plt.xlabel('Payment Type')
plt.ylabel('Average Tip ($)')
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Bar Chart 2: Tip Frequency (%)
plt.figure(figsize=(8, 4))
sns.barplot(data=summary, x='payment_type_label', y='tip_rate_percent')
plt.title('Tip Frequency by Payment Type')
plt.xlabel('Payment Type')
plt.ylabel('Tip Frequency (%)')
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
