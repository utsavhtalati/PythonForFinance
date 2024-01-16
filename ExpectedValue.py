import requests 

KEY = ''

SPORT = 'americanfootball_nfl'

REGIONS = 'us'

MARKETS = 'h2h'

ODDS_FORM = 'american'

DATE_FORM = 'iso'

# Constructing the endpoint URL
url = f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds/?apiKey={KEY}&regions={REGIONS}&markets={MARKETS}'

# Making the GET request
sports_response = requests.get(url)

if sports_response.status_code != 200:
    print(f'Failed to get sports: status_code {sports_response.status_code}, response body {sports_response.text}')
else:
    data = sports_response.json()
    for game in data:
        print(f"{game['sport_title']}: {game['home_team']} vs {game['away_team']}")
        for bookmaker in game['bookmakers']:
            if bookmaker['key'] in ['fanduel', 'draftkings']:
                print(f"  Bookmaker: {bookmaker['title']}")
                for market in bookmaker['markets']:
                    if market['key'] == 'h2h':
                        for outcome in market['outcomes']:
                            print(f" {outcome['name']}: {outcome['price']}")