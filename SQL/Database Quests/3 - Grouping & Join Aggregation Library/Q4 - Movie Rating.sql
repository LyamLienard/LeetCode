-- https://leetcode.com/problems/movie-rating/description/
-- MySQL

(SELECT
u.name AS results
FROM MovieRating AS m
JOIN Users AS u ON m.user_id = u.user_id
GROUP BY m.user_id
ORDER BY COUNT(m.movie_id) DESC, name ASC
LIMIT 1)

UNION ALL

(SELECT
m.title AS results
FROM MovieRating AS mr
JOIN Movies AS m ON mr.movie_id = m.movie_id
WHERE mr.created_at BETWEEN "2020-02-01" AND "2020-02-29"
GROUP BY mr.movie_id
ORDER BY AVG(rating) DESC, title ASC
LIMIT 1)