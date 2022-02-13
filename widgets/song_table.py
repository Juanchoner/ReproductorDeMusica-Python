import tkinter
from constants import style

class SongsTable(tkinter.Frame):
    def __init__(self, parent, route, songs, play):
        super().__init__(parent)

        self.route_songs = route
        self.play_song = play
        self.songs_name = songs
        self.create_table()

    def selected_song(self, event):
        widget = event.widget
        selected = widget.curselection()
        song = self.songs_name[selected[0]]
        route = f'{self.route_songs}/{song}'
        try:
            self.play_song(route)
        except:
            print(self.route_songs)

    def create_table(self):
        self.song_table = tkinter.Listbox(self, **style.LISTBOX)
        for key, value in self.songs_name.items():
            self.song_table.insert(key, value)

        self.song_table.bind("<ButtonRelease-1>", self.selected_song)
        self.song_table.grid(column=0, row=0, sticky=tkinter.NSEW)

        self.grid_columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
    