-- Write your query below

SELECT
    sp.name
FROM sales_person as sp
WHERE sp.sales_id NOT IN (
    SELECT o.sales_id
    FROM orders as o
    JOIN company c on o.com_id = c.com_id
    WHERE c.name = 'CRIMSON'
);