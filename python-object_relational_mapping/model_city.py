#!/usr/bin/python3
"""
Module who define class city to link Cities table.
"""

from model_state import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String


class City(Base):
    """city class, inherits from base"""

    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
