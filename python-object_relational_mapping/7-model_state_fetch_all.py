#!/usr/bin/python3
"""Use the ORM to print all state from hbtn_0e_6_use"""
import sys
from sqlalchemy import create_engine

if __name__ == "__main__":
    use, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}"
    )

    with Session() as session:
        session.query(State).all
        for data in states:
            print(f"{s.id}: {s.name}")
