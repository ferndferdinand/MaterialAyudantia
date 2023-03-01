fecha = input("Ingrese una fecha en el formato día/mes/año: ").lower()

#fecha = "28/02/2023"
#fecha = "28-febrero-2023"
#fecha = "28 feb 23"
#fecha = "29/feb/2023"
#fecha = "1/mar/23"

"""
Cómente las siguientes líneas de código detalladamente.
Escribir qué hacen y cuál es la justificación de que estén
construidas así.
Es decir, por qué tomamos esas subcadenas(fecha[:2], fecha[1:],etc....),
por qué definimos el separador así, y cómo ésta forma nos ayuda a validar
cualquier formato de entrada del usuario.
"""
if fecha[:2].isdigit():
    dia = fecha[:2]
    fecha = fecha[2:]
else:
    dia = fecha[:1]
    fecha = fecha[1:]

sep = fecha[0]

mes = fecha[1:fecha.find(sep,1)]
anio = fecha[fecha.find(sep,1)+1:]


#Si el mes está escrito por su nombre o su abreviatura lo cambiamos a su dígito
if mes in "enero":
    mes = 1
elif mes in "febrero":
    mes = 2
elif mes in "marzo":
    mes = 3
elif mes in "abril":
    mes = 4
elif mes in "mayo":
    mes = 5
elif mes in "junio":
    mes = 6
elif mes in "julio":
    mes = 7
elif mes in "agosto":
    mes = 8
elif mes in "septiembre":
    mes = 9
elif mes in "octubre":
    mes = 10
elif mes in "noviembre":
    mes = 11
elif mes in "diciembre":
    mes = 12
#si ningún mes coincide con su nombre o abreviatura y no es ya un dígito
#sabemos que ya está mal, lo cambiamos cambiamos por un dígito que nos invalide la fecha
elif not mes.isdigit():
    mes = 13

#Casteamos nuestras variables a datos enteros
dia = int(dia)
mes = int(mes)
anio = int(anio)

#Vairables auxiliares para validar
d = False
m = False
a = False


#Validamos que el día dado esté en su intervalo según el mes correspondiente

if mes == 4 or mes == 6 or mes == 9 or mes ==11:
    #Para los meses de 30 días
    if dia > 0 and dia <= 30:
        d = True

#La cantidad de días de febrero depende del año
if mes == 2:
    #Para años bisiestos
    if anio%4 == 0:
        if dia > 0 and dia <= 29:
            d = True
    #Para los demás años
    else:
        if dia > 0 and dia <= 28:
            d = True
#Para los meses de 31 días
else:
    if dia > 0 and dia <= 31:
        d = True

#Validamos que el mes esté en el intervalo [1,12]
if mes > 0 and mes <= 12:
    m = True

#Validamos el año
if anio > 0:
    a = True

#Si el día, el mes y año son correctos, la fecha es correcta
if d and m and a :
    print("Fecha válida")

#Si alguno es falso, la fecha es incorrecta
else:
    print("Fecha no válida")
