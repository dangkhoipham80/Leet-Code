-- Write your PostgreSQL query statement below
SELECT
    x,
    y,
    z,
    CASE
        WHEN (x + y - z) * (y + z - x) * (z + x - y) > 0 AND x > 0 AND y > 0 AND z > 0
        THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;
