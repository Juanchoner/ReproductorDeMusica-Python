'''
Clase para controlar las operaciones del reproductor
'''
import tkinter
from tkinter import filedialog
from pygame import mixer
from pathlib import Path

class MusicControl:
    def __init__(self):
        mixer.init()

        self.song_names = dict()
        self.pause = True

    def show_songs(self, directory = None):
        '''
        Mustra las canciones que se encuentran dentro de la ruta 
        selecionada.
        Retorna un diccionario
        '''
        try:
            song_route = Path(directory)
            i = 0
            for song in song_route.iterdir():
                self.song_names.setdefault(i, f'{song.name}')
                i += 1
        except:
            self.song_names.setdefault(0, 'There are not songs...')    
        return self.song_names
    
    def create_reference_table(self, table):
        '''
        Se crea una referencia de la tabla deonde se muestran las canciones
        '''
        self.reference_table = table

    def select_route(self):
        '''
        Cuando se seleciona una nueva ruta borra los viejas referencias y 
        crea unas nuevas.
        '''
        directory = filedialog.askdirectory(title='Seleccione su carpeta de música')
        if len(directory) > 0:
            self.save_directory = directory
            for key, value in self.song_names.items():
                self.reference_table.delete(key, tkinter.END)
            self.song_names.clear()
            self.song_names = self.show_songs(directory)
            for key, value in self.song_names.items():
                self.reference_table.insert(key, value)
        else:
            return

    def selected_song(self, event):
        widget = event.widget
        selected = widget.curselection()
        song = self.song_names[selected[0]]
        print(song)
        try:
            mixer.music.load(f'{self.save_directory}/{song}')
            mixer.music.play()
        except:
            print('Algo rato esta pasando..')

    def pause_play(self):
        if self.pause == True:
            mixer.music.pause()
            self.pause = False
        else:
            mixer.music.unpause()
            self.pause = True