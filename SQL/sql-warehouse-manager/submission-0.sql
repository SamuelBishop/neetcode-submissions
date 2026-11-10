-- Write your query below
SELECT
    wh.name AS warehouse_name,
    SUM(wh.units * p.width * p.length * p.height) AS volume
FROM warehouse as wh
INNER JOIN products as p
    ON wh.product_id = p.product_id
GROUP BY wh.name;