#!/usr/bin/python3
"""A script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
Each state represents a columns in the Table
"""
import MySQLdb
import sys

if __name__ == "__main__":
    dbase = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306
    )
    dbObj = dbase.cursor()
    dbObj.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    stateList = dbObj.fetchall()
    for state instates:
        print(state)
    dbObj.close()
    dbase.close()
