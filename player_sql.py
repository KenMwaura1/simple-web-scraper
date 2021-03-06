# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 00:29:26 2020

@author: Ken Mwaura
"""

from sqlalchemy import Column, String, Integer, Date

from base_sql import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    place = Column(String())
    xp = Column(Integer())

    def __init__(self, username, place, xp):
        self.place = place
        self.username = username
        self.xp = xp
