{{ config(materialized='table') }}

-- depends_on: {{ source('fontasya_raw', 'energy_balance_daily') }}

SELECT *
FROM read_csv_auto('{{ var("raw_path") }}/energy_balance_daily.csv.gz')
