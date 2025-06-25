import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("cleaned_retail_sales.csv")
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M").astype(str)

# Style
sns.set_theme(style="whitegrid")

# 1. 📊 sales by region
plt.figure(figsize=(6, 4))
region_sales = df.groupby("region")["sales"].sum().sort_values()
region_sales.plot(kind="barh", color="#A0E7E5")
plt.title("sales by region")
plt.xlabel("sales (₹)")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()

# 2. 📂 profit by category
plt.figure(figsize=(6, 4))
category_profit = df.groupby("category")["profit"].sum().sort_values()
category_profit.plot(kind="bar", color="#FFB6B9")
plt.title("profit by category")
plt.ylabel("profit (₹)")
plt.tight_layout()
plt.savefig("profit_by_category.png")
plt.show()

# 3. 📅 monthly sales Trend
monthly_sales = df.groupby("month")["sales"].sum()
plt.figure(figsize=(8, 4))
sns.lineplot(data=monthly_sales, marker="o", color="#7FB3D5")
plt.title("monthly sales Trend")
plt.ylabel("sales (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.show()
