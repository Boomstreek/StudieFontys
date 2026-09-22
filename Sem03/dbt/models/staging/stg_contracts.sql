{{ config(materialized='table') }}

SELECT *
FROM read_csv_auto('/home/bram/Documents/Studie/Sem03/Data&Opdracht/Generate dataset Fontasya Electric/fontasya_representatieve_jaarset_200_klanten/contracts.csv.gz')
