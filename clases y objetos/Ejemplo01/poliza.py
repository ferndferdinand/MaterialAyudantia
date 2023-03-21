#Clase Póliza para quizá una póliza de automovil
class Poliza:

    def __init__(self,reclamo:int,siniestro:int):
        """
        Método constructor

        Params:
            reclamo(int): Año del reclamo de la póliza
            siniestro(int): Monto del siniestro ocurrido
        Returns:
            none
        """
        self.__vigencia = 4
        self.__deducible = 2000
        self.__limite = 10000
        self.__anioEmision = 2019
        self.__anioReclamo = reclamo
        self.__siniestro = siniestro

    def set_siniestro(self,sin:int):
        """
        Método set para siniestro

        Params:
            sin(int): Monto del siniestro ocurrido
        Returns:
            none
        """
        self.__siniestro = sin

    def vigente(self):
        """
        Método para saber si una póliza aún está vigente

        Params:
            none
        Returns:
            bool: True si está vigente, False si no está vigente
        """
        return self.__anioReclamo - self.__anioEmision <= self.__vigencia

    def vig(self):
        """
        Método vig para mostrar si la póliza está vigente (str)

        Params:
            none
        Returns:
            str: "Vigente", "No vigente"
        """
        if self.vigente():
            return "Vigente"
        else:
            return "No vigente"

    def pago(self):
        """
        Método para determinar el pago de la suma asegurada

        Params:
            none
        Returns:
            int: Monto del pago que obtiene el asegurado
        """

        if self.vigente():
            
            if self.__siniestro < self.__deducible:
                return 0
            elif self.__siniestro > self.__deducible and self.__siniestro < self.__limite:
                return self.__siniestro - self.__deducible
            else:
                return self.__limite - self.__deducible
        else:
            return 0

    def __str__(self):
        """
        Método str, para imprimir los datos de la clase

        Params:
            none
        Returns:
            str: Datos de la póliza, y pago al asegurado
        """
        return "Vigencia de la póliza: " + str(self.__vigencia) + " años" + \
               "\nEstatus vigencia: " + self.vig() + \
               "\nDeducible: $" + str(self.__deducible) + \
               "\nLímite de póliza: $" + str(self.__limite) + \
               "\nSinistro ocurrido: $" + str(self.__siniestro) + \
               "\n\nPago: $" + str(self.pago())
    

#Objetos de la clase Poliza con diferentes años de reclamo y montos de siniestro
poliza1 = Poliza(2023,13000)
poliza2 = Poliza(2024,13000)
poliza3 = Poliza(2022,1500)
poliza4 = Poliza(2021,9000)

#Imprimimos los objetos
print("Póliza 1: ",poliza1,sep="\n", end="\n\n\n")
print("Póliza 2: ",poliza2,sep="\n", end="\n\n\n")
print("Póliza 3: ",poliza3,sep="\n", end="\n\n\n")
print("Póliza 4: ",poliza4,sep="\n", end="\n\n\n")





