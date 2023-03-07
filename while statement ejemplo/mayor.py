
#str con los números que queremos comparar
n = "12,14,27,54,43,98,13,19,29,67,88,21"

#Contamos el número de números que tenemos que comparar
num = n.count(",")
#Encontramos el primer número por medio de la ","
sep = n.find(",")
mayor = int(n[:sep])

i = 0
#Usamos while para comparar cada número
while i < num:
    #nuestro str n, empieza a partir del siguiente número
    n = n[sep+1:]
    sep = n.find(",")
    #Si llegamos al último número no habrá más "," entonces sep = -1
    if sep != -1:
        valor = int(n[:sep])
    else:
        #último valor de n
        valor = int(n)
    #Si el número que comparamos es menor que le otro entonces lo actualizamos
    if mayor < valor:
        mayor = valor
    #Aumentamos iterador
    i += 1

#Imprimimos el mayor número de nuestro str
print(f"El número más grande es: {mayor}")




"""
Otra forma de hacerlo, por medio de una función iterativa
"""
#función para obetener el valor del str
def Valor(n):
    sep = n.find(",")
    #Si llegamos al último número no habrá más "," entonces sep = -1
    if sep != -1:
        valor = int(n[:sep])
    else:
        #último valor de n
        valor = int(n)
    #nuestro str n, empieza a partir del siguiente número
    n = n[sep+1:]
    #Regresamos el valor separado y el resto del str
    return valor, n


#La función recibe un str n con los números a comparar y el número mayor
def numMayor(n, mayor = 0):
    num = n.count(",")
    #Obtenemos el valor a comparar y el nuevo str
    valor, n = Valor(n)

    if mayor < valor:
        mayor = valor
    #i no cambia su valor dado que quien cambia es num (se reduce)
    i = 1
    #Llamamos a la misma función hasta que hayamos comparado todos los números en n
    if i <= num:
        mayor = numMayor(n,mayor)
    #Regresamos el mayor número
    return mayor

n = "12,14,27,54,43,98,13,19,29,67,88,21"
mayor = numMayor(n)

print("El número más grande es:", mayor)
