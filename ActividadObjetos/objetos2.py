from cancion import *
from album import *
from datetime import *

c1 = Cancion("Arcade Fire","Reflektor", "Trapped in a prism, in a prism of light...", "7:34")
c2 = Cancion("Arcade Fire","We Exist", "They're walking around...", "5:44")
c3 = Cancion("Arcade Fire","Flashbulb Eyes", "What if the camera...", "2:42")
c4 = Cancion("Arcade Fire","Here Comes the Night Time","When the sun goes down...", "6:31")
c5 = Cancion("Arcade Fire","Normal Person", "Do you like rock and roll music?...", "4:22")
c6 = Cancion("Arcade Fire","You Already Know", "We have fabulous music from...","3:59")
c7 = Cancion("Arcade Fire","Joan of Arc", "You're the one that thy used to hate...", "5:24")

canciones = [c1,c2,c3,c4,c5,c6,c7]

reflektor = Album("Arcade Fire", "Reflektor", canciones, date(2013,10,28))

# 1.
print("El método get_name() es un dato: ",type(c2.get_name()))

# 2. Hay que ingresar al código e imprimir el tipo de dato de esas variables

# 3. Hay que ingresar al código e imprimir el tipo de dato de esas variables
print("El método duracion() es un dato: ", type(c2.duracion()))

# 4.
print(c2.duracion())

# 5.
print(c2)

# 6. Hay que ingresar al código e imprimir el tipo de dato de esas variables, se imprimiría al crear el objeto

# 7. Ya vimos este dato en la pregunta 3. Ingresar al código e imprimir length en el for, se imprimiría al crear el objeto.

# 8. No, hay que ingresar al código e imprimir el tipo de dato de esas variables en cada línea, se imprimiría al crear el objeto.

# 9.
print("El método get_year() es un dato: ",type(reflektor.get_year()))

# 10. Hay que ingresar al código e imprimir el tipo de dato de esas variables.
print(type(reflektor.ver_cancion("We Exist")))

# 11.
print()
print(reflektor.ver_cancion("We exist"))

# 12.
print()
print(reflektor.ver_cancion("We Exist"))

# 13. Hay que ingresar al código e imprimir el tipo de dato de esas variables por cada una, se imprimirán al ejecutar la siguiente instrucción.
reflektor.mostrar_songs()

# 14. Hay que ingresar al código e imprimir el tipo de dato de esas variables por cada una en su respectiva línea, se imprimirán al ejecutar la siguiente instrucción.
reflektor.mostrar_songs()


# 15. Como existe el método str se puede imprimir el objeto, si no existe se imprime el id del objeto, comenten el método para ver la diferencia
print()
print(reflektor)

