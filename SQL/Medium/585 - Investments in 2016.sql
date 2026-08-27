-- https://leetcode.com/problems/investments-in-2016/description/
-- MySQL

WITH flagged_tiv_2016 AS (
    SELECT
    tiv_2016,
    COUNT(*) OVER (PARTITION BY tiv_2015) AS count_of_same_tiv_2015,
    COUNT(*) OVER (PARTITION BY lat, lon) AS count_with_same_lat_lon
    FROM Insurance
)
SELECT
ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM flagged_tiv_2016
WHERE count_with_same_lat_lon = 1 AND count_of_same_tiv_2015 > 1