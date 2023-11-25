#!/usr/bin/python3
"""Displays values from states table based on  input"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
                "Usage: {} <username> <password> <database> <state_name>"
                .format(sys.argv[0])
                )
        sys.exit(1)

    try:
        db = MySQLdb.connect(
                host="localhost",
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                port=3306
                )
        cur = db.cursor()
        state_name = sys.argv[4]
        query = "SELECT * FROM states WHERE name =
        '{}' ORDER BY id ASC".format(state_name)
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)
