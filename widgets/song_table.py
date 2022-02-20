import tkinter
from tkinter import ttk
from constants import style

class SongsTable(tkinter.Frame):
    def __init__(self, parent, control):
        super().__init__(parent)
        self.table_control = control

        self.create_table()
        self.table_control.create_reference_table(self.song_table)

    def create_table(self):
        self.song_table = tkinter.Listbox(self, **style.LISTBOX)
        songs = self.table_control.show_songs()
        for key, value in songs.items():
            self.song_table.insert(key, value)

        #Barra de desplazamiento vertical
        y = ttk.Scrollbar(self, orient='vertical', command=self.song_table)
        y.grid(row=0, column=1, sticky=tkinter.NS)
        self.song_table.configure(yscrollcommand=y.set)
        y.config(command=self.song_table.yview)

        self.song_table.bind("<<ListboxSelect>>", self.table_control.selected_song)
        self.song_table.grid(column=0, row=0, sticky=tkinter.NSEW)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
