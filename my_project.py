# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 03:28:25 2026

@author: badri
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('C:/Users/badri/Desktop/pr/sales_data_dirty.xlsx')
print(df.head())

print(df.isnull().sum())

print(df.duplicated().sum())

df=df.drop_duplicates()

df['Sales']=df['Sales'].fillna(df['Sales'].mean())

df['Category']=df['Category'].fillna('unknown')

print(df.head())

sales_category=df.groupby('Category')['Sales'].sum()
print(sales_category)

sales_category.plot(kind='bar',color='skyblue')
plt.title('total salary by category')
plt.xlabel('category')
plt.ylabel('sales')
plt.show()

df=df.sort_values('Date')
plt.plot(df['Date'],df['Sales'],marker='o')
plt.title('sales over time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.show()