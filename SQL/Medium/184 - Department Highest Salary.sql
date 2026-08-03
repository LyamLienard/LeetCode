-- https://leetcode.com/problems/department-highest-salary/description/
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
    RANK() OVER(PARTITION BY d.name ORDER BY e.salary DESC) as ranked_salary
    FROM Employee as e
    INNER JOIN Department as d
    ON e.departmentId = d.id
) as sub
WHERE ranked_salary = 1