CREATE TABLE IF NOT EXISTS raw.yellow_tripdata (
	vendor_id INTEGER,
	tpep_pickup_datetime TIMESTAMP,
	tpep_dropoff_datetime TIMESTAMP,
	passenger_count DOUBLE PRECISION,
	trip_distance DOUBLE PRECISION,
	ratecode_id DOUBLE PRECISION,
	store_and_fwd_flag TEXT,
	pu_location_id INTEGER,
	do_location_id INTEGER,
	payment_type INTEGER,
	fare_amount DOUBLE PRECISION,
	extra DOUBLE PRECISION,
	mta_tax DOUBLE PRECISION,
	tip_amount DOUBLE PRECISION,
	tolls_amount DOUBLE PRECISION,
	improvement_surcharge DOUBLE PRECISION,
	total_amount DOUBLE PRECISION,
	congestion_surcharge DOUBLE PRECISION,
	airport_fee DOUBLE PRECISION,
	source_file TEXT,
	ingested_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS raw.taxi_zone_lookup (
	location_id INTEGER,
	borough TEXT,
	zone TEXT,
	service_zone TEXT,
	source_file TEXT,
	ingested_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
