
#Función factorial
#Uso de docstring
def factorial(n:int):
    """

    Calcula el factorial de un número entero n. (n!)

    Params:
        n (int): Valor entero

    Returns:
        fac (int): El factorial calculado
        
    """
    fac = 1
    
    for i in range(n,1,-1):
        fac *= i
        
    return fac



