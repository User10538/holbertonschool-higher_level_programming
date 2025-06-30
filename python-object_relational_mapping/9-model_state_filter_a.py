#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import Session


from sqlalchemy import (create_engine)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("Usage: ./script.py <username> <password> "
                 "<database> <state_name>")

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(username, password, db_name),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    states_with_a = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id)\
        .all()
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    session.close()
