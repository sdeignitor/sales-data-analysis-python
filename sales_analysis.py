import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
df.info()

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Basic Statistics
print("\nStatistics:")
print(df.describe())

# Total Revenue
total_revenue = df["Total_Sales"].sum()
print("\nTotal Revenue:", total_revenue)

# Average Sale
print("Average Sale:", df["Total_Sales"].mean())

# Highest Sale
print("Highest Sale:", df["Total_Sales"].max())

# Lowest Sale
print("Lowest Sale:", df["Total_Sales"].min())

# Best Selling Product
best_product = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)

print("\nBest Selling Products:")
print(best_product)

# Region-wise Sales
region_sales = df.groupby("Region")["Total_Sales"].sum()

print("\nRegion-wise Sales:")
print(region_sales)

# Monthly Sales
df["Month"] = df["Date"].dt.month_name()

monthly_sales = df.groupby("Month")["Total_Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Save cleaned dataset
df.to_csv("cleaned_sales.csv", index=False)

# Save report
summary = pd.DataFrame({
    "Metric": [
        "Total Revenue",
        "Average Sale",
        "Highest Sale",
        "Lowest Sale"
    ],
    "Value": [
        total_revenue,
        df["Total_Sales"].mean(),
        df["Total_Sales"].max(),
        df["Total_Sales"].min()
    ]
})

summary.to_csv("sales_summary.csv", index=False)

print("\nAnalysis Completed Successfully.")

import matplotlib.pyplot as plt


# Region-wise Sales
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Region-wise Sales")
plt.show()

# Monthly Sales
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

