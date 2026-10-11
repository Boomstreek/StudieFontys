{{ config(materialized='table') }}

-- depends_on: {{ source('fontasya_raw', 'generation_production_daily') }}

SELECT *
FROM read_csv_auto('{{ var("raw_path") }}/generation_production_daily.csv.gz')
