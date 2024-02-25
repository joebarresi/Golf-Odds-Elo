import json
import pandas as pd
import requests

def get_fanduel_odds():
    headers = {
        'authority': 'sbapi.md.sportsbook.fanduel.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'if-none-match': 'W/"a1da5-3RMUrQNMUky0gnN0T+EdTVEFPFE"',
        'origin': 'https://sportsbook.fanduel.com',
        'referer': 'https://sportsbook.fanduel.com/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    params = {
        'page': 'SPORT',
        'eventTypeId': '3',
        '_ak': 'FhMFpcPWXMeyZxOx',
        'timezone': 'America/New_York',
    }

    response = requests.get('https://sbapi.md.sportsbook.fanduel.com/api/content-managed-page', params=params, headers=headers).json()


    # Shrinks Json into only attachements key
    odds = response['attachments']

    market_odds = []

    # Filters to only win-only markets for each win only market appends a new tuple type: string * dataframe (contest name, dataframe of odds)
    # to the list with each player and their odds
    for element in odds['markets']:
        if(odds['markets'][element]['marketName'] == 'Win Only'):
            market_df = pd.DataFrame(columns = ['Name', 'Odds'])
            for runner in odds['markets'][element]['runners']:
                # Adds next competitor to current dataframe
                new_row = {'Name': runner['runnerName'], "Odds" : runner['winRunnerOdds']['americanDisplayOdds']['americanOdds']}
                market_df.loc[len(market_df)] = new_row

            # Appends new market to market list 
            # Gets name by searching events key with given ID
            event_id = odds['markets'][element]['eventId']
            market_odds.append((odds['events'][str(event_id)]['name'], market_df))


    return market_odds
        
    
    

def main():
    odds = get_fanduel_odds()





