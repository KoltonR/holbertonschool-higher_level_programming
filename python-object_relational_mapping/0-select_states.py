#!/usr/bin/python3
""" Script that list rows of a database """

import MySQLdb
import sys

if __name__ == "__main__":
    
    """script that lists all states from the database hbtn_0e_0_usa"""
    
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], database=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()