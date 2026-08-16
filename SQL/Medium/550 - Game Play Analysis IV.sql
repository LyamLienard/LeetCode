-- https://leetcode.com/problems/game-play-analysis-iv/description/
-- MySQL

WITH f AS (
    SELECT
    player_id,
    MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
)
SELECT
ROUND(COUNT(DISTINCT a.player_id) / (SELECT COUNT(*) FROM f), 2) AS fraction
FROM Activity AS a 
JOIN f
ON a.player_id = f.player_id 
AND a.event_date = DATE_ADD(f.first_login, INTERVAL 1 DAY)