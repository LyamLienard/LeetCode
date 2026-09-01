-- https://leetcode.com/problems/trips-and-users/description/
-- MySQL

WITH valid_trips AS (
    SELECT
    t.client_id,
    t.driver_id,
    t.city_id,
    t.status,
    t.request_at
    FROM Trips AS t
    JOIN Users AS u1 ON t.client_id = u1.users_id
    JOIN Users AS u2 ON t.driver_id = u2.users_id
    WHERE u1.banned = "NO" AND u2.banned = "NO" AND request_at BETWEEN "2013-10-01" AND "2013-10-03"
),
valid_trips_per_day AS (
    SELECT
    request_at,
    COUNT(*) AS total_trips_per_day
    FROM valid_trips AS v
    GROUP BY request_at
),
cancelled_trips_per_day AS (
    SELECT
    request_at,
    COUNT(*) AS total_cancelled_trips_per_day
    FROM valid_trips
    WHERE status LIKE "cancelled%"
    GROUP BY request_at
)
SELECT
v.request_at AS "Day",
ROUND(IFNULL(total_cancelled_trips_per_day, 0) / total_trips_per_day, 2) AS "Cancellation Rate"
FROM cancelled_trips_per_day AS c
RIGHT JOIN valid_trips_per_day AS v
ON c.request_at = v.request_at

--Not my proudest work when I looked at other answers and learned that we could put things other than * or column names inside aggregation function, which compact so much work and is so much faster!
--example from best answer : ROUND(SUM(CASE WHEN status='cancelled_by_driver' OR status='cancelled_by_client' THEN 1 ELSE 0 END) / COUNT(request_at),2)
--Which, after a bit of seaching why this is even allowed, can be reduced further to ROUND(SUM(status!='cancelled_by_driver' OR status='cancelled_by_client') / COUNT(request_at),2)
--as boolean are enough since MySQL and SQLite don't use a strict type checking as every other relational database engine does.
--On a side note, in this case ROUND(SUM(status != 'completed') / COUNT(request_at), 2) would be even better

-- cf Database Quest P4 Q1