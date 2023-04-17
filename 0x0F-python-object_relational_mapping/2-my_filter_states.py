#!/usr/bin/python3
"""A script that  takes in an argument and
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
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
    dbObj.execute("SELECT * FROM states WHERE Binary name ='%s'", (state,))
    stateList = dbObj.fetchall()
    for records in stateList:
        print(records)

    dbObj.close()
    dbase.close()
