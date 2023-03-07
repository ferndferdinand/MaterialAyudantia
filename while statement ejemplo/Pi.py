import math #importamos librería 

#Pedimos al uusario el número de términos para calcular pi
n = int(input("Escribe el número de términos: "))

#Definición de variables
termino = 0
producto = 1
i = 0

#Para la cantidad de términos que ingresó el usuario
while i < n:
    #termino va a actualizar su valor a partir del último
    termino = math.sqrt(2+termino)
    #Se va calculando el producto de cada término calculado
    producto *= termino/2
    i += 1

#Se calcula pi
pi = 2/producto

#Se imprime pi
#chr(960) es la instrucción que devuelve la letra pi: π
print("La aproximación de", chr(960), f"con {n} términos es: {pi}" )



