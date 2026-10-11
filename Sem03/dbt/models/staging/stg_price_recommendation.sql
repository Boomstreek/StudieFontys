{{ config(materialized='table') }}

-- depends_on: {{ source('fontasya_raw', 'price_recommendation') }}

SELECT *
FROM read_csv_auto('{{ var("raw_path") }}/price_recommendation.csv.gz')
