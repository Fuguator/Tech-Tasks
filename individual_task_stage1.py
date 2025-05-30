import pandas as pd
import hashlib

df = pd.read_csv('/home/fugu/.cache/kagglehub/datasets/nehalbirla/vehicle-dataset-from-cardekho/versions/4/Car details v3.csv')
print(df.head())
print(df.tail())

print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print(df.isnull().sum())

df['name'] = df['name'].fillna('Unknown')
df['selling_price'] = df['selling_price'].fillna(0)

df['selling_price'] = df['selling_price'].astype(str).str.replace('₹', '', regex=False)
df['selling_price'] = df['selling_price'].str.replace(',', '', regex=False)
df['selling_price'] = df['selling_price'].str.strip()
df['selling_price'] = pd.to_numeric(df['selling_price'], errors='coerce')

df['Marka'] = df['name'].str.split().str[0]
df['Model'] = df['name'].str.split().str[1]
df['Buraxilis_ili'] = df['year']

df['ID'] = df['name'].astype(str) + df['year'].astype(str) + df['fuel'].astype(str) + df['transmission'].astype(str)
df['ID'] = df['ID'].apply(lambda x: hashlib.md5(x.encode()).hexdigest())

print(df[['ID', 'Marka', 'Model', 'Buraxilis_ili', 'selling_price']].head())

df.to_csv('cleaned_car_data.csv', index=False)
print("Saved to cleaned_car_data.csv")
