{{ config(materialized='table') }}

-- depends_on: {{ source('fontasya_raw', 'weather_forecast_daily') }}

SELECT *
FROM read_csv_auto(
    '{{ var("raw_path") }}/weather_forecast_daily.csv.gz',
    types = {'ean_code': 'VARCHAR'}
)
