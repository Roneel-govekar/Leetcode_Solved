# Write your MySQL query statement below
select a.contest_id,round(100*count(distinct a.user_id)/count( distinct b.user_id),2) as percentage
from register a, users b
group by contest_id
order by percentage desc, contest_id


