#!/usr/bin/python3
"""
A script that lists all City objects from the database hbtn_0e_101_usa
REQUIREMENTS
- Your script should take 3 arguments:
mysql username, mysql password and database name
- You must use the module SQLAlchemy
- Your script should connect to a MySQL server running on localhost at
port 3306
- You must use only one query to the database
- You must use the state relationship tO access
the State object linked to the City object
- Results must be sorted in ascending order by cities.id
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
        for city_ins in instance.cities:
            print(city_ins.id, city_ins.name, sep=": ", end="")
            print(" -> " + instance.name)
