#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import Session


from sqlalchemy import (create_engine)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit("Usage: ./script.py <username> <password> "
                 "<database> <search>")

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search = sys.argv[4]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(username, password, db_name),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    # Query for states whose name contains the search string
    results = session.query(State).filter(State.name.like(f"%{search}%")).order_by(State.id).first()
    
    if results:
        for state in results:
            print(f"{state.id}")
    else:
        print(f"Not found")

    session.close()
