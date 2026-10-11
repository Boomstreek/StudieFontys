{{ config(materialized='table') }}

-- depends_on: {{ source('fontasya_raw', 'pv_assets') }}

SELECT *
FROM read_csv_auto(
    '{{ var("raw_path") }}/pv_assets.csv.gz',
    types = {'ean_code': 'VARCHAR'}
)
