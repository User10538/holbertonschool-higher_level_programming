#!/usr/bin/python3
"""
Lists all cities in the database hbtn_0e_4_usa
Takes 3 arguments: mysql username, mysql password, and database name.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit("Usage: ./script.py <username> <password> <database> <state_name>")

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )
    cur = db.cursor()

    # Execute single query to get cities and their states,
    # ordered by city id ascending
    # It’s a clean and readable way to define a long SQL string.
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))

    # Print each row as a tuple exactly as requested
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
