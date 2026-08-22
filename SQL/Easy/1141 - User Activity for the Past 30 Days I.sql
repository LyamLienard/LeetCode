-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description/
-- MySQL

SELECT
activity_date AS day,
COUNT(DISTINCT user_id) AS active_users
FROM Activity
GROUP BY day
HAVING day BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND "2019-07-27"