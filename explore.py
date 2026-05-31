import pandas as pd 
import numpy as np


df = pd.read_csv(r'E:\superstore\train.csv', encoding='latin-1')

print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\n" + "=" * 50)
print("COLUMN NAMES & DATA TYPES")
print("=" * 50)
print(df.dtypes)


print("\n" + "=" * 50)
print("FIRST 5 ROWS")
print("=" * 50)
print(df.head())

print("\n" + "=" * 50)
print("Null values")
print("=" * 50)
print(df.isnull().sum())

print("\n" + "=" * 50)
print("Data Description")
print("=" * 50)
print(df.describe())

print("\n" + "=" * 50)
print("UNIQUE VALUES PER COLUMN")
print("=" * 50)
for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")


print("\n" + "=" * 50)
print("Duplicates")
print("=" * 50)
print(df.duplicated().sum())


df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)


df['Order Date'] = pd.to_datetime(df['Order Date'])

df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df['Postal Code'] = df['Postal Code'].astype(str)

df.drop(columns=['Country', 'Row ID'],inplace=True)



print(df.dtypes)

print(df.isnull().sum())

print(df.shape)


print(df.head())


df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days

df['Sales Category'] = np.where(df['Sales'] > 500, 'High', np.where(df['Sales'] >= 100, 'Medium','Low'))

df['Order Year'] = df['Order Date'].dt.year

df['Order Month'] = df['Order Date'].dt.month


print(df.shape)

print(df.columns)

print(df[['Shipping Days','Sales Category','Order Year']])

print(df['Shipping Days'].min())



print(df[df['Postal Code'].isnull()][['Order ID', 'Customer Name', 'City', 'State', 'Postal Code']])


df.loc[df['City'] == 'Burlington' , 'Postal Code'] = '05401'

print(df['Postal Code'].isnull().sum())


df.to_csv(r'E:\superstore\superstore_cleaned.csv', index=False)
