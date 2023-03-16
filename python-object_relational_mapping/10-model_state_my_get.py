#!/usr/bin/python3
""" Table Print """
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)

    query = session().query(State.id, State.name).filter_by(name=str(sys.argv[4]))
    for row in query:
        print("{}".format(row[0]))
    # if query.first():
    if query.first() is None:
        print("Not found")

    session().close()
