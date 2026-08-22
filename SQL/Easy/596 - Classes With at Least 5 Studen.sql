-- https://leetcode.com/problems/classes-with-at-least-5-students/description/
-- MySQL

SELECT
class
FROM Courses
GROUP BY class
HAVING COUNT(*) > 4