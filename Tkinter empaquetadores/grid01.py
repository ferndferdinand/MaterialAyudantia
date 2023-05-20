from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Ejemplo grid")
root.config(bg= "blue")

frame = Frame(root, bg = "green")
#Empaquetamos el frame con pack
frame.pack(expand = True, fill = BOTH, padx = 10, pady = 10)

#Empaquetamos los Label en el frame con grid
for r in range(10):
   for c in range(10):
       ttk.Label(frame,
                 text = "("+str(r)+","+ str(c)+")").grid(column = c , row = r , padx = 2, pady = 2)

root.mainloop()

