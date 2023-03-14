#!/usr/bin/python3
""" doc """
import MySQLdb
import sys

if len(sys.argv) == 4:
    # Connection
    username_ = sys.argv[1]
    password_ = sys.argv[2]
    database_ = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username_,
                         password=password_, database=database_, port=3306)

    # Action
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Print
    for i in cursor.fetchall():
        print(i)

    db.close()
