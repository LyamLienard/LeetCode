-- https://leetcode.com/problems/department-top-three-salaries/description/
-- MySQL

SELECT
Department,
Employee,
Salary
FROM (
    SELECT
    d.name as Department,
    e.name as Employee,
    e.salary as Salary,
    DENSE_RANK() OVER(PARTITION BY d.name ORDER BY e.salary DESC) as ranked_salary
    FROM Employee as e
    INNER JOIN Department as d
    ON e.departmentId = d.id
) as sub
WHERE ranked_salary <= 3