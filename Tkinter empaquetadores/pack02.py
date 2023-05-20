from tkinter import *
from tkinter import ttk
root = Tk()

root.title("Ejemplo pack02")

box1 = Frame(root, bg= "green", width = 60, height = 300)
box1.pack(side = LEFT, fill= BOTH)

box2 = Frame(root, bg= "red", width = 240, height = 30)
box2.pack(side = TOP, fill= BOTH)

box3 = Frame(root, bg= "blue", width = 60, height = 270)
box3.pack(side = LEFT, fill= BOTH)

box4 = Frame(root, bg= "yellow", width = 180, height = 30)
box4.pack(side = TOP, fill= BOTH)

box5 = Frame(root, bg= "orange", width = 60, height = 240)
box5.pack(side = LEFT, fill= BOTH)



root.mainloop()
