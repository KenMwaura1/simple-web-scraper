"""
Created on Sun Feb 9:20:31 2019

@author: Ken Mwaura 
"""

import requests
from bs4 import BeautifulSoup
from datetime import date

from base_sql import Session, engine, Base
from top_earning_players_sql import Earning_Player

# 1 generate database schema
Base.metadata.create_all(engine)


# 2 Create a new session
session = Session()

# get the data
data = requests.get("https://umggaming.com/leaderboards/earnings")

# load data into bs4
soup = BeautifulSoup(data.text, "html.parser")

leaderboard = soup.find("table", {"id": "leaderboard-table"})
tbody = leaderboard.find("tbody")

for tr in tbody.find_all("tr"):
    place = tr.find_all("td")[0].text.strip()
    username = tr.find_all("td")[1].find_all("a")[1].text.strip()
    earnings = tr.find_all("td")[4].text.strip()[1:]
    # print('position','username','earnings', sep='\t')
    print("Place", "Username", "Earnings", sep="\t")
    print(place, username, earnings, sep="\t")
    # leaderboard-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5)
    # create players
    player = Earning_Player(username=username, place=place, earnings=float(earnings))
    try:
        # Check if player exists
        players = session.query(Earning_Player).all()
        if session.query(Earning_Player).filter(Earning_Player.username == username):
            pass
    except True as identifier:
        pass
    else:
        session.add(player)
    session.commit()

session.close()
