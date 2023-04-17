#!/usr/bin/python3
""" A script that prints the first State object from the database hbtn_0e_6_usa
REQUIREMENTS
- Your script should take 3 arguments:
mysql username, mysql password and database name
- You must use the module SQLAlchemy
- You must import State and Base from
model_state - from model_state import Base, State
- Your script should connect to a MySQL server running on localhost at
port 3306
- The state you display must be the first in states.id
- You are not allowed to fetch all states from the database before displaying
the result
- The results must be displayed as they are in the example below
- If the table states is empty, print Nothing followed by a new line
- Your code should not be executed when imported
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).first()
    if instance is None:
        print("Nothing")
    else:
        print(instance.id, instance.name, sep=": ")
