
"""
Programa para mostrar los números naturales
perfectos entre 1 y 1000
"""

#Recorremos cada número entre 1 y 1000
for i in range(1,1000):
    suma = 0
    #Del número i en que nos encontramos varificamos si
    #los números anteriores son divisores de i
    for j in range(1,i):
        #Si algún número es divisor de i lo sumamos
        if i % j == 0:
            suma += j
    #Si la suma de los divisores es igual a i entonces i es
    #un número natural perfecto
    if suma == i:
        print(f"{i} es natural perfecto")
