-- Write your query below

-- SELECT
--     c.NAME
-- FROM customers as c
-- INNER JOIN orders as o
--     On c.id = o.customer_id
-- GROUP BY customer_id
-- HAVING COUNT(o.id) = 0;

SELECT name
FROM customers
WHERE id NOT IN (SELECT customer_id FROM orders);