import requests
import pandas as pd
import json
from difflib import SequenceMatcher


# ESPN BOOK CHANGES REQUEST FOR NEW EVENT, HAVE TO FIND ANOTHER REQUEST CHANNEL TO WORK THIS
def get_espn_odds():

    cookies = {
    '__cf_bm': 'TiVNFJMemJBochAcmtRN6Nga9be4uQvN.qymlqeHPL8-1708827235-1.0-AfgYvujHDdgJn55uCv1A0Gwm7rLfENOfYBX4+ELBXZzzYZMhKZoG4bpryO4bO+RGOv8ihtHMxexTqjfQuYOPVUU=',
    '__cfwaitingroom': 'ChhIdGpqNjFEbDVIVnNOdStycW1qTHJnPT0ShAJLb3c0MGtoQjlUL3B2dDJzQTdKbUR5SmVLejZhZmJSU21MR3phSEJCWUs1cWJSbEQwdFdrTldGNCtyYkhlMVdkRE5qdjlKY1dWZ3FGYzRYSmhPNXl2bXlGUXJCS29UWWNYQ3VqT0d3cmVSWjdPaTMvdzVlMW51V251RmE3RnpJNmVuNW5xYmR2ZWdMejFLdW1TbU1jWkJpeENZK0VrOVJTWHM2R2cwdVBReXFsSmxGWXF1S1N0VFhwblBkNkVqTmFiUmFiQ1J5M1Qxd1dlby9vVnVOT055WUJjV1FITUs5eDd0RTVlUVFXcjFNU1h3UXJvL0U1T1c2dHpaOFdmcHVRU3dFPQ%3D%3D',
    }

    headers = {
        'authority': 'sportsbook-espnbet.us-md.thescore.bet',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        # 'cookie': '__cf_bm=TiVNFJMemJBochAcmtRN6Nga9be4uQvN.qymlqeHPL8-1708827235-1.0-AfgYvujHDdgJn55uCv1A0Gwm7rLfENOfYBX4+ELBXZzzYZMhKZoG4bpryO4bO+RGOv8ihtHMxexTqjfQuYOPVUU=; __cfwaitingroom=ChhIdGpqNjFEbDVIVnNOdStycW1qTHJnPT0ShAJLb3c0MGtoQjlUL3B2dDJzQTdKbUR5SmVLejZhZmJSU21MR3phSEJCWUs1cWJSbEQwdFdrTldGNCtyYkhlMVdkRE5qdjlKY1dWZ3FGYzRYSmhPNXl2bXlGUXJCS29UWWNYQ3VqT0d3cmVSWjdPaTMvdzVlMW51V251RmE3RnpJNmVuNW5xYmR2ZWdMejFLdW1TbU1jWkJpeENZK0VrOVJTWHM2R2cwdVBReXFsSmxGWXF1S1N0VFhwblBkNkVqTmFiUmFiQ1J5M1Qxd1dlby9vVnVOT055WUJjV1FITUs5eDd0RTVlUVFXcjFNU1h3UXJvL0U1T1c2dHpaOFdmcHVRU3dFPQ%3D%3D',
        'origin': 'https://espnbet.com',
        'referer': 'https://espnbet.com/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'x-anonymous-authorization': 'Bearer eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkExMjhDQkMtSFMyNTYifQ.XcyKtq3NRC6G7P6Hio0zIS6lcDeYBf9cs_hCnR8sTHtUHQ80DswAi_ROJHkia5GD6rBBO4WswFZv6uHd7_fCt02q8HJ-_FJAtq8kZHaQVCgWTNm_zosZGNBMl-hpkqo4ff8Kz-V5nXe1RnmzdZFm-P9DSI5u4By8PmXYQki5bLiZypvOM8VvbLPw20Q6FxH0WdUwgjyYdDBcww30PAg8zg2j4qZWL21OosdaQJQvHURWm6GCRPxO0r94PZI6AU95ArtZ-rcQfwMexi68T8iY9dg3uvu7Ny9MneT_-9qMtYfzh9M2IJfdtKYqOR1itb6QTMlxPXzAo0OYW7JE6VXrfxZX3chzdskd5Z-l3sPLUc23YZplxrV-0S8ZrFfS7mo91dFB9lUr5aZKTayX1tPqFluAbbti9SYKldRTvIA5yqv59iCI6e4ScwuOhcNT92CVyDKeXDrfOihk0OKeM7RpEm5sBVB5WQPTtg40_OYYmI-avOrq8nogKFukMWCotanEuK5G_5flPmNp50CIAXP_Eyu2w5iUlvVRT8ut34PVyIkMrHjKIz48XbWpQGwGv6UGUaugaavH9qyQOOQuGCxgirBLv-MrPEjbigqhHkVb2DIX31AtPc5r1MCXa1W0zEak7mK87k3iin-0d4GwUxGLAdK4FmK-eVCcsRBFgSgf14I.eAtj-IhEOymgPwDvmDqaiw.2BEkfLvWh_t0vw18obxBJ4BxXz8MDqFVi76RZzWd_l6vDEqIiNFEPRCm2vKurWHkkNXAp0CY1TyeVqdm0_JrDdIesW0guyIRt0M4Z7dUi3t89v1hTWWdkFx--fDMJHPXebt1R1Ei4RuczXHCVVLDYoyfyrjHaGVjE-Jos-bECAsAg0KhYmYmuGPRVWroEkfCk1Tx1yrtfAqv9O52ttzGPQTTUZOR19HzRQMYBLs9AgFwZGCFsc77ACTZ_BOitczEZQSHk8K2yZjQpftQSlg-BA.ubVVRLBO_yvPlVLds54EeQ',
        'x-app': 'espnbet',
        'x-app-version': '24.3.0',
        'x-platform': 'web',
    }

    json_data = {
        'operationName': 'Node',
        'variables': {
            'includeSectionDefaultField': False,
            'id': 'Section:f4c294e8-cdc5-40ad-a0d8-f68e4ee2d6ed',
            'oddsFormat': 'AMERICAN',
            'selectedFilterId': '',
            'includeRichEvent': True,
            'includeMediaUrl': True,
        },
        'extensions': {
            'persistedQuery': {
                'version': 1,
                'sha256Hash': 'bdd2a965f62f53849021a2ca39b41db9773492e4db2ff0941ffbc28c2e5e23be',
            },
        },
    }

    response = requests.post(
        'https://sportsbook-espnbet.us-md.thescore.bet/graphql/persisted_queries/bdd2a965f62f53849021a2ca39b41db9773492e4db2ff0941ffbc28c2e5e23be',
        cookies=cookies,
        headers=headers,
        json=json_data,
    ).json()
    print(response)

    # Cleans Data to only have the odds of all available events
    odds = response['data']['node']['sectionChildren']
    print(odds)

    # List of tuple to contain Market Name and odds associated with each player
    market_odds = []

    #Iterate through all open events to bet on
    for event in odds:
        # Iterate through all props to bet on
        for child in event['drawerChildren']:
            # Iterate through Marketplaces
            for subchild in child['marketplaceShelfChildren']:
                # Condition to only find Tournament Winner Odds
                if(subchild['market']['name'] == 'Tournament Winner'):
                    # Append all players and their respective odds to dataframe
                    market_df = pd.DataFrame(columns = ['Name', 'Odds'])
                    for person in subchild['market']['selections']:
                        new_row = {'Name': person['name']['fullName'], 'Odds': person['odds']['formattedOdds']}
                        market_df.loc[len(market_df)] = new_row
                    market_odds.append((subchild['fallbackEvent']['name'], market_df))

    return market_odds


