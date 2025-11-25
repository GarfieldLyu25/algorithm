with t as (
    select
        *,
        count(*) over (partition by tiv_2015) as same_tiv_2015_num,
        count(*) over (partition by lat, lon) as same_position_num
    from Insurance
)
select
    round(sum(tiv_2016), 2) as tiv_2016
from t
where same_tiv_2015_num > 1 and same_position_num = 1