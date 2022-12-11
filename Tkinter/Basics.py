from tkinter import *
from tkinter import ttk

#create window as parent
root = Tk()

#as ttk
button = ttk.Button(root, text = 'click me')
#without ttk
button2 = Button(root, text='potato')

#change text
button['text'] = 'press me'
button.config(text = 'push me')

#show properties
print(button.config())

#know identifier of button
#know heirarchy of widgets
print(str(button))


#display it
button.pack()
button2.pack()

#important for event handling
root.mainloop()

