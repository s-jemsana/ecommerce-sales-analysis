import pandas as pd
import matplotlib as plt

# 1. Load Data
file_name = "ecommerce_sales_analytics_5000.csv"
df = pd.read_csv(file_name)

# 2. Clean Data
# Drop duplicates
df = df.drop_duplicates()

# Convert 'order-date' to DateTime object
df["order_date"] = pd.to_datetime(df["order_date"])

# Extract Month and Year
df["month_year"] = df["order_date"].dt.to_period("M")

print("--- DATASET SUMMARY ---")
print(df.info())
print("\n")