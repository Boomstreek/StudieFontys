{{ config(materialized='table') }}

SELECT *
FROM read_csv_auto(
    '/home/bram/Documents/Studie/Sem03/Data&Opdracht/Generate dataset Fontasya Electric/fontasya_representatieve_jaarset_200_klanten/pv_feedin_daily/*.csv.gz',
    filename = true
)
