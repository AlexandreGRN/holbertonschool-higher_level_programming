#!/usr/bin/python3
""" doc """
import MySQLdb
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    
    def __init__(self):
        