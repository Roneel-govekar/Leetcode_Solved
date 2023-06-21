# Write your MySQL query statement below
select user_id, max(time_stamp) as last_stamp
from (select * from logins
     where time_stamp like "2020%") as a
group by user_id
