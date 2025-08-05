# 🗽 NYC Yellow Taxi Data Analysis (June 2025)
This project explores NYC Yellow Taxi trip data to uncover patterns in passenger behavior, trip fares, tips, and congestion trends using Python and pandas.

## 🔍 Dataset
- Source: NYC TLC Taxi Trips  
- File Used: `yellow_tripdata_2025-06.parquet`  
- Size: 4.3 million rows × 20 columns

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

outputs/feature_engineering/
├── trip_duration_distribution.png
├── trip_speed_distribution.png
├── trips_by_time_of_day.png
├── trips_by_day_of_week.png
└── rush_hour_trip_count.png

