class TipoHab:

    def __init__(self,capacidad:int,precio:int):
        self.__nombre = str
        self.__capacidad = capacidad
        self.__precio = precio

    
    def get_nombre(self):
        if self.__capacidad == 1:
            self.__nombre = "Habitación inidividual"
        elif self.__capacidad == 2:
            self.__nombre = "Habitación para dos personas"
        elif self.__capacidad == 3:
            self.__nombre = "Habitación para tres personas"
        else:
            self.__nombre = "Habitación para cuatro personas"
        return self.__nombre

    def get_precio(self):
        return self.__precio
