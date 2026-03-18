import argparse
from pathlib import Path
import requests

def build_trip_url(year: str, month:str) -> str:
    return f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month}.parquet"

def build_trip_dest_path(year: str, month: str) -> Path:
    return Path(f"data/raw/yellow_tripdata_{year}-{month}.parquet")

def build_zone_url() -> str:
    return "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"

def build_zone_dest_path() -> Path:
    return Path("data/raw/taxi_zone_lookup.csv")

def ensure_data_dir(path: Path) -> None:

    # Create directory and missing parent directories
    path.parent.mkdir(parents=True, exist_ok=True)

def download_file(url: str, dest: Path) -> None:

    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(dest, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)


def validate_file(path: Path) -> bool:
    return path.exists() and path.is_file() and path.stat().st_size > 0

def valid_month(month: str) -> str:
    if month not in {f"{i:02d}" for i in range(1, 13)}:
        raise ValueError("Month must be between 01 and 12.")
    return month

def valid_year(year: str) -> str:
    if year not in {f"{i:04d}" for i in range(2009, 3000)}:
        raise ValueError("Must be a valid year. Data only available beginnining in 2009.")
    return year

def main() -> None:
    parser = argparse.ArgumentParser(
            description="use inputs to create url and download trip data and zone data if it doesn't exist"
            )
    parser.add_argument("year", type=valid_year, help="The year of the data needed, entered as a 4 digit number e.g. 2026")
    parser.add_argument("month", type=valid_month, help="The month of the data needed, entered as a 2 digit number e.g. january  = 01")

    args = parser.parse_args()

    trip_data_url = build_trip_url(args.year, args.month)
    trip_data_dest_path = build_trip_dest_path(args.year, args.month)
    zone_dest_path = build_zone_dest_path()
    zone_csv_url = build_zone_url()

    # Check if trip data folder exits, if not it will be created
    ensure_data_dir(trip_data_dest_path)
    ensure_data_dir(zone_dest_path)

    # Check if taxi_zone_lookup.csv has been downloaded, if not download it
    if validate_file(zone_dest_path):
        print(f"taxi_zone_lookup.csv already downloaded")
    else:
        print(f"Downloading taxi_zone_lookup.csv...")
        download_file(zone_csv_url, zone_dest_path)
        if not validate_file(zone_dest_path):
            raise ValueError("Zone CSV download failed validation")

    # Check if that month and year trip data has already been downloaded, if not download it
    if validate_file(trip_data_dest_path):
        print(f"Trip data for {args.year}-{args.month} was already downloaded.")
    else:
        print(f"Downloading trip data for {args.year}-{args.month}...")
        download_file(trip_data_url, trip_data_dest_path)
        if not validate_file(trip_data_dest_path):
            raise ValueError(f"Trip parquet download failed validation for {args.year}-{args.month}.")



if __name__ == "__main__":
    main()
