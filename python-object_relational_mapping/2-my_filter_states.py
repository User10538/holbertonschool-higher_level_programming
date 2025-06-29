#!/usr/bin/python3
"""

Your script should take 3 arguments: mysql username, mysql password
and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
This is to filter states
"""
import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    searched = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=name, charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM states "
    "WHERE name = '{}' ORDER BY id ASC".format(searched)
    cur.execute(query)

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
