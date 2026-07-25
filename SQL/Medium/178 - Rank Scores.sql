-- https://leetcode.com/problems/rank-scores/description/
-- MySQL

SELECT
score,
DENSE_RANK() OVER (ORDER BY score DESC) as "rank"
FROM Scores