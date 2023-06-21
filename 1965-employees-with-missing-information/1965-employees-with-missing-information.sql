# Write your MySQL query statement below
select * from(select a.employee_id
from employees a
where a.employee_id not in (select employee_id from salaries)
union 
select b.employee_id
from salaries b
where b.employee_id not in (select employee_id from employees))as c
order by c.employee_id