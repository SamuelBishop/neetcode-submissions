-- Write your query below
SELECT
    DISTINCT c.title
FROM tv_program as p
JOIN content as c
    ON p.content_id = c.content_id
WHERE c.kids_content = 'Y' and c.content_type = 'Movies' and p.program_date >= '2020-06-01 00:00' and p.program_date < '2020-07-01 00:00';