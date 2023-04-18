#!/usr/bin/python3
"""
script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
REQUIREMENTS
- Your script should take 3 arguments:
mysql username, mysql password and database name
- You must use the module SQLAlchemy
- The connection to your MySQL server must be to localhost on port 3306
- You must only use one query to the database
- You must use the cities relationship for all State objects
- Results must be sorted in ascending order by states.id and cities.id
- Results must be displayed as they are in the example below
- Your code should not be executed when imported
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
        for city_ins in instance.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")
