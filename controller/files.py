import os

from controller import towns as controller
from .helpers import saving as file_util
from view import util as view_util
from model import towns as model

FILENAME = 'map.db'
export_file = None


def open_towns():
    try:
        controller.reset()
        model.town_list = file_util.load_towns('map.db')
        controller.update_view()
    except:
        view_util.error('Error loading map.db. Making new one')


def save():
    file_util.save_towns('map.db', model.town_list)
    view_util.popup(
        'Heads Up',
        "Don't forget to copy map.db to Resources/Data/map.db\nAnd put the images in Resources/Media/Images/Menu"
    )
