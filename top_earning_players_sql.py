"""
Created on Mon Feb 9 00:29:26 2020

@author: Ken Mwaura
"""

from sqlalchemy import Column, String, Numeric, Date, Integer, Float

from base_sql import Base


class Earning_Player(Base):
    __tablename__ = "paid_players"

    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    place = Column(String())
    earnings = Column(Float())

    def __init__(self, username, place, earnings):
        self.place = place
        self.username = username
        self.earnings = earnings
