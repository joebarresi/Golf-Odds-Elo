# draft_king_scraper.py>

import requests
import pandas
from bs4 import BeautifulSoup

def get_draftkings_odds(event_name):
    rq = requests.get("https://sportsbook.draftkings.com/leagues/golf/" + event_name)
    if rq.status_code != 200:
        return None
    
    bs = BeautifulSoup(rq.text)
    divclass = bs.find("div", {"class": "component-18-wrapper"})
    lists = divclass.find_all("ul")
    tags_players = lists[0].find_all("li")
    tags_outright = lists[1].find_all("li")

    players = []
    for node in tags_players:
        players.append(''.join(node.findAll(text=True)))

    outright_odds = []
    for node in tags_outright:
        outright_odds.append(''.join(node.findAll(text=True)))

    draftkings_odds = pandas.DataFrame(
        {'Players': players,
        'Odds': outright_odds
        })

    return draftkings_odds