-- A  script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
-- Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)
SELECT city, temperature
FROM Temperatures
WHERE (month = 'July' OR month = 'August')
ORDER BY temperature DESC
LIMIT 3;
