## ----------------------------Diccionarios-----------------------------------------
# es parte de las estructuras de datos por defecto en python. Esta estructura
# es desordenada, puede modificarse y funciona con llaves y valores (key/value)
# En un diccionario pueden repetirse los valores pero las llaves deben ser unicas
# los diccionarios se crean utilizando llaves 


diccionario = {1 : 3, "palabra": 'hola',"lista":[1,2,3,4,5]}

#Mostrar el diccionario
print(diccionario)
#Acceso al valor de la llave '1'
print(diccionario[1])
#Acceso al valor de la llave 'palabra'
print(diccionario["palabra"])
#Acceso al valor de la llave 'lista'
print(diccionario["lista"])
#Acceso a un elemento del valor de la llave 'lista' (list)
print(diccionario["lista"][2])
#Agregar valor
diccionario["Nuevo valor"] = 19
print(diccionario)
#Si la llave ya existía sólo se modifica el valor 
#Modificando valor de la llave '1'
diccionario["palabra"] = "Hello"
print(diccionario, end = "\n\n")

#Iterando
print("Iterando diccionario")
for i in diccionario.items():
    print(i) # imprime los elementos como tuplas
    print(type(i))
print()

### Métodos del diccionario


print("Método keys(): ")
llaves = diccionario.keys()
print(llaves)
print(list(llaves),end = "\n\n")

print("Método values():")
valores = diccionario.values()
print(valores)
print(list(valores), end = "\n\n")

print("Método items():")
elementos = diccionario.items()
print(elementos)
print(list(elementos))
print(list(elementos)[2])
print(type(list(elementos)[2]),end ="\n\n")

print("Método get():")
print(diccionario.get("palabra"))
print(diccionario.get("key"))
print(diccionario.get("1", "Elemento no encontrado"), end = "\n\n")

print("Método pop():")
print(diccionario.pop(1))
print(diccionario)
print(diccionario.pop(1,"No encontado"))

print("Método clear()")
diccionario.clear()
print(diccionario, end = "\n\n")

print("Método setdefault()")
d = {'uno': 1, 'dos': 2}
d.setdefault('uno', 1.0)
print(d)
d.setdefault('tres', 3)
print(d)
d.setdefault('cuatro')
print(d, end ="\n\n")

print("Método update()")
#Dos diccionarios
my_dict = {"nombre": "Fernando", "edad": 20, "profesion": "actuario (según)"}
additional_info = {"ciudad": "CDMX", "lenguajes": ["Python", "Java", "R"]}
#Actulizamos el primer diccionario agregando los datos del segundo
my_dict.update(additional_info)

print(my_dict, end = "\n\n")

## Funciones que regresan diccionarios
print("Función dict():")
print(dict(valor_1 = 1, valor_2 = 2))
print(dict([("Valor 1", 1),("Valor 2",2)]),end ="\n\n")

from collections import Counter

print("Función Counter():")
lista = [19,21,13,89,2,4,2,1,3,45,2,1,19,19,12,21,13,2,2,3,4,2,2]
print(Counter(lista))



    




