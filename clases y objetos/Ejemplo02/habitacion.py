from tipoHab import TipoHab


class Habitacion:

    def __init__(self):
        self.__tipoHab = TipoHab()
        self.__status = bool
        self.__numHab = str
        self.__piso = str


    def set_status(self):
        self.__status = not self.__status

    def get_numHab(self):
        return self.__numHab
    
    def get_statys(self):
        return self.__status

    def get_piso(self):
        if self.__numHab[0] == "0":
            self.__piso = "Planta baja"
        elif self.__numHab[0] == "1":
            self.__piso = "Pirmer piso"
        else:
            self.__piso = "Segundo piso"
            
        return self.__piso

    def tipo(self):
        return self.__tipoHab.get_nombre()

    def precio(self):
        return self.__tipoHab.get_precio()




        










        
