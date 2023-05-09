from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from GenerosPeliculas import * #Cargamos el módulo propio que ya incluye los objetos creados


#----------------------------------------Datos------------------------------------------------------------------

#Diccionario Nombre de la clasificación, objeto 
generos = {"Estilo": estilo,
           "Audiencia": audiencia,
           "Formato": formato,
           "Ambientación": ambientacion}

generosPor =["Estilo","Audiencia","Formato", "Ambientación"] #Lista primer clasificación

#-----------------------------------------root------------------------------------------------------------------
root = Tk() #Raíz
root.title('Géneros de cine') #Título
root.geometry('450x370') #Tamaño de la ventana


#----------------------------------------Label clasificación de cine--------------------------------------------
label = ttk.Label(root,text="Clasificación del cine según su:") #Label sobre la raíz
label.place(x=10,y= 10)#Posición del label


#-----------------------------------------Combobox--------------------------------------------------------------

opcionesP = ttk.Combobox(root, state ="readonly") #Lista desplegable, no deja escribir al usuario
opcionesP.pack(fill='x',padx= 10, pady=35) #Posición de la lista desplegable
opcionesP.set("Selecciona una opción") #Valor por default en la lista desplegable
opcionesP["values"] = generosPor #Asignar valores a la lista desplegable


#----------------------------------------Label subgénero--------------------------------------------------------
label = ttk.Label(root,text = "Géneros de cine según:") #Label para el subgénero
label.place(x=10,y= 65) #Posición


#-----------------------------------------Combobox 2------------------------------------------------------------
opciones = ttk.Combobox(root,state ="readonly")#Lista desplegable para el subgénero
opciones.pack(fill='x',padx= 10)
opciones.set("Selecciona una opción")


#------------------------------------------text-----------------------------------------------------------------
texto = Text(root,wrap="word")#Cuadro de texto sin cortes en palabras
texto.pack(fill='x',padx= 10,pady = 25)

#-------------------------------------funciones de selección-------------------------------------------------------

#función que se ejecuta al elegir una clasificación de cine
def selection(event):
    
    seleccion = opcionesP.get() #Opción de clasificación seleccionada (str)
    
    #Actualizamos el label del subgénero dependiento la selección anterior
    label.config(text="Géneros de cine según su " + seleccion.lower() + ":")

    seleccion = generos[seleccion] #Obtenemos el objeto por medio del diccionario
    
    #Cambiamos la lista de valores del subgénero dependiendo la selección
    opciones.set("Selecciona una opción")
    opciones["values"] = seleccion.get_list() #obtenes lista de nombres (subgeneros) del objeto seleccionado

    #Selección del subgenero
    def selection2(event):
        seleccion2 = opciones.get()#Opción de subgénero seleccionada (str)
        texto.delete("1.0","end") #Elimar el texto anterior para reemplazarlo por uno nuevo en cada consulta
        texto.insert(INSERT,seleccion.get_inf(seleccion2))#Insertar el nuevo texto con la inf del subgénero
        

    #---------------------------------selección de un subgénero---------------------------------------------------
    opciones.bind("<<ComboboxSelected>>", selection2)


#---------------------------------selección de una clasificación de cine------------------------------------------
opcionesP.bind("<<ComboboxSelected>>", selection)


#---------------------------------------ciclo de la ventana-------------------------------------------------------

root.mainloop()


























































