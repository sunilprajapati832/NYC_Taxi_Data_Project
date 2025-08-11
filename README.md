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
df = df.dropna()
df = df[df['passenger_count'] > 0]
```

---

## ✅ Step 6: Feature Understanding

20 original columns including:
- `trip_distance`, `tip_amount`, `payment_type`, `fare_amount`, `congestion_surcharge`

---

## ✅ Step 7: Data Transformation

Created:
- `trip_duration`, `hour`, `day_of_week`, `price_per_mile`

```python
df['trip_duration'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60
```

---

## ✅ Step 8: Exploratory Data Analysis (EDA)

- Distributions: Distance, Fare, Tip
- Time Patterns: Hour, Weekday
- Visuals: Histograms, Boxplots, Countplots

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
