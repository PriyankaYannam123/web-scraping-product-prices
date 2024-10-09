import pandas as pd
import numpy as np

# Load data
data = pd.read_csv('sales_data.csv')

# Display first few rows of the dataset
print(data.head())

# Clean the data (remove duplicates, handle missing values)
data = data.dropna()  # Remove rows with missing values
data = data.drop_duplicates()  # Remove duplicates

# Data Analysis - Calculate total sales per product
total_sales = data.groupby('Product')['Sales'].sum()
print("Total Sales per Product:")
print(total_sales)

# Visualize the sales data (optional)
import matplotlib.pyplot as plt

total_sales.plot(kind='bar')
plt.title('Total Sales per Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.show()
