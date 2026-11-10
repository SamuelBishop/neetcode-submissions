-- Write your query below
-- For each sale we need to find which distinct pair sold it

SELECT
    date_id,
    make_name,
    COUNT(DISTINCT lead_id) AS unique_leads,
    COUNT(DISTINCT partner_id) AS unique_partners
FROM daily_sales
GROUP BY date_id, make_name;