#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Découpage propre pour respecter la limite des 79 caractères
    connection_url = (
        f"mysql+mysqldb://{username}:{password}"
        f"@localhost:3306/{db_name}"
    )
    engine = create_engine(connection_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()
