# Write your MySQL query statement below

delete e2  
from person e1, person e2
where e1.id < e2.id
and e1.email=e2.email;
 