import tkinter as tk

from controller import towns as controller


class TownList(tk.LabelFrame):
    def _update_selected(self):
        try:
            selection = self.town_list.curselection()[0]
            if selection != self.last_selection:
                self.last_selection = selection
                self.town_name.set(self.town_list.get(selection))
        except:
            poop = []  # haha
        self.after(100, self._update_selected)

    def _update(self):
        controller.update(self.town_name.get())

    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, text='Towns', height=250)

        self.add_button = tk.Button(self, text='Add', command=controller.add)
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

        self.town_list_frame = tk.LabelFrame(self)
        self.scrollbar = tk.Scrollbar(self.town_list_frame)

        self.town_list = tk.Listbox(self.town_list_frame, yscrollcommand=self.scrollbar.set, exportselection=False)
        self.town_list.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar.config(command=self.town_list.yview)
        self.town_list_frame.grid(column=0, row=0, rowspan=3, padx=3)

        self.grid(row=4, column=0, padx=3, pady=20)

        self.grid(row=1, column=0, sticky=tk.W+tk.E)

        self.last_selection = -1
        self.after(100, self._update_selected)

    def get_selected_song(self):
        return int(self.town_list.curselection()[0])

    def set_song_list(self, sl):
        self.town_list.delete(0, tk.END)
        self.town_list.selection_clear(0, tk.END)
        self.town_name.set('')
        for s in sl:
            self.town_list.insert(tk.END, s)

    def set_entry(self, file):
        self.town_name.set(file)

    def get_entry(self):
        return self.town_name.get()

    def clear(self):
        self.town_list.delete(0, tk.END)
