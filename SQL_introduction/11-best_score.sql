-- Order by score only the one with a good score above < 10
SELECT
    score,
    name
    
FROM
    second_table

WHERE
    score >= 10

ORDER BY
    score DESC;