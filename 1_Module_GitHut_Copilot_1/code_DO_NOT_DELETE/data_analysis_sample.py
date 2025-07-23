import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    'Product': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Region': ['East', 'West', 'North', 'South', 'East', 'West'],
    'Sales': [100, 150, 200, 130, 180, 120],
    'Profit': [20, 35, 50, 25, 40, 30]
}

df = pd.DataFrame(data)

# Basic Data Inspection
print("— Basic Data Inspection —")
print(df.head())
print("\nInformation about the DataFrame:")
print(df.info())

# Scatter plot of sales vs. profit
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Sales', y='Profit', hue='Product', data=df)
plt.title('Sales vs. Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.grid(True)
plt.show()

# Histogram of sales distribution
plt.figure(figsize=(8, 6))
sns.histplot(df['Sales'], bins=5, kde=True)
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

# ✅ Standard Deviation Visualization (as added by Copilot)
print("\n— Standard Deviation Visualization —")
sales_std = df.groupby('Region')['Sales'].std().reset_index()
plt.figure(figsize=(8, 6))
sns.barplot(x='Region', y='Sales', data=sales_std)
plt.title('Standard Deviation of Sales by Region')
plt.xlabel('Region')
plt.ylabel('Standard Deviation of Sales')
plt.show()