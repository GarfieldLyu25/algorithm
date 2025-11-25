# Write your MySQL query statement below
SELECT DISTINCT visited_on,
       sum_amount AS amount,
       ROUND(sum_amount/7, 2) AS average_amount
FROM (
    SELECT visited_on,
       SUM(amount) OVER ( ORDER BY visited_on ROWS 6 PRECEDING ) AS sum_amount
    FROM (
        SELECT visited_on,
            SUM(amount) AS amount
        FROM Customer
        GROUP BY visited_on
         ) TT
     ) LL
WHERE DATEDIFF(visited_on, (SELECT MIN(visited_on) FROM Customer)) >= 6
