from api import get_player_profile
import random as rand
import json
import unicodedata as unicode

# Query constants
ID = "id"
POSITION = "position"; MAIN = "main"  # Position is a dictionary with a key named main
NAME = "name"
NATIONALITY = "citizenship"


def format_player_name(player: dict):
    if player[NAME] == "Lucas Paquetá":
        player[NAME] = "Paqueta"
    if len(player[NAME].split()) == 2:
        if player[NATIONALITY][0] == 'Brazil':
            player[NAME] = str(player[NAME].split()[0])
        if "de" in player[NAME].lower():
            index = player[NAME].lower().index("de")
            player[NAME] = player[NAME][index:].strip()
        elif "van" in player[NAME].lower():
            index = player[NAME].lower().index("van")
            player[NAME] = player[NAME][index:].strip()

    player[NAME] = player[NAME].replace("Ø", "O")
    player[NAME] = player[NAME].replace(" ", "")
    player[NAME] = player[NAME].replace("-", "")

    player[NAME] = unicode.normalize('NFKD', player[NAME]).encode('ASCII', 'ignore').decode('utf-8')

    return player


def random_player():
    with open("players.json", "rb") as players_file:
        players = json.load(players_file)

        random_index = rand.randint(0, len(players) - 1)

        player_profile = None

        while player_profile is None:
            player_profile = get_player_profile(players[random_index][ID])
            if player_profile is None:
                print(f"Error searching profile of player with name: {players[random_index][ID]}")

        player_profile = format_player_name(player_profile)

        return player_profile


while True:
    player = random_player()
    print(f"Formatted name: {player[NAME]}")
