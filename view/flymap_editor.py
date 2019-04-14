import tkinter as tk

from .menu_bar import MenuBar
from .town_list import TownList


class FlymapEditor:
    def __init__(self):
        self.TK_ROOT = tk.Tk()
        self.TK_ROOT.title('Fly Map Editor')
        self.TK_ROOT.resizable(False, False)
        self.TK_ROOT.iconbitmap('resources/icon.ico')

        self.menu_bar = MenuBar(self.TK_ROOT)
        self.town_list = TownList(self.TK_ROOT)

        self.TK_ROOT.configure(menu=self.menu_bar)
        self.menu_bar.set_editor(self)

        self.TK_ROOT.update()

    def get_town_list(self):
        return self.town_list

    def get_menu(self):
        return self.menu_bar

    def mainloop(self):
        self.TK_ROOT.mainloop()
