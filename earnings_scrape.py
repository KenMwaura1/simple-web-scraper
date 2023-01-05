"""
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
    print("Place", "Username", "Earnings", sep="  ")
    print(place, username, earnings, sep="   ")
    # create players
    player = Earning_Player(username=username, place=place, earnings=float(earnings))
    players = session.query(Earning_Player).all()
    try:
        if session.query(Earning_Player).filter(Earning_Player.id > 0).all():
            # Check if player exists
            pl = session.query(Earning_Player).filter(Earning_Player.username == username).first()
            if pl:
                # print(pl.username, pl.place, pl.earnings)
                session.delete(pl)
                session.commit()
                
    except Exception as e:
        session.rollback()
        print(e)
    else:
        session.add(player)

        session.commit()

session.close()
