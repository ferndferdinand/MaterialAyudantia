from hotel import Hotel
from usuario import Usuario
from habitacion import Habitacion
from tipoHab import TipoHab

import random as rd

#Lista con los 4 objetos de tipo de habitación
tipo = [TipoHab(1,400),TipoHab(2,550),TipoHab(3,750),TipoHab(4,1000)]

#Lista para guardar distintos objetos habitación creados de forma aleatoria
habitaciones = []
j = 0
for i in range(2):
    if i < 10:
        aux = "0"
    else:
        aux = str(i)[0]
    j += 1
    if j == 10:
        num = aux + str(j)
        j = 0
    else:
        num = aux + "0" + str(j)
    hab = rd.randrange(1)
    habitaciones.append(Habitacion(tipo[hab],num))

#Una habitación más de prueba
habitaciones.append(Habitacion(tipo[2],num))

#Objeto hotel con las habitaciones creadas (Por el momento solo 2)
hotel = Hotel(habitaciones)

#Menú de opciones para el usuario
while True:
    print("1. Ver tipos de habitaciones disponibles")
    print("2. Reservar habitación")
    print("3. Cancelar toda la reservación resevación")
    print("4. Resumen de la reservación")
    print("5. Para salir\n")
    opc = int(input("Ingrese la opción que desea consultar: "))

    if opc == 1:
        hab = hotel.tipo_habitaciones_dis()
        precio = hotel.precios()
        for i in range(len(hab)):
            print(f"{i+1}. {hab[i]} ${precio[i]}")
        print()
        
    elif opc == 2:
        pass

    elif opc == 3:
        pass

    elif opc == 4:
        pass

    else:
        break



    







    
