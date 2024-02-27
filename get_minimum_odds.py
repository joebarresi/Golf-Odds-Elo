import fan_duel_scraper as fd
import espn_bet_scraper as eb
import bet_mgm_scraper as mg
import pandas as pd
import functools as ft

# This function takes all the lines from the given books
# Currently pretty slow
def get_minimum_odds(odds_list, book_order):
    
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

    print(best_odd_df)
    return best_odd_df





def get_list_of_odds():
    # Grabbing Odds of Supported Books
    fan_duel_odds = fd.get_fanduel_odds()
    bet_mgm_odds = mg.get_mgm_odds()
    espn_bet_odds = eb.get_espn_odds()    

    # Now we organize each DF to be organized by alphabetical order of players
    fan_duel_odds = fan_duel_odds.sort_values(by=fan_duel_odds.columns[0])
    espn_bet_odds = espn_bet_odds.sort_values(by=espn_bet_odds.columns[0])
    bet_mgm_odds = bet_mgm_odds.sort_values(by=bet_mgm_odds.columns[0])

    odds_list = [fan_duel_odds, espn_bet_odds, bet_mgm_odds]
    book_order = ["Fan Duel", "Espn Bet", "Bet MGM"]

    return (odds_list, book_order)


(odd_list, book_order) = get_list_of_odds()
get_minimum_odds(odd_list, book_order)



        




