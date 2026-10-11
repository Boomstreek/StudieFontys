{{ config(severity='warn') }}

-- Contracten met een einddatum in het verleden die toch op ACTIVE staan
SELECT contract_id, contract_type, end_date, status
FROM {{ ref('stg_contracts') }}
WHERE end_date < current_date AND status = 'ACTIVE'
