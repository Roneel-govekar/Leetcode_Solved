# Write your MySQL query statement below
select a.product_id from (select product_id,
case when low_fats ="Y" and recyclable = "Y" then "Y"
else "N"
end as accept
from products) as a
where a.accept="Y"