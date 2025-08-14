# 🗽 NYC Yellow Taxi Trip Data Analytics Project (focused on Transportation Application of Data Analytics)
**Project Duration:** June 2025  
**Dataset Size:** ~4.3M rows × 20 columns `yellow_tripdata_2025-06.parquet`(.parquet format)  
**Project Type:** Real-World, End-to-End Data Analytics with Community Collaboration  (This project explores NYC Yellow Taxi trip data to uncover patterns in passenger behavior, trip fares, tips, and congestion trends using Python and pandas.)

## 📊 Columns Explained
| **Column Name**         | **Description**                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------- |
| `VendorID`              | Code for the provider (1 = Creative Mobile Technologies, 2 = VeriFone Inc, 4/5/7 = Other vendors) |
| `tpep_pickup_datetime`  | Date and time when the trip started (pickup)                                                      |
| `tpep_dropoff_datetime` | Date and time when the trip ended (drop-off)                                                      |
| `passenger_count`       | Number of passengers in the taxi                                                                  |
| `trip_distance`         | Total distance of the trip in miles                                                               |
| `RatecodeID`            | Rate code used for fare calculation (1 = Standard, 2 = JFK, etc.)                                 |
| `store_and_fwd_flag`    | 'Y' if the trip record was stored in the taxi’s memory before sending; 'N' otherwise              |
| `PULocationID`          | TLC Taxi Zone ID where the trip started (pickup location)                                         |
| `DOLocationID`          | TLC Taxi Zone ID where the trip ended (drop-off location)                                         |
| `payment_type`          | Method used to pay: 1 = Credit card, 2 = Cash, 3 = No charge, etc.                                |
| `fare_amount`           | Fare for the trip before extra fees and surcharges                                                |
| `extra`                 | Extra charges (e.g., for rush hour or night travel)                                               |
| `mta_tax`               | \$0.50 Metropolitan Transportation Authority tax per trip                                         |
| `tip_amount`            | Tip amount paid by the passenger (non-zero usually for card payments)                             |
| `tolls_amount`          | Amount paid for tolls during the trip                                                             |
| `improvement_surcharge` | \$0.30 fee for taxi improvement projects (added to each trip)                                     |
| `total_amount`          | Total amount paid by the customer (fare + all charges + tips)                                     |
| `congestion_surcharge`  | Fee added for trips below 96th St in Manhattan (usually \$2.75)                                   |
| `Airport_fee`           | Flat fee for pickups from airports (like JFK, LaGuardia)                                          |
| `cbd_congestion_fee`    | Congestion fee for entering Manhattan’s Central Business District                                 |



Step 1: Define the Problem Statement
Step 2: Understand the Business Context
Step 3: Data Collection
Step 4: Data Inspection & Loading
Step 5: Data Cleaning
Step 6: Feature Understanding
Step 7: Data Transformation
Step 8: Exploratory Data Analysis (EDA)
Step 9: Advanced Insights
Step 10: Geospatial Mapping (Optional)
Step 11: Machine Learning
Step 12: Data Visualization & Storytelling
Step 13: Publishing & GitHub Upload
Step 14: Decision Making & Actions




---

## ✅ Step 1: Define the Problem Statement

**Goal:** Uncover meaningful insights from NYC Yellow Taxi trip data — such as peak demand hours, tipping behavior, airport ride patterns, and cost breakdowns — using scalable analytics workflows.

### Key Questions:

1- When are most taxi rides occurring (peak hours)?
2- How do payment types affect tip amounts & which method is most commonly preferred by customers?
3- Are there differences in fare trends between weekdays and weekends?
4- What are the most frequent pickup and dropoff locations?
5- Can we build features like trip duration, speed or surge indicators?


### Answers (after complete analysis):

## 1- 📈 Answer:
According to our analysis of NYC Yellow Taxi trip data for June 2025, the peak ride demand occurs between 3:00 PM and 7:00 PM.
🕒 Top Peak Hours Identified:
Highest trip volumes observed during: 3:00 PM to 7:00 PM (Consistent daily spikes in this evening window)
🔍 Why This Happens:
This time frame aligns with the end of standard office hours (9:00 AM to 4:00 PM). As workers leave offices, demand for taxis increases sharply — especially in business districts like Midtown and Downtown Manhattan.

