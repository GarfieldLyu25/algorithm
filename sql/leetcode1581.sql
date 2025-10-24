# Write your MySQL query statement below
select customer_id ,count(*) as count_no_trans  from visits as v left join Transactions as t on v.visit_id=t.visit_id
where t.transaction_id  is null
group by customer_id

# 会出现有transaction_id没有amount的情况 属于输入错误，很有可能会消费