#!/usr/bin/python3
""" A script that prints all City objects from the database hbtn_0e_14_usa:
REQUIREMENTS
- Your script should take 3 arguments:
mysql username, mysql password and database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from
model_state import Base, State
- Your script should connect to a MySQL server running on localhost at
port 3306
- Results must be sorted in ascending order by cities.id
- Results must be display as they are in the example below
(<state name>: (<city id>) <city name>)
- Your code should not be executed when imported
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(instance[0] + ": (" + str(instance[1]) + ") " + instance[2])
