import json
from api import (search_competition, search_club, search_player, get_competition_clubs,
                 get_club_profile, get_club_players, get_player_profile, get_player_market_value,
                 get_player_transfers, get_player_stats)

# Filters
MIN_PRICE_CLUB = 400_000_000
MIN_PRICE_PLAYER = 50_000_000
competitions = ("LaLiga", "Premier League", "Serie A")
# Constants
ADAPT_NUMBER = 10_000
# API query constants
ID = "id"
CURRENT_MARKET_VALUE = "currentMarketValue"
MARKET_VALUE = "marketValue"
NAME = "name"


def remove_letters(string: str):
    only_numbers = ''.join(character for character in string if character.isdigit())
    return int(only_numbers)


def filter_clubs_by_competition(competition_id: str):
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

        if check[CURRENT_MARKET_VALUE][-1] == 'n':
            approved_clubs.append(club)
        elif check[CURRENT_MARKET_VALUE][-1] == 'm':
            price = remove_letters(check[CURRENT_MARKET_VALUE]) * ADAPT_NUMBER
            if price >= MIN_PRICE_CLUB:
                approved_clubs.append(club)
            else:
                break
        else:
            break

    return approved_clubs


def filter_clubs(competition_name: str):
    approved_clubs = []

    result = None

    while result is None:
        result = search_competition(competition_name)

        if result is None:
            print(f"Error searching competition with name: {competition_name}.")
        else:
            approved_clubs = filter_clubs_by_competition(result[0][ID])

    return approved_clubs


def filter_players_by_club(club_id: str):
    players = None

    while players is None:
        players = get_club_players(club_id)

        if players is None:
            print(f"Error searching players from club with ID: {club_id}.")

    approved_players = []

    for player in players:
        if MARKET_VALUE in player:
            if player[MARKET_VALUE][-1] == 'm':
                price = remove_letters(player[MARKET_VALUE]) * ADAPT_NUMBER
                if price >= MIN_PRICE_PLAYER:
                    approved_players.append(player)

    return approved_players


def filter_players(club_name: str):
    approved_players = []

    result = None

    while result is None:
        result = search_club(club_name)

        if result is None:
            print(f"Error searching players from club with name {club_name}.")
        else:
            approved_players = filter_players_by_club(result[0][ID])

    return approved_players


def update_players():
    filtered_clubs = []

    for competition in competitions:
        filtered_clubs.extend(filter_clubs(competition))

    filtered_players = []

    for club in filtered_clubs:
        filtered_players.extend(filter_players(club[NAME]))

    with open("players.json", "w") as players_file:
        json.dump(filtered_players, players_file)
