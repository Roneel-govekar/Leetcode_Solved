# Write your MySQL query statement below
select distinct author_id as id  
from(select author_id
from views
where author_id = viewer_id
) as a
order by id