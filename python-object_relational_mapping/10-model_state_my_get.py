#!/usr/bin/python3
"""
Module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = (session.query(State)
             .filter(State.name == argv[4])
             .first())

    if state is None:
        print("Not found")
    else:
        print(state.id)

    if session:
        session.close()