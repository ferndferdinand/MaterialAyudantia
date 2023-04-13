class Usuario:

     def __init__(self, name:str, age: int, email:str, tel: str):
         self.__nombre = name
         self.__edad = age
         self.__correo = email
         self.__telefono = tel
         self.__habitaciones = []
         self.__fechaRes = None

     def reservarHab(self,hab,fecha):
          self.__habitaciones.append(hab)
          self.__fechaRes = fecha

     def get_habitaciones(self):
          return self.__habitaciones

     def get_fecha(self):
          return self.__fechaRes

     def cancelar(self,hab):
          self.__habitaciones.remove(hab)

     def totalHab(self):
          total = 0
          for hab in self.__habitaciones:
               total += hab.get_tipo().get_precio()
          return total

     def __str__(self):
          habs = ""

          for hab in self.__habitaciones:
               habs += hab.__str__()+ "\n\n"
               
          return f"Reservación para el {self.__fechaRes} \n" +\
                 "Nombre: " + self.__nombre + "\n" +\
                 "Edad: " + str(self.__edad) + "\n" +\
                 "Correo: " + self.__correo + "\n" +\
                 "Telefono: " + self.__telefono + "\n\n"+\
                 habs +\
                 f"Total: ${self.totalHab()}" + "\n\n"
          
          
          
     

    
