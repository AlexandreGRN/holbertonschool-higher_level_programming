#!/usr/bin/python3
""" doc """
import MySQLdb
import sys

if len(sys.argv) >= 4:
    # Connection
    username_ = sys.argv[1]
    password_ = sys.argv[2]
    database_ = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username_,
                         password=password_, database=database_, port=3306)

    # Action
    cursor = db.cursor()

    # SQL Command
    querry = """
    SELECT *
        FROM states
        WHERE
            states.name LIKE BINARY '%{}'
        ORDER BY states.id ASC
    """.format(state_name_searched)

    cursor.execute(querry)
    # Print
    for i in cursor.fetchall():
        print(i)

    db.close()
