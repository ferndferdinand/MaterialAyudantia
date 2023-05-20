from tkinter import *
from tkinter import ttk

# root window
root = Tk()
root.title('Login')
root.config(bg= "blue")


# username
username_label = ttk.Label(root, text = "Username:")
username_label.grid(column = 0, row = 0, sticky = W, padx = 5, pady = 5)

username_entry = ttk.Entry(root)
username_entry.grid(column = 1, row = 0, sticky = E, padx = 5, pady = 5)

# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column = 0, row = 1, sticky = W, padx = 5, pady = 5)

password_entry = ttk.Entry(root,  show="*")
password_entry.grid(column = 1, row = 1, sticky = E, padx = 5, pady = 5)

# login button
login_button = ttk.Button(root, text = "Login")
login_button.grid(column = 0, row = 3, padx = 5, pady = 5, columnspan = 2)


root.mainloop()
