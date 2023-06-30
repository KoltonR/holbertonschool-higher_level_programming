#!/usr/bin/python3
"""takes in an argument and displays all values in the state table"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE \
                BINARY name='{}'".format(argv[4]))
    [print(state) for state in cur.fetchall()]