import requests
import pandas as pd
import json
import current_pga_event
from difflib import SequenceMatcher


def get_mgm_odds():

    cookies = {
        'redirex-original': 'http://sports.betmgm.com/en/sports/golf-13/betting/world-6',
        '__cf_bm': '0rH5gsqXYWJ7UrwQq2MFwqOxOXf6Jo5khMC0wBHVtuw-1708836413-1.0-AVkeI2ZCOSAPA73CI0PQrEaY+GZcXKAXMoxZlJX195EuatR7V/3RkvVP0PpIE5IU5TKIF1k/HPU80evGjnNqCt0=',
        '_cfuvid': 'OHJDnyLiYUC8KGm2nikrngmnw4djQf8dYCZ3G8exyiE-1708836413372-0.0-604800000',
        'isLanguageChanged': 'false',
        'lang': 'en',
        'trackerId': '7037292',
        'seoLandingUrl': 'http%3A%2F%2Fsports.md.betmgm.com%2Fen%2Fsports%2Fgolf-13%2Fbetting%2Fworld-6',
        'vnSession': 'd861f842-0b32-425a-a14f-a5ea05f30986',
        'usersettings': 'cid%3Den-US%26vc%3D1%26sst%3D2024-02-25T04%3A46%3A53.5612137Z%26psst%3D0001-01-01T00%3A00%3A00.0000000Z',
        'trc.cid': '50d352b94bb04309ba40553b6e17a248',
        'tdpeh2': '',
        'trackerId2': '7037292',
        'DAPROPS': '"bS:0|scsVersion:2.3|sdeviceAspectRatio:1707/960|sdevicePixelRatio:1.5|bjs.deviceMotion:1|sjs.webGlRenderer:ANGLE (AMD, AMD Radeon(TM) Graphics (0x00001638) Direct3D11 vs_5_0 ps_5_0, D3D11)|srendererRef:02090417563|sscreenWidthHeight:1707/960|sch.model:|saudioRef:781311942|bE:0"',
        'lastKnownProduct': '%7B%22url%22%3A%22https%3A%2F%2Fsports.md.betmgm.com%2Fen%22%2C%22name%22%3A%22sports%22%2C%22previous%22%3A%22unknown%22%2C%22platformProductId%22%3A%22BETTING%22%7D',
        'kndctr_6B47D0245A26653C0A495CDC_AdobeOrg_identity': 'CiY4NTEzNDg3MjMzMzI0NDI5MzU1MDE5NzE3NDYwNTg2MDMwMzEwNVIQCLTH2fTdMRgBKgNWQTYwAaABucfZ9N0x8AG0x9n03TE=',
        'kndctr_6B47D0245A26653C0A495CDC_AdobeOrg_cluster': 'va6',
        'AMCV_6B47D0245A26653C0A495CDC%40AdobeOrg': 'MCMID|85134872333244293550197174605860303105',
        'tq': '%5B%5D',
        'LPVID': 'hjZTVhNzZmMDk0ZTEzMWI0',
        'LPSID-5003492': '4eh7_i17R4KbosKZ7Wah1w',
        '_gcl_au': '1.1.828062814.1708836418',
        '_sp_ses.3176': '*',
        '_sp_id.3176': '4e9f854a-ce29-4529-adc4-5a52afb3a190.1708836419.1.1708836419.1708836419.f97b13ed-eeec-4464-9732-5511a7f2243e',
        '_fbp': 'fb.1.1708836418701.1171708156',
        'setSessionFired': 'true',
        '_uetsid': 'e8a83bd0d39811eea03cf5eb75eff1e7|g9u9ab|2|fjk|0|1516',
        '_gid': 'GA1.2.1397764648.1708836419',
        '_dc_gtm_UA-174640404-16': '1',
        '_dc_gtm_UA-174640404-21': '1',
        '_uetvid': 'e8a875a0d39811ee8658dd4f4a7e7163|ju6izd|1708836418973|1|1|bat.bing.com/p/insights/c/p',
        '_ga': 'GA1.2.883043850.1708836419',
        'medallia-random-id': '6',
        'hq': '%5B%7B%22name%22%3A%22homescreen%22%2C%22shouldShow%22%3Afalse%7D%5D',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Feb+24+2024+23%3A47%3A06+GMT-0500+(Eastern+Standard+Time)&version=6.18.0&isIABGlobal=false&hosts=&consentId=f097bc48-6983-4b33-acf1-a2f874eb76ef&interactionCount=1&landingPath=https%3A%2F%2Fsports.md.betmgm.com%2Fen%2Fsports%2Fgolf-13%2Fbetting%2Fworld-6&groups=C0001%3A1%2CC0004%3A1%2CC0002%3A1%2CC0003%3A1',
        '_ga_V1ZPVXDH9Y': 'GS1.1.1708836418.1.0.1708836426.52.0.0',
        '_ga_SM5BJ4XV8X': 'GS1.1.1708836418.1.0.1708836426.52.0.0',
        'RT': '"z=1&dm=betmgm.com&si=ac56ede9-3dde-4d2e-ad0b-c89faf45edaa&ss=lt112vf6&sl=1&tt=2jo&bcn=%2F%2F173bf108.akstat.io%2F"',
        '__cf_bm': 'j07m4FbjNyo3QuPbTJi6bPkDHAt5wYOif_Z_.NEAfVM-1708836428-1.0-Ad+H7VNq4fS9nmRQxZ/uBUlytLeVsfNB62TrUGnHKMCmHMuuk8k6ZpizCed3Br99TSSTs4VUz6aoDcRg2sPyhb4=',
    }

    headers = {
        'authority': 'sports.md.betmgm.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'redirex-original=http://sports.betmgm.com/en/sports/golf-13/betting/world-6; __cf_bm=0rH5gsqXYWJ7UrwQq2MFwqOxOXf6Jo5khMC0wBHVtuw-1708836413-1.0-AVkeI2ZCOSAPA73CI0PQrEaY+GZcXKAXMoxZlJX195EuatR7V/3RkvVP0PpIE5IU5TKIF1k/HPU80evGjnNqCt0=; _cfuvid=OHJDnyLiYUC8KGm2nikrngmnw4djQf8dYCZ3G8exyiE-1708836413372-0.0-604800000; isLanguageChanged=false; lang=en; trackerId=7037292; seoLandingUrl=http%3A%2F%2Fsports.md.betmgm.com%2Fen%2Fsports%2Fgolf-13%2Fbetting%2Fworld-6; vnSession=d861f842-0b32-425a-a14f-a5ea05f30986; usersettings=cid%3Den-US%26vc%3D1%26sst%3D2024-02-25T04%3A46%3A53.5612137Z%26psst%3D0001-01-01T00%3A00%3A00.0000000Z; trc.cid=50d352b94bb04309ba40553b6e17a248; tdpeh2=; trackerId2=7037292; DAPROPS="bS:0|scsVersion:2.3|sdeviceAspectRatio:1707/960|sdevicePixelRatio:1.5|bjs.deviceMotion:1|sjs.webGlRenderer:ANGLE (AMD, AMD Radeon(TM) Graphics (0x00001638) Direct3D11 vs_5_0 ps_5_0, D3D11)|srendererRef:02090417563|sscreenWidthHeight:1707/960|sch.model:|saudioRef:781311942|bE:0"; lastKnownProduct=%7B%22url%22%3A%22https%3A%2F%2Fsports.md.betmgm.com%2Fen%22%2C%22name%22%3A%22sports%22%2C%22previous%22%3A%22unknown%22%2C%22platformProductId%22%3A%22BETTING%22%7D; kndctr_6B47D0245A26653C0A495CDC_AdobeOrg_identity=CiY4NTEzNDg3MjMzMzI0NDI5MzU1MDE5NzE3NDYwNTg2MDMwMzEwNVIQCLTH2fTdMRgBKgNWQTYwAaABucfZ9N0x8AG0x9n03TE=; kndctr_6B47D0245A26653C0A495CDC_AdobeOrg_cluster=va6; AMCV_6B47D0245A26653C0A495CDC%40AdobeOrg=MCMID|85134872333244293550197174605860303105; tq=%5B%5D; LPVID=hjZTVhNzZmMDk0ZTEzMWI0; LPSID-5003492=4eh7_i17R4KbosKZ7Wah1w; _gcl_au=1.1.828062814.1708836418; _sp_ses.3176=*; _sp_id.3176=4e9f854a-ce29-4529-adc4-5a52afb3a190.1708836419.1.1708836419.1708836419.f97b13ed-eeec-4464-9732-5511a7f2243e; _fbp=fb.1.1708836418701.1171708156; setSessionFired=true; _uetsid=e8a83bd0d39811eea03cf5eb75eff1e7|g9u9ab|2|fjk|0|1516; _gid=GA1.2.1397764648.1708836419; _dc_gtm_UA-174640404-16=1; _dc_gtm_UA-174640404-21=1; _uetvid=e8a875a0d39811ee8658dd4f4a7e7163|ju6izd|1708836418973|1|1|bat.bing.com/p/insights/c/p; _ga=GA1.2.883043850.1708836419; medallia-random-id=6; hq=%5B%7B%22name%22%3A%22homescreen%22%2C%22shouldShow%22%3Afalse%7D%5D; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Feb+24+2024+23%3A47%3A06+GMT-0500+(Eastern+Standard+Time)&version=6.18.0&isIABGlobal=false&hosts=&consentId=f097bc48-6983-4b33-acf1-a2f874eb76ef&interactionCount=1&landingPath=https%3A%2F%2Fsports.md.betmgm.com%2Fen%2Fsports%2Fgolf-13%2Fbetting%2Fworld-6&groups=C0001%3A1%2CC0004%3A1%2CC0002%3A1%2CC0003%3A1; _ga_V1ZPVXDH9Y=GS1.1.1708836418.1.0.1708836426.52.0.0; _ga_SM5BJ4XV8X=GS1.1.1708836418.1.0.1708836426.52.0.0; RT="z=1&dm=betmgm.com&si=ac56ede9-3dde-4d2e-ad0b-c89faf45edaa&ss=lt112vf6&sl=1&tt=2jo&bcn=%2F%2F173bf108.akstat.io%2F"; __cf_bm=j07m4FbjNyo3QuPbTJi6bPkDHAt5wYOif_Z_.NEAfVM-1708836428-1.0-Ad+H7VNq4fS9nmRQxZ/uBUlytLeVsfNB62TrUGnHKMCmHMuuk8k6ZpizCed3Br99TSSTs4VUz6aoDcRg2sPyhb4=',
        'referer': 'https://sports.md.betmgm.com/en/sports/golf-13/betting/world-6',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'x-app-context': 'default',
        'x-bwin-browser-url': 'https://sports.md.betmgm.com/en/sports/golf-13/betting/world-6',
        'x-from-product': 'sports',
    }

    params = {
        'x-bwin-accessid': 'YmNkZjhiMzEtYWIwYS00ZDg1LWE2MWYtOGMyYjljNTdjYjFl',
        'lang': 'en-us',
        'country': 'US',
        'userCountry': 'US',
        'subdivision': 'US-Florida',
        'fixtureTypes': 'Standard',
        'state': 'Latest',
        'offerMapping': 'Filtered',
        'offerCategories': 'Outrights',
        'fixtureCategories': 'Outrights',
        'sportIds': '13',
        'regionIds': '6',
        'competitionIds': '',
        'conferenceIds': '',
        'isPriceBoost': 'false',
        'statisticsModes': 'None',
        'skip': '0',
        'take': '50',
        'sortBy': 'Tags',
    }

    response = requests.get(
        'https://sports.md.betmgm.com/cds-api/bettingoffer/fixtures',
        params=params,
        cookies=cookies,
        headers=headers,
    ).json()

    current_event = current_pga_event.get_current_pga_event()

    # Iterates thruogh all tournaments to bet on
    for fixture in response['fixtures']:
        tournament_name = fixture['name']['value']
        event_comparison = SequenceMatcher(None, current_event, tournament_name)
        if event_comparison.ratio() > .5:

            # Iterates through all betting props for that game
            for game in fixture['games']:
                if game['name']['value'] == "Tournament Winner":
                    # Append all players and their respective odds to dataframe
                    market_df = pd.DataFrame(columns = ['Name', 'Odds'])
                    for player in game['results']:
                        new_row = {'Name': player['name']['value'], 'Odds': player['americanOdds']}
                        market_df.loc[len(market_df)] = new_row
                    

                    return market_df
                
    return None

