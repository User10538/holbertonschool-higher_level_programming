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
                 "<database>")

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(username, password, db_name),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    # Delete state
    delete_state = session.query(State)\
        .filter((State.name).like('%a%')).all()
    
    for state in delete_state:
        session.delete(state)

    session.commit()
    session.close()
