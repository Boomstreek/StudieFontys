-- De sleutel van een trade is (trade_id, source_type): trade_id is per dag, niet per regel uniek.
SELECT trade_id, source_type, count(*) AS n
FROM {{ ref('stg_procurement_trades') }}
GROUP BY 1, 2
HAVING count(*) > 1
