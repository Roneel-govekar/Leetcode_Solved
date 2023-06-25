# Write your MySQL query statement below
select * from(select activity_date as day, count(distinct user_id) as active_users
from activity 
group by day
order by day) as a
where a.day between '2019-06-28' and '2019-07-27' 