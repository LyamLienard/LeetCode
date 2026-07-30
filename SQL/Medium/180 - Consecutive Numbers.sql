-- https://leetcode.com/problems/consecutive-numbers/
-- MySQL

SELECT DISTINCT
num as ConsecutiveNums
FROM (
    SELECT
    num,
    MAX(num) OVER is_consecutive as maximum,
    MIN(num) OVER is_consecutive as minimum,
    COUNT(num) OVER is_consecutive as counter
    FROM Logs
    WINDOW is_consecutive as (ORDER BY id ASC ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING)
) as sub
WHERE maximum = minimum and counter = 3

-- This was the best solution I found before learning about the LEAD() function and that writing "l1 JOIN l2 ON l1.num + 1 = l2.num" was even possible/allowed...
-- I'm still uploading this solution because it's the one I found, not someone else's