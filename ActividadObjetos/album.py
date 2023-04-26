from datetime import *
class Album:

    def __init__(self, artista:str, nombre:str, canciones:list, fecha:object):
        self.__artist = artista
        self.__name = nombre
        self.__songs = canciones
        self.__date = fecha
        self.__length = str 
        
        self.set_length()

    def get_artist(self):
        return self.__artist

    def get_name(self):
        return self.__name

    def get_songs(self):
        return self.__songs

    def get_date(self):
        return self.__date

    def get_length(self):
        return self.__length

    def set_length(self):
        length = 0
        for song in self.__songs:
            length += song.duracion()

        horas = length//3600
        minutos = (length%3600)//60
        segundos = length%3600%60

        if horas > 0:
            length = str(horas) + ":" + f"{minutos:02d}" + ":" + f"{segundos:02d}"
        else:
            length = f"{minutos:02d}" + ":" + f"{segundos:02d}"
            
        self.__length = length 
    
    def get_year(self):
        year = self.__date.year
        return year

    def ver_cancion(self,nombre:str):
        for song in self.__songs:
            if song.get_name() == nombre:
                return song
        return f"No existe la canción {nombre} en {self.__name}"
        

    def mostrar_songs(self):
        canciones = ""
        
        longitud = 0
        for song in self.__songs:
            if len(song.get_name()) > longitud:
                longitud = len(song.get_name())
        longitud += 3
        
        for i, song in enumerate(self.__songs,start = 1):
            space1 = longitud - len(song.get_name())
            space1 = " "*space1
            space2 = ""
            if i < 10:
                space2 = " "
            canciones += str(i) + ". " + space2 + song.get_name() + space1 + song.get_length() +"\n"
        return canciones
    

    def __str__(self):
        return f"{self.__artist}\n"+\
               f"{self.__name} ({self.get_year()})\n\n"+\
               self.mostrar_songs()+\
               f"\nDuración: {self.__length}"
               
        
        

    
        
