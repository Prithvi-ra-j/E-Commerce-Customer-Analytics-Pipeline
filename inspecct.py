import pandas as pd
df = pd.read_csv("data.csv", encoding="latin-1")
print("Columns:", df.columns.tolist())
print("\nSample Data:\n", df.head())
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())