# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 20:20:31 2019

@author: Ken Mwaura 
"""

import requests
from bs4 import BeautifulSoup
from datetime import date

from base_sql import Session, engine, Base
from player_sql import Player

# 1 generate database schema
Base.metadata.create_all(engine)


# 2 Create a new session
session = Session()

# get the data
data = requests.get("https://www.umggaming.com/leaderboards")

# load data into bs4
soup = BeautifulSoup(data.text, "html.parser")

leaderboard = soup.find("table", {"id": "leaderboard-table"})
tbody = leaderboard.find("tbody")

for tr in tbody.find_all("tr"):
    place = tr.find_all("td")[0].text.strip()
    username = tr.find_all("td")[1].find_all("a")[1].text.strip()
    xp = tr.find_all("td")[4].text.strip()
    # print('position','username','xp', sep='\t')
    print("Place", "Username", "XP", sep="  ")
    print(place, username, xp, sep="  ")
    # leaderboard-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5)

    # create players
    player = Player(username=username, place=place, xp=xp)
    # Check if player exists
    players = session.query(Player).all()
    try: 
        pl = session.query(Player).filter(Player.username == username).first()
        if pl:
            session.delete(pl)
            session.commit()
    except Exception as e:
        session.rollback()
        print(e)
    else:
        session.add(player)
    session.commit()

session.close()
