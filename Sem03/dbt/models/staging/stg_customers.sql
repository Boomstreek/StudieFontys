{{ config(materialized='table') }}

-- depends_on: {{ source('fontasya_raw', 'customers') }}

SELECT *
FROM read_csv_auto(
    '{{ var("raw_path") }}/customers.csv.gz',
    types = {'ean_code': 'VARCHAR'}
)
