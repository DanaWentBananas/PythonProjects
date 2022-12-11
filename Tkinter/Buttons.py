from tkinter import *
from tkinter import ttk

#functions
def btnClick():
    print('clicked')

root = Tk()

button = Button(root, text = "Click Me")
button.config(command = btnClick)

#pretend its clicked
button.invoke()

#button state (its a ttk thing)
#check what the state of the button is
#button.instate(['!disabled'])
#button.state(['disabled'])

#images
#can only use : gif, PGM/PPM
logo = PhotoImage(file = 'img.gif')
#resize
smallLogo = logo.subsample(5,5)

button.config(image = smallLogo)

#compound property
#bottom,top,center,left,right, none(default)
button.config(compound = 'center')

#s=ttk.Style()
#s.configure('anything.TButton',font=('Courier',18),background='blue')
#button.config(style='anything.TButton')

button.config(font = ('Courier', 18),activebackground='blue')
button.config(background='maroon',activeforeground='maroon',foreground='blue')

print(button.config())

button.pack()

root.mainloop()