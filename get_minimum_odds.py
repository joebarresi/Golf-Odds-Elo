import fan_duel_scraper as fd
import espn_bet_scraper as eb
import bet_mgm_scraper as mg
import current_pga_event
import pandas as pd
import requests
import json

def get_minimum_odds():
    # Pulls data of current tournaments odds
    fan_duel_odds = fd.get_fanduel_odds()
    # espn_bet_all_odds =eb.get_espn_odds()
    bet_mgm_odds = mg.get_mgm_odds()


    

    

    # Now we organize each DF to be organized by alphabetical order of players
    fan_duel_odds = fan_duel_odds.sort_values(by=fan_duel_odds.columns[0])
    
    # espn_bet_odds = espn_bet_odds.sort_values(by=fan_duel_odds.columns[0])
    bet_mgm_odds = bet_mgm_odds.sort_values(by=bet_mgm_odds.columns[0])

    print(fan_duel_odds)
    print(bet_mgm_odds)
    # There are minor discrepancies on gaining the info from each book
    # I.e: some books return 3 players to bet on while others only have 2
    # This is why I am sorting on all the same DF, will have to come back to this issue when
    # The error is more detectable

    # merged_df = pd.merge(fan_duel_odds, espn_bet_odds, on='Name')
    # merged_df = pd.merge(merged_df, mgm_odds, on='Name')

    # TOURNAMENT JUST ENDED, NOW NO DATAFRAMES BY SCRAPING, MAY HAVE TO REVISIT THE CALL TO GET
    # BETTING INFORMATION MEANING INCLUDING CHECKS IF NO BETTING IS AVAILABLE



# def clean_book(book : list, current_event):
#     cleaned_book = []

#     # Clean the data to only show the current PGA Event in the odds list for each sportsbook
#     for (tournament_name, tournament_df) in book:
#         event_comparison = SequenceMatcher(None, current_event, tournament_name)
#         if event_comparison.ratio() > .5:
#             cleaned_book.append((tournament_name, tournament_df))

#     return cleaned_book[0][1]




get_minimum_odds()



        




