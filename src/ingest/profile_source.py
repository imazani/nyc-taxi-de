import os
import pandas as pd
import pyarrow.parquet as pq

tripdata_parquet_path =  "data/raw/yellow_tripdata_2024-01.parquet"
zones_csv_path = "data/raw/taxi_zone_lookup.csv"


def require_file(path: str) -> None:
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Missing file: {path}\n"
            "Check to see if the dataset was download to the correct location data/raw/?"
        )

def profile_parquet(path: str, n: int = 3) -> None:
    require_file(path)
    
    pf = pq.ParquetFile(path)
    column_names = pf.schema.names
    
    print("++++ TRIPS PARQUET ++++")
    print(f"Path: {path}")
    print(f"Columns ({len(column_names)}): {column_names}")

    # Small 
    df = pd.read_parquet(path)
    print("Dtypes:")
    print(df.dtypes)
    print(f"Rows: {len(df)}")
    print(f"Head ({n}):")
    print(df.head(n))
    print("")

def profile_csv(path: str, n: int = 3) -> None:
    require_file(path)
    df = pd.read_csv(path)
    print("++++ ZONES CSV ++++")
    print(f"Path: {path}")
    print(f"Columns ({df.shape[1]}): {df.columns.tolist()}")
    print("Dtypes:")
    print(df.dtypes)
    print(f"Rows: {len(df)}")
    print(f"Head ({n}):")
    print(df.head(n))
    print("")

def main() -> None:
    profile_parquet(tripdata_parquet_path)
    profile_csv(zones_csv_path)

if __name__ == "__main__":
    main()