Refrences : ├── figure_1 A2 Rides by Hour of Day (Data Visualization)
            ├── figure_1 Heatmap Number of Rides by Day and Hour (Advance Visualization)
            ├── figure_3 Total Passenger by Hour (Time Series Data Analysis)
            ├── nyc_taxi_data_analysis.py
            ├── DataVisualization.py
            ├── AdvancedVisualization.py
            ├── TimeSeriesDataAnalysis.py


## 2- 📈 Answer: 
This analysis revealed that payment type significantly impacts ride & tipping behavior. Specifically:
💳 Credit card payments are associated with: 
Credit cards are the overwhelmingly preferred payment method (85.8 %) with Higher average tip amounts (4.43 $)
Tip Frequency 93.39%
Greater likelihood of leaving a tip
💵 Cash payments tend to show:
Lower recorded tips ( 0.0004 $ Avg ) possibly due to offline tipping
Analysis of 4.3 million taxi rides shows that both tipping behavior and payment preferences strongly favor Credit Cards (Refrenced by PyCharm Console Result Table).

Refrences : ├── Figure_1.1 Trip Frequency by Payment Type (DataVisualizationForTip)
            ├── Figure_1 Average Tip Amount by Payment Type (DataVisualizationForTip)
            ├── Figure_4 Distribution of Payment Types (Blue: Credit Card) (TimeSeriesDataAnalysis)
            ├── Figure_5 Daily Trends in Payment Types (TimeSeriesDataAnalysis)
            ├── payment_type_distribution (Type 1: Credit Card) (nyc_taxi_eda_pipeline)
            ├── Figure_3.2 Feature Importance XGBoost (nyc_taxi_fare_prediction_ML)
            ├── Figure_4 Feature Importance Random Forest (nyc_taxi_fare_prediction_ML)
            ├── DataVisualizationForTip.py
            ├── nyc_taxi_eda_pipeline.py
            ├── nyc_taxi_fare_prediction_ML.py
            ├── TimeSeriesDataAnalysis.py
           

## 3- 📈 Answer: 
Yes — our analysis confirms clear differences in fare patterns between weekdays and weekends. While the average fare remains similar, we observe notable variations in trip distance, rider behavior and volume. 
## Console O/P
|  **Day Type**           |          **Avg Fare ($)**          |             **Avg Tip ($)**        |        **Avg Distance (mi)**       |      **Total Rides**        |
| ----------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- | --------------------------- |
| Weekday                 |               20	               |                3.83                |               3.42                 |          "2,182,054"        |
| Weekend                 |               20.37	               |                3.72                |               3.74                 |          "796,350"          |

While weekend rides are slightly more expensive and cover longer distances, the average tips are marginally lower than weekdays — possibly due to higher fare base and more leisure/non-work-related trips.

## 
|  **Day**           |          **Avg Fare ($)**          |             **Avg Tip ($)**        |        **Avg Distance (mi)**       |
| ------------------ | ---------------------------------- | ---------------------------------- | ---------------------------------- | 
| Mondday            |               20.35                |                3.86                |               3.71                 |
| Tuesday            |               19.46	          |                3.81                |               3.32                 |
| Wednesday          |               20.24                |                3.82                |               3.21                 |
| Thursday           |               19.9	          |                3.88                |               3.35                 |
| Friday             |               20.05	          |                3.78                |               3.51                 |
| Saturday           |               19.13	          |                3.51                |               3.37                 |
| Friday             |               21.52	          |                3.92                |               4.09                 |

Sunday stands out with the highest fare, longest rides, and highest tipping — likely reflecting longer, leisure-focused trips, airport transfers, or post-weekend travel.

