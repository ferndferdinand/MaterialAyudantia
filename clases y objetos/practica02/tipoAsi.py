



class TipoAsiento:
    def __init__(self, tipo = "Tradicional", porcentaje = 0.10):
        self.__tipo = tipo
        self.__porcentaje = porcentaje

    def get_tipo(self):
        return self.__tipo
    
    def get_porcentaje(self):
        return self.__porcentaje
