import pandas as pd

DATA_FILE = "data/system_data.csv"

df = pd.read_csv(DATA_FILE)
print(df.head())
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["date"] = df["timestamp"].dt.date
df["hour"] = df["timestamp"].dt.hour

print("\nColetas por dia:")
print(df["date"].value_counts())


