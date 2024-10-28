import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from a CSV file
# Replace 'path_to_your_file.csv' with the actual file path
df = pd.read_csv('dataset.csv')

# Output 1: Calculate total sales by category
total_sales_by_category = df.groupby('Category').agg({'Sales': 'sum'}).reset_index()
print("Total Sales by Category:")
print(total_sales_by_category)

# Output 2: Calculate average profit by category
average_profit_by_category = df.groupby('Category').agg({'Profit': 'mean'}).reset_index()
print("\nAverage Profit by Category:")
print(average_profit_by_category)

# Visualize total sales by category
plt.figure(figsize=(10, 6))
sns.barplot(x='Sales', y='Category', data=total_sales_by_category, palette='viridis')
plt.title('Total Sales by Category')
plt.xlabel('Total Sales ($)')
plt.ylabel('Category')
plt.show()

# Output 3: Scatter plot for discount vs profit
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Discount', y='Profit', data=df, hue='Category', style='Segment', s=100)
plt.title('Discount vs Profit')
plt.xlabel('Discount (%)')
plt.ylabel('Profit ($)')
plt.show()
