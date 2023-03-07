

#Función para determinar si un número es primo
def primo(k):
    i = 2
    while i < k:
        #Si el residuo es cero en alguna de las iteraciones el
        #número no es primo, la función devuelve Falso
        if k % i == 0:
            return False
        i += 1
        #Si ya se revisó para todos los números entre 2 y k y no
        #hubo residuos iguales a 0 entonces el número es primo,
        #la función devuelve verdadero
    else:
        return True


mersenne = 1
n = 1
#Imprimir los primos de mersenne entre 1 y 10,000
while mersenne < 10000:
    #Formula de mersenne
    mersenne = 2**n-1
    #Validamos que el mersenne sea primo con nuestra función
    #se imprime sólo si es primo
    if primo(mersenne):
        print(mersenne)
    n += 1
