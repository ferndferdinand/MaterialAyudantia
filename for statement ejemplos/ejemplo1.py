"""
Programa para obtener el producto y suma de los primeros n
enteros pares o impares que el usuario ingresó
"""
n = int(input("Escribe un número entero: "))

suma = 0
producto = 1

#Se suman los primeros n impares.
#Como nuestro step va de 2 en 2, para obtener los primeros n impares debemos recorrer hasta los primeros n*2 números
for i in range(1,2*n,2):
    suma+= i
    producto *= i

#Imprimir con formato, los valores dentro de los {}, toman el valor de la variable que hace referencia
print(f"La suma den los primeros {n} impares es: {suma}")
print(f"El producto de los primros {n} impares es: {producto}",end = "\n\n")



suma = 0
producto = 1

#Se suman los primeros n pares
for i in range(2,2*n+1,2):
    suma+= i
    producto *= i

print(f"La suma den los primeros {n} pares es: {suma}")
print(f"El producto de los primros {n} pares es: {producto}",end = "\n\n")


