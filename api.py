import requests as rq
import json
from io import BytesIO

URL = "https://transfermarkt-api.vercel.app"


def get_competition(competition_name: str):
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
    competition_id = competition_id.replace(" ", "%20")

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


# Testing
leagues = get_competition("premier league")
index = 0

for league in leagues:
    if league["name"] == "Premier League":
        break
    else:
        index += 1

clubs = get_competition_clubs(leagues[index]["id"])
print(clubs)
