from tkinter import *

def btn1click():
    greeting['text'] = "Hello, Faheem"
    
def btn2click():
    greeting['text'] = "Hello, Dana"

root = Tk()

greeting = Label(root, text = "Hello, you")

btn1 = Button(root, text = "Faheem", command = btn1click)
btn2 = Button(root, text = "Dana", command = btn2click)
#pack
greeting.pack()
btn1.pack()
btn2.pack()

root.mainloop()