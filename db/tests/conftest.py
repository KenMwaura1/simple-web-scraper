import pytest
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv("..")

engine = create_engine(
    os.getenv(
        "DB",
        "postgresql+psycopg2://test:testpassword@localhost:5432/xp_db",
    )
)
Session = sessionmaker()


@pytest.fixture(scope="module")
def connection():
    connection = engine.connect()
    yield connection
    connection.close()


@pytest.fixture(scope="function")
def session(connection):
    transaction = connection.begin()
    session = Session(bind=connection)
    yield session
    session.close()
    transaction.rollback()
