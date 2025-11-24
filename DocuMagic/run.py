# Install required packages first if you haven't
# pip install pandas sqlalchemy mysql-connector-python

import pandas as pd
from sqlalchemy import create_engine

# -------------------------
# 1. Connection details
# -------------------------
username = 'root'              # your MySQL username
password = 'root'     # your MySQL password
host = 'localhost'             # MySQL server host
port = 3306                    # default MySQL port
database = 'salesdb'           # your database name

# -------------------------
# 2. Create SQLAlchemy engine
# -------------------------
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}')

# -------------------------
# 3. Read the sales_data table into a pandas DataFrame
# -------------------------
df = pd.read_sql('sales_data', con=engine)
print("First 5 rows of sales_data:")
print(df.head())

# -------------------------
# 4. Basic Data Operations
# -------------------------
# Total revenue
total_revenue = df['revenue'].sum()
print(f"\nTotal Revenue: {total_revenue}")

# Total units sold per product
units_per_product = df.groupby('product')['sold_units'].sum()
print("\nUnits sold per product:")
print(units_per_product)

# Filter data: sales in Mumbai
mumbai_sales = df[df['city'] == 'Mumbai']
print("\nSales in Mumbai:")
print(mumbai_sales)

# -------------------------
# 5. Write a modified DataFrame back to MySQL (optional)
# -------------------------
# Example: Add a column with revenue per unit
df['revenue_per_unit'] = df['revenue'] / df['sold_units']

# Save back to a new table
df.to_sql('sales_data_with_calc', con=engine, if_exists='replace', index=False)
print("\nNew table 'sales_data_with_calc' created in MySQL!")
