{{ config(materialized='table') }}

-- depends_on: {{ source('fontasya_raw', 'network_system_daily') }}

SELECT *
FROM read_csv_auto(
    '{{ var("raw_path") }}/network_system_daily.csv.gz',
    types = {'ean_code': 'VARCHAR'}
)
