#Clases creadas
from hotel import Hotel
from usuario import Usuario
from habitacion import Habitacion
from tipoHab import TipoHab

#funciones adicionales
from funciones import validarFecha
from datetime import date

import random as rd

tipo = [TipoHab(1,400),TipoHab(2,550),TipoHab(3,750),TipoHab(4,1000)]

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
    #Lista de 70 habitaciones para el Hotel, el tipo de habitación es aleatorio
    habitaciones.append(Habitacion(tipo[hab],num))

habitaciones.append(Habitacion(tipo[2],num))
    

hotel = Hotel(habitaciones)


fer = Usuario("Fernando Ortega", 22, "ferd.fernando@gmail.com", "5537623552")

fecha = None

while True:
    print("1. Ver tipos de habitaciones disponibles")
    print("2. Reservar habitación")
    print("3. Cancelar toda la reservación resevación")
    print("4. Resumen de la reservación")
    print("5. Para salir\n")
    opc = int(input("Ingrese la opción que desea consultar: "))
    print()

    if opc == 1:
        hab = hotel.tipo_habitaciones_dis()
        precio = hotel.precios()
        for i in range(len(hab)):
            print(f"{i+1}. {hab[i]} ${precio[i]}")
        print()
        
    elif opc == 2:
        #índice en en la lista de los tipos de habitaciones
        hab = int(input("Ingrese el número del tipo de habitación que desea reservar: "))
        if fecha is None:
            fecha = input("Ingrese la fecha que desea reservar reservación, el el formato dd-mm-aaaa: ")
            fecha = validarFecha(fecha)
            while type(fecha) is str or fecha < date.today():
                print("Fecha inválida")
                fecha = input("Ingrese la fecha que desea reservar reservación, el el formato dd-mm-aaaa: ")
                fecha = validarFecha(fecha)
        print()
        cap = hotel.capacidad(hab)
        hotel.reservar(cap,fecha,fer)
        print()
        

    elif opc == 3:
        hotel.cancelar(fer)

    elif opc == 4:
        hotel.resumen(fer)

    else:
        break


