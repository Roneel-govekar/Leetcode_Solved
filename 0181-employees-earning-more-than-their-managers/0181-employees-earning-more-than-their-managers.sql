# Write your MySQL query statement below

SELECT A.name as employee
FROM Employee A, Employee B
WHERE A.salary > B.salary
and B.id=A.managerId;