
from funciones import *
from random import *

class Vuelo_destino:
    def __init__(self, destino:str, costo:int, asientos:list)
    self.__destino = destino
    self.__costo = costo
    self.__asientos = asientos
    self.__fechas = sample(fechas_disponibles(),10)
    self.__precioAT = float
    self.__precioAV = float

    self.set_precios()

    def set_precios(self):
        aux = []
        for asiento in self.__asientos:
            if asiento.get_tipo() not in aux:
                aux.append(asiento.get_tipo())

        self.__precioAT = self.__costo * (1 + aux[0].get_porcentaje())
        self.__precioAV = self.__costo * (1 + aux[1].get_porcentaje())


    def get_precioAT(self):
        return self.__precioAT

    def get_precioAV(self):
        return self.__precioAV
            
    
        
