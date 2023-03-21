#Ax^2 +Bxy + Cy^2 +Dx +Ey + F = 0

class EcuacionGeneral:

    def __init__(self,A:int,B:int,C:int,D:int,E:int,F:int):

        """
        Método constructor de la clase

        Params:
            A(int): coeficiente A de la ecuación general de segundo grado
            B(int): coeficiente B de la ecuación general de segundo grado
            C(int): coeficiente C de la ecuación general de segundo grado
            D(int): coeficiente D de la ecuación general de segundo grado
            E(int): coeficiente E de la ecuación general de segundo grado
            F(int): coeficiente F de la ecuación general de segundo grado

        Returns:
            none
        """
        self.__A = A
        self.__B = B
        self.__C = C
        self.__D = D
        self.__E = E
        self.__F = F

    def __coef(self,coef):
        """
        Método privado coef para obtener los coeficiente que debe llevar la ecuación

        Params:
            coef(int): coeficiente del término
        Returns:
            str: En caso de no ser cero
            int: 0 En caso de ser cero
        """
        if coef == 0:
            return 0
        elif coef == 1:
            return "+"
        elif coef == -1:
            return "-"
        elif coef > 0:
            return "+" + str(coef)
        else:
            return str(coef)
        

    def eqcGeneral(self):
        """
        Método para armar la ecuación con los coeficientes dados

        Params:
            none
        Returns:
            str: la ecuación general
        """
        ecuacion = ""
        aux = self.__coef(self.__A)
        if type(aux) is str:
            if aux[0] == "+":
                ecuacion += aux[1:] + "x^2"
            else:
                ecuacion += aux + "x^2"
                
        aux = self.__coef(self.__B)
        if type(aux) is str:
            ecuacion += aux + "xy"

        aux = self.__coef(self.__C)
        if type(aux) is str:
            ecuacion += aux + "y^2"

        aux = self.__coef(self.__D)
        if type(aux) is str:
            ecuacion += aux + "x"

        aux = self.__coef(self.__E)
        if type(aux) is str:
            ecuacion += aux + "y"

        aux = self.__coef(self.__F)
        if type(aux) is str:
            if len(aux) == 1:
                ecuacion += aux+"1"
            else:
                ecuacion += aux

        ecuacion += "=0"
        return ecuacion
    
    def get_A(self):
        """
        Método get
        Params:
            none
        Returns:
            int: Coeficiente A
        """
        return self.__A

    def get_B(self):
        """
        Método get
        Params:
            none
        Returns:
            int: Coeficiente B
        """
        return self.__B

    def get_C(self):
        """
        Método get
        Params:
            none
        Returns:
            int: Coeficiente C
        """
        return self.__C

    def get_D(self):
        """
        Método get
        Params:
            none
        Returns:
            int: Coeficiente D
        """
        return self.__D

    def get_E(self):
        """
        Método get
        Params:
            none
        Returns:
            int: Coeficiente E
        """
        return self.__E

    
    def get_F(self):
        """
        Método get
        Params:
            none
        Returns:
            int: Coeficiente F
        """
        return self.__F

    def conica(self):

        """
        Método para obtener qué cónica es

        Params:
            none

        Returns:
             str: La cónica correspondiente
        """
        discriminante = self.__B**2 - 4*self.__A*self.__C
        
        if discriminante < 0:
            if self.__A == self.__C:
                return "Circunferencia"
            else:
                return "Elipse"
        elif discriminante == 0:
            return "Parábola"
        elif discriminante > 0:
            return "Hipérbola"

    def rotar(self):
        """
        Método para eliminar el término xy si existe
        """
        pass

    def trasladar(self):
        """
        Método para eliminar el términos 'x' y 'y' si existen
        """
        pass
    
    def focos(self):
        """
        Método para encontrar los puntos donde se encuentran los focos

        #Podríamos usar la clase punto y regresar un objeto Punto()
        """
        pass

    def centro(self):
        """
        Método para encontrar el punto del centro de la cónica

        #Podríamos usar la clase punto y regresar un objeto Punto()
        """
        pass
    
    def vertices(self):
        """
        Método para encontrar los puntos donde se encuentran los vértices

        #Podríamos usar la clase punto y regresar un objeto Punto()
        """
        pass

    def valor_a(self):
        """
        Método para calcular el valor a (distancia del centro al vértice)
        """
        pass

    def valor_b(self):
        """
        Método para calcular el valor b (por pitágoras con a y c)
        """
        pass

    def valor_c(self):
        """
        Método para calcular el valor c (distancia del centro al foco)
        """
        #Para estos métodos que se calcula la distancia podríamos usar el método de dintancia
        #entre dos puntos de la clase Punto()
        pass
    

    def ecuacion(self):
        """
        Método para acomodar la ecuación dependiendo de la cónica.

        Returns:
            str: Ecuación de la cónica
        """
        pass

    def directriz(self):
        """
        Método para calcular la ecuación de la directriz

        Returns:
            str: Ecuación
        """
        pass
    
    def asintotas(self):
        """
        Método para calcular las ecuaciones de las asintotas de la hipérbola
        """
        pass

    def excentricidad(self):
        """
        Método para calcular la excentricidad de la cónica

        Returns:
            float: Excentricidad
        """
        pass

    def __str__(self):
        """
        Método str, imprime nuestros datos de la clase
        Params:
            none
        Returns:
            str
        """
        return "Ecuación: " +self.eqcGeneral() + \
               "\nCónica: " + self.conica() #Agregar focos, directriz, etc.
    
        

eq1 = EcuacionGeneral(5,-9,6,-9,-9,-19)
eq2 = EcuacionGeneral(5,0,-5,12,-9,0)
eq3 = EcuacionGeneral(2,-4,2,13,7,28)
eq4 = EcuacionGeneral(3,0,3,-10,-9,1)

print(eq1, end = "\n\n")
print(eq2, end = "\n\n")
print(eq3, end = "\n\n")
print(eq4, end = "\n\n")







