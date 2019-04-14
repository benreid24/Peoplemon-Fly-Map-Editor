import json

town_list = []
TOWN_TEMPLATE = {
    'disp_name': 'town display name',
    'ref_name': 'reference name for map visited',
    'description': 'town description',
    'image': 'file of image for town',
    'x': 'x pos on map screen',
    'y': 'y pos on map screen',
    'map_name': 'name of map to load',
    'spawn': 'spawn number in map'
}


def clear():
    global town_list

    town_list = []


def add_town(town):
    global town_list

    town_list.append(town)
