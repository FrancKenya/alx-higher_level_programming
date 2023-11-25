#!/usr/bin/python3
""" lists states from database """
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
