"""
Podemos importar todo el archivo con:

import Factorial

Y para usar la función necesaria sólo la llamamos con un .
Factorial.factorial(n)

Por lo general cuando necesitamos varias funciónes que alojamos en un mismo archivo
"""
#import Factorial

"""
Podemos importar sólo una función del archivo con:

from Factorial import factorial

y llamar a la función directamente:  factorial(n)
"""
from Factorial import factorial


n = int(input("Ingresa el entero al que quieres calcularle el factorial: "))
print(f"\nEl factorial de {n} = ", factorial(n))
