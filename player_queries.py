# *- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:34:55 2020

@author: Ken Mwaura
"""

# 1 imports
from datetime import date
from player_sql import Player
from base_sql import Session

# 2 Extract a session
session = Session()

# 3 extract all players
players = session.query(Player).all()
for player in players:
    print(player.id,player.place, player.username, player.xp)
