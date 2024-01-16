import requests

KEY = ''
SPORT = 'soccer_fa_cup'
REGIONS = 'us'
MARKETS = 'h2h'
ODDS_FORM = 'decimal'
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
        best_odds = {}
        best_bookmakers = {}
        # Find the best odds for each outcome across all bookmakers
        for bookmaker in game['bookmakers']:
            for market in bookmaker['markets']:
                if market['key'] == 'h2h':
                    for outcome in market['outcomes']:
                        if outcome['name'] not in best_odds or best_odds[outcome['name']] < outcome['price']:
                            best_odds[outcome['name']] = outcome['price']
                            best_bookmakers[outcome['name']] = bookmaker['title']

        # Calculate and sum the implied probabilities for these best odds
        total_probability = sum(1 / price for price in best_odds.values())

        # Print only if total probability is less than 1
                # Print only if total probability is less than 1
        if total_probability < 1.2:
            print(f"{game['sport_title']}: {game['home_team']} vs {game['away_team']}")
            print("Opportunity:")
            for outcome, price in best_odds.items():
                print(f"    Bet on {outcome} at {best_bookmakers[outcome]} with odds {price}")
            print(f"  Total Implied Probability: {total_probability}")

