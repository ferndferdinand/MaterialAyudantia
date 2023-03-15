"""
Programa para mostrar un número al revés.
El número es ingresado por el usuario.
"""
n = input("Ingresa un número: ")


#------------------------------------------------------
#Una forma de hacerlo es obtener los caracteres del str
#por medio de sus índices, recorriendo el str de atrás
#hacia delante
backwards = ""


for i in range(len(n)-1,-1,-1):
    backwards += n[i]

print(backwards)



#------------------------------------------------------
#La otra forma de hacerlo es tomando directamente los
#caracteres del str ya que el str es un objeto iterable
backwards = ""

#c es cada caracter en n
for c in n:
    backwards = c + backwards

print(backwards)
