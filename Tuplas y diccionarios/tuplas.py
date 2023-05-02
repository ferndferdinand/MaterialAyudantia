
#-------------------------------------Tuplas--------------------------------------------
tupla1 = (1,19,7,9,2,13,7)
tupla2 = ("hola","hello","bonjour")
tupla3 = ([1,2,3,4],[5,6,7,8])
print("Tuplas ejemplos: ")
print(type(tupla1))
print(tupla1)
print(tupla2)
print(tupla3, end = "\n\n")

### Empaquetado de elementos
tupla4 = 5,8,9
print(type(tupla4), end = "\n\n")

### desempaquetado de elementos
print("Desempaquetando elementos de la tupla 4: ")
elemento_1,elemento_2,elemento_3 = tupla4
print(elemento_1)
print(elemento_2)
print(elemento_3, end = "\n\n")

### Métodos de tuplas
## Conteo e indices
print("Métodos: \n")
print("Contar la cantidad de elemento '7' en la tupla: ",tupla1.count(7))
print("índice del elemento 'hello' en la tupla: ",tupla2.index("hello"), end = "\n\n")

## Concatenacion de tuplas
print("Concatenación tupla 2 y 1: ")
print(tupla2 + tupla1, end = "\n\n")

## Repetición de tuplas
print("Operador de repetición en tupla 1: ")
print(tupla1*2, end= "\n\n")

## Acceso por medio de indices
print("Elementos por medio de índices: ")
print(tupla1[2])
print("Slices de la tupla 1: ")
print(tupla1[-1:])
print(tupla1[2:4]) 
print(tupla3[0][2], end = "\n\n") #Acceso al elemento (una lista), posteriormente acceso al elemento de la lista


### Funciones que aceptan tuplas
print("Funciones: \n")
print("Ordenar tupla: ",sorted(tupla1))
print("Sumar elementos de la tupla: ",sum(tupla1))
print("Máximo de la tupla: ",max(tupla1))
print("Mínimo de la tupla: ",min(tupla1))
print("Tamaño de la tupla: ",len(tupla1))
print("Cast de una tupla a una lista: ",list(tupla1),end= "\n\n")

## Recorrido de tuplas (estructura iterable)
print("Iterando la tupla 1:")
for i in tupla1:
    print(i)
print()

print("Funciones que regresan tuplas: ")
## enumerate
print("Enumetare: ")
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
print(type(list(enumerate(seasons))[0]),end = "\n\n")

## zip
print("zip(): ")
questions = ['name', 'favorite food', 'favorite color']
answers = ['Fernando', 'enchiladas de mole', 'olive green']
print(list(zip(questions, answers)))
print(type(list(zip(questions, answers))[0]))

#El for puede iterar más de un valor gracias a las tuplas
for q, a in zip(questions, answers):
    print(f'What is your {q}?  It is {a}.')

print()

## divmod
print("divmod: ")
print(divmod(18,3))
print(type(divmod(18,4)))

divide, residuo = divmod(19,13)
print(divide)
print(residuo)
# Equivalente a las siguientes operaciones:
divide_1 = 19//113
residuo_1 = 19%13
print(divide_1)
print(residuo_1,end = "\n\n")

print("Funciones creadas por nosotros")
## Funciones/métodos que regresan tuplas, es lo mismo que los 
#ejemplos anteriores pero creada por nosotros
def tupla():
    return 19,89,13

x, y, z = tupla()
print("Qué tipo de dato regresa esta función? ",type(tupla()), end = "\n\n")
print(x,y,z)


