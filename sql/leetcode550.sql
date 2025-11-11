# Write your MySQL query statement below
select round(sum(if(temp.player_id is null, 0, 1)) / count(distinct a.player_id), 2) as fraction
from Activity a
left join (
    select player_id, min(event_date) as earlistDate
    from Activity
    group by player_id
) as temp
on a.player_id = temp.player_id
and datediff(a.event_date, temp.earlistDate) = 1