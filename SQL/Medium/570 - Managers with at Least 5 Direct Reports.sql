-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/
-- MySQL

SELECT
name
FROM Employee
WHERE id in (
    SELECT
    managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) > 4
)