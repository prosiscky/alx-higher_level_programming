#!/usr/bin/python3
"""A script that  takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa

- The script should be safe from MySQL injections!
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
    state = sys.argv[4]
    dbObj = dbase.cursor()
    dbObj.execute("SELECT cities.name FROM cities INNER JOIN states ON\
            states.id=cities.state_id WHERE Binary states.name\
            LIKE %s", (state, ))
    stateList = dbObj.fetchall()
    for records in stateList:
        print(records)

    dbObj.close()
    dbase.close()
