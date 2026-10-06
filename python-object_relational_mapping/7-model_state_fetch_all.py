#!/usr/bin/python3
"""Use the ORM to print all state from hbtn_0e_6_use"""
import sys
from sqlalchemy import create_engine

if __name__ == "__main__":
    user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, pwd, db),
        pool_pre_ping=True
    )

    with Session(engine) as session:
        states = session.query(State).order_by(State.id).all()
        for data in states:
            print(f"{s.id}: {s.name}")
