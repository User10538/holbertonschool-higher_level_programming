#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
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

    # Join State and City tables and order by City.id
    results = session.query(State.name, City.id, City.name)\
        .join(City, City.state_id == State.id)\
        .order_by(City.id).all()

    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")

    session.close()
