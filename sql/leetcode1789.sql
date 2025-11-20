-- # Write your MySQL query statement below
WITH t AS (
    SELECT
        employee_id,
        department_id,
        primary_flag,
        COUNT(*) OVER(PARTITION BY employee_id) AS count_over
    FROM Employee
            )
SELECT employee_id,department_id
FROM t
WHERE count_over = 1 or primary_flag = 'Y';

SELECT employee_id, department_id
FROM Employee
WHERE primary_flag='Y' OR
    employee_id in
    (SELECT employee_id
    FROM Employee
    Group by employee_id
    having count(employee_id)=1);