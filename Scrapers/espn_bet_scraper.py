import requests
import pandas as pd
import json
import current_pga_event
from difflib import SequenceMatcher


# ESPN BOOK CHANGES REQUEST FOR NEW EVENT, HAVE TO FIND ANOTHER REQUEST CHANNEL TO WORK THIS
def get_espn_odds():

    # cookies = {
    # '__cf_bm': 'TiVNFJMemJBochAcmtRN6Nga9be4uQvN.qymlqeHPL8-1708827235-1.0-AfgYvujHDdgJn55uCv1A0Gwm7rLfENOfYBX4+ELBXZzzYZMhKZoG4bpryO4bO+RGOv8ihtHMxexTqjfQuYOPVUU=',
    # '__cfwaitingroom': 'ChhIdGpqNjFEbDVIVnNOdStycW1qTHJnPT0ShAJLb3c0MGtoQjlUL3B2dDJzQTdKbUR5SmVLejZhZmJSU21MR3phSEJCWUs1cWJSbEQwdFdrTldGNCtyYkhlMVdkRE5qdjlKY1dWZ3FGYzRYSmhPNXl2bXlGUXJCS29UWWNYQ3VqT0d3cmVSWjdPaTMvdzVlMW51V251RmE3RnpJNmVuNW5xYmR2ZWdMejFLdW1TbU1jWkJpeENZK0VrOVJTWHM2R2cwdVBReXFsSmxGWXF1S1N0VFhwblBkNkVqTmFiUmFiQ1J5M1Qxd1dlby9vVnVOT055WUJjV1FITUs5eDd0RTVlUVFXcjFNU1h3UXJvL0U1T1c2dHpaOFdmcHVRU3dFPQ%3D%3D',
    # }

    # headers = {
    #     'authority': 'sportsbook-espnbet.us-md.thescore.bet',
    #     'accept': 'application/json',
    #     'accept-language': 'en-US,en;q=0.9',
    #     'content-type': 'application/json',
    #     # 'cookie': '__cf_bm=TiVNFJMemJBochAcmtRN6Nga9be4uQvN.qymlqeHPL8-1708827235-1.0-AfgYvujHDdgJn55uCv1A0Gwm7rLfENOfYBX4+ELBXZzzYZMhKZoG4bpryO4bO+RGOv8ihtHMxexTqjfQuYOPVUU=; __cfwaitingroom=ChhIdGpqNjFEbDVIVnNOdStycW1qTHJnPT0ShAJLb3c0MGtoQjlUL3B2dDJzQTdKbUR5SmVLejZhZmJSU21MR3phSEJCWUs1cWJSbEQwdFdrTldGNCtyYkhlMVdkRE5qdjlKY1dWZ3FGYzRYSmhPNXl2bXlGUXJCS29UWWNYQ3VqT0d3cmVSWjdPaTMvdzVlMW51V251RmE3RnpJNmVuNW5xYmR2ZWdMejFLdW1TbU1jWkJpeENZK0VrOVJTWHM2R2cwdVBReXFsSmxGWXF1S1N0VFhwblBkNkVqTmFiUmFiQ1J5M1Qxd1dlby9vVnVOT055WUJjV1FITUs5eDd0RTVlUVFXcjFNU1h3UXJvL0U1T1c2dHpaOFdmcHVRU3dFPQ%3D%3D',
    #     'origin': 'https://espnbet.com',
    #     'referer': 'https://espnbet.com/',
    #     'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    #     'sec-ch-ua-mobile': '?0',
    #     'sec-ch-ua-platform': '"Windows"',
    #     'sec-fetch-dest': 'empty',
    #     'sec-fetch-mode': 'cors',
    #     'sec-fetch-site': 'cross-site',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    #     'x-anonymous-authorization': 'Bearer eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkExMjhDQkMtSFMyNTYifQ.XcyKtq3NRC6G7P6Hio0zIS6lcDeYBf9cs_hCnR8sTHtUHQ80DswAi_ROJHkia5GD6rBBO4WswFZv6uHd7_fCt02q8HJ-_FJAtq8kZHaQVCgWTNm_zosZGNBMl-hpkqo4ff8Kz-V5nXe1RnmzdZFm-P9DSI5u4By8PmXYQki5bLiZypvOM8VvbLPw20Q6FxH0WdUwgjyYdDBcww30PAg8zg2j4qZWL21OosdaQJQvHURWm6GCRPxO0r94PZI6AU95ArtZ-rcQfwMexi68T8iY9dg3uvu7Ny9MneT_-9qMtYfzh9M2IJfdtKYqOR1itb6QTMlxPXzAo0OYW7JE6VXrfxZX3chzdskd5Z-l3sPLUc23YZplxrV-0S8ZrFfS7mo91dFB9lUr5aZKTayX1tPqFluAbbti9SYKldRTvIA5yqv59iCI6e4ScwuOhcNT92CVyDKeXDrfOihk0OKeM7RpEm5sBVB5WQPTtg40_OYYmI-avOrq8nogKFukMWCotanEuK5G_5flPmNp50CIAXP_Eyu2w5iUlvVRT8ut34PVyIkMrHjKIz48XbWpQGwGv6UGUaugaavH9qyQOOQuGCxgirBLv-MrPEjbigqhHkVb2DIX31AtPc5r1MCXa1W0zEak7mK87k3iin-0d4GwUxGLAdK4FmK-eVCcsRBFgSgf14I.eAtj-IhEOymgPwDvmDqaiw.2BEkfLvWh_t0vw18obxBJ4BxXz8MDqFVi76RZzWd_l6vDEqIiNFEPRCm2vKurWHkkNXAp0CY1TyeVqdm0_JrDdIesW0guyIRt0M4Z7dUi3t89v1hTWWdkFx--fDMJHPXebt1R1Ei4RuczXHCVVLDYoyfyrjHaGVjE-Jos-bECAsAg0KhYmYmuGPRVWroEkfCk1Tx1yrtfAqv9O52ttzGPQTTUZOR19HzRQMYBLs9AgFwZGCFsc77ACTZ_BOitczEZQSHk8K2yZjQpftQSlg-BA.ubVVRLBO_yvPlVLds54EeQ',
    #     'x-app': 'espnbet',
    #     'x-app-version': '24.3.0',
    #     'x-platform': 'web',
    # }

    # json_data = {
    #     'operationName': 'Node',
    #     'variables': {
    #         'includeSectionDefaultField': False,
    #         'id': 'Section:f4c294e8-cdc5-40ad-a0d8-f68e4ee2d6ed',
    #         'oddsFormat': 'AMERICAN',
    #         'selectedFilterId': '',
    #         'includeRichEvent': True,
    #         'includeMediaUrl': True,
    #     },
    #     'extensions': {
    #         'persistedQuery': {
    #             'version': 1,
    #             'sha256Hash': 'bdd2a965f62f53849021a2ca39b41db9773492e4db2ff0941ffbc28c2e5e23be',
    #         },
    #     },
    # }

    # response = requests.post(
    #     'https://sportsbook-espnbet.us-md.thescore.bet/graphql/persisted_queries/bdd2a965f62f53849021a2ca39b41db9773492e4db2ff0941ffbc28c2e5e23be',
    #     cookies=cookies,
    #     headers=headers,
    #     json=json_data,
    # ).json()
        
    cookies = {
        '__cf_bm': 'nu7DHXJXM..Ocu16IMj9MNfr3iB31dZ2anJnjcPRZNM-1709003157-1.0-AX9Tfhz99qjHejhCmy89gMTACO/fHTFyvG4bO3DiwFTkKTwjd49M7Kh7ZvEcjSTnUZvdNxvhOMmTpI42RSbdfw4=',
        '__cfwaitingroom': 'Chh0aXNKU05ROGM4ZU1VK01zbkVyNUF3PT0ShAJ6Y08yeFNVY0s1L2xqRnoyZWxLYlF3N2VmWTJaV3JxajFJWkhOdjU1YWJkUTc4MHVRNVVtLzAvTFdTdDJTVzBheHh0ZllTNFQ2QWpaUDVKOTA0NTl2UFlBVmY1OGY5R2kzYmtkQkRQT2JjNXdrV3BMOHptZndTUlZRTXJhRlR3VWpucG84dHFiWW44eVl3TzM2ZlUwOEJuaE5KQzlTb01VazUrUVdQNW1yeUJXVEZ0VzV2eDJWV3IxUE96UFNjdXU2aXdYTFRVT0dTL0ZPZDFOM1crQWgzZy9hYWxWUEZiT2FtZEdCcU15YVRaRkZCcG1XU0E4bmw5K2FnNXhESTl4ZzdFPQ%3D%3D',
        }

    headers = {
        'authority': 'sportsbook-espnbet.us-default.thescore.bet',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        # 'cookie': '__cf_bm=nu7DHXJXM..Ocu16IMj9MNfr3iB31dZ2anJnjcPRZNM-1709003157-1.0-AX9Tfhz99qjHejhCmy89gMTACO/fHTFyvG4bO3DiwFTkKTwjd49M7Kh7ZvEcjSTnUZvdNxvhOMmTpI42RSbdfw4=; __cfwaitingroom=Chh0aXNKU05ROGM4ZU1VK01zbkVyNUF3PT0ShAJ6Y08yeFNVY0s1L2xqRnoyZWxLYlF3N2VmWTJaV3JxajFJWkhOdjU1YWJkUTc4MHVRNVVtLzAvTFdTdDJTVzBheHh0ZllTNFQ2QWpaUDVKOTA0NTl2UFlBVmY1OGY5R2kzYmtkQkRQT2JjNXdrV3BMOHptZndTUlZRTXJhRlR3VWpucG84dHFiWW44eVl3TzM2ZlUwOEJuaE5KQzlTb01VazUrUVdQNW1yeUJXVEZ0VzV2eDJWV3IxUE96UFNjdXU2aXdYTFRVT0dTL0ZPZDFOM1crQWgzZy9hYWxWUEZiT2FtZEdCcU15YVRaRkZCcG1XU0E4bmw5K2FnNXhESTl4ZzdFPQ%3D%3D',
        'origin': 'https://espnbet.com',
        'referer': 'https://espnbet.com/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'x-anonymous-authorization': 'Bearer eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkExMjhDQkMtSFMyNTYifQ.onZlmPA7hyNp9FbESN21HyEVpxMuuA4Ac1SjZ8hYgyEHvILKCpkHxwvs6NticUl_GMg7KdpXGM70e3PV9v0hPlNHrtXL_hqlG5aJXCPEdve7d-5Wr7Htv8Uu6qUrETo7DYBYdRwOc_a-FEFV-t0FDqr7PI7aH4TRx5Ez7xQtKfOh-h0iRAil_QYbOQ4xcDoUJg5Xo0RqsPGWVzKFXiZGm-wN3ZUexSJyGcg7Bo3MRll-55eAaEO92pRqgZwd82YVMmpAMMHByw2yp9v66d8aEhpDyVTiEkU3DaMlIJXwbQmH11kaGeWzRnh_ytfdWwhSFudJMSvMNNLzIhKQnOIccpfsCEEjPD_5uCySZrtg96fKpNuQXnMT1P__-stPSMll7EQv6W_MJRXTAJJTywItUknnuSl-PJkUms279Zs7O2CNUxpT4KXmLvP34clfQ6zKj5vCRsd5nBqxNjYc074Enq-8OM02U20AaCorMfUzoMEAbcmExo3hnkZuqg8VO765FtTYf3XtD4_CjHrXVaYhnCkhH-S5b2YNPudrpA3ijGHhTUS_EViKcBZTVlA-fqECanuR0t4pO9oGzHQGH-lK1IaKyzU2gCOUEM0dVb2UFqJx2kljvZ3DLbz-JQ6PcwvzGcwYrjMew1MJjp6zlExryvTClq16YFRaxPAWIdV7t34.-fFQpqcfdKx5-LrPicPaIg.SLxrHlibofcM5M5qCYo8wdqENgNNMeitIsiKqg6-smUcUDKOXH2b2gJu_CbvYboL6zJu5MlIHrORVrgvHLv7k3ZnnH4Y51pDytRlepz0Sbos9vHOaJy3VqrCLciZfOq6sH0WYoqeeH1DDCERZYackWQbLoo1pANs9RqFZe5BdriebzcZGqgIamKFbrIm8SA4g8wVtW6vlwA4hDx_i9c-6nQ0XZl9W2-mjVpP4MfPt76CsWh7B55as_5ocBZn0fjTm5MKeuMboKWuztthUcbl4Q.kRMHFOrwWFSB_EjyBkuclQ',
        'x-app': 'espnbet',
        'x-app-version': '24.3.0',
        'x-platform': 'web',
    }

    json_data = {
        'operationName': 'Node',
        'variables': {
            'includeSectionDefaultField': False,
            'id': 'Section:c713602c-ae5b-4198-83e0-52c9c7c28a97',
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
        'https://sportsbook-espnbet.us-default.thescore.bet/graphql/persisted_queries/bdd2a965f62f53849021a2ca39b41db9773492e4db2ff0941ffbc28c2e5e23be',
        cookies=cookies,
        headers=headers,
        json=json_data,
    ).json()


    # Cleans Data to only have the odds of all available events
    odds = response['data']['node']['sectionChildren']

    # Find current PGA event
    current_event = current_pga_event.get_current_pga_event()

    #Iterate through all open events to bet on
    for event in odds:
        # Iterate through all props to bet on
        for child in event['drawerChildren']:
            # Iterate through Marketplaces
            for subchild in child['marketplaceShelfChildren']:
                # Check if name is similar to current PGA event
                event_comparison = SequenceMatcher(None, current_event, subchild['fallbackEvent']['name'])
                if event_comparison.ratio() > .5:
                    # Condition to only find Tournament Winner Odds
                    if(subchild['market']['name'] == 'Tournament Winner'):
                        # Append all players and their respective odds to dataframe
                        market_df = pd.DataFrame(columns = ['Name', 'Odds'])
                        for person in subchild['market']['selections']:
                            new_row = {'Name': person['name']['fullName'], 'Odds': int(person['odds']['formattedOdds'])}
                            market_df.loc[len(market_df)] = new_row
                        return market_df
    return None


get_espn_odds()