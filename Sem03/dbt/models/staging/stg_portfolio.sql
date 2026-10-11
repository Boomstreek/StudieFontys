{{ config(materialized='table') }}

-- depends_on: {{ source('fontasya_raw', 'portfolio') }}

SELECT *
FROM read_csv_auto(
    '{{ var("raw_path") }}/portfolio.csv.gz',
    types = {'ean_code': 'VARCHAR'}
)
