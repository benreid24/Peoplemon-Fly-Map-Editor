from model import towns as model
from view import util as view_util

DIRTY = False
APP = None


def init(app):
    global APP
    APP = app


def add():
    global DIRTY

    DIRTY = True
    # TODO - add
    update_view()


def delete():
    global DIRTY
    DIRTY = True
    del model.town_list[APP.get_song_list().get_selected_song()]
    update_view()


def update(town):
    global DIRTY
    DIRTY = True
    # TODO - update
    update_view()


def browse():
    global DIRTY
    DIRTY = True
    file = view_util.get_song_file()
    if file:
        APP.get_song_list().set_entry(file)


def reset():
    model.clear()
    APP.get_song_list().clear()
    clear_dirty()


def update_view():
    town_names = [town['name'] for town in model.town_list]
    APP.get_town_list().set_town_list(town_names)


def dirty_state():
    return DIRTY


def clear_dirty():
    global DIRTY
    DIRTY = False
