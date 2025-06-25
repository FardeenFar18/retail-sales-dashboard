import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("cleaned_retail_sales.csv")
df["date"] = pd.to_datetime(df["date"])  # Add this line to fix the error
df["year"] = df["date"].dt.to_period("M").astype(str)
monthly = df.groupby("year")["sales"].sum().reset_index()
monthly["month"] = range(1, len(monthly)+1)

print(monthly)


X = monthly[["month"]]
y = monthly["sales"]

print(X,y)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Build model
model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)


# Plot results
plt.figure(figsize=(8,4))
plt.scatter(X, y, label="Actual sales", color="blue")
plt.plot(X, y_pred, label="Predicted sales", color="red")
plt.title("Sales Prediction using Linear Regression")
plt.xlabel("Month Number")
plt.ylabel("Sales (₹)")
plt.legend()
plt.tight_layout()
plt.savefig("sales_prediction.png")
plt.show()


next_month = [[monthly["month"].max() + 1]]
next_sales = model.predict(next_month)
print(f"🔮 Predicted sales for Next Month: ₹{next_sales[0]:,.2f}")
