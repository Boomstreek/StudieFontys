{{ config(materialized='table') }}

-- depends_on: {{ source('fontasya_raw', 'market_price_daily') }}

SELECT *
FROM read_csv_auto('{{ var("raw_path") }}/market_price_daily.csv.gz')
