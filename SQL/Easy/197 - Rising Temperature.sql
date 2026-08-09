-- https://leetcode.com/problems/rising-temperature/description/
-- MySQL

SELECT
w2.id
FROM Weather AS w1
JOIN Weather AS w2
ON DATE_ADD(w1.recordDate, INTERVAL 1 DAY) = w2.recordDate
WHERE w2.temperature > w1.temperature