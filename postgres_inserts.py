# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 01:01:49 2020

@author: Ken Mwaura
"""
from datetime import date

from base_sql import Session, engine, Base
from player_sql import Player

# 1 generate database schema
Base.metadata.create_all(engine)

# 2 Create a new session
session = Session()

# create players
print(session)
