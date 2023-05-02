
class Cancion:

    def __init__(self, artista:str, nombre:str, letra:str, duracion: str):
        self.__artist = artista
        self.__name = nombre
        self.__lyrics = letra
        self.__length = duracion

        self.set_length()

    def get_artist(self):
        return self.__artist
        
    def get_name(self):
        return self.__name

    def get_lyrics(self):
        return self.__lyrics
    
    def get_length(self):
        return self.__length

    def set_length(self):
        length = self.__length
        minuto = length[:length.find(":")]
        segundo = int(length[length.find(":")+1:])
        self.__length = minuto + ":" + f"{segundo:02d}"

    def duracion(self):
        length = self.__length
        minuto = int(length[:length.find(":")])
        segundo = int(length[length.find(":")+1:])
        return minuto*60 + segundo
        
    def __str__(self):
        return f"Artista: {self.__artist}\n"+\
               f"Nombre: {self.__name}\n" +\
               f"Duración: {self.__length}\n" +\
               f"Letra: {self.__lyrics}"
