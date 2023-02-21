"""
Función print
"""
variable1 = 5
variable2 = 10

print("Ejemplo 1: ")
#Se imprime los valores de las variables en la misma línea (sep = " ") default
print(variable1, variable2)

#Lo siguiente en la pantalla se imprime después de un salto de línea (end = "\n") default
#Se imprime el resultado de la suma
print(variable1 + variable2)

print("\nEjemplo 2: ")
#Se imprime los valores de las variables sin separación,
#lo siguiente en la pantalla se imprime después de dos saltos de línea
print(variable1, variable2, sep = "",end ="\n\n")
print(variable1 + variable2)

print("\nEjemplo 3: ")
#Se imprime los valores de las variables con un salto de línea
#lo siguiente en la pantalla se imprime después de un espacio
print(variable1, variable2, sep = "\n",end = " ")
print(variable1 + variable2)

"""
Print con formato
"""

x = 5
y = 8
print(f"El resultado de {x} + {y} = ", x+y)

"""
Función input
"""

print("\n\nEjemplo 1: ")
#Se abre el espacio para ingresar datos
variable3 = input()
print(type(variable3))

print("\nEjemplo 2: ")
#Se abre el espacio para ingresar datos con la instrucción
variable3 = input("Ingresa un valor: ")
print(type(variable3))

#Se imprime el 5 veces (valor de variable1), el str que se ingresó
print("El operador * funciona con tipos de datos distintos ",variable3*variable1)


print("\nEjemplo 3: ")
#Se convierte el valor ingresado en un dato entero (int) de ser posible
variable3 = int(input("Ingresa un valor: "))
print(type(variable3))
#Se imprime el prodeucti de variable1 con el valor ingresado
print(variable3," * ", variable1, " = " ,variable3*variable1, end = "\n\n\n")


"""
Operadores aritméticos
"""
x = 3
y = 2
print(f"x = {x}, y = {y}")
print("Suma de x + y = ", x+y)
print("Resta de x - y = ",x-y)
print("Producto de x * y = ",x*y)
print("División de x / y = ",x/y)
print("Residuo de x / y = ",x%y)
print("Parte entera de x / y = ",x//y)
print("Potencia de x^y = ",x**y, end = "\n\n")

exp1 = (2**5-13//2) < (2*3**4-146.5) or (5/2 == 22//6)  
print(exp1, end = "\n\n\n")

"""
Operadores de comparación
"""
x = 13
y = 19
z = 13
print(f"¿{x} es igual que {y}? ", x == y)
print(f"¿{x} es distinto que {y}? ", x != y)
print(f"¿{x} es menor que {y}? ", x < y)
print(f"¿{x} es mayor que {y}? ",x > y)
print(f"¿{x} es menor o igual que {z}? ",x <= z)
print(f"¿{x} es mayor o igual que {y}? ", x >= y)
