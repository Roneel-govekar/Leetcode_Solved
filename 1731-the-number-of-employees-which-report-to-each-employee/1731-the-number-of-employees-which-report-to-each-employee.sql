# Write your MySQL query statement below
select b.employee_id,b.name,count(a.employee_id) as reports_count,round(avg(a.age))as average_age
from employees a
join employees b
on b.employee_id=a.reports_to
group by b.employee_id
order by b.employee_id 

