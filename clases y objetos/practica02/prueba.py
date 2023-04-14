
from tipoAsi import TipoAsiento
from asiento import Asiento
from destino import Vuelo_destino

#Dos tipos de asiento (2 objetos)
#Tradicional, #VIP
tipoAsiento = [TipoAsiento(), TipoAsiento("VIP",0.50)]

#50 asientos, 30 tradicionales, 20 vip
asientos = []
j = 0
for i in range(50):

    if i <= 30:
        aux = "T"
        tipo = tipoAsiento[0]
    else:
        aux = "V"
        tipo = tipoAsiento[1]

    j += 1
    if j >= 10 and j <= 30:
        num = aux + str(j)
    elif j > 30:
        j = 0
        continue
    else:
        num = aux + "0"+ str(j)

    asientos.append(Asiento(tipo,num))
    
    copia1 = asientos.copy

#Tres destinos (3 objetos)
destinos = [Vuelo_destino("Hawaii",14000,copia1),
            Vuelo_destino("Cancún",7000,asientos),\
            Vuelo_destino()]

vuelo = Vuelos(destinos)

"""
1. Hawaii

Fechas disponibles:
2023-04-14
2023-04-17
2023-05-01
2023-04-16

Asientos:
Tradicional: $15400.00
VIP: $21000.00

2. Cancún
Fechas disponibles:
2023-04-14
2023-04-17
2023-05-01
2023-04-16

Asientos:
Tradicional: $15400.00
VIP: $21000.00

"""


while True:
    print("1. Ver los destinos disponibles")
    print("2. Reservar destino")
    print("3. cancelar destino")
    print("4. Resumen vuelo")
    op = int(input("Ingresa una opción: "))

    if op == 1:
        print("Destinos diponibles.")
        vuelo.mostrarDestinos()
    elif op == 2:
        destino = int(input("Selecciona el destino: "))
        fecha = input("")
        asiento = input("")
        vuelo.reservar(destino, fecha, asiento)
    elif op == 3:
        pass
    elif op == 4:
        pass
    else:
        break

        



