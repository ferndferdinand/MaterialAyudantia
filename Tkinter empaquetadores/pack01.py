from tkinter import *
from tkinter import ttk
root = Tk()

root.title("Ejemplo pack")

box1 = Frame(root, bg= "red", width = 300, height = 50)
box1.pack(side = TOP, fill= BOTH)

box2 = Frame(root, bg= "green",width = 300, height = 50)
box2.pack(side = TOP, fill= BOTH)

box3 = Frame(root, bg= "blue",width = 300, height = 50)
box3.pack(side = TOP, fill= BOTH)

box4 = Frame(root, bg= "purple",width = 100, height = 50)
box4.pack(side = LEFT, fill= BOTH)

box5 = Frame(root, bg= "yellow",width = 100, height = 50)
box5.pack(side = RIGHT, fill= BOTH)

box6 = Frame(root, bg= "pink",width = 100, height = 50)
box6.pack(side = BOTTOM, fill= BOTH)

root.mainloop()
