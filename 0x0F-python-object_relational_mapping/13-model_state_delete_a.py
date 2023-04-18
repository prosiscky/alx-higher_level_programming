#!/usr/bin/python3
""" A script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
REQUIREMENTS
- Your script should take 3 arguments:
mysql username, mysql password and database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from
model_state import Base, State
- Your script should connect to a MySQL server running on localhost at
port 3306
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
    for obj in session.query(State).filter(State.name.like('%a%')):
        session.delete(obj)
    session.commit()
