import pandas as pd

# 1. Load the original CSV
df = pd.read_csv("retail_sales.csv")

# 2. Clean currency symbols
df["sales"] = df["sales"].replace('[\₹$,]', '', regex=True).astype(float)
df["profit"] = df["profit"].replace('[\₹$,]', '', regex=True).astype(float)

# 3. Convert 'date' to datetime
df["date"] = pd.to_datetime(df["date"], errors='coerce')

# 4. Reorder columns – put 'date' first

# 5. Save cleaned CSV
df.to_csv("cleaned_retail_sales.csv", index=False)

print("✅ Cleaned CSV saved with 'date' as first column.")
