#!/usr/bin/python3
"""A script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    dbase = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306
    )
    
    dbObj = dbase.cursor()
    dbObj.execute("SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON states.id=cities.state_id")
    stateList = dbObj.fetchall()
    for records in stateList:
        print(records)

    dbObj.close()
    dbase.close()
