#!/usr/bin/python3
"""

Inherits from Base Tips, links to the MySQL table states
class attribute id that represents a column of
an auto-generated, unique integer, can’t be null and is a primary key
class attribute name that represents a column
of a string with maximum 128 characters and can’t be null
"""
import sys
from sqlalchemy import Column, Integer, String

""" 
Create the base class for class definitions
"""
Base = declarative_base()

class State():
    __tablename__ = "states"

    id = Column(Integer, Primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
