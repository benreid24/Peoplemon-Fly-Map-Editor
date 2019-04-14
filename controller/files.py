import os

import tkinter as tk

from controller import towns as controller
from .helpers import saving as file_util
from view import util as view_util
from model import towns as model

FILENAME = 'map.db'
export_file = None


def open_towns():
    if os.path.isfile(FILENAME):
        controller.reset()
        # TODO - load into model
        controller.update_view()


def save():
    # TODO - save towns
    view_util.popup(
        'Heads Up',
        "Don't forget to copy map.db to Resources/Data/map.db\nAnd put the images in Resources/Media/Images/Menu"
    )
