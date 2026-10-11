{{ config(materialized='table') }}

-- depends_on: {{ source('fontasya_raw', 'electricity_consumption_daily') }}

-- source_file bevat alleen de bestandsnaam (bijv. year=2026_month=03.csv.gz), geen lokaal pad
SELECT
    * EXCLUDE (filename),
    regexp_extract(filename, '[^/\\]+$') AS source_file
FROM read_csv_auto(
    '{{ var("raw_path") }}/electricity_consumption_daily/*.csv.gz',
    filename = true,
    types = {'ean_code': 'VARCHAR'}
)
