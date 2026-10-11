{{ config(materialized='table') }}

-- depends_on: {{ source('fontasya_raw', 'contracts') }}

-- Datumtypes expliciet vastgelegd: end_date is leeg bij FLEX-contracten en zou bij een set zonder
-- ingevulde einddatum anders als tekst worden ingelezen.
SELECT *
FROM read_csv_auto(
    '{{ var("raw_path") }}/contracts.csv.gz',
    types = {'ean_code': 'VARCHAR', 'start_date': 'DATE', 'end_date': 'DATE'}
)
