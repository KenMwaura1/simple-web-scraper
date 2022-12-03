"""
Created on Mon Jan 28 00:18:04 2020

@author: Ken Mwaura
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()


db = os.getenv(
    "DB", "postgresql+psycopg2://test:testpassword@localhost:5432/xp_db"
)
engine = create_engine(db)
engine.connect()
print(engine)
Session = sessionmaker(bind=engine)

Base = declarative_base()
