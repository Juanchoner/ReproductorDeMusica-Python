import tkinter
from constants import style
from screens.player import MusciPlayer

class Manager(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Reproductror de música")
        container = tkinter.Frame(self)
        container.pack(
            side=tkinter.TOP,
            fill=tkinter.BOTH,
            expand=True
        )

        container.configure(background=style.BACKGROUND)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        
        frame = MusciPlayer(container)
        frame.grid(column=0, row=0, sticky=tkinter.NSEW)