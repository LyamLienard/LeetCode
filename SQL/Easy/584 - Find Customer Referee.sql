-- https://leetcode.com/problems/find-customer-referee/description/
-- MySQL

-- select
-- c1.name
-- from Customer as c1
-- inner join Customer as c2
-- on c1.referee_id = c2.id
-- where c1.referee_id != 2
-- union
-- select
-- name
-- from Customer
-- where referee_id is null

-- I'm sorry but the 5th testcase is wrong, Duangkaew's referee (21) doesn't even exist in the table... He thus isn't refered by any customer technically. I don't see why imaginary customer should count. Even if a customer is deleted, there should be a placeholder rather than an empty link, otherwise it's too prone to error that can't be differentiated from actual dead link.

select name
from Customer
where referee_id != 2 or referee_id is null