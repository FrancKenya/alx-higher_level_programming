#!/usr/bin/python3
"""Lists states with names starting with 'N' from the database"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    try:
        ldb = MySQLdb.connect(
                host="localhost",
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                port=3306
                )
        cur = ldb.cursor()
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
            cur.close()
            ldb.close()
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)
