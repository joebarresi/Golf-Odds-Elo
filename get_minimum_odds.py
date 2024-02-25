import fan_duel_scraper as fd
import espn_bet_scraper as eb
import bet_mgm_scraper as mg
import pandas as pd
import requests
import json
from difflib import SequenceMatcher

def get_minimum_odds():
    # PULLING DATA OF ALL POSSIBLE TOURNAMENTS TO BET ON FROM ALL SITES
    # Hold as a tuple because will end up with a final dataframe that has 
    # name of player, min odd, what book
    fan_duel_all_odds = fd.get_fanduel_odds()
    espn_bet_all_odds =eb.get_espn_odds()
    bet_mgm_all_odds = mg.get_mgm_odds()

    # Return name of current event
    current_event = str(get_pga_events())

    # Cleans the books to only have current PGA event in list of tournaments to bet on
    # There will only be one to bet on
    (fan_duel, fan_duel_odds) = ("Fan Duel", clean_book(fan_duel_all_odds, current_event))
    (espn_bet, espn_bet_odds) = ("Espn Bet", clean_book(espn_bet_all_odds, current_event))
    (mgm, mgm_odds) = ("MGM", clean_book(bet_mgm_all_odds, current_event))
    

    # Now we organize each DF to be organized by alphabetical order of players
    fan_duel_odds = fan_duel_odds.sort_values(by=fan_duel_odds.columns[0])
    espn_bet_odds = espn_bet_odds.sort_values(by=fan_duel_odds.columns[0])
    mgm_odds = mgm_odds.sort_values(by=fan_duel_odds.columns[0])

    # There are minor discrepancies on gaining the info from each book
    # I.e: some books return 3 players to bet on while others only have 2
    # This is why I am sorting on all the same DF, will have to come back to this issue when
    # The error is more detectable

    merged_df = pd.merge(fan_duel_odds, espn_bet_odds, on='Name')
    merged_df = pd.merge(merged_df, mgm_odds, on='Name')

    # TOURNAMENT JUST ENDED, NOW NO DATAFRAMES BY SCRAPING, MAY HAVE TO REVISIT THE CALL TO GET
    # BETTING INFORMATION MEANING INCLUDING CHECKS IF NO BETTING IS AVAILABLE



def clean_book(book : list, current_event):
    cleaned_book = []
    # Clean the data to only show the current PGA Event in the odds list for each sportsbook
    for (tournament_name, tournament_df) in book:
        event_comparison = SequenceMatcher(None, current_event, tournament_name)
        if event_comparison.ratio() > .6:
            cleaned_book.append((tournament_name, tournament_df))

    return cleaned_book[0][1]





# Pulls the schedule for all upcoming pga events and then returns current/most upcoming event
# This doesn't change so maybe should look to just access a single json instead of calling
# request each time
def get_pga_events():
    # headers = {
    # 'authority': 'orchestrator.pgatour.com',
    # 'accept': '*/*',
    # 'accept-language': 'en-US,en;q=0.9',
    # 'content-type': 'application/json',
    # 'origin': 'https://www.pgatour.com',
    # 'referer': 'https://www.pgatour.com/',
    # 'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'sec-fetch-dest': 'empty',
    # 'sec-fetch-mode': 'cors',
    # 'sec-fetch-site': 'same-site',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    # 'x-amz-user-agent': 'aws-amplify/3.0.7',
    # 'x-api-key': 'da2-gsrx5bibzbb4njvhl7t37wqyl4',
    # 'x-pgat-platform': 'web',
    # }

    # json_data = {
    #     'operationName': 'Schedule',
    #     'variables': {
    #         'tourCode': 'R',
    #         'year': '2024',
    #     },
    #     'query': 'query Schedule($tourCode: String!, $year: String, $filter: TournamentCategory) {\n  schedule(tourCode: $tourCode, year: $year, filter: $filter) {\n    completed {\n      month\n      year\n      monthSort\n      ...ScheduleTournament\n    }\n    filters {\n      type\n      name\n    }\n    seasonYear\n    tour\n    upcoming {\n      month\n      year\n      monthSort\n      ...ScheduleTournament\n    }\n  }\n}\n\nfragment ScheduleTournament on ScheduleMonth {\n  tournaments {\n    tournamentName\n    id\n    beautyImage\n    champion\n    champions {\n      displayName\n      playerId\n    }\n    championEarnings\n    championId\n    city\n    country\n    countryCode\n    courseName\n    date\n    dateAccessibilityText\n    purse\n    sortDate\n    startDate\n    state\n    stateCode\n    status {\n      roundDisplay\n      roundStatus\n      roundStatusColor\n      roundStatusDisplay\n    }\n    ticketsURL\n    tourStandingHeading\n    tourStandingValue\n    tournamentLogo\n    display\n    sequenceNumber\n    tournamentCategoryInfo {\n      type\n      logoLight\n      logoDark\n      label\n    }\n  }\n}',
    # }

    # response = requests.post('https://orchestrator.pgatour.com/graphql', headers=headers, json=json_data).json()

    with open("pga.json", "r") as json_file:
        response = json.load(json_file)
    # This pulls the event to most soon occur/the one that is happening Real Time
    current_event = response['data']['schedule']['upcoming'][0]['tournaments'][0]['tournamentName']
    
    return current_event


get_minimum_odds()



        




