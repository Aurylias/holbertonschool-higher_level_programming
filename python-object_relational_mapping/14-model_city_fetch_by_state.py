#!/usr/bin/python3
"""Use the ORM to print all state from hbtn_0e_6_use"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}',
        pool_pre_ping=True
    )

    with Session(engine) as session:
        cities = session.query(State, City).filter(
            State.id == City.state_id
        ).order_by(City.id).all()
        for state, city in cities:
            print(f"{state.name}: ({city.id}) {city.name}")
