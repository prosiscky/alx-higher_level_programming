#!/usr/bin/python3
"""
Python file named model_city.py that contains the class definition of a City
REQUIREMENTS
- City class:
inherits from Base (imported from model_state)
- links to the MySQL table cities
- class attribute id that represents a column of an auto-generated,
unique integer, can’t be null and is a primary key
- class attribute name that represents a column of a string of 128
characters and can’t be null
- class attribute state_id that represents a column of an integer,
can’t be null and is a foreign key to states.id
- You must use the module SQLAlchemy
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    Class that defines each city and
    inherits from Base (imported from model_state)
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
