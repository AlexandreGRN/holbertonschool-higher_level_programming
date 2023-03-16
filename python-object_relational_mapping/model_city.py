#!/usr/bin/python3
""" Class  """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

T = True
F = False
class City(Base):
    """ class """

    __tablename__= "cities"

    id = Column(Integer, autoincrement=T, unique=T, nullable=F, primary_key=T)
    name = Column(String(128), nullable=F)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=F)
