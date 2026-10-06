#!/usr/bin/python3
"""Use the ORM to print the first state object from hbtn_0e_6_use"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}',
        pool_pre_ping=True
    )

    with Session(engine) as session:
        states = session.query(State).order_by(State.id).first()
        for data in states:
            print(f"{data.id}: {data.name}")
