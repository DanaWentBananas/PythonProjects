from tkinter import *

def clicked():
    check.config(text = state.get())

root = Tk()

check = Checkbutton(root, text="YES?", command = clicked)

#variables for checkbutton
state = StringVar()
check.config(variable = state, onvalue = 'clicked', offvalue='unclicked')

check.pack()

root.mainloop()