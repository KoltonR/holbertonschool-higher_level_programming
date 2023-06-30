#!/usr/bin/python3
"""lists all the states that start with an N from hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]