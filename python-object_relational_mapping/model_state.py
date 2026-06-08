#!/bin/usr/bin/python3
"""
Module class state and his instance Base
"""

from sqlalchemy import Colums, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Class State, link to the state table in MySQL"""
    __tablename__ = 'states'
    
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    
    name = Column(String(128), nullable=False)
