import tkinter

class ButtonsMusic(tkinter.Frame):
    def __init__(self, parent, play):
        super().__init__(parent)
        self.configure(background='red')

        self.con = True

        self.play_music = play
        self.create_buttons()
    
    def play_pause(self):
        if self.con == True:
            self.play_music(1)
            self.con = False
        else:
            self.play_music(2)
            self.con = True

    def create_buttons(self):
        tkinter.Button(self, text='Atras').grid(column=0, row=0)
        tkinter.Button(self, text='Play', command=self.play_pause).grid(column=1, row=0)
        tkinter.Button(self, text='Siguiente').grid(column=2, row=0)
