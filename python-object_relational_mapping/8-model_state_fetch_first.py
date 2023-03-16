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

    query = session().query(State.id, State.name)
    if query is not None:
        print("{}: {}".format(query[0][0], query[0][1]))
    else:
        print("Nothing")

    session().close()
