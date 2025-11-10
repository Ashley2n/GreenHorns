import os
import sys
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from domain.models import Base

engine = create_engine('sqlite:///test.db')
Session = sessionmaker(bind=engine)

@pytest.fixture(scope='function')
def db_session():
    """
        Creates Database table, makes a session
        Then yield it for use-cases,
        After everything it is then closed.

    """
    Base.metadata.create_all(engine)
    session = Session()

    yield session

    session.close()
    Base.metadata.drop_all(engine)