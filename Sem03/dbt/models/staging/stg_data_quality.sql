{{ config(materialized='table') }}

-- depends_on: {{ source('fontasya_raw', 'data_quality') }}

SELECT *
FROM read_csv_auto('{{ var("raw_path") }}/data_quality.csv.gz')
