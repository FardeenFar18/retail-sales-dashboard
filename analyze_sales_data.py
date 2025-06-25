import pandas as pd

# Load cleaned data
df = pd.read_csv("cleaned_retail_sales.csv")

# Convert date if not already done
df["date"] = pd.to_datetime(df["date"], errors='coerce')

# Total KPIs
total_sales = df["sales"].sum()
total_profit = df["profit"].sum()
total_quantity = df["quantity"].sum()

print("📊 Total sales   : ₹{:,.2f}".format(total_sales))
print("📦 Total quantity: {}".format(total_quantity))
print("💰 Total profit  : ₹{:,.2f}".format(total_profit))

# Group by region
region_sales = df.groupby("region")["sales"].sum().sort_values(ascending=False)
print("\n📍 sales by region:")
print(region_sales)

# Group by category
category_profit = df.groupby("category")["profit"].sum().sort_values(ascending=False)
print("\n📂 profit by category:")
print(category_profit)

# monthly Trend
df["month"] = df["date"].dt.to_period("M")
monthly_sales = df.groupby("month")["sales"].sum()

print("\n📅 monthly sales:")
print(monthly_sales)
