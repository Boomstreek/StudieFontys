{{ config(materialized='table') }}

-- depends_on: {{ source('fontasya_raw', 'generation_assets') }}

SELECT *
FROM read_csv_auto(
    '{{ var("raw_path") }}/generation_assets.csv.gz',
    types = {'ean_code': 'VARCHAR'}
)
