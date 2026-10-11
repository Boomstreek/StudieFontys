{{ config(severity='warn') }}

-- Verbruik na de einddatum van het contract (komt voor in de synthetische set: 1-jaarscontracten)
SELECT e.customer_id, count(*) AS rows_after_end
FROM {{ ref('stg_electricity_consumption') }} e
JOIN {{ ref('stg_contracts') }} c USING (customer_id)
WHERE c.end_date IS NOT NULL AND e.date > c.end_date
GROUP BY 1
