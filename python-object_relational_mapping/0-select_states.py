#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    
    username = sys.argv[1] 
    password = sys.argv[2]
    name = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
