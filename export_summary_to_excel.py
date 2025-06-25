import pandas as pd

# Load cleaned data
df = pd.read_csv("cleaned_retail_sales.csv")
df["date"] = pd.to_datetime(df["date"], errors='coerce')
df["month"] = df["date"].dt.to_period("M").astype(str)

# Summary calculations
total_sales = df["sales"].sum()
total_profit = df["profit"].sum()
total_quantity = df["quantity"].sum()

# Create summary DataFrame
summary_df = pd.DataFrame({
    "Metric": ["Total sales", "Total profit", "Total quantity"],
    "Value": [total_sales, total_profit, total_quantity]
})

# Group summaries
region_sales = df.groupby("region")["sales"].sum().reset_index()
category_profit = df.groupby("category")["profit"].sum().reset_index()
monthly_sales = df.groupby("month")["sales"].sum().reset_index()

# Export all to Excel
with pd.ExcelWriter("sales_summary.xlsx", engine="openpyxl") as writer:
    summary_df.to_excel(writer, sheet_name="KPIs", index=False)
    region_sales.to_excel(writer, sheet_name="region by sales", index=False)
    category_profit.to_excel(writer, sheet_name="profit by category", index=False)
    monthly_sales.to_excel(writer, sheet_name="monthly sales", index=False)

print("✅ Exported all summaries to 'sales_summary.xlsx'")
