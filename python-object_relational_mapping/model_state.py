#!/usr/bin/python3
# doc
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import relationship

Base = declarative_base()
"""
    State
"""


class State(Base):
    """ doc """

    __tablename__ = "states"
    id = Column(Integer,autoincrement=True, unique=True, 
                 nullable=False,primary_key=True)
    name = Column(String(128),nullable=False)

    cities = relationship("City", backref="states")
