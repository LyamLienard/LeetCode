-- https://leetcode.com/problems/delete-duplicate-emails/description/
-- MySQL

WITH occurance_ranking AS (
    SELECT
    id,
    ROW_NUMBER() OVER (PARTITION BY email ORDER BY id ASC) AS occurance_number
    FROM Person
)
DELETE p 
FROM Person AS p
JOIN occurance_ranking AS o
ON p.id = o.id
WHERE o.occurance_number > 1