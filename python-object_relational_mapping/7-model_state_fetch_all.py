#!/usr/bin/python3
"""
Script qui liste tous les objets 'State' de la base de données
Connexion explicite à localhost sur le port 3306
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    connection_url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"

    engine = create_engine(connection_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        

    session.close()
