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
        self.name = tkinter.StringVar()

    def show_songs(self, directory = None):
        '''
        Mustra las canciones que se encuentran dentro de la ruta 
        selecionada.
        Retorna un diccionario el cual contiene las canciones
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
        song = self.reference_table.get("anchor")
        self.name.set(song)
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

    def back_song(self):
        '''
        Al dar clic en el botón "Back"  se escuchara la canción 
        anterior
        '''
        back_song = self.reference_table.curselection()
        back_song = back_song[0] - 1
        self.name.set(self.song_names[back_song])
        try:
            mixer.music.load(f'{self.save_directory}/{self.song_names[back_song]}')
            mixer.music.play()
        except:
            print('Algo rato esta pasando..')

        self.reference_table.select_clear(0, 'end')
        self.reference_table.activate(back_song)
        self.reference_table.select_set(back_song)

    def next_song(self):
        '''
        Al dar clic en el botón "Next" se escuchara la canción 
        siguiente
        '''
        next_song = self.reference_table.curselection()
        next_song = next_song[0] + 1
        self.name.set(self.song_names[next_song])

        try:
            mixer.music.load(f'{self.save_directory}/{self.song_names[next_song]}')
            mixer.music.play()
        except:
            print('Algo rato esta pasando..')

        self.reference_table.select_clear(0, 'end')
        self.reference_table.activate(next_song)
        self.reference_table.select_set(next_song)
