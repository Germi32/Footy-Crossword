import requests as rq
import json

# TODO: check to change API (maybe)
URL = "https://transfermarkt-api.vercel.app"
# TODO: add query constants


# Competitions
def search_competition(competition_name: str):
    competition_name = competition_name.replace(" ", "%20")

    response = rq.get(URL + f"/competitions/search/{competition_name}")

    if response.status_code == 200:
        competitions = json.loads(response.content)
        result = competitions["results"]

        if len(result) != 0:
            return result
        else:
            return None
    else:
        return None


def get_competition_clubs(competition_id: str):
    response = rq.get(URL + f"/competitions/{competition_id}/clubs")

    if response.status_code == 200:
        clubs = json.loads(response.content)
        result = clubs["clubs"]

        if len(result) != 0:
            return result
        else:
            return None
    else:
        return None


# Clubs
def search_club(club_name: str):
    club_name = club_name.replace(" ", "%20")

    response = rq.get(URL + f"/clubs/search/{club_name}")

    if response.status_code == 200:
        clubs = json.loads(response.content)
        result = clubs["results"]

        if len(result) != 0:
            return result
        else:
            return None
    else:
        return None


def get_club_profile(club_id: str):
    response = rq.get(URL + f"/clubs/{club_id}/profile")

    if response.status_code == 200:
        profile = json.loads(response.content)

        return profile
    else:
        return None


def get_club_players(club_id: str):
    response = rq.get(URL + f"/clubs/{club_id}/players")

    if response.status_code == 200:
        players = json.loads(response.content)
        result = players["players"]

        return result
    else:
        return None


# Players
def search_player(player_name: str):
    response = rq.get(URL + f"/players/search/{player_name}")

    if response.status_code == 200:
        players = json.loads(response.content)
        result = players["results"]

        if len(players) != 0:
            return result
        else:
            return None
    else:
        return None


def get_player_profile(player_id: str):
    response = rq.get(URL + f"/players/{player_id}/profile")

    if response.status_code == 200:
        profile = json.loads(response.content)

        return profile
    else:
        return None


def get_player_market_value(player_id: str):
    response = rq.get(URL + f"/players/{player_id}/market_value")

    if response.status_code == 200:
        result = json.loads(response.content)

        market_value_history = result["marketValueHistory"]
        ranking = result["ranking"]
        
        return market_value_history, ranking
    else:
        return None


def get_player_transfers(player_id: str):
    response = rq.get(URL + f"/players/{player_id}/transfers")

    if response.status_code == 200:
        result = json.loads(response.content)
        transfers = result["transfers"]

        return transfers
    else:
        return None


def get_player_stats(player_id: str):
    response = rq.get(URL + f"/players/{player_id}/stats")

    if response.status_code == 200:
        result = json.loads(response.content)
        stats = result["stats"]

        return stats
    else:
        return None
