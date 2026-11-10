-- Write your query below
-- Want a left join for sure
-- Filter by name or salary is NULL
-- SELECT e.employee_id
-- FROM employees AS e
-- LEFT JOIN salaries as s
--     ON e.employee_id = s.employee_id
-- WHERE e.name IS NULL OR s.salary IS NULL
-- ORDER BY e.employee_id ASC;

SELECT employee_id
FROM employees
WHERE employee_id NOT IN (
    SELECT employee_id
    FROM salaries
)
UNION
SELECT employee_id
FROM salaries
WHERE employee_id NOT IN (
    SELECT employee_id
    FROM employees
)
ORDER BY employee_id ASC;