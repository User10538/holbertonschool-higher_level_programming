#!/usr/bin/python3
"""

Inherits from Base Tips, links to the MySQL table states
class attribute id that represents a column of
an auto-generated, unique integer, can’t be null and is a primary key
class attribute name that represents a column
of a string with maximum 128 characters and can’t be null
"""
import sys
import model_state
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

"""
Create the base class for class definitions
"""
Base = declarative_base()


class City (Base):
    """
     State class linked to the 'cities' table
     """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
