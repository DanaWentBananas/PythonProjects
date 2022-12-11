from tkinter import *
from tkinter import ttk

root = Tk()

month = StringVar()

#combobox


combo = ttk.Combobox(root, textvariable = month)

combo.config(values = ("June","January","July"))

combo.pack()

#spinbox
year = StringVar()

spin = Spinbox(root, from_ = 1990, to = 2014, textvariable = year)

spin.pack()


root.mainloop()