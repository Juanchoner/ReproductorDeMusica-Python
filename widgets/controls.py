import tkinter
from constants import style

class ButtonsMusic(tkinter.Frame):
    def __init__(self, parent, control):
        super().__init__(parent)
        self.configure(background='red')

        self.buttons_control = control 
        self.create_buttons()
    
    def create_buttons(self):
        name_song = tkinter.Frame(self)
        name_song.grid(column=0, row=0, sticky=tkinter.EW)
        name_song.configure(background=style.BACKGROUND)
        tkinter.Label(name_song, text='Song', **style.LABELS).pack()

        buttons = tkinter.Frame(self)
        buttons.configure(background=style.BACKGROUND)
        buttons.grid(column=0, row=1, sticky=tkinter.EW)
        
        tkinter.Button(buttons, text='Atras').grid(column=0, row=0, **style.BUTTONS)
        tkinter.Button(buttons, text='Play', command=self.buttons_control.pause_play).grid(column=1, row=0, **style.BUTTONS)
        tkinter.Button(buttons, text='Siguiente').grid(column=2, row=0, **style.BUTTONS)

        buttons.columnconfigure(0, weight=1)
        buttons.columnconfigure(1, weight=1)
        buttons.columnconfigure(2, weight=1)

        self.columnconfigure(0, weight=1)
