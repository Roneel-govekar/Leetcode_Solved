# Write your MySQL query statement below

SELECT A.name as employee
FROM Employee A
left join Employee B
on B.id=A.managerId
where A.salary > B.salary;
