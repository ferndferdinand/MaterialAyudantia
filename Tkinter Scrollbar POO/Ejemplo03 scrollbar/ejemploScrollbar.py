from tkinter import *
from tkinter import ttk

root = Tk()
root.config(bg="blue")

#-----------------------scrollbar, canvas, frame-----------------------
scrollbar = Scrollbar(root)
canvas = Canvas(root,bg="green",highlightthickness=0) #Este último atributo es para quitar el borde feo
frame = Frame(canvas,bg="orange")

#---------------------------empaquetar--------------
scrollbar.pack(side="right", fill =Y,padx = 10)
canvas.pack(expand= True, fill =BOTH,padx=10,pady= 10) #pad para que se vea que la raíz está abajo, en la implementación quitar pda
canvas.create_window((0,0),window = frame, anchor = "nw")

#-----------------------configuraciones---------------------------
scrollbar.config(command = canvas.yview)
canvas.configure(yscrollcommand = scrollbar.set)

def config(event):
    canvas.configure(scrollregion= canvas.bbox("all"), height = 500)
    
frame.bind("<Configure>",config)

#------------------------widgets en frame-------------------------------
for i in range(50):
    label = Label(frame, text ="estas van a ser las preguntas y opciones",bg="yellow")
    label.pack(expand=False,fill=X,padx=10,pady=2)#pad para que se vea el frame, en la implementación quitar pad


root.mainloop()
