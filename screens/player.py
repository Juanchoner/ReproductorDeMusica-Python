import tkinter
from tkinter import filedialog
from pygame import mixer
from constants import style
from widgets.song_table import SongsTable
from widgets.controls import ButtonsMusic
from pathlib import Path

class MusciPlayer(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        
        mixer.init()

        self.music_directory = f'Seleccione una carpeta de música....'
        self.dict_songs = self.show_songs()
        self.create_widgets()
    
    def select_route(self):
        route = filedialog.askdirectory(title="Seleciona la carpeta de música")
        if len(route) > 0:
            print(f'Carpeta selecionada {route}')
            self.dict_songs = self.show_songs(route)
            self.update_table(1)
            self.update_table(0)
        else:
            print('Carpeta no selecionada')
    
    def music_play_table(self, ruta):
        '''Reproduce la canción selecionada en la tabla
        Argumento:
            ruta: La ruta donde se encuentra la canción a reproducir'''
        mixer.music.load(ruta)
        mixer.music.play()

    def music_controllers(self, control):
        '''Controla la reproducción
        Argumentos:
            control: La señal que se mandan los controles, para ejecutar una acción 
            en especifico
        '''
        if control == 1:
            mixer.music.pause()
        if control == 2:
            mixer.music.unpause()
    
    def show_songs(self):
        '''Mustra las canciones que se encuentran dentro de la ruta 
        selecionada.
        Retorna un diccionario'''
        try:
            route = Path(self.music_directory)
            songs_name = dict()
            i = 0
            for file in route.iterdir():
                songs_name.setdefault(i, f'{file.name}')
                i += 1
            return songs_name
        except:
            return {0: 'Seleccione una carpeta de música...'}

    
    def create_widgets(self):
        tkinter.Label(self, text="Música", justify=tkinter.CENTER,**style.TITLE).pack(side = tkinter.TOP, fill = tkinter.BOTH, padx = 10, pady = 5)

        tkinter.Button(self, text="Selecionar carpeta", command=self.select_route).pack()

        content = tkinter.Frame(self)
        content.configure(background=style.BACKGROUND)
        content.pack(
            side = tkinter.TOP,
            fill = tkinter.BOTH,
            expand = True,
            padx = 10,
            pady = 5
        )

        SongsTable(content, self.music_directory, self.dict_songs, self.music_play_table).grid(column=0, row=0, sticky=tkinter.NSEW)
        ButtonsMusic(content, self.music_controllers).grid(column=0, row=1, sticky=tkinter.NSEW)

        content.grid_columnconfigure(0, weight=1)
        content.grid_rowconfigure(0, weight=1)
        content.grid_rowconfigure(1, weight=0)


