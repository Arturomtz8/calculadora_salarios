import json

with open('players.json') as file:
    data = json.load(file)
    for player in data['jugadores']:
        print(player)