Refrences : ├── Figure_1 Average Fare Weekdays vs Weekends (DataVisualizationFareTrends)
            ├── Figure_7 Daily Average Trip Distance (TimeSeriesDataAnalysis)
            ├── Figure_1 B2 Fare Amount vs Trip Distance (DataVisualization) 
            ├── Figure_1 Average Fare Amount Over Time (AdvancedVisualizations)
            ├── Figure_1 A4 Average Fare by Day of Week (DataVisualization)
            ├── DataVisualizationFareTrends (Console O/P)
            ├── DataVisualizationFareTrends.py
            ├── DataVisualizations.py
            ├── AdvancedVisualization.py
            ├── TimeSeriesDataAnalysis.py
           

## 4- 📈 Answer: 
Airports (JFK & LaGuardia) are major pickup points but not as dominant for drop-offs → indicating tourists and business travelers arriving more than departing in taxis.
## 
|  **Zone**                        |          **total_rides**          |  
| -------------------------------- | --------------------------------- | 
| JFK Airport                      |               171194              |
| Upper East Side South            |               154916	           |
| Midetown Center                  |               147111              | 
| Upper East Side North            |               128834	           |  
| Penn Station/Madison Sq West     |              110812               | 
| Midtown East                     |               109940	           |
| LaGuardia Airport                |               109905	           |
| Times Sq/Theatre District        |               101763	           | 
| Lincoln Square East              |               91611	           |
| Murray Hill                      |               88751	           |

Midtown & Times Square areas dominate both lists due to high tourist activity, business hubs, and entertainment venues.
Upper East Side (both North & South) appears in top positions for both pickups and dropoffs → likely affluent residential demand.

## 
|  **Zone**                        |          **total_rides**          |  
| -------------------------------- | --------------------------------- | 
| Upper East Side South            |               137227              |
| Upper East Side North            |               136889	           |
| Midetown Center                  |               117612              | 
| Times Sq/Theatre Distric         |               96575	           |  
| Midtown East                     |               88228	           | 
| Murray Hill                      |               87752	           |
| Upper West Side South            |               82373	           |
| Lincoln Square East              |               81400	           | 
| Lenox Hill West                  |               78051	           |
| East Chelsea                     |               77715	           |

Refrences : ├── Figure_1 Top 10 Pickup Location in NYC (June 2025) (TopPickupDropoffLocationsAnalysis)
            ├── Figure_2 Figure_1 Top 10 Dropoff Locations in NYC (June 2025) (TopPickupDropoffLocationsAnalysis)
            ├── TopPickupDropoffLocationsAnalysis.py
            ├── yellow_tripdata_2025-06_cleaned.parquet
            ├── taxi+_zone_lookup.csv
            ├── Top_10_Dropoff_Locations.csv (got from output)  
            ├── Top_10_Pickup_Locations.csv (got from output)

## 5- 📈 Answer: 
Yes — the data strongly supports building features for trip duration, average speed and surge indicators.

├─ Trip Duration Patterns
Graph Reference: fare_vs_duration
Insight: Most trips are short, under 20 minutes, with a steep drop in frequency for longer rides.
A small percentage of very long trips suggests either intercity travel or anomalies (possible driver waiting times or recording errors).

├─ Speed Variations by Hour
Graph Reference: fare_vs_distance + Average Trip Distance by Hour
Insight: Speeds are highest during off-peak hours (late night & early morning).
Significant drops during rush hours (7–9 AM and 4–6 PM) due to traffic congestion.
Lowest speeds align with high-demand periods, which impacts ETAs and customer satisfaction.

├─ Surge-like Indicator (Demand Heatmap by Day & Hour)
Graph Reference: hourly_trip_metrics + Average Trip Distance by Hour
Insight: Evening peaks (5–8 PM weekdays, late nights on weekends) dominate demand.
Morning commute shows smaller peaks compared to evenings.
Lowest demand is consistently 3–5 AM daily.

Refrences : ├── Average Speed by Hour of Day (Q5visualization)
            ├── Trip Demand Heatmap by Day and Hour (Q5visualization)
            ├── Trip Duration Distribution (Minutes) (Q5visualization)
            ├── yellow_tripdata_2025-06_cleaned.parquet
            ├── NYC_Taxi_with_Features.csv
         
