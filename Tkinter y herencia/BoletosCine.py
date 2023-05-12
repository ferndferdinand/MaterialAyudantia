from tkinter import *
from tkinter import ttk
from herencia import *

"""
Script para crear una interfaz gráfica del usuario (GUI)
"""

#--------------------------------------raíz----------------------------------------------------------
root = Tk()
root.title("Boletos de cine")

#root.config(bg="black") #Cambio de color en la raíz para ver los tamaños de los widgets que agregamos

#--------------------------------------imagen--------------------------------------------------------
poster = PhotoImage(file='EvilDeadPoster.png').subsample(3)#Cargamos la imagen y la reducimos, importante que sea .png

imagen = ttk.Label(root,image=poster, anchor="center",background="black") #Creamos el label
imagen.pack(side=TOP,expand = True,fill = BOTH)#La ponemos en el frame1 con pack()

#--------------------------------------Cálculo del precio--------------------------------------------
#Objetos de clase tkinter. Datos variables
total = StringVar(value = '$ 0.00') #Valor inicial en 0

numAdul = IntVar(value = 0) #Valor inicial en 0
numChild = IntVar(value = 0)
formato = StringVar(value = format1.getFormat())#Se inicializa ya con una opción (2D), valor interno del radiobutton
imax = BooleanVar() 
dx = BooleanVar()
vip = BooleanVar()

#Diccionario con llaves "2D" y "3D", y valores los dos objetos creados
formatos = {format1.getFormat():format1 ,format2.getFormat():format2}

##Función para calcular el precio
def calcular(*args):
    boleto = formatos[formato.get()] #Obtenemos el objeto al que se hace refencia con el radiobutton
    
    #Actualizmos los valores de los atributos del objeto del formatoi
    boleto.setAdult(numAdul.get())
    boleto.setChild(numChild.get())
    lista = [imax.get(),dx.get(),vip.get()]
    boleto.setExperience(lista)

    #actualizamos el objeto variable total con el valor que nos regresa el método del objeto del formatoi
    total.set(boleto.getTotal())
    
#-----------------------------------LABEL 1---------------------------------------------------------
#Etiqueta para la sección Cantidad de boletos por personas
etiq1 = ttk.Label(root, text="Cantidad de boletos:")
#Probar fill = BOTH con el fondo negro
etiq1.pack(side=TOP,expand = True,fill = Y,pady=5)

#-----------------------------------Num adultos-----------------------------------------------------
#Etiqueta "Adultos" indicador del número de botelos adulto
etiq2 = ttk.Label(root, text="Adultos:")
etiq2.pack(side=TOP,expand = True,fill = BOTH,padx = 10,pady=5)

#Spinbox para tomar un número de boletos de adultos
adultos = Spinbox(root, from_=0, #inicio de opciones
                  to=10, #fin de opciones
                  wrap=True, #despues de 10 sigue 0 otra vez
                  textvariable=numAdul, #valor asignado al objeto varibale numAdul
                  state='readonly',
                  command=calcular,
                  width = 5)
adultos.pack(side=TOP,expand = True,fill = BOTH,padx= 10,pady=0)

#------------------------------------Num niños------------------------------------------------------
#Etiqueta "Niños" indicador del número de botelos adulto
etiq3 = ttk.Label(root, text="Niños:")
etiq3.pack(side=TOP,expand = True,fill = BOTH,padx= 10,pady=5)

#Spinbox para tomar un número de boletos de adultos
child = Spinbox(root, from_=0, to=10, wrap=True,
                textvariable=numChild,
                state='readonly',
                command=calcular,
                width = 5)
child.pack(side=TOP,expand = True,fill = BOTH,padx= 10,pady=0)

#------------------------------------LABEL----------------------------------------------------------
etiq4 = ttk.Label(root, text="Formato:")
etiq4.pack(side=TOP,expand = True,fill = Y,padx= 10,pady=5)

#------------------------------------Formato de la cinta--------------------------------------------
#Radiobutton (selección de una sola opción)
formato1 = ttk.Radiobutton(root,
                           text = format1.getFormat(), #Etiqueta del botón
                           variable = formato, #le asigna el valor al objeto formato
                           value = format1.getFormat(), #Valor interno que toma si se selecciona
                           command = calcular)
formato1.pack(side=TOP,expand = True,fill = BOTH,padx= 10,pady=0)


formato2 = ttk.Radiobutton(root,
                           text = format2.getFormat(),#Etiqueta del botón
                           variable = formato,
                           value = format2.getFormat(),#Valor interno que toma si se selecciona
                           command = calcular)
formato2.pack(side=TOP,expand = True,fill = BOTH,padx= 10,pady=0)

#-------------------------------------LABEL---------------------------------------------------------
#Etiqueta sección de Experiencia
etiq5 = ttk.Label(root, text="Experiencia:")
etiq5.pack(side=TOP,expand = True,fill = Y,padx= 10,pady=5)

#-------------------------------------Experiencia en la sala----------------------------------------
#Checkbutton 1 (Casillas opcionales)
exp1 = ttk.Checkbutton(root, text='IMAX', #Equiqueta del botón
                       variable = imax, #objeto variable asignado
                       onvalue=True, #valor si se selcciona
                       offvalue=False, #valor si no se selecciona
                       command=calcular)
exp1.pack(side=TOP,expand = True,fill = BOTH,padx= 10,pady=0)

#Checkbutton 2
exp2 = ttk.Checkbutton(root, text='4DX',
                       variable = dx,
                       onvalue=True, offvalue=False,
                       command=calcular)
exp2.pack(side=TOP,expand = True,fill = BOTH,padx= 10,pady=0)

#Checkbutton 3
exp3 = ttk.Checkbutton(root, text='VIP',
                       variable = vip,
                       onvalue=True, offvalue=False,
                       command=calcular)
exp3.pack(side=TOP,expand = True,fill = BOTH,padx= 10,pady=0)


#--------------------------------------SEPARACIÓN-------------------------------------------------
sep = ttk.Separator(root, orient=HORIZONTAL)
sep.pack(side=TOP,expand = True,fill = BOTH,padx= 10,pady=10)

#--------------------------------------LABEL------------------------------------------------------
#Etiqueta para el total
etiq6 = ttk.Label(root, text="Total:") #Texto estático (siempre el mismo)
etiq6.pack(side=TOP,expand = True,fill = BOTH,padx= 10,pady=5)

#--------------------------------------LABEL con el total del precio------------------------------
#Total
etiq7 = ttk.Label(root,foreground="white",
                  background="black",
                  textvariable = total) #Texto que cambia asigando al objeto variable total
etiq7.pack(side=TOP,expand = True,fill = BOTH,padx= 10,pady=5)

#--------------------------------------BOTÓN PARA SALIR-------------------------------------------
boton = ttk.Button(root, text="Comprar", command=quit)
boton.pack(side=TOP,expand = True,fill = BOTH,padx= 10,pady=10)
#-------------------------------------------------------------------------------------------------


root.mainloop()

