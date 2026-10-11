{{ config(materialized='table') }}

-- depends_on: {{ source('fontasya_raw', 'procurement_trades_daily') }}

SELECT *
FROM read_csv_auto('{{ var("raw_path") }}/procurement_trades_daily.csv.gz')