---

## ✅ Step 2: Understand the Business Context

- **Domain:** Urban Transportation & Public Mobility
- **Stakeholders:** Taxi companies, planners, analysts, passengers
- **Tools:** Python, Pandas, Seaborn, PyArrow, Gamma App, GitHub


# 1 - Answer's 🧠 Business Implication:
Taxi operators and mobility platforms can: Prioritize driver dispatch and dynamic pricing in these hours
                                           Strategically position vehicles near office zones to capture evening demand
                              Data Source: Trip count grouped by pickup hour from 4.3M rides in June 2025 (tpep_pickup_datetime → .dt.hour) (Data Transformation)
                              
# 2 - Answer's 🧠 Business Implication:
Digital payments (especially credit cards) dominate both in usage and tipping behavior. Riders who pay via credit card are over 13,000x more likely to leave a tip compared to cash. Digital tipping is clearly favored, likely due to in-app prompts and ease of entry. 
Encourage and prioritize digital payment systems to enhance driver earnings and customer experience. Tip-based incentive programs should be optimized around card-paying customers.

# 3 - Answer's 🧠 Business Implication:
Weekends → Longer trips, slightly higher fares, fewer total rides
Sundays → Opportunity for surge pricing, leisure promotions, or targeted services
Weekdays → Bulk of the volume; optimize driver distribution during peak office hours
Use time-based pricing, weekend promos and targeted driver placement to maximize revenue across different day types.

# 4 - Answer's 🧠 Business Implication:
Driver Allocation: Position drivers at JFK and LaGuardia during peak flight hours and in Midtown during rush hours.
Pricing Strategy: Implement zone-based surge pricing for high-demand areas like Times Square, Midtown Center and Upper East Side.
Tourism Services: Partnership opportunities with hotels, airports, and event organizers in these top areas.
Customer Experience: Offer pre-booking or fixed-fare services from airports to popular dropoff neighborhoods.

# 5 - Answer's 🧠 Business Implication:
Duration can be a predictive feature for pricing and supply planning.
Outlier filtering can improve model accuracy and operational reliability.
Average speed can serve as an indicator of congestion and expected delays.
Useful for dynamic ETAs and real-time fare adjustments.
Surge indicators can be derived from high-demand vs low-supply time blocks.
Helps optimize driver shift allocation and surge pricing to balance demand.
These features can improve fare prediction accuracy, optimize driver allocation and enhance customer experience by predicting congestion and wait times.

---

## ✅ Step 3: Data Collection

- **Source:** NYC Taxi & Limousine Commission (TLC)
- **File:** `yellow_tripdata_2025-06.parquet`
- **Why Parquet?** Fast, compressed, scalable format

```python
import pandas as pd
# df = pd.read_csv("yellow_tripdata_2025-06.csv") // if data in .csv file
df = pd.read_parquet('yellow_tripdata_2025-06.parquet', engine='pyarrow')
# we can use either 'pyarrow' or 'fastparquet' as the engine
# df = pd.read_parquet("yellow_tripdata_2025-06_cleaned.parquet") for cleaned data
print(df.columns)
'''
Index(['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime','passenger_count', 'trip_distance', 'RatecodeID', 'store_and_fwd_flag','PULocationID', 'DOLocationID', 'payment_type', 'fare_amount', 'extra',
       'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge','total_amount', 'congestion_surcharge', 'Airport_fee','cbd_congestion_fee'], dtype='object')

'''

# Save cleaned dataset
df.to_parquet('yellow_tripdata_2025-06_cleaned.parquet')      
```
Refrences : ├── nyc_taxi_data_analysis & all .py files (Use data collection)
            | 
---

## ✅ Step 4: Data Inspection & Loading

