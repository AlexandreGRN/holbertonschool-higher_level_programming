-- Supress every bad grades person (they are too bad)
DELETE

    FROM
        second_table
    WHERE
        score <= 5;