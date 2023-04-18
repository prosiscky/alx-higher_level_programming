#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
Adapted from model_state.py
REQUIREMENT
- In addition to previous requirements,
the class attribute cities must represent
a relationship with the class City. If the State object is deleted,
all linked City objects must be automatically deleted.
Also, the reference from a City object to his State should be named state
- You must use the module SQLAlchemy
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    State class with id and name attributes of each state
    represents an improvement on model_state.py
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
