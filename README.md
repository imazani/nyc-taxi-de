## 

**Definition of Done (DoD):**
- [ ] Postgres warehouse runs locally via Docker
- [ ] 1 month of Yellow Taxi trips loaded into raw.yellow_tripdata
- [ ] Taxi zone lookup loaded into raw.taxi_zone_lookup
- [ ] dbt builds staging + marts successfully
- [ ] Data tests pass (schema + value rules)
- [ ] One documented metric query runs successfully

**Data Contract:**
- Source: NYC TLC Yellow Taxi trip records + Taxi Zone lookup
- Raw: raw.yellow_tripdata, raw.taxi_zone_lookup
- Staging: cleaned/typed trips + zones
- Marts: fact_trips + dim_location + dim_date + dim_payment_type + dim_rate_code
- Quality rules (examples):
    -> pickup_datetime and dropoff_datetime not null
    -> dropoff_datetime > pickup_datetime
    -> trip_id unique

