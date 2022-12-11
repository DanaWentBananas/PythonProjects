from tkinter import *

root = Tk()

breakfast = StringVar()

#setting variable name to text variable
#radio.config(textvariable = breakfast)

radio1 = Radiobutton(root, text = 'orange' , variable = breakfast, value = "orange")
radio2 = Radiobutton(root, text = 'apples' , variable = breakfast, value = "apple")
radio3 = Radiobutton(root, text = 'potatos', variable = breakfast, value = "potatos")


radio1.pack()
radio2.pack()
radio3.pack()



root.mainloop()