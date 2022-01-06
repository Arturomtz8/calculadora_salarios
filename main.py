import json
import pandas as pd


def open_json(file_name):
    with open(file_name) as file:
        data = json.load(file)
        return data


def convert_into_dataframe():
    data = open_json("players.json")
    df = pd.DataFrame(data['jugadores'])

    return df
     