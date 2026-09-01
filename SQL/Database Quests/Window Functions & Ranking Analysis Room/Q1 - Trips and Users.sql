-- https://leetcode.com/problems/trips-and-users/
-- MySQL

SELECT
t.request_at AS "Day",
ROUND(AVG(t.status != 'completed'), 2) AS "Cancellation Rate"
FROM Trips AS t
JOIN Users AS u1 ON t.client_id = u1.users_id AND u1.banned = "NO"
JOIN Users AS u2 ON t.driver_id = u2.users_id AND u2.banned = "NO"
WHERE request_at BETWEEN "2013-10-01" AND "2013-10-03"
GROUP BY request_at

-- This is the improved version of "SQL problem 262 - Trips and Users" (hard) as it was part of the quest question and, 
-- even though I already solved it, I though the change were interesting enough to include them, both for archive and display purposes