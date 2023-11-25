#!/usr/bin/python3
""" lists states from database """
import sys
import MySQLdb

if __name__ == "__main__":
    ldb = MySQLdb.connect(
            host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], ldb=sys.argv[3], port=3306)
    cur = ldb.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        cur.close()
        ldb.close()
