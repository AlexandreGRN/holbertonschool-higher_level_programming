#!/usr/bin/python3
""" doc """
import MySQLdb
import sys

if len(sys.argv) >= 4:
    # Connection
    username_ = sys.argv[1]
    password_ = sys.argv[2]
    database_ = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username_,
                         password=password_, database=database_, port=3306)

    # Action
    cursor = db.cursor()

    # SQL Command
    querry = """
    SELECT cities.id, cities.name, states.name
        FROM cities, states
        WHERE cities.state_id = states.id
        ORDER BY cities.id ASC
    """

    cursor.execute(querry)
    # Print
    for i in cursor.fetchall():
        print(i)

    db.close()
