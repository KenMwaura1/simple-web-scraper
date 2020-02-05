"""
Created on Mon Jan 28 00:18:04 2020

@author: Ken Mwaura
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgres+psycopg2://ken:ken1738@localhost:5432/testdb", pool_pre_ping=True
)
engine.connect()
print(engine)
Session = sessionmaker(bind=engine)


Base = declarative_base()
