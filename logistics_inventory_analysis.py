"""
Week 1 Logistics Data Analysis
Project: Inventory Management Optimization for a Retail Company

Purpose:
This script demonstrates a proposed Python-based approach for exploring
sales and inventory data, calculating logistics KPIs, identifying
fast/slow-moving products, and supporting inventory decisions.

Expected input columns in a real dataset:
Product, Sales, Inventory, Orders, Stockouts, Lead_Time_Days
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Load data
# ---------------------------------------------------------
# Replace this path with the company's actual CSV file.
# df = pd.read_csv("sales_inventory_data.csv")

# Demo dataset for illustrating the proposed approach.
data = {
    "Product": ["Product A", "Product B", "Product C", "Product D", "Product E"],
    "Sales": [1200, 450, 900, 150, 700],
    "Inventory": [300, 500, 250, 600, 350],
    "Orders": [100, 55, 80, 30, 70],
    "Stockouts": [5, 12, 3, 2, 7],
    "Lead_Time_Days": [5, 8, 6, 10, 7],
}

df = pd.DataFrame(data)

# ---------------------------------------------------------
# 2. Basic data validation
# ---------------------------------------------------------
print("Dataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())

# ---------------------------------------------------------
# 3. KPI calculations
# ---------------------------------------------------------
df["Stockout_Rate_%"] = (df["Stockouts"] / df["Orders"]) * 100
df["Inventory_Turnover"] = df["Sales"] / df["Inventory"]
df["Average_Inventory"] = df["Inventory"]

print("\nCalculated KPIs:")
print(df[[
    "Product",
    "Stockout_Rate_%",
    "Inventory_Turnover",
    "Lead_Time_Days"
]])

# ---------------------------------------------------------
# 4. Identify fast and slow-moving products
# ---------------------------------------------------------
fast_moving = df.sort_values("Inventory_Turnover", ascending=False)
slow_moving = df.sort_values("Inventory_Turnover", ascending=True)

print("\nFast-moving products:")
print(fast_moving[["Product", "Inventory_Turnover"]].head(3))

print("\nSlow-moving products:")
print(slow_moving[["Product", "Inventory_Turnover"]].head(3))

# ---------------------------------------------------------
# 5. Identify products with higher stockout risk
# ---------------------------------------------------------
high_stockout_risk = df[df["Stockout_Rate_%"] > 10]

print("\nProducts with stockout rate above 10%:")
print(high_stockout_risk[["Product", "Stockout_Rate_%"]])

# ---------------------------------------------------------
# 6. Simple inventory planning flag
# ---------------------------------------------------------
df["Planning_Action"] = np.where(
    df["Stockout_Rate_%"] > 10,
    "Review replenishment / increase safety stock",
    np.where(
        df["Inventory_Turnover"] < 1,
        "Review excess or slow-moving inventory",
        "Monitor"
    )
)

print("\nRecommended planning actions:")
print(df[["Product", "Planning_Action"]])

# ---------------------------------------------------------
# 7. Visualization
# ---------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.bar(df["Product"], df["Inventory_Turnover"])
plt.title("Inventory Turnover by Product")
plt.xlabel("Product")
plt.ylabel("Inventory Turnover")
plt.tight_layout()
plt.savefig("inventory_turnover.png", dpi=150)
plt.show()

# ---------------------------------------------------------
# 8. Strategic roadmap
# ---------------------------------------------------------
roadmap = [
    "1. Collect historical sales, inventory, order and lead-time data.",
    "2. Clean missing values, duplicates and inconsistent records.",
    "3. Calculate logistics KPIs and identify performance gaps.",
    "4. Analyze demand patterns and fast/slow-moving products.",
    "5. Identify stockout and excess-inventory risks.",
    "6. Develop replenishment and safety-stock recommendations.",
    "7. Track KPIs regularly and improve the model using new data.",
]

print("\nStrategic Analysis Roadmap:")
for step in roadmap:
    print(step)

print("\nAnalysis completed successfully.")
