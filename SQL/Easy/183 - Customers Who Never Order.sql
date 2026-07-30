-- https://leetcode.com/problems/customers-who-never-order/description/
-- MySQL

SELECT
c.name as Customers
FROM Customers as c
LEFT JOIN Orders as o
ON c.id = o.customerId
WHERE o.id is NULL