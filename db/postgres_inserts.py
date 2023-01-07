# -*- coding: utf-8 -*-
"""
@author: Ken Mwaura
"""

from base_sql import Session, engine, Base
from player_sql import Player

# 1 generate database schema
Base.metadata.create_all(engine, Base.metadata.tables.values(), checkfirst=True)

# 2 Create a new session
session = Session()

# create players
print(len(session.query(Player).all()))
