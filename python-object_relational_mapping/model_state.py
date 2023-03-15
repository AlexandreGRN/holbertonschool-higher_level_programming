#!/usr/bin/python3
""" doc """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy

Base = declarative_base()
""" Base """

class State(Base):
    """ State """

    id = Column(Integer,autoincrement=True, unique=True, 
                 nullable=False,primary_key=True)
    name = Column(String(128),nullable=False)

    cities = sqlalchemy.relationship("City", backref="states")
