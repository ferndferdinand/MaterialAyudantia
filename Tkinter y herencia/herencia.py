class SalaCine:
    """
    Clase Padre
    """
    def __init__(self):
        self.__adult = 0 #Número de boletos de adulto
        self.__child = 0 #Número de boletos de niño
        self.__experience = [False,False,False] #IMAX, 4DX, VIP (se pueden ser los tres, ninguno, algunos) se inicializa sin esto
        self.__total = 0 #Total a pagar
        
    def setAdult(self,num:int):
        self.__adult = num

    def getAdult(self):
        return self.__adult
        
    def setChild(self,num:int):
        self.__child = num

    def getChild(self):
        return self.__child

    def setExperience(self,lista:list):
        self.__experience = lista

    def getExperience(self):
        return self.__experience

    def calculo(self):
        pass

    def setTotal(self,total:float):
        self.__total = total

    def getTotal(self):
        self.calculo() #Se recalcula antes de regresarlo
        return "$ "+ "{0:.2f}".format(self.__total) #Con formato


class Formato(SalaCine):
    """
    Clase hijo
    """
    def __init__(self,formato:str, porcentaje:float):
        """
        Método constructor de la clase Formato (herencia desde la clase SalaCine)

        Params:
        formato (str): Formato de la película
        porcentaje (float): Porcentaje en que aumenta el precio según el formato

        Returns:
            None.
        """
        self.__format = formato
        self.__porcentaje = porcentaje
        super().__init__()#Llamamos método constructor para inicializar los atributos en esta clase desde la clase padre

    def getFormat(self):
        return self.__format

    def calculo(self):
        total = 0
        adultos = 80 #Precio base adulto
        ninos = 60 #Precio base niño
        
        total += adultos*self.getAdult() #Tenemos acceso a los métodos de la clase padre que no están definidos explicitamente en la clase hijo
        total += ninos*self.getChild()

        if total > 0:
            total *= 1 + self.__porcentaje #Aumento según el formato

            #Aumento si es IMAX
            if self.getExperience()[0]:
                total *= 1.55
                
            #Ayumento si es 4DX
            if self.getExperience()[1]:
                total *= 1.60

            #Aumento si es VIP
            if self.getExperience()[2]:
                total *= 1.65
            
        self.setTotal(total)

#Objetos de ambos tipos de formato 
format1 = Formato("2D", 0)
format2 = Formato("3D", 0.15)

#format1.setAdult(5)
#format2.setChild(3)
#print(format1.getTotal())
#print(format2.getTotal())
    
    
