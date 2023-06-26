# Write your MySQL query statement below
select product_name, units as unit from (select product_name, sum(unit) as units
from products p
join orders o 
on p.product_id  = o.product_id  
where order_date like '%-02-%' 
group by p.product_id
) as a
where units >=100