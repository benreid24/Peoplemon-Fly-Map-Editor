import json

town_list = []
TOWN_TEMPLATE = {
    'name': 'town name',
    'description': 'town description',
    'image': 'file of image for town',
    'x': 'x pos on map screen',
    'y': 'y pos on map screen'
}


def clear():
    global town_list

    town_list = []


def add_town(town):
    global town_list

    town_list.append(town)
