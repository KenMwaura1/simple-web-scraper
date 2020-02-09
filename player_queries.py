# *- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:34:55 2020

@author: Ken Mwaura
"""

# 1 imports
from sqlalchemy import func
from sqlalchemy import *
from datetime import date
from player_sql import Player
from base_sql import Session

# 2 Extract a session
session = Session()

# 3 extract all players
players = session.query(Player).all()
for player in players:
    print(player.id, player.place, player.username, player.xp)
    # 4 Delete duplicate values in the database
    test = session.query(Player).filter(Player.username).distinct()
    # print(test)

# helper subquery: find first row (by primary key) for each unique name
subq = (
    session.query(Player.username, func.min(Player.id).label("min_id")).group_by(
        Player.username
    )
).subquery("name_min_id")

# query to find all duplicates
q_duplicates = session.query(Player).join(
    subq, and_(Player.username == subq.c.username, Player.id != subq.c.min_id)
)

for x in q_duplicates:
    print("Will delete %s" % x)
    session.delete(x)
session.commit()
