with t0 as 
(select client_id, status, request_at,
case status 
when 'completed' then 0
when 'cancelled_by_client' then 1
when 'cancelled_by_driver' then 1
else 0 end as cancel_cnt
from trips t
left join users u on t.client_id = u.users_id
where banned != 'yes'),

t1 as
(select count(client_id) total, request_at   
from t0
group by request_at)

select day as Day, round(cancelled_sum/total,2) as 'Cancellation Rate'
from
(
select sum(cancel_cnt) cancelled_sum, t0.request_at day, t1.total total
from t0
left join t1 on t0.request_at = t1.request_at
group by t0.request_at
) t3