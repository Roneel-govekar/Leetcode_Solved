# Write your MySQL query statement below
select tweet_id
from tweets
where not length(content)<=15