- Loaded dataset
- Viewed shape, columns, data types
```python

print(df.head())
'''
    VendorID tpep_pickup_datetime  ... Airport_fee  cbd_congestion_fee
0         1  2025-06-01 00:02:50  ...        1.75                0.75
1         2  2025-06-01 00:11:27  ...        0.00                0.75
2         1  2025-06-01 00:43:47  ...        0.00                0.75
3         1  2025-06-01 00:01:15  ...        0.00                0.75
4         7  2025-06-01 00:16:32  ...        0.00                0.75
'''
print(df.shape)
# (4322960, 20)
print(df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4322960 entries, 0 to 4322959
Data columns (total 20 columns):
 #   Column                 Dtype         
---  ------                 -----         
 0   VendorID               int32         
 1   tpep_pickup_datetime   datetime64[us]
 2   tpep_dropoff_datetime  datetime64[us]
 3   passenger_count        float64       
 4   trip_distance          float64       
 5   RatecodeID             float64       
 6   store_and_fwd_flag     object        
 7   PULocationID           int32         
 8   DOLocationID           int32         
 9   payment_type           int64         
 10  fare_amount            float64       
 11  extra                  float64       
 12  mta_tax                float64       
 13  tip_amount             float64       
 14  tolls_amount           float64       
 15  improvement_surcharge  float64       
 16  total_amount           float64       
 17  congestion_surcharge   float64       
 18  Airport_fee            float64       
 19  cbd_congestion_fee     float64       
dtypes: datetime64[us](2), float64(13), int32(3), int64(1), object(1)
memory usage: 610.2+ MB
None
Process finished with exit code 0
'''
print(df.describe())
'''
VendorID  ... cbd_congestion_fee
count  4.322960e+06  ...       4.322960e+06
mean   1.887364e+00  ...       5.332318e-01
min    1.000000e+00  ...      -7.500000e-01
25%    2.000000e+00  ...       0.000000e+00
50%    2.000000e+00  ...       7.500000e-01
75%    2.000000e+00  ...       7.500000e-01
max    7.000000e+00  ...       1.250000e+00
std    7.588800e-01  ...       3.585827e-01
[8 rows x 19 columns]
Process finished with exit code 0
'''

   
```
Refrences : ├── nyc_taxi_data_analysis.py
            | 
---
---

## ✅ Step 5: Data Cleaning

- Handled nulls
- Fixed datatypes
- Removed invalid records

```python
########## Referenced from nyc_taxi_data_analysis.py
# Nulls
print(df.isnull().sum())

# Drop Duplicates
df = df.drop_duplicates()

# Remove invalid rows
df = df[df['trip_distance'] > 0]
df = df[df['passenger_count'] > 0]
df = df[df['fare_amount'] >= 0]

# Fix passenger count (replace zeros with median)
median_passenger = df['passenger_count'].median()
df.loc[df['passenger_count'] == 0, 'passenger_count'

########## outlier_detection
# Remove invalid entries
df = df[(df['fare_amount'] > 0) & (df['trip_distance'] > 0) & (df['trip_duration_minutes'] > 0)]

########## nyc_taxi_fare_prediction & nyc_taxi_full_pipeline 
# Drop rows with missing values in features or target
df = df.dropna(subset=features + [target])

```
Refrences : ├── nyc_taxi_data_analysis.py
            ├── outlier_detection.py
            ├── nyc_taxi_fare_prediction.py
            ├── nyc_taxi_full_pipeline.py
         
---

## ✅ Step 6: Feature Understanding

20 original columns including:
- `trip_distance`, `tip_amount`, `payment_type`, `fare_amount`, `congestion_surcharge`
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_parquet("yellow_tripdata_2025-06_cleaned.parquet")

# Columns: tpep_pickup_datetime, tpep_dropoff_datetime, trip_distance, fare_amount

# Ensure datetime format
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

# Creating day of week column 
# df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['day_of_week'] = df['tpep_pickup_datetime'].dt.day_name()

# Create weekday/weekend column
df['day_type'] = df['day_of_week'].apply(lambda x: 'Weekend' if x in ['Saturday', 'Sunday'] else 'Weekday')

# Create output directory for charts
os.makedirs("outputs/eda_charts", exist_ok=True)

