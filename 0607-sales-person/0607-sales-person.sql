# Write your MySQL query statement below
select a.cname as name from  (select s.name as cname, c.name as coloname
from salesPerson s 
left join orders o
on s.sales_id= o.sales_id 
left join company c
on o.com_id = c.com_id 
group by s.name
having c.name is null or c.name !="red") as a

