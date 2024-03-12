import requests


# Pulls the schedule for all upcoming pga events and then returns current/most upcoming event
# This doesn't change so maybe should look to just access a single json instead of calling
# request each time
def get_current_pga_event():
    headers = {
    'authority': 'orchestrator.pgatour.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.pgatour.com',
    'referer': 'https://www.pgatour.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'x-amz-user-agent': 'aws-amplify/3.0.7',
    'x-api-key': 'da2-gsrx5bibzbb4njvhl7t37wqyl4',
    'x-pgat-platform': 'web',
    }

    json_data = {
        'operationName': 'Schedule',
        'variables': {
            'tourCode': 'R',
            'year': '2024',
        },
        'query': 'query Schedule($tourCode: String!, $year: String, $filter: TournamentCategory) {\n  schedule(tourCode: $tourCode, year: $year, filter: $filter) {\n    completed {\n      month\n      year\n      monthSort\n      ...ScheduleTournament\n    }\n    filters {\n      type\n      name\n    }\n    seasonYear\n    tour\n    upcoming {\n      month\n      year\n      monthSort\n      ...ScheduleTournament\n    }\n  }\n}\n\nfragment ScheduleTournament on ScheduleMonth {\n  tournaments {\n    tournamentName\n    id\n    beautyImage\n    champion\n    champions {\n      displayName\n      playerId\n    }\n    championEarnings\n    championId\n    city\n    country\n    countryCode\n    courseName\n    date\n    dateAccessibilityText\n    purse\n    sortDate\n    startDate\n    state\n    stateCode\n    status {\n      roundDisplay\n      roundStatus\n      roundStatusColor\n      roundStatusDisplay\n    }\n    ticketsURL\n    tourStandingHeading\n    tourStandingValue\n    tournamentLogo\n    display\n    sequenceNumber\n    tournamentCategoryInfo {\n      type\n      logoLight\n      logoDark\n      label\n    }\n  }\n}',
    }

    response = requests.post('https://orchestrator.pgatour.com/graphql', headers=headers, json=json_data).json()

    # with open("pga.json", "r") as json_file:
    #     response = json.load(json_file)
    # This pulls the event to most soon occur/the one that is happening Real Time
    current_event = response['data']['schedule']['upcoming'][0]['tournaments'][0]['tournamentName']
    
    return current_event