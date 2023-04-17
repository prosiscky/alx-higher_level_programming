#!/usr/bin/python3
import MySQLdb
import sys

"""A script that lists all states from the database hbtn_0e_0_usa
The states represents the columns in the Table
"""
# REQUIREMENTS
    '''
    - This script should take 3 arguments:
    mysql username, mysql password and database name
    (no argument validation needed)

    - The result of the query is ordered by the Auto generated
    id hence no need for order by clause
    '''
if __name__=="__main__":
    dbase = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306
    )
    dbObj = dbase.cursor()
    dbObj.execute("SELECT * FROM states")
    stateList = dbObj.fetchall()
    for state in stateList:
        print(state)
    dbObj.close()
    dbase.close()
