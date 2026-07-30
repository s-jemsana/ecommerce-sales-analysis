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

# 3. Advanced Aggregation & Insights
# KPI 1: Total Revenue
total_revenue = df["revenue"].sum()
print(f"Total Revenue: ${total_revenue:,.2f}")

# KPI 2: Sales by Region
print("\n Revenue by Region")
region_sales = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
print(region_sales.apply(lambda x: f"${x:,.2f}"))

# KPI 3: Logistics & Satisfaction
avg_metrics = df[["delivery_days", "customer_rating"]].mean().round(2)
print("\n Operationsl Averages:")
print(f"Average Delivery Time: {avg_metrics["delivery_days"]} days")
print(f"Average Customer Rating: {avg_metrics["customer_rating"]} / 5.0")