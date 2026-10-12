import pandas as pd
import matplotlib.pyplot as plt

#=======================================================================
# 1. LOAD DATA
#=======================================================================

file_name = "ecommerce_sales_analytics_5000.csv"
df = pd.read_csv(file_name)

#=======================================================================
# # 2. DATA VALIDATION
#=======================================================================

print("=" * 60)
print("DATASET VALIDATION")
print("=" * 60)

print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]:,}")

print("\nColumns:")
print(df.columns.tolist())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check for duplicate rows
print(f"\nDuplicate rows: {df.duplicated().sum():,}")

# Check that order IDs are unique
print(f"Unique order IDs: {df['order_id'].nunique():,}")


#=======================================================================
# 3. DATA CLEANING
#=======================================================================

# Drop duplicate rows
df = df.drop_duplicates()

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(
    df["order_date"],
    format="%m/%d/%Y",
    errors="coerce"
    )

# Check for invalid dates
invalid_dates = df["order_date"].isna().sum()

print(f"\nInvalid dates: {invalid_dates:,}")

#=======================================================================
# 4. VALIDATE NUMERIC DATA
#=======================================================================

print("\nNumeric validation:")

print(
    f"Invalid quantities: "
    f"{(~df['quantity'].gt(0)).sum():,}"
)

print(
    f"Invalid unit prices: "
    f"{(~df['unit_price'].gt(0)).sum():,}"
)

print(
    f"Invalid discounts: "
    f"{(~df['discount'].between(0, 0.35)).sum():,}"
)

print(
    f"Invalid delivery days: "
    f"{(~df['delivery_days'].between(1, 11)).sum():,}"
)

print(
    f"Invalid customer ratings: "
    f"{(~df['customer_rating'].between(1, 5)).sum():,}"
)

print(
    f"Invalid revenue values: "
    f"{(~df['revenue'].gt(0)).sum():,}"
)

# Revenue should equal quantity * unit_price * (1 - discount)
expected_revenue = (
    df["quantity"] * df["unit_price"] * (1 - df["discount"])
).round(2)

revenue_mismatches = ((df["revenue"] - expected_revenue).abs() > 0.01).sum()

print(f"Revenue mismatches: {revenue_mismatches:,}")


#=======================================================================
# 5. CREATE DATE FEATURES
#=======================================================================

df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["month_year"] = df["order_date"].dt.to_period("M")

#=======================================================================
# 6. CORE KPI ANALYSIS
#=======================================================================

# Calculate the key performance indicators
# Currency is unspecified in the source dataset

total_revenue = df["revenue"].sum()
total_orders = df["order_id"].nunique()
unique_customers = df["customer_id"].nunique()
total_quantity_sold = df["quantity"].sum()

average_order_value = total_revenue / total_orders
average_order_per_customer = total_orders / unique_customers
average_discount = df["discount"].mean() * 100
average_customer_rating = df["customer_rating"].mean()
average_delivery_time = df["delivery_days"].mean()

# Display the KPIs
print("\n" + "=" * 60)
print("CORE E-COMMERCE KPIs")
print("=" * 60)

print(f"Total Revenue:                  {total_revenue:,.2f}")
print(f"Total Orders:                   {total_orders:,}")
print(f"Unique Customers:               {unique_customers:,}")
print(f"Total Quantity Sold:            {total_quantity_sold:,}")
print(f"Average Order Value:            {average_order_value:,.2f}")
print(f"Average Orders per Customer:    {average_order_per_customer:.2f}")
print(f"Average Discount:               {average_discount:.2f}%")
print(f"Average Customer Rating:        {average_customer_rating:.2f} / 5")
print(f"Average Delivery Time:          {average_delivery_time:.2f} days")

#=======================================================================
# 6. DATASET SUMMARY
#=======================================================================

print("\n" + "=" * 60)
print("DATASET SUMMARY")
print("=" * 60)

print(
    f"Date range: {df['order_date'].min().date()} "
    f"to {df['order_date'].max().date()}"
      )

today = pd.Timestamp.today().normalize()
future_orders = (df["order_date"] > today).sum()

print(f"Orders dated after today: {future_orders:,}")

print(f"Total orders: {len(df):,}")

print(f"Unique customers: {df['customer_id'].nunique():,}")

print(f"Product categories: "
      f"{df['product_category'].nunique()}")

print(f"Regions: {df['region'].nunique()}")

print(f"Payment methods: "
      f"{df['payment_method'].nunique()}")

#=======================================================================
# 7. DATA PREVIEW
#=======================================================================

print("\nFirst 5 rows:")
print(df.head())
