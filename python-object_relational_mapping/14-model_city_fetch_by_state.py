#!/usr/bin/python3
""" Table Print """
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City).order_by(City.id.asc())
    for i in query:
        print("{}: ({}) {}".format(i.state_id, i.id, i.name))

    session.commit()
    session.close()
