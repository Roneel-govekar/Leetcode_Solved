# Write your MySQL query statement below

select email from(select email , count(email) as counte
from person
group by email
having counte>1) as q