import tkinter as tk

from controller import towns as controller
from . import util


class TownList(tk.LabelFrame):
    def _update_selected(self):
        try:
            selection = self.town_list.curselection()[0]
            if selection != self.last_selection:
                self.last_selection = selection
                self.set_entry(controller.get_town(selection))
        except:
            poop = []  # haha
        self.after(100, self._update_selected)

    def _get_town(self):
        try:
            town = {
                'name': self.town_name.get(),
                'description': self.town_desc.get(),
                'image': self.town_image.get(),
                'x': int(self.town_x.get()),
                'y': int(self.town_y.get())
            }
            return town
        except:
            util.error('Invalid input')
            return None

    def _update(self):
        town = self._get_town()
        if town:
            controller.update(town)

    def _add(self):
        town = self._get_town()
        if town:
            controller.add(town)

    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, text='Towns', height=250)

        self.add_button = tk.Button(self, text='Add', command=self._add)
        self.update_button = tk.Button(self, text='Update', command=self._update)
        self.del_button = tk.Button(self, text='Delete', command=controller.delete, background='#ff0000')
        self.add_button.grid(row=0, column=1, padx=3)
        self.update_button.grid(row=0, column=2, padx=3)
        self.del_button.grid(row=0, column=3, padx=3)

        self.town_name = tk.StringVar()
        self.town_entry = tk.Entry(self, textvariable=self.town_name)
        self.town_label = tk.Label(self, text='Name')
        self.town_label.grid(row=1, column=1)
        self.town_entry.grid(row=1, column=2)

        self.town_desc = tk.StringVar()
        self.desc_label = tk.Label(self, text='Description')
        self.desc_entry = tk.Entry(self, textvariable=self.town_desc)
        self.desc_label.grid(row=2, column=1)
        self.desc_entry.grid(row=2, column=2)

        self.town_image = tk.StringVar()
        self.image_label = tk.Label(self, text='Image')
        self.image_entry = tk.Entry(self, textvariable=self.town_image)
        self.image_label.grid(row=3, column=1)
        self.image_entry.grid(row=3, column=2)

        self.town_x = tk.StringVar()
        self.x_label = tk.Label(self, text='X')
        self.x_entry = tk.Entry(self, textvariable=self.town_x)
        self.x_label.grid(row=4, column=1)
        self.x_entry.grid(row=4, column=2)

        self.town_y = tk.StringVar()
        self.y_label = tk.Label(self, text='Y')
        self.y_entry = tk.Entry(self, textvariable=self.town_y)
        self.y_label.grid(row=4, column=3)
        self.y_entry.grid(row=4, column=4)

        self.town_list_frame = tk.LabelFrame(self)
        self.scrollbar = tk.Scrollbar(self.town_list_frame)

        self.town_list = tk.Listbox(self.town_list_frame, yscrollcommand=self.scrollbar.set, exportselection=False)
        self.town_list.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar.config(command=self.town_list.yview)
        self.town_list_frame.grid(column=0, row=0, rowspan=5, padx=3)

        self.grid(row=4, column=0, padx=3, pady=20)

        self.grid(row=1, column=0, sticky=tk.W+tk.E)

        self.last_selection = -1
        self.after(100, self._update_selected)

    def get_selected_town(self):
        return int(self.town_list.curselection()[0])

    def set_town_list(self, sl):
        self.town_list.delete(0, tk.END)
        self.town_list.selection_clear(0, tk.END)
        self.town_name.set('')
        self.town_desc.set('')
        self.town_image.set('')
        self.town_x.set('')
        self.town_y.set('')
        for s in sl:
            self.town_list.insert(tk.END, s)

    def set_entry(self, town):
        self.town_name.set(town['name'])
        self.town_desc.set(town['description'])
        self.town_image.set(town['image'])
        self.town_x.set(str(town['x']))
        self.town_y.set(str(town['y']))

    def clear(self):
        self.town_list.delete(0, tk.END)
