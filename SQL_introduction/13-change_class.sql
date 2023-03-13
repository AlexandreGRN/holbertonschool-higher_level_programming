-- Supress every bad grades person (they are too bad)
USE hbtn_0c_0;

DELETE

    FROM
        second_table
    WHERE
        score <= 5;