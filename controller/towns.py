from model import towns as model

DIRTY = False
APP = None


def init(app):
    global APP
    APP = app


def add(town):
    global DIRTY

    DIRTY = True
    model.add_town(town)
    update_view()


def delete():
    global DIRTY
    DIRTY = True
    del model.town_list[APP.get_town_list().get_selected_town()]
    update_view()


def update(town):
    global DIRTY
    DIRTY = True
    model.town_list[APP.get_town_list().get_selected_town()] = town
    update_view()


def get_town(index):
    return model.town_list[index]


def reset():
    model.clear()
    APP.get_town_list().clear()
    clear_dirty()


def update_view():
    town_names = [town['name'] for town in model.town_list]
    APP.get_town_list().set_town_list(town_names)


def dirty_state():
    return DIRTY


def clear_dirty():
    global DIRTY
    DIRTY = False
