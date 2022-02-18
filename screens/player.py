import tkinter
from constants import style
from control.music_control import MusicControl
from widgets.song_table import SongsTable
from widgets.controls import ButtonsMusic

class MusciPlayer(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.control = MusicControl()
        
        self.create_widgets()

    def create_widgets(self):
        tkinter.Label(self, text="Música", justify=tkinter.CENTER,**style.TITLE).pack(side = tkinter.TOP, fill = tkinter.BOTH, padx = 10, pady = 5)

        tkinter.Button(self, text="Selecionar carpeta", command=self.control.select_route).pack()

        content = tkinter.Frame(self)
        content.configure(background=style.BACKGROUND)
        content.pack(
            side = tkinter.TOP,
            fill = tkinter.BOTH,
            expand = True,
            padx = 10,
            pady = 5
        )

        SongsTable(content, self.control).grid(column=0, row=0, sticky=tkinter.NSEW)
        ButtonsMusic(content, self.control).grid(column=0, row=1, sticky=tkinter.NSEW)

        content.grid_columnconfigure(0, weight=1)
        content.grid_rowconfigure(0, weight=1)
        content.grid_rowconfigure(1, weight=0)


