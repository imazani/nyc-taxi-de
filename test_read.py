import pandas as pd

df = pd.read_parquet("data/raw/yellow_tripdata_2024-01.parquet")
print(df.shape)
print(df.columns.tolist())
