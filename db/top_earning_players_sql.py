"""
@author: Ken Mwaura
"""

from sqlalchemy import Column, String, Date, Integer, Float
from datetime import date as dt

from base_sql import Base


class Earning_Player(Base):
    __tablename__ = "paid_players"

    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    place = Column(String())
    earnings = Column(Float())
    date = Column(Date)

    def __init__(self, username, place, earnings):
        self.place = place
        self.username = username
        self.earnings = earnings
        self.date = dt.today()
