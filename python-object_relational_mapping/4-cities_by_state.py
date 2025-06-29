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

    # Establish connection
    conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=username, passwd=password,
        db=db_name, charset="utf8"
    )
    cur = conn.cursor()

    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()
