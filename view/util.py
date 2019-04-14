import os

import tkinter.messagebox as mbox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter as tk


def popup(title, message):
    mbox.showinfo(title, message)


def error(message):
    mbox.showerror('Error', message)


def yesnobox(question):
    return mbox.askyesno('WTF', question) == tk.YES


def get_song_file():
    file = askopenfilename(
        title='Add Song',
        filetypes=[
            ('Songs', '*.ogg')
        ]
    )
    return os.path.basename(file)


def get_open_file(folder=''):
    return askopenfilename(
        title='Open Playlist',
        filetypes=[('Playlist', '*.plst')],
        initialdir=folder
    )


def get_save_file(folder=''):
    return asksaveasfilename(
        title='Save Playlist',
        defaultextension='.plst',
        filetypes=[('Playlist', '*.plst')],
        initialdir=folder
    )
