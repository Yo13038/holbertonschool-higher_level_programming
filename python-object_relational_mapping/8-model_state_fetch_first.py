#!/usr/bin/python3
"""
Script that list state object from database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    connection_url = (
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    )
    engine = create_engine(connection_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if first_state is None:
        print("Nothing")
    else:
        print("{first_state.id}: {first_state.name}")

    session.close()
