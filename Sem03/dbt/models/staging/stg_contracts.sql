{{ config(materialized='table') }}

-- depends_on: {{ source('fontasya_raw', 'contracts') }}

SELECT *
FROM read_csv_auto(
    '{{ var("raw_path") }}/contracts.csv.gz',
    types = {'ean_code': 'VARCHAR'}
)
