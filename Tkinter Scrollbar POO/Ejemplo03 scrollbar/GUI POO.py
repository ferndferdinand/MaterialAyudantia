from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random as rd
from Examen import *

#-------------------------------------------Calse interfaz---------------------------------------------------
class Interfaz():
    
    def __init__(self):
        #--------------------------------------raíz----------------------------------------------------------
        self.root = Tk()
        self.root.title("Examen programación con Python")
        #self.root.config(bg="black")
        
        #-------------------- lista de objetos pregunta desde el objeto examen-------------------------------
        self.preguntas = examen.getPreguntas()
        self.op = [] #Lista de botones de opciones
        
        #Crear canvas sobre la raiz para poder usar el scrollbar
        self.canvas = Canvas(self.root,width=650,height=550,highlightthickness=0)
        #Crear scrollbar
        self.scrollbar = ttk.Scrollbar(self.root,orient = "vertical",command = self.canvas.yview)
        self.scrollbar.pack(side = "right",fill = Y)
        
        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        #Empaquetamos el canvas que llene ambos ejes
        self.canvas.pack(expand = True,fill = BOTH)

        #Creamos un frame dentro de canvas para poner nuestras preguntas
        self.frame = Frame(self.canvas)
        #"Empaquetar" el frame en canvas
        self.canvas.create_window((0,0),window = self.frame, anchor = 'nw')
        
        self.frame.bind("<Configure>",self.config)

        #Nombre del alumno
        self.nombre = ttk.Label(self.frame, text = "Nombre: ")
        self.nombre.pack(side=TOP,expand = False,fill = X,padx= 10,pady=5)
        self.entry = ttk.Entry(self.frame)
        self.entry.pack(side=TOP,expand = False,fill = X,padx= 10,pady=2)

    #Método para definir widgets de las preguntas
    def preguntar(self,i):
        
        pregunta = self.preguntas[i] #Objeto pregunta
        options = pregunta.getOpciones().copy() #Copia de la lista de opciones por pregunta
        rd.shuffle(options) #Revolver las opciones
        
        #Respuesta seleccionada de los botones, obejeto variable
        respuesta = StringVar(value = '') #Se inicializa sin opción seleccionada
        
        #--------------------------------------Evaluación--------------------------------------------
        #Función para cambiar la selección
        def seleccion(*args):
            pregunta.setRespuesta(respuesta.get()) #Se cambia la respuesta de la pregunta
            
        #------------------------------------Pregunta ----------------------------------------------------------
        preg = ttk.Label(self.frame, text = str(i+1) + ".- " + pregunta.getPregunta())
        preg.pack(side=TOP,expand = False,fill = X,padx= 10,pady=10)

        #------------------------------------Botones para seleccionar respuesta--------------------------------------------
        #Radiobutton (selección de una sola opción)
        for opcion in options:
            op = ttk.Radiobutton(self.frame,
                                 text = opcion, #Etiqueta del botón 
                                 variable = respuesta,#respuesta cambia su valor por el valor interno
                                 value = opcion, #Valor interno que toma si se selecciona
                                 command = seleccion)
            op.pack(side=TOP,expand = False,fill = X,padx= 10,pady=0)
            self.op.append(op) #Agregamos botón a la lista


    #Método para mostrar separación y botón de finalizado
    def boton(self):
        #--------------------------------------Linea de separación-------------------------------------------------
        sep = ttk.Separator(self.root, orient=HORIZONTAL)
        sep.pack(side=TOP,expand = False,fill = X,padx= 10,pady=10)

        #-----------------------------------botón para terminar intento-------------------------------------------
        self.boton = ttk.Button(self.root, text = "Terminar", command = self.enviar)
        self.boton.pack(side=TOP,expand = False,padx= 0,pady=2)
        
    #Método para enviar respuestas
    def enviar(self,*args):
        
        self.nombre = self.entry.get()
        if len(self.nombre): #Revisamos que si escribió el nombre
            self.entry.config(state=DISABLED) #Ya no se puede cambiar de nombre
        else:
            messagebox.showwarning('Warning', 'No olvide escribir su nombre')
            return False

        #Ya no se pueden editar las respuestas una vez enviado
        for op in self.op:
            op.config(state=DISABLED) 

        cal = ttk.Label(self.root, text = "Calificación: " + str(examen.calificar()))
        cal.pack(side=TOP,expand = False,fill = X,padx= 10,pady=10)
        
        if 0 < examen.calificar() < len(self.preguntas):
            messagebox.showinfo(message = examen.getCorrectas() + "\n" + examen.getIncorrectas(), title="Respuestas")
            
        self.boton.config(text = "Salir", command = quit)
        
        #preguntar por otro intento-------------------
        
    #Método para cargar las preguntas y el botón
    def mostrar(self):
        for i in range(len(self.preguntas)): #Mostramos las 10 preguntas
            self.preguntar(i)
        self.boton() #Mostramos el botón de terminar examen

    def config(self,event):
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))
        

#Mostrar interfaz
def main():
    mi_app = Interfaz()#Se crea objeto de la Interfaz
    mi_app.mostrar() #Método para cargar todo
    
if __name__ == '__main__':
    main()
    
