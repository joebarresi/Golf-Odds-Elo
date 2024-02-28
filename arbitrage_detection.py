import pandas as pd
import numpy as np
import math
import get_minimum_odds as gmo
import functools as ft


# Function to convert American odds to decimal odds
def american_to_decimal(odds):
    return 100 / abs(odds)

# Function to calculate implied probability
def calculate_implied_probability(odds):
    return 1 / odds

# Function to check for arbitrage opportunity for all golfers
# This only detects an arbitrage event for two golfers and It needs a lot of work
def detect_arbitrage(odds_df):
    for _, row in odds_df.iterrows():
        player_odds = american_to_decimal(row['Odds'])
        player_imp_prob_score = calculate_implied_probability(player_odds) * 100
        print(player_imp_prob_score)
        for _, rowj in odds_df.iterrows():
            second_player_odds =american_to_decimal(rowj['Odds'])
            player_two_imp_prob_score = calculate_implied_probability(second_player_odds) * 100
            arb_score = player_imp_prob_score + player_two_imp_prob_score
            if((arb_score) < 100):
                print("ARBITRAGE")
                print(row['Name'])
                print(rowj['Name'])

    return None    


(odd_list, book_order) = gmo.get_list_of_odds()
golfers_df = gmo.get_minimum_odds(odd_list, book_order)
print(golfers_df)
detect_arbitrage(golfers_df)


