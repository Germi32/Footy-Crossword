from api import (search_competition, search_club, search_player, get_competition_clubs,
                 get_club_profile, get_club_players, get_player_profile, get_player_market_value,
                 get_player_transfers, get_player_stats)

# Filters
MIN_PRICE_CLUB = 400000000
competitions = ("LaLiga", "Premier League", "Serie A")
# API query constants
ID = "id"
CURRENT_MARKET_VALUE = "currentMarketValue"


def remove_letters(string: str):
    only_numbers = ''.join(character for character in string if character.isdigit())
    return int(only_numbers)


def filter_clubs_by_competition(competition_id):
    clubs = None

    while clubs is None:
        clubs = get_competition_clubs(competition_id)
        if clubs is None:
            print(f"Error searching clubs from competition with ID: {competition_id}.")

    approved_clubs = []

    for club in clubs:
        check = None

        while check is None:
            check = get_club_profile(club[ID])
            if check is None:
                print(f"Error getting profile from club with ID: {club[ID]}.")

        if check["currentMarketValue"][-1] == 'n':
            approved_clubs.append(club)
        elif check["currentMarketValue"][-1] == 'm':
            price = remove_letters(check["currentMarketValue"]) * 10000
            if price > MIN_PRICE_CLUB:
                approved_clubs.append(club)
            else:
                break
        else:
            break

    return approved_clubs


def filter_clubs(competition_name):
    approved_clubs = []

    result = None

    while result is None:
        result = search_competition(competition_name)
        if result is None:
            print(f"Error searching competition with name: {competition_name}.")
        else:
            approved_clubs = filter_clubs_by_competition(result[0][ID])

    return approved_clubs


# TODO: filter players
filtered_clubs = []

for competition in competitions:
    filtered_clubs.extend(filter_clubs(competition))

for club in filtered_clubs:
    print(get_club_players(club[ID]))
