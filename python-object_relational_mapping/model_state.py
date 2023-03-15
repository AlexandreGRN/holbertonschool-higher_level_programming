#!/usr/bin/python3
"""
    Class definition of a State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
""""
    Base class for all tables
"""

class State(Base):
    """ State base """

    __tablename__ = "states"
    id = Column(Integer,autoincrement=True, unique=True, 
                 nullable=False,primary_key=True)
    name = Column(String(128),nullable=False)

    cities = relationship("City", backref="states")