# Create Trip Duration (minutes)
df['trip_duration_min'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60

# Filter out unrealistic trips
df = df[(df['trip_duration_min'] > 0) & (df['trip_duration_min'] < 300)]  # less than 5 hours

# Create Average Speed (mph)
df['avg_speed_mph'] = df['trip_distance'] / (df['trip_duration_min'] / 60)
df = df[(df['avg_speed_mph'] > 0) & (df['avg_speed_mph'] < 80)]  # filter unrealistic speeds

# Create Surge-like Indicator
df['hour'] = df['tpep_pickup_datetime'].dt.hour
df['day_of_week'] = df['tpep_pickup_datetime'].dt.day_name()

# Mark surge hours (Morning 8-9 AM, Evening 3-7 PM)
df['surge_flag'] = df['hour'].apply(lambda x: 1 if (8 <= x <= 9) or (15 <= x <= 19) else 0)

# Load your cleaned dataset
df = pd.read_parquet('yellow_tripdata_2025-06_cleaned.parquet')

# Feature Engineering
df['pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

df['trip_duration'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds() / 60  # minutes
df['pickup_hour'] = df['pickup_datetime'].dt.hour
df['day_of_week'] = df['pickup_datetime'].dt.day_name()
df['trip_speed_mph'] = df['trip_distance'] / (df['trip_duration'] / 60)

df['is_weekend'] = df['day_of_week'].isin(['Saturday', 'Sunday'])
df['rush_hour_flag'] = df['pickup_hour'].isin([7, 8, 9, 16, 17, 18])

def time_of_day(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'
df['time_of_day'] = df['pickup_hour'].apply(time_of_day)


# Save engineered dataset
df.to_csv('NYC_Taxi_with_Features.csv', index=False)
print("Feature engineered dataset saved as 'NYC_Taxi_with_Features.csv'")
```
Refrences : ├── Q5visualization.py
            ├── DataVisualizationFareTrends.py
            ├── nyc_taxi_eda_pipeline.py
            ├── DataFeatureEngineering.py
            ├── NYC_Taxi_with_Features.csv
---

## ✅ Step 7: Data Transformation

Created:
- `trip_duration`, `hour`, `day_of_week`, `price_per_mile`

```python
df['trip_duration'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60
```

---

## ✅ Step 8: Exploratory Data Analysis (EDA)
Exploration Goals:
            Understand patterns in trip timing, distance, and fare
            Identify tipping trends
            Segment rides by hours, days, zones
Visuals Used:
            Histograms (trip distance, fare)
            Boxplots (tips vs day)
            Countplots (payment type, passenger count)

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set styles
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

# Load the cleaned dataset
data_path = "yellow_tripdata_2025-06_cleaned.parquet"
df = pd.read_parquet(data_path)

# Create output directory for charts
os.makedirs("outputs/eda_charts", exist_ok=True)

# 1. Basic Information
print("\nShape of Dataset:", df.shape)
print("\nInfo:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# 2. Feature Engineering
df['pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'], errors='coerce')
df['dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'], errors='coerce')
df['trip_duration'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds() / 60
df['pickup_hour'] = df['pickup_datetime'].dt.hour
df['pickup_day'] = df['pickup_datetime'].dt.day_name()

# 3. Univariate Analysis

# Passenger Count Distribution
sns.countplot(x='passenger_count', hue='passenger_count', data=df, palette='viridis', legend=False)
plt.title("Passenger Count Distribution")
plt.savefig("outputs/eda_charts/passenger_count_distribution.png")
plt.clf()

# Payment Type
sns.countplot(x='payment_type', hue='payment_type', data=df, palette='Set2', legend=False)
plt.title("Payment Type Distribution")
plt.savefig("outputs/eda_charts/payment_type_distribution.png")
plt.clf()

# Trip Distance Histogram
sns.histplot(df['trip_distance'], bins=50, kde=True, color='skyblue')
plt.title("Trip Distance Distribution")
plt.savefig("outputs/eda_charts/trip_distance_distribution.png")
plt.clf()

# Fare Amount Histogram
sns.histplot(df['fare_amount'], bins=50, kde=True, color='orange')
plt.title("Fare Amount Distribution")
plt.savefig("outputs/eda_charts/fare_amount_distribution.png")
plt.clf()

# Trip Duration Histogram
sns.histplot(df['trip_duration'], bins=50, kde=True, color='green')
plt.title("Trip Duration Distribution (min)")
plt.savefig("outputs/eda_charts/trip_duration_distribution.png")
plt.clf()

# 4. Bivariate Analysis

# Fare vs Distance
sns.scatterplot(x='trip_distance', y='fare_amount', data=df, alpha=0.3)
plt.title("Fare vs Trip Distance")
plt.savefig("outputs/eda_charts/fare_vs_distance.png")
plt.clf()

# Fare vs Duration
sns.scatterplot(x='trip_duration', y='fare_amount', data=df, alpha=0.3)
plt.title("Fare vs Trip Duration")
plt.savefig("outputs/eda_charts/fare_vs_duration.png")
plt.clf()

# 5. Temporal Analysis

# Hourly Trends
hourly_stats = df.groupby('pickup_hour')[['fare_amount', 'trip_distance', 'trip_duration']].mean().reset_index()
sns.lineplot(x='pickup_hour', y='fare_amount', data=hourly_stats, label='Avg Fare ($)')
sns.lineplot(x='pickup_hour', y='trip_distance', data=hourly_stats, label='Avg Distance (miles)')
sns.lineplot(x='pickup_hour', y='trip_duration', data=hourly_stats, label='Avg Duration (min)')
plt.title("Hourly Trip Metrics")
plt.legend()
plt.savefig("outputs/eda_charts/hourly_trip_metrics.png")
plt.clf()

# Weekday Trip Count
sns.countplot(x='pickup_day', data=df, order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'], hue='pickup_day', palette='coolwarm', legend=False)
plt.title("Trips by Day of the Week")
plt.xticks(rotation=45)
plt.savefig("outputs/eda_charts/weekday_trip_counts.png")
plt.clf()

print("EDA pipeline executed successfully. Charts saved to outputs/eda_charts/")
```
Refrences : ├── nyc_taxi_eda_pipeline.py
            ├── fare_amount_distribution.png
            ├── fare_vs_distance.png
            ├── fare_vs_duration.png
            ├── hourly_trip_metrics.png
            ├── passenger_count_distribution.png
            ├── payment_type_distribution.png
            ├── trip_distance_distribution.png
            ├── trip_duration_distribution.png
            ├── weekday_trip_counts.png
---

## ✅ Step 9: Advanced Insights

- Tip by payment method
- Weekend vs Weekday fare comparison
- Airport ride analysis

---

## ✅ Step 10: Geospatial Mapping (Optional)

Mapped pickup/dropoff zones using Taxi Zone GeoJSON

---

## ✅ Step 11: Machine Learning (Optional)

- Predicting tip_amount
- Logistic regression for tip/no tip classification

---

## ✅ Step 12: Data Visualization & Storytelling

- Gamma App for AI-powered presentation
- Matplotlib & Seaborn for charts

---

## ✅ Step 13: Publishing & GitHub Upload

**Repo Includes:**
- Scripts
- Notebooks
- Visuals
- Project README

---

## ✅ Step 14: Decision Making & Actions

- Evening rides are most common
- Credit card rides yield more tips
- Airport rides follow fixed fee model

---

## 📎 Final Notes

- 📁 [Dataset Source](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- 🔗 GitHub: [Insert Your Repo Link]
- 🛠 Built by: Sunil Prajapati | Python + Data + Gamma

---

## 📌 Tags

#DataAnalytics #NYCTaxi #Python #EDA #FeatureEngineering #AIApps #GammaApp #TransportationAnalytics #PortfolioProject #LinkedInProjects


outputs/feature_engineering/
├── trip_duration_distribution.png
├── trip_speed_distribution.png
├── trips_by_time_of_day.png
├── trips_by_day_of_week.png
└── rush_hour_trip_count.png
