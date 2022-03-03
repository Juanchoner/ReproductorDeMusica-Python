'''
Clase para controlar las operaciones del reproductor
'''
import tkinter
from tkinter import filedialog
from pygame import mixer
from pathlib import Path
import os
import json

class MusicControl:
    def __init__(self):
        mixer.init()

        self.song_names = dict()
        self.pause = True
        self.name = tkinter.StringVar()
        self.create_settings()

    def show_songs(self, directory = None):
        '''
        Mustra las canciones que se encuentran dentro de la ruta 
        selecionada.

        Parametros:
        directory: Direccion de la carpeta de la cual se mostraran las 
        canciones

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

        Parametros:
        Tabla de la que de la cual se desea hacer referencia 
        '''
        self.reference_table = table

    def create_settings(self):
        '''
        Crea el archivo de configuración para guardar la ruta
        de la ultima carpeta seleccionada.
        '''
        ruta = Path(".").parent.resolve()
        check = f'{ruta}\config.json'
        if not os.path.exists(check):
            print('Creando configuración...')
            settings = {"ruta" : ""}
            with open("config.json", "w") as file_settings:
                json.dump(settings, file_settings)
        else:
            with open("config.json", "r") as route:
                load_config = json.load(route)
            print('Se a cargado la siguinete ruta {}'.format(load_config["ruta"]))
            self.show_songs(load_config["ruta"])
            self.save_directory = load_config["ruta"]
            

    def save_last_route(self, directory):
        '''
        Guarda la ultima ruta que se utilizo en un json

        Parametros:
        directory: La dirección de la ultima carpeta que de la cual se escucho música
        '''
        with open("config.json", "r") as take:
            load_config = json.load(take)
        with open("config.json", "w") as update:
            load_config["ruta"] = str(directory)
            json.dump(load_config, update)

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
            self.save_last_route(directory)
        else:
            return
        
    def play_music(self, song_route):
        '''
        Intenta reproducir la canción que ha sido selecionada en la tabla, o con 
        los botones de back o back

        Parmetros: 
        song_route: La ruta de la canción selecionada
        '''
        try:
            mixer.music.pause()
            mixer.music.load(song_route)
            mixer.music.play()
        except:
            print('Algo rato esta pasando..')

    def selected_song(self, event):
        '''
        Una vez selecionada la canción mediante la tabla esta comezará su 
        reproducción
        '''
        song = self.reference_table.get("anchor")
        self.name.set(song)
        self.play_music(f'{self.save_directory}/{song}')

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
        if back_song[0] == 0:
            return
        back_song = back_song[0] - 1
        self.name.set(self.song_names[back_song])
        self.play_music(f'{self.save_directory}/{self.song_names[back_song]}')

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
        if next_song == len(self.song_names):
            return
        self.name.set(self.song_names[next_song])
        self.play_music(f'{self.save_directory}/{self.song_names[next_song]}')

        self.reference_table.select_clear(0, 'end')
        self.reference_table.activate(next_song)
        self.reference_table.select_set(next_song)
