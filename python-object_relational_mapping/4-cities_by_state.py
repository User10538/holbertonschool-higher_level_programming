#!/usr/bin/python3
"""
Lists all values in the `states` table where name matches the argument.
Takes 4 arguments: mysql username, mysql password,
database name, and state name.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    searched = sys.argv[4]

    # Establish connection
    conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=username, passwd=password,
        db=db_name, charset="utf8"
    )
    cur = conn.cursor()

    # Sanitize single quotes in input (very basic protection)
    searched_safe = searched.replace("'", "''")

    cur.execute()

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()
