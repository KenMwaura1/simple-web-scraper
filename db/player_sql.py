# -*- coding: utf-8 -*-
"""
@author: Ken Mwaura
"""

from sqlalchemy import Column, String, Integer, Date
from datetime import date as dt

from base_sql import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    place = Column(String())
    xp = Column(Integer())
    date = Column(Date)

    def __init__(self, username, place, xp):
        self.place = place
        self.username = username
        self.xp = xp
        self.date = dt.today()
    
    def __repr__(self):
        return f"{self.username} {self.place} {self.xp} {self.date}"

    def __str__(self):
        return f"{self.username} {self.place} {self.xp} {self.date}"


if __name__ == "__main__":
    print("Player class")
    