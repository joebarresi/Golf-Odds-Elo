import fan_duel_scraper as fd
import espn_bet_scraper as eb
import bet_mgm_scraper as mg
import pandas as pd
import functools as ft


# This function takes all the lines from the given books
# Currently pretty slow
def get_minimum_odds(event_name):
    odds_list, book_order = get_list_of_odds(event_name)

    # Merge Odds Lists on Odds
    all_odds_df = ft.reduce(lambda left, right: pd.merge(left, right, on='Name'), odds_list)

    best_odd_df = pd.DataFrame(columns = ['Name', 'Odds', 'Book'])
    for index, row in all_odds_df.iterrows():
        # Find max betting odds and column index associated with it, send it to best_odds
        max_value = row[1:].max()
        associated_column = (row.index.get_loc(row[row == max_value].index[0]) - 1)
        new_row = {'Name': row['Name'], 'Odds': max_value, 'Book': book_order[associated_column]}
        best_odd_df.loc[len(best_odd_df)] = new_row

    # Sorts Best Odds_df by most popular player
    # May consider doing this for each book as a better way to lose less names
    best_odd_df = best_odd_df.sort_values(by = best_odd_df.columns[1])
    best_odd_df = best_odd_df.reset_index(drop=True)

    return best_odd_df.to_json(orient='records')

def get_list_of_odds(event):
    # Grabbing Odds of Supported Books
    fan_duel_odds = None
    bet_mgm_odds = None
    espn_bet_odds = None


    fan_duel_odds = fd.get_fanduel_odds()
    bet_mgm_odds = mg.get_mgm_odds()
    espn_bet_odds = eb.get_espn_odds()    

    odds_list = []
    book_order = []

    # Now we organize each DF to be organized by alphabetical order of players
    if fan_duel_odds is not None:
        fan_duel_odds = fan_duel_odds.sort_values(by=fan_duel_odds.columns[0])
        odds_list.append(fan_duel_odds)
        book_order.append("FanDuel")
    else:
        print("Error gathering FanDuel Odds for", event)

    if espn_bet_odds is not None:
        espn_bet_odds = espn_bet_odds.sort_values(by=espn_bet_odds.columns[0])
        odds_list.append(espn_bet_odds)
        book_order.append("ESPN Bet")
    else:
        print("Error gathering ESPN Bet Odds for", event)

    if bet_mgm_odds is not None:
        bet_mgm_odds = bet_mgm_odds.sort_values(by=bet_mgm_odds.columns[0])
        odds_list.append(bet_mgm_odds)
        book_order.append("Bet MGM")
    else:
        print("Error gathering Bet MGM Odds for", event)

    return (odds_list, book_order)



        